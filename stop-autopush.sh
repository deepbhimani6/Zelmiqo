#!/bin/bash
# Stop the auto-push service

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PID_FILE="$SCRIPT_DIR/.autopush.pid"

if [ -f "$PID_FILE" ]; then
    PID=$(cat "$PID_FILE")
    if ps -p "$PID" > /dev/null 2>&1; then
        kill "$PID"
        rm -f "$PID_FILE"
        echo "Auto-push service (PID: $PID) stopped."
        exit 0
    else
        rm -f "$PID_FILE"
    fi
fi

# Fallback: kill any matching autopush.py process in this directory
PIDS=$(pgrep -f "python3.*$SCRIPT_DIR/autopush.py")
if [ -n "$PIDS" ]; then
    kill $PIDS
    echo "Auto-push service stopped."
else
    echo "Auto-push service is not currently running."
fi
