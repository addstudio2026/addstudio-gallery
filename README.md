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
