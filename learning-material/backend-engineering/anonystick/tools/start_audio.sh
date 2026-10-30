#!/usr/bin/env bash
# Start the headless PulseAudio server with the "rec" null sink (idempotent).
# Config: ~/.config/pulse/{default.pa,daemon.conf,client.conf}; socket /tmp/pulse-box/native
set -euo pipefail
mkdir -p /tmp/pulse-box && chmod 700 /tmp/pulse-box
if pactl info >/dev/null 2>&1; then echo "pulseaudio already running"; else
  PULSE_CLIENTCONFIG=/dev/null pulseaudio --start --log-target=file:/tmp/pulseaudio.log
  sleep 1
fi
pactl info | grep -E 'Server String|Default Sink|Default Source'
