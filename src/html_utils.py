import requests


def fetch_html(url):
    """Fetch HTML content from the given URL. Raises HTTPError on bad response."""
    response = requests.get(url)
    response.raise_for_status()
    return response.text


def extract_headers(soup):
    """Extract (tag, text) tuples for all header tags."""
    headers = []
    for tag in soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"]):
        headers.append((tag.name.upper(), tag.get_text(strip=True)))

    return headers


def extract_main_text(soup, length=600):
    """Extract main text from <p> tags (first 600 chars by default)."""
    paragraphs = [p.get_text(strip=True) for p in soup.find_all("p")]
    main_text = " ".join(paragraphs)[:length]

    return main_text
