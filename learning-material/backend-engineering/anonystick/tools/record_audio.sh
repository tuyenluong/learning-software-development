#!/usr/bin/env bash
# Usage: record_audio.sh <outfile.wav> <seconds>
# Records the "rec" null sink monitor (where Chrome audio plays) as 16 kHz mono WAV.
set -euo pipefail
out="${1:?usage: record_audio.sh <outfile.wav> <seconds>}"
secs="${2:?usage: record_audio.sh <outfile.wav> <seconds>}"
export PULSE_SERVER="${PULSE_SERVER:-unix:/tmp/pulse-box/native}"
pactl info >/dev/null 2>&1 || "$(dirname "$0")/start_audio.sh"
mkdir -p "$(dirname "$out")"
exec ffmpeg -hide_banner -loglevel warning -y -f pulse -i rec.monitor -t "$secs" -ac 1 -ar 16000 -c:a pcm_s16le "$out"
