import pandas as pd
import sqlite3
import os

# Paths
DATA_DIR = "../data"
DB_PATH = "../titanic.db"
TRAIN_CSV = os.path.join(DATA_DIR, "train.csv")
TEST_CSV = os.path.join(DATA_DIR, "test.csv")

# Connect to SQLite
conn = sqlite3.connect(DB_PATH)
print(f"Connected to {DB_PATH}")

# Load and insert train data
df_train = pd.read_csv(TRAIN_CSV)
df_train.to_sql("passengers", conn, if_exists="replace", index=False)
print(f"Loaded {len(df_train)} train records")

# Load test data (append, since test has no 'Survived')
df_test = pd.read_csv(TEST_CSV)
df_test["survived"] = None  # Test has no survived column
df_test.to_sql("passengers", conn, if_exists="append", index=False)
print(f"Appended {len(df_test)} test records. Total: {len(df_train)+len(df_test)}")

# Verify
print("\nSample data:")
print(pd.read_sql("SELECT * FROM passengers LIMIT 5", conn))

conn.close()
print("Done! Database created.")
