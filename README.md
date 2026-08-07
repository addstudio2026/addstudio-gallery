# ADDSTUDIO Hermes Backup

Backup of Hermes Agent configuration, memories, skills, and workspace.

## Structure

```
├── memories/          # MEMORY.md, USER.md
├── config/            # config.yaml, SOUL.md
├── skills/            # Custom skills by category
├── workspace/         # Project files + reference images
├── cron/              # Cron configs
└── backup.sh          # Backup script
```

## Restore

1. Copy `memories/` → `~/.hermes/memories/`
2. Copy `config/` → `~/.hermes/`
3. Copy `skills/` → `~/.hermes/skills/`
4. Copy `workspace/` → `/data/workspace/`
