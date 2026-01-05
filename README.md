# 🚢 Titanic ML + Database Project

**End-to-end data science pipeline** (74.8% accuracy)

## 📊 Results
| Component | Status |
|-----------|--------|
| Database | 1309 passengers in SQLite |
| EDA | Class 1 (60%), Female (75%) survival |
| Model | Logistic Regression **74.8%** accuracy |
| Kaggle | submission.csv ready (~0.77 score) |

## 🚀 Usage

```bash
git clone https://github.com/Arijeet007FC/titanic-ml-db
cd titanic-ml-db
pip install -r requirements.txt

# Download Titanic CSVs to data/
python src/load_data.py          # Create titanic.db
jupyter notebook notebooks/01_eda_ml.ipynb  # EDA + model
python src/make_submission.py    # Kaggle submission.csv

