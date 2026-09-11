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
    is_domain_ip = 1 if (
        all(
            part.isdigit()
            for part in domain_without_port.split(".")
            if part
        )
        and "." in domain_without_port
    ) else 0

    # Count subdomains
    domain_parts = domain_without_port.split(".")
    num_subdomains = max(len(domain_parts) - 2, 0)

    # URL statistics
    url_length = len(url)
    domain_length = len(domain_without_port)

    num_letters = sum(char.isalpha() for char in url)
    num_digits = sum(char.isdigit() for char in url)

    # Special character counts
    num_dots = url.count(".")
    num_hyphens = url.count("-")
    num_slashes = url.count("/")
    num_at_symbols = url.count("@")
    num_percent = url.count("%")
    num_colons = url.count(":")
    num_semicolons = url.count(";")

    # Query and path information
    path = parsed_url.path
    query = parsed_url.query

    path_length = len(path)
    query_length = len(query)

    # Simple obfuscation detection
    suspicious_chars = ["%", "@", "\\", ".."]

    has_obfuscation = 1 if any(
        char in url for char in suspicious_chars
    ) else 0

    # Suspicious words commonly seen in phishing URLs
    suspicious_words = [
        "login",
        "signin",
        "verify",
        "verification",
        "account",
        "update",
        "secure",
        "security",
        "password",
        "confirm",
        "bank",
        "payment",
        "recover",
        "webscr",
        "credential"
    ]

    url_lower = url.lower()

    num_suspicious_words = sum(
        word in url_lower
        for word in suspicious_words
    )

    has_suspicious_word = 1 if num_suspicious_words > 0 else 0

    features = {

        # Existing features
        "url_length": url_length,
        "domain_length": domain_length,
        "is_domain_ip": is_domain_ip,
        "num_subdomains": num_subdomains,
        "has_obfuscation": has_obfuscation,
        "num_obfuscated_chars": num_percent,
        "num_letters": num_letters,
        "num_digits": num_digits,
        "num_equals": url.count("="),
        "num_question_marks": url.count("?"),
        "num_ampersands": url.count("&"),
        "has_https": 1 if parsed_url.scheme.lower() == "https" else 0,

        # New URL structure features
        "num_dots": num_dots,
        "num_hyphens": num_hyphens,
        "num_slashes": num_slashes,
        "num_at_symbols": num_at_symbols,
        "num_colons": num_colons,
        "num_semicolons": num_semicolons,
        "path_length": path_length,
        "query_length": query_length,
        "has_suspicious_word": has_suspicious_word,
        "num_suspicious_words": num_suspicious_words
    }

    return features