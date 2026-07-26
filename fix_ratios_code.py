import re

file_path = "src/analytics/financial_ratios.py"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Fix DB Path
content = content.replace('database/nifty100.db', 'data/nifty100.db')

# Remove the broken row-to-column assignment
content = re.sub(r'pl\.columns\s*=\s*pl\.iloc\[0\]\r?\n\s*pl\s*=\s*pl\.iloc\[1\:]\.reset_index\(drop=True\)', '# Column headers already loaded from SQL', content)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("✅ Patched DB path and removed broken column overwrite in financial_ratios.py!")
