# format python and webdev
#!/usr/bin/env bash
set -e

# dont forget to source the env with 
source .venv/bin/activate

echo "Formatting Python files..."
black .
isort .

echo "Formatting Jinja / HTML templates..."
djlint . --reformat
djlint . --format-css --reformat

echo "All formatting complete ✅"
