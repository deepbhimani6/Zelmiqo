#!/usr/bin/env python3
"""
Zelmiqo Auto-Push Service
Watches the repository for any changes, automatically commits and pushes to GitHub.
"""

import os
import sys
import time
import subprocess
import signal
from datetime import datetime

REPO_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(REPO_DIR, ".autopush.log")
PID_FILE = os.path.join(REPO_DIR, ".autopush.pid")
POLL_INTERVAL = 3  # seconds
DEBOUNCE_WAIT = 3  # seconds to wait for file operations to settle

def log(msg: str):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted = f"[{timestamp}] {msg}"
    print(formatted, flush=True)
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(formatted + "\n")
    except Exception:
        pass

def run_git(args: list) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["git"] + args,
        cwd=REPO_DIR,
        capture_output=True,
        text=True
    )

def check_remote_configured() -> bool:
    res = run_git(["remote", "get-url", "origin"])
    return res.returncode == 0 and bool(res.stdout.strip())

def auto_commit_and_push():
    # Debounce wait
    time.sleep(DEBOUNCE_WAIT)
    
    # Stage all changes
    add_res = run_git(["add", "-A"])
    if add_res.returncode != 0:
        log(f"Error running git add: {add_res.stderr.strip()}")
        return

    # Check what is staged
    diff_res = run_git(["diff", "--cached", "--name-only"])
    changed_files = [f for f in diff_res.stdout.splitlines() if f.strip()]
    if not changed_files:
        return

    # Create descriptive commit message
    if len(changed_files) == 1:
        change_summary = changed_files[0]
    elif len(changed_files) <= 3:
        change_summary = ", ".join(changed_files)
    else:
        change_summary = f"{changed_files[0]} and {len(changed_files) - 1} other files"

    timestamp_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    commit_msg = f"Auto-update: {change_summary} ({timestamp_str})"

    commit_res = run_git(["commit", "-m", commit_msg])
    if commit_res.returncode != 0:
        log(f"Commit error: {commit_res.stderr.strip()}")
        return
    log(f"Committed {len(changed_files)} change(s): {commit_msg}")

    # Push to GitHub
    if check_remote_configured():
        push_res = run_git(["push", "origin", "main"])
        if push_res.returncode == 0:
            log("Successfully pushed changes to GitHub (origin/main).")
        else:
            log(f"Push error: {push_res.stderr.strip()}")
    else:
        log("Notice: origin remote not yet configured or reachable. Push deferred.")

def cleanup(signum=None, frame=None):
    log("Auto-push service stopped.")
    try:
        if os.path.exists(PID_FILE):
            os.remove(PID_FILE)
    except Exception:
        pass
    sys.exit(0)

def main():
    with open(PID_FILE, "w", encoding="utf-8") as f:
        f.write(str(os.getpid()))

    signal.signal(signal.SIGINT, cleanup)
    signal.signal(signal.SIGTERM, cleanup)

    log("Zelmiqo Auto-Push Service started. Monitoring for changes...")

    while True:
        try:
            status_res = run_git(["status", "--porcelain"])
            if status_res.returncode == 0 and status_res.stdout.strip():
                log("Detected local file changes. Syncing...")
                auto_commit_and_push()
            time.sleep(POLL_INTERVAL)
        except Exception as e:
            log(f"Unexpected error: {e}")
            time.sleep(POLL_INTERVAL)

if __name__ == "__main__":
    main()
