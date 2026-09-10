from urllib.parse import urlparse


def extract_url_features(url):

        # Normalize URL by removing trailing slash
    if url.endswith("/") and not url.endswith("://"):
        url = url.rstrip("/")
        
    parsed_url = urlparse(url)

    domain = parsed_url.netloc

    # Remove username/password if present
    if "@" in domain:
        domain = domain.split("@")[-1]

    # Remove port number
    domain_without_port = domain.split(":")[0]

    # Check whether the domain is an IP address
    is_domain_ip = 1 if all(
        part.isdigit()
        for part in domain_without_port.split(".")
        if part
    ) and "." in domain_without_port else 0

    # Count subdomains
    domain_parts = domain_without_port.split(".")
    num_subdomains = max(len(domain_parts) - 2, 0)

    # URL statistics
    num_letters = sum(char.isalpha() for char in url)
    num_digits = sum(char.isdigit() for char in url)

    # Simple obfuscation detection
    suspicious_chars = ["%", "@", "\\", ".."]
    has_obfuscation = 1 if any(
        char in url for char in suspicious_chars
    ) else 0

    num_obfuscated_chars = url.count("%")

    features = {
        "url_length": len(url),
        "domain_length": len(domain_without_port),
        "is_domain_ip": is_domain_ip,
        "num_subdomains": num_subdomains,
        "has_obfuscation": has_obfuscation,
        "num_obfuscated_chars": num_obfuscated_chars,
        "num_letters": num_letters,
        "num_digits": num_digits,
        "num_equals": url.count("="),
        "num_question_marks": url.count("?"),
        "num_ampersands": url.count("&"),
        "has_https": 1 if parsed_url.scheme.lower() == "https" else 0
    }

    return features