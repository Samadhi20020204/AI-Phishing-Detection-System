import joblib
import pandas as pd

from feature_extraction import extract_url_features


# Load the trained model
model = joblib.load("ml_model/phishing_model.pkl")


def predict_url(url):
    # Extract features from the URL
    extracted = extract_url_features(url)

    # Use the same feature names used during model training
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

    # Make prediction
    prediction = model.predict(features)[0]

    # Convert prediction into readable result
    if prediction == 1:
        return "Legitimate"
    else:
        return "Phishing"


# Test the prediction system
if __name__ == "__main__":

    test_url = "https://www.google.com"

    result = predict_url(test_url)

    print("URL:", test_url)
    print("Prediction:", result)