
import joblib
import pandas as pd

from ml_model.feature_extraction import extract_url_features


# ==========================================
# Load the trained model
# ==========================================

model = joblib.load("ml_model/phishing_model.pkl")


# ==========================================
# URL Prediction Function
# ==========================================

def predict_url(url):

    # --------------------------------------
    # 1. Extract features from URL
    # --------------------------------------

    extracted = extract_url_features(url)

    # --------------------------------------
    # 2. Display extracted features
    # --------------------------------------

    print("\n======================================")
    print("URL:", url)
    print("======================================")

    print("\nExtracted Features:")

    for key, value in extracted.items():
        print(f"{key}: {value}")

    # --------------------------------------
    # 3. Create DataFrame
    # --------------------------------------

    features = pd.DataFrame([{
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
        "has_https": extracted["has_https"]
    }])

    # --------------------------------------
    # 4. Make prediction
    # --------------------------------------

    prediction = model.predict(features)[0]

    # --------------------------------------
    # 5. Get prediction probabilities
    # --------------------------------------

    probabilities = model.predict_proba(features)[0]

    print("\nRaw Model Prediction:", prediction)

    print("\nPrediction Probabilities:")

    for class_label, probability in zip(model.classes_, probabilities):
        print(
            f"Class {class_label}: "
            f"{probability * 100:.2f}%"
        )

    # --------------------------------------
    # 6. Convert prediction to readable result
    #
    # Dataset:
    # 0 = Phishing
    # 1 = Legitimate
    # --------------------------------------

    if prediction == 1:
        result = "Legitimate"
    else:
        result = "Phishing"

    print("\nFinal Prediction:", result)

    print("======================================\n")

    return result


# ==========================================
# Test Prediction
# ==========================================

if __name__ == "__main__":

    test_url = "https://www.google.com"

    result = predict_url(test_url)

    print("Test URL:", test_url)
    print("Prediction:", result)

