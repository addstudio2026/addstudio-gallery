---
name: operational-safety
description: "Backup safety, password enforcement, data integrity rules."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [backup, git, security, password, data-integrity, operational]
    category: productivity
---

# Operational Safety Protocols

Cross-cutting safety rules for ALL agent operations. Learned from critical failures.

## 1. Backup Safety Protocol (CRITICAL)

### The Problem
The `backup.sh` script at `/data/hermes-backup/backup.sh` has **two dangerous behaviors**:

**A) It only STAGES files, never commits.**
Running `backup.sh` does `git add` but NOT `git commit`. If the agent says "backup done" after running the script, it's LYING. The files are staged but not committed to the remote.

**Correct workflow:**
1. Run `backup.sh` to stage
2. Show user what changed (`git status`)
3. `git commit -m 'message'`
4. `git push origin main`

**B) It can DELETE files from GitHub if local/remote structures diverge.**
If the backup directory structure doesn't match what git expects, git interprets missing local files as "user wants to delete them." This has caused complete loss of all tag files (R001-R046) multiple times.

**Prevention:**
- ALWAYS copy files from workspace to backup dir BEFORE running `git add`
- Verify with `ls` that files exist in the backup dir before committing
- NEVER trust "Everything up-to-date" — it means files weren't staged

### Emergency Recovery
```bash
cp /data/workspace/addstudio-v01/tags/*.yaml /data/hermes-backup/workspace/addstudio-v01/tags/
cd /data/hermes-backup
git add .
git commit -m 'CRITICAL RESTORE: restore deleted files'
git push origin main
```

## 2. Security & Trust Model

### ⚠️ PASSWORD SYSTEM CANCELLED (2026-08-09)
The user explicitly cancelled the password system: "داستان پسورد کاملا منتفیه!"
Do NOT ask for passwords. Do NOT reference security.yaml. The file may still exist on disk but is NOT in use.

### Lesson: Don't Build Unenforceable Security
I built a "soft guard" password system that:
1. I couldn't technically enforce (no OS-level barrier)
2. I forgot to enforce in practice (user tested me and I failed)
3. Caused the user to lose a file during the failed test

**Rule: Never build security systems that depend on LLM compliance alone.** If there's no technical enforcement mechanism (sudo, file permissions, API keys), the system is theater. Instead:
- Use GitHub Deploy Keys or Fine-grained PATs for repo access control
- Use OS-level permissions for file access
- Don't create false sense of security

### What IS Enforceable (and already works)
- Backup.sh script safety (copy files before git add)
- Data integrity verification (read back files after writing)
- Git safety (check for deletions before push)
- These are TECHNICAL controls, not behavioral ones

## 3. Data Integrity Checklist

Before reporting any file operation as "complete":
- [ ] Did the write actually succeed? (check `verified: true`)
- [ ] Are all expected files present? (count them)
- [ ] Are the files non-empty? (read a sample)
- [ ] Is the backup committed AND pushed? (`git log -1`)
- [ ] Did git show any deletions? (`git diff --stat HEAD~1`)

### The "false success" trap
Agent tools return `status: success` even when the operation partially failed. ALWAYS verify independently.

## 4. Video Prompt Consistency

When writing prompts for video generation:
- NEVER let the model change the product's appearance
- Use Identity Anchor: "strictly maintain the exact [product] from reference"
- Negative prompt: "morphing bottle, changing label, distorted product"
- Keep Motion Strength LOW (2-3)
- ALWAYS use Image-to-Video, not text-only

## 5. Theme Consistency in Iterative Prompts

When user specifies a color theme:
- Theme applies to ALL subsequent prompts
- Do NOT introduce competing colors unless user says so
- When switching topics, maintain the same palette
- If user says "you drifted" — immediately revert

## 6. Cross-User Messaging

### hermes send Command
Send messages to other Telegram users without LLM processing:
```bash
hermes send --to telegram:<chat_id> "message"
hermes send --to telegram:Ali "سلام"
hermes send --list  # list all available targets
```

### Available Users (as of 2026-08-09)
- Hosein Mirhoseini (owner)
- Ali (dm)
- Alireza Emtiaz (dm)
- m4dsi (dm)

### Rules
- Only send messages when user explicitly requests
- Never send unsolicited messages
- Always confirm before sending to another user
- Read-only commands (list, status) do NOT need confirmation

## Cross-References
- Backup script: `/data/hermes-backup/backup.sh`
- Tags: `/data/workspace/addstudio-v01/tags/`
- GitHub: `https://github.com/addstudio2026/ADDSTUDIOhERMES`
- Send command: `hermes send --help`
