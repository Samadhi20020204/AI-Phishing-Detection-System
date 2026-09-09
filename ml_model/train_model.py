import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)


# ==========================================
# 1. Load Dataset
# ==========================================

df = pd.read_csv("dataset/PhiUSIIL_Phishing_URL_Dataset.csv")


# ==========================================
# 2. Select Features
# ==========================================

features = [
    "URLLength",
    "DomainLength",
    "IsDomainIP",
    "NoOfSubDomain",
    "HasObfuscation",
    "NoOfObfuscatedChar",
    "NoOfLettersInURL",
    "NoOfDegitsInURL",
    "NoOfEqualsInURL",
    "NoOfQMarkInURL",
    "NoOfAmpersandInURL",
    "IsHTTPS"
]


# Input features
X = df[features]

# Target label
y = df["label"]


# ==========================================
# 3. Split Dataset
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# ==========================================
# 4. Create Random Forest Model
# ==========================================

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)


# ==========================================
# 5. Train Model
# ==========================================

print("Training Random Forest model...")

model.fit(X_train, y_train)

print("Model training completed!")


# ==========================================
# 6. Make Predictions
# ==========================================

y_pred = model.predict(X_test)


# ==========================================
# 7. Calculate Evaluation Metrics
# ==========================================

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)


# ==========================================
# 8. Display Evaluation Results
# ==========================================

print("\nModel Evaluation:")
print("-------------------------")
print("Accuracy :", round(accuracy, 4))
print("Precision:", round(precision, 4))
print("Recall   :", round(recall, 4))
print("F1 Score :", round(f1, 4))


# ==========================================
# 9. Confusion Matrix
# ==========================================

cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix:")
print("-------------------------")
print(cm)


# ==========================================
# 10. Save Trained Model
# ==========================================

model_path = "ml_model/phishing_model.pkl"

joblib.dump(model, model_path)

print("\nModel saved successfully!")
print("Model path:", model_path)