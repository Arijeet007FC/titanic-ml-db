import pandas as pd
import sqlite3
from sklearn.linear_model import LogisticRegression

print("🔮 Generating Kaggle submission...")

# Load FULL test data (418 rows exactly)
conn = sqlite3.connect('../titanic.db')
df_test = pd.read_sql('SELECT * FROM passengers WHERE PassengerId > 891', conn)
print(f"Test set loaded: {len(df_test)} rows")  # Must be 418
conn.close()

# Features (fill missing values)
df_test_ml = df_test[['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare']].copy()
df_test_ml['Age'].fillna(df_test_ml['Age'].median(), inplace=True)
df_test_ml['Fare'].fillna(df_test_ml['Fare'].median(), inplace=True)
df_test_ml['Sex'] = df_test_ml['Sex'].map({'male': 0, 'female': 1})

# Train on full training data
conn = sqlite3.connect('../titanic.db')
df_train = pd.read_sql('SELECT * FROM passengers WHERE PassengerId <= 891', conn)
df_train_ml = df_train[['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Survived']].dropna()
df_train_ml['Sex'] = df_train_ml['Sex'].map({'male': 0, 'female': 1})

model = LogisticRegression(max_iter=200)
model.fit(df_train_ml[['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare']], df_train_ml['Survived'])

# Predict ALL 418 test rows
predictions = model.predict(df_test_ml)

# Kaggle format (PassengerId 892-1309)
submission = pd.DataFrame({
    'PassengerId': df_test['PassengerId'],
    'Survived': predictions
})

submission.to_csv('../submission.csv', index=False)
print("✅ submission.csv created (418 rows)!")
print(f"Rows: {len(submission)}, Survival rate: {predictions.mean():.1%}")
print(submission.head())
print("\n📤 Upload submission.csv to Kaggle!")
