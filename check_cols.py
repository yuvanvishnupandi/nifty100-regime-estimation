import sqlite3
import pandas as pd

conn = sqlite3.connect("data/nifty100.db")
df = pd.read_sql("SELECT * FROM profitandloss LIMIT 1", conn)
print("\n--- Profit & Loss Columns ---")
print(df.columns.tolist())
conn.close()
