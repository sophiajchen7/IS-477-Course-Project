#!/bin/bash

set -e

echo "Running full workflow..."

python scripts/acquire_data.py
python scripts/check_integrity.py
python scripts/clean_data.py
python scripts/merge_data.py
python scripts/analyze.py

echo "All steps complete."
