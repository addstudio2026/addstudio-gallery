#!/bin/bash
# Hermes Agent Backup Script (non-interactive)
# Collects files and shows changes. Push handled separately.

set -e

BACKUP_DIR="/data/hermes-backup"
HERMES_HOME="$HOME/.hermes"

# Clean previous backup content (keep .git)
cd "$BACKUP_DIR"
find . -maxdepth 1 -not -name '.git' -not -name '.' -not -name 'backup.sh' -exec rm -rf {} +

# === COLLECT ===
mkdir -p memories config skills workspace/addstudio-v01 cron

# Memories
cp "$HERMES_HOME/memories/MEMORY.md" memories/ 2>/dev/null || true
cp "$HERMES_HOME/memories/USER.md" memories/ 2>/dev/null || true

# Config
cp "$HERMES_HOME/config.yaml" config/ 2>/dev/null || true
cp "$HERMES_HOME/SOUL.md" config/ 2>/dev/null || true

# Skills
find "$HERMES_HOME/skills" -name "SKILL.md" -not -path "*/.git/*" | while read skill_file; do
    skill_dir=$(dirname "$skill_file")
    skill_name=$(basename "$skill_dir")
    category=$(basename "$(dirname "$skill_dir")")
    mkdir -p "skills/$category/$skill_name"
    cp "$skill_file" "skills/$category/$skill_name/"
    for sub in references templates scripts assets; do
        if [ -d "$skill_dir/$sub" ]; then
            cp -r "$skill_dir/$sub" "skills/$category/$skill_name/" 2>/dev/null || true
        fi
    done
done

# Workspace
if [ -d "/data/workspace/addstudio-v01" ]; then
    cp /data/workspace/addstudio-v01/*.md workspace/addstudio-v01/ 2>/dev/null || true
    cp /data/workspace/addstudio-v01/*.jpg workspace/addstudio-v01/ 2>/dev/null || true
fi

# Cron
cp "$HERMES_HOME/cron/"* cron/ 2>/dev/null || true

# === SHOW CHANGES ===
cd "$BACKUP_DIR"
git add -A
echo "=== CHANGES ==="
git diff --cached --stat
echo "=== END ==="
