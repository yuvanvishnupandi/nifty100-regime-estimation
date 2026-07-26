import re

files = ["src/screener/engine.py", "src/analytics/peer.py"]

for file_path in files:
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        # 1. Update SQLite connection path
        content = content.replace('database/nifty100.db', 'data/nifty100.db')

        # 2. Remove any row-to-column assignment overrides
        content = re.sub(
            r'\w+\.columns\s*=\s*\w+\.iloc\[0\]\r?\n\s*\w+\s*=\s*\w+\.iloc\[1\:]\.reset_index\(drop=True\)', 
            '# Columns loaded directly from database', 
            content
        )

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

        print(f"✅ Successfully patched {file_path}")
    except Exception as e:
        print(f"❌ Error patching {file_path}: {e}")
