# format python and webdev
#!/usr/bin/env bash
set -e

# dont forget to source the env with 
# source .venv/bin/activate

echo "Formatting Python files..."
black .
isort .

echo "Formatting Jinja / HTML templates..."
djlint src/templates/ --reformat


djlint . --format-css --reformat

echo "Formatting CSS files..."
prettier --write "**/*.css"

echo "All formatting complete ✅"