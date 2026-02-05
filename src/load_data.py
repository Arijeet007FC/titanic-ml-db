import pandas as pd
import sqlite3
import os

# Absolute base directory (project root)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Paths
DATA_DIR = os.path.join(BASE_DIR, "data")
DB_PATH = os.path.join(BASE_DIR, "titanic.db")
TRAIN_CSV = os.path.join(DATA_DIR, "train.csv")
TEST_CSV = os.path.join(DATA_DIR, "test.csv")

# Debug prints (optional but helpful)
print("Base dir:", BASE_DIR)
print("Train CSV:", TRAIN_CSV)
print("Test CSV:", TEST_CSV)

# Connect to SQLite
conn = sqlite3.connect(DB_PATH)
print(f"Connected to {DB_PATH}")

# Load and insert train data
df_train = pd.read_csv(TRAIN_CSV)
df_train.to_sql("passengers", conn, if_exists="replace", index=False)
print(f"Loaded {len(df_train)} train records")

# Load test data (append, since test has no 'Survived')
df_test = pd.read_csv(TEST_CSV)
df_test["survived"] = None
df_test.to_sql("passengers", conn, if_exists="append", index=False)
print(f"Appended {len(df_test)} test records. Total: {len(df_train) + len(df_test)}")

# Verify
print("\nSample data:")
print(pd.read_sql("SELECT * FROM passengers LIMIT 5", conn))

conn.close()
print("Done! Database created.")

