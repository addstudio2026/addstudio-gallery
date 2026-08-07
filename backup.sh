#!/bin/bash
# Hermes Agent Backup Script
# Backs up memories, skills, config, and workspace to GitHub

set -e

BACKUP_DIR="/data/hermes-backup"
HERMES_HOME="$HOME/.hermes"
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')

echo "🔄 Starting Hermes backup at $TIMESTAMP"

# Clean previous backup content (keep .git)
cd "$BACKUP_DIR"
find . -maxdepth 1 -not -name '.git' -not -name '.' -not -name 'backup.sh' -exec rm -rf {} +

# === 1. MEMORIES (highest priority) ===
echo "📦 Backing up memories..."
mkdir -p memories
cp "$HERMES_HOME/memories/MEMORY.md" memories/ 2>/dev/null || true
cp "$HERMES_HOME/memories/USER.md" memories/ 2>/dev/null || true

# === 2. CONFIG ===
echo "⚙️ Backing up config..."
mkdir -p config
cp "$HERMES_HOME/config.yaml" config/ 2>/dev/null || true
cp "$HERMES_HOME/SOUL.md" config/ 2>/dev/null || true

# === 3. SKILLS (custom ones) ===
echo "🛠️ Backing up skills..."
mkdir -p skills
# Only backup custom/bundled skills, not the .git dirs
find "$HERMES_HOME/skills" -name "SKILL.md" -not -path "*/.git/*" | while read skill_file; do
    skill_dir=$(dirname "$skill_file")
    skill_name=$(basename "$skill_dir")
    category=$(basename "$(dirname "$skill_dir")")
    mkdir -p "skills/$category/$skill_name"
    cp "$skill_file" "skills/$category/$skill_name/"
    # Copy linked files (references, templates, scripts, assets)
    for sub in references templates scripts assets; do
        if [ -d "$skill_dir/$sub" ]; then
            cp -r "$skill_dir/$sub" "skills/$category/$skill_name/" 2>/dev/null || true
        fi
    done
done

# === 4. WORKSPACE (product shot project) ===
echo "📁 Backing up workspace..."
mkdir -p workspace/addstudio-v01
if [ -d "/data/workspace/addstudio-v01" ]; then
    cp /data/workspace/addstudio-v01/*.md workspace/addstudio-v01/ 2>/dev/null || true
    cp /data/workspace/addstudio-v01/*.jpg workspace/addstudio-v01/ 2>/dev/null || true
    cp /data/workspace/addstudio-v01/*.skill workspace/addstudio-v01/ 2>/dev/null || true
fi

# === 5. CRON JOBS ===
echo "⏰ Backing up cron config..."
mkdir -p cron
cp "$HERMES_HOME/cron/"* cron/ 2>/dev/null || true

# === 6. README ===
cat > README.md << 'EOF'
# ADDSTUDIO Hermes Backup

Automated backup of Hermes Agent configuration, memories, skills, and workspace.

## Structure

```
├── memories/          # MEMORY.md, USER.md (persistent memory)
├── config/            # config.yaml, SOUL.md
├── skills/            # Custom skills organized by category
│   └── <category>/
│       └── <skill-name>/
│           ├── SKILL.md
│           └── references/ (if any)
├── workspace/         # Project files
│   └── addstudio-v01/
│       ├── PRODUCT_SHOT_SKILL.md
│       └── *.jpg (reference images)
├── cron/              # Cron job configs
└── backup.sh          # This backup script
```

## Restore

To restore on a new machine:
1. Copy `memories/` to `~/.hermes/memories/`
2. Copy `config/` to `~/.hermes/`
3. Copy `skills/` contents to `~/.hermes/skills/`
4. Copy `workspace/` to `/data/workspace/`

## Auto Backup

This backup runs via Hermes cron job every 6 hours.
EOF

# === 7. GIT COMMIT & PUSH ===
echo "🚀 Pushing to GitHub..."
cd "$BACKUP_DIR"
git add -A
git commit -m "🔄 Backup: $TIMESTAMP" || echo "No changes to commit"
git push -u origin main 2>&1 || echo "Push failed - check token/repo"

echo "✅ Backup complete at $TIMESTAMP"
