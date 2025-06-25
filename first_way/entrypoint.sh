#!/bin/bash
set -e
if [ $# -eq 0 ]; then
  echo "Usage: $0 <video-file>"
  exit 1
fi
python anonymize.py "$1"
