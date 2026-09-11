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

from feature_extraction import extract_url_features


# ==========================================
# 1. Load Dataset
# ==========================================

print("Loading dataset...")

df = pd.read_csv("dataset/PhiUSIIL_Phishing_URL_Dataset.csv")

print("Dataset loaded successfully!")
print("Number of URLs:", len(df))


# ==========================================
# 2. Extract Features From URLs
# ==========================================

print("\nExtracting URL features...")

feature_data = []

for url in df["URL"]:
    extracted = extract_url_features(url)

    feature_data.append({
    "url_length": extracted["url_length"],
    "domain_length": extracted["domain_length"],
    "is_domain_ip": extracted["is_domain_ip"],
    "num_subdomains": extracted["num_subdomains"],
    "has_obfuscation": extracted["has_obfuscation"],
    "num_obfuscated_chars": extracted["num_obfuscated_chars"],
    "num_letters": extracted["num_letters"],
    "num_digits": extracted["num_digits"],
    "num_equals": extracted["num_equals"],
    "num_question_marks": extracted["num_question_marks"],
    "num_ampersands": extracted["num_ampersands"],
    "has_https": extracted["has_https"],

    "num_dots": extracted["num_dots"],
    "num_hyphens": extracted["num_hyphens"],
    "num_slashes": extracted["num_slashes"],
    "num_at_symbols": extracted["num_at_symbols"],
    "num_colons": extracted["num_colons"],
    "num_semicolons": extracted["num_semicolons"],
    "path_length": extracted["path_length"],
    "query_length": extracted["query_length"],
    "has_suspicious_word": extracted["has_suspicious_word"],
    "num_suspicious_words": extracted["num_suspicious_words"]
})


X = pd.DataFrame(feature_data)

print("Feature extraction completed!")


# ==========================================
# 3. Target Label
# ==========================================

y = df["label"]


# ==========================================
# 4. Split Dataset
# ==========================================

print("\nSplitting dataset...")

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# ==========================================
# 5. Create Random Forest Model
# ==========================================

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)


# ==========================================
# 6. Train Model
# ==========================================

print("\nTraining Random Forest model...")

model.fit(X_train, y_train)

print("Model training completed!")


# ==========================================
# 7. Make Predictions
# ==========================================

y_pred = model.predict(X_test)


# ==========================================
# 8. Calculate Evaluation Metrics
# ==========================================

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)


# ==========================================
# 9. Display Evaluation Results
# ==========================================

print("\nModel Evaluation:")
print("-------------------------")
print("Accuracy :", round(accuracy, 4))
print("Precision:", round(precision, 4))
print("Recall   :", round(recall, 4))
print("F1 Score :", round(f1, 4))


# ==========================================
# 10. Confusion Matrix
# ==========================================

cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix:")
print("-------------------------")
print(cm)


# ==========================================
# 11. Save Trained Model
# ==========================================

model_path = "ml_model/phishing_model.pkl"

joblib.dump(model, model_path)

print("\nModel saved successfully!")
print("Model path:", model_path)