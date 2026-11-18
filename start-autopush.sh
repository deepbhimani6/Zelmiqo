#!/bin/bash
# Start the auto-push service in the background

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PID_FILE="$SCRIPT_DIR/.autopush.pid"

if [ -f "$PID_FILE" ]; then
    PID=$(cat "$PID_FILE")
    if ps -p "$PID" > /dev/null 2>&1; then
        echo "Auto-push service is already running (PID: $PID)."
        exit 0
    fi
fi

nohup python3 "$SCRIPT_DIR/autopush.py" > /dev/null 2>&1 &
echo "Auto-push service started in the background (PID: $!)."
echo "Live logs can be viewed in: $SCRIPT_DIR/.autopush.log"
