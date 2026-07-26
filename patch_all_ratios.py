import re

file_path = "src/analytics/financial_ratios.py"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. DB path fix
content = content.replace('database/nifty100.db', 'data/nifty100.db')

# 2. Remove all instances of `.columns = .iloc[0]` patterns
content = re.sub(r'\w+\.columns\s*=\s*\w+\.iloc\[0\]\r?\n\s*\w+\s*=\s*\w+\.iloc\[1\:]\.reset_index\(drop=True\)', '# SQL columns used directly', content)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("✅ Patched all table column loads in financial_ratios.py!")
