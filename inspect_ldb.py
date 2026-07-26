import sqlite3
import database.load_to_db as ldb

# Check where load_to_db points
db_file = getattr(ldb, 'DB_PATH', getattr(ldb, 'DB_NAME', getattr(ldb, 'db_path', 'data/nifty100.db')))
print(f"Target DB Path: {db_file}")

# Try connecting to that specific path
conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Tables in target DB:", [t[0] for t in tables])

# Also check profitandloss columns if table exists
if 'profitandloss' in [t[0] for t in tables]:
    cursor.execute("PRAGMA table_info(profitandloss);")
    cols = [row[1] for row in cursor.fetchall()]
    print("ProfitAndLoss Columns:", cols)

conn.close()
