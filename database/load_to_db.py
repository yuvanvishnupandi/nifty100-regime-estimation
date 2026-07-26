import pandas as pd
import sqlite3
import os

# Ensure data directory exists
os.makedirs("data", exist_ok=True)

# Point to data/nifty100.db as expected by downstream analytics scripts
conn = sqlite3.connect("data/nifty100.db")

folder = "data/raw"

if os.path.exists(folder):
    for file in os.listdir(folder):
        if file.endswith(".xlsx"):
            table_name = file.replace(".xlsx", "")
            df = pd.read_excel(
                os.path.join(folder, file),
                header=1
            )
            df.to_sql(
                table_name,
                conn,
                if_exists="replace",
                index=False
            )
            print(f"{table_name} loaded")

# Explicitly commit and close
conn.commit()
conn.close()
print("Database successfully committed to data/nifty100.db!")
