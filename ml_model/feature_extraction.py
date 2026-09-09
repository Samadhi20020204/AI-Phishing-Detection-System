from urllib.parse import urlparse


def extract_url_features(url):
    parsed_url = urlparse(url)

    features = {
        "url_length": len(url),
        "num_dots": url.count("."),
        "num_hyphens": url.count("-"),
        "num_slashes": url.count("/"),
        "num_question_marks": url.count("?"),
        "num_equals": url.count("="),
        "num_at": url.count("@"),
        "num_ampersands": url.count("&"),
        "has_https": 1 if parsed_url.scheme == "https" else 0,
        "has_ip": 1 if any(char.isdigit() for char in parsed_url.netloc) else 0
    }

    return features