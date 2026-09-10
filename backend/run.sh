#!/usr/bin/env bash
# Start the API on http://localhost:8000  (docs at /docs)
set -e
cd "$(dirname "$0")"
python3 -m venv ../.venv 2>/dev/null || true
../.venv/bin/pip install -q -r requirements.txt
exec ../.venv/bin/python -m uvicorn app.main:app --reload --port 8000
