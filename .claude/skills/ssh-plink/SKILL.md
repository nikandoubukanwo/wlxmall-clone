---
name: ssh-plink
description: SSH to Linux servers using Windows plink (PuTTY CLI) for disk inspection, log cleanup, and remote management
---

# ssh-plink

Connect to remote Linux servers via SSH using Windows PuTTY's `plink` CLI, wrapped via Python `subprocess` for non-interactive command execution. Useful for server inspection, disk cleanup, log management, and general remote administration.

This skill uses **plink** (from PuTTY) for SSH — avoids needing `sshpass` or `expect`. The method is: Python script calls `plink.exe` with password and hostkey, collects stdout/stderr as text.

## Prerequisites

- **PuTTY** installed (provides `plink.exe`) — typically at `D:\PuTTY\plink.exe` or `/d/PuTTY/plink` in Git Bash
- **Python 3** — for the wrapper that handles plink process execution and encoding
- Server IP, username (default `root`), password

## Driver

The driver is inline in this skill — a Python script template you fill with commands.

### Standard wrapper

```python
import subprocess

def ssh(cmd):
    proc = subprocess.run(
        ['D:\\PuTTY\\plink.exe', '-ssh', '-batch',
         '-hostkey', '<FINGERPRINT>',
         '-pw', '<PASSWORD>',
         '<USER>@<IP>', cmd],
        capture_output=True,
        text=False,
        timeout=20
    )
    out = (proc.stdout or b'').decode('utf-8', errors='replace')
    err = (proc.stderr or b'').decode('utf-8', errors='replace')
    return out + err

# Usage:
print(ssh("df -h"))
```

### No-wrapper one-liner (for ad-hoc use via Bash)

```bash
python -c "import subprocess; p=subprocess.run(['D:\\PuTTY\\plink.exe','-ssh','-batch','-hostkey','<FINGERPRINT>','-pw','<PASSWORD>','root@<IP>','df -h'],capture_output=True,text=False,timeout=15); print((p.stdout or b'').decode('utf-8',errors='replace'))"
```

## First-time connection (get host key fingerprint)

The first time you connect to a server, you need its host key fingerprint. Run without `-hostkey`:

```bash
python -c "
import subprocess
p = subprocess.run(['D:\\PuTTY\\plink.exe','-ssh','-batch','-pw','<PASSWORD>','root@<IP>','df -h'],
    capture_output=True,text=False,timeout=10)
print((p.stderr or b'').decode('utf-8',errors='replace'))
"
```

It will print the fingerprint like:
```
The server's ssh-ed25519 key fingerprint is:
  ssh-ed25519 255 SHA256:abc123...
```

Copy this fingerprint and add `-hostkey 'ssh-ed25519 255 SHA256:abc123...'` to subsequent calls.

## Common recipes

### Quick disk check
```python
print(ssh("df -h"))
```

### Find big directories
```python
print(ssh("du -sh /* 2>/dev/null | sort -rh | head -10"))
```

### Find deleted-but-open files (space leaks)
```python
print(ssh("lsof +L1 2>/dev/null | head -30"))
```

### Truncate a deleted-but-open log file
```python
print(ssh(": > /proc/<PID>/fd/1 2>&1"))
```

### MySQL binlog cleanup (via debian-sys-maint)
```python
print(ssh("mysql -u debian-sys-maint -p<DEBIAN_PW> -e 'PURGE BINARY LOGS BEFORE DATE_SUB(NOW(), INTERVAL 3 DAY);' 2>&1"))
```

### Run any command
```python
print(ssh("your-command-here"))
```

## Troubleshooting

| Error | Fix |
|-------|-----|
| `The host key is not cached` | Add `-hostkey '<FINGERPRINT>'` from the error message |
| `FATAL ERROR: Cannot confirm a host key` | Same as above — use `-hostkey` flag |
| `Access denied` | Check password, or user might not be `root` |
| `timeout` | Server unreachable or firewall; check IP and port 22 |
| `UnicodeDecodeError: 'gbk' codec...` | Use `text=False` and decode manually as `utf-8` with `errors='replace'` |
| `timed out after 15 seconds` | Increase `timeout=` in the Python call, or check network connectivity |
