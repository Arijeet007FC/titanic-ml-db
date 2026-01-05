import pandas as pd
import sqlite3
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import joblib

# Load test data (no Survived column)
conn = sqlite3.connect('../titanic.db')
df_test = pd.read_sql('SELECT * FROM passengers WHERE survived IS NULL', conn)
conn.close()

print(f"Test set: {len(df_test)} passengers")

# Prepare features (same as training)
features = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare']
df_test_ml = df_test[features].dropna()
df_test_ml['Sex'] = df_test_ml['Sex'].map({'male': 0, 'female': 1})

# Train model on all training data
conn = sqlite3.connect('../titanic.db')
df_train = pd.read_sql('SELECT * FROM passengers WHERE survived IS NOT NULL', conn)
df_train_ml = df_train[features + ['Survived']].dropna()
df_train_ml['Sex'] = df_train_ml['Sex'].map({'male': 0, 'female': 1})

model = LogisticRegression(max_iter=200)
model.fit(df_train_ml[features], df_train_ml['Survived'])

# Predict
predictions = model.predict(df_test_ml)
submission = pd.DataFrame({
    'PassengerId': df_test_ml.index + 1,  # Adjust IDs
    'Survived': predictions
})

submission.to_csv('../submission.csv', index=False)
print("submission.csv created! Upload to Kaggle.")
print(submission.head())
joblib.dump(model, '../model.pkl')  # Save model
print("Model saved as model.pkl")
