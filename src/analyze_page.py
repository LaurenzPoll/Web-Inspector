import sys

from bs4 import BeautifulSoup
from header_analysis import check_header_order
from html_utils import extract_headers, extract_main_text, fetch_html


def analyze(url: str):
    try:
        html = fetch_html(url)
    except Exception as e:
        print(f"Failed to fetch {url}:\n{e}")
        return

    soup = BeautifulSoup(html, "html.parser")
    headers = extract_headers(soup)
    main_text = extract_main_text(soup)

    tips = []
    if not any(h[0] == "H1" for h in headers):
        tips.append("[MUST] Add at least one H1 header.")
    if len(headers) < 3:
        tips.append("[SHOULD] Add more header tags for better structure.")
    if len(main_text) < 200:
        tips.append("[COULD] Consider adding more main content.")
    if header_tips := check_header_order(headers):
        tips.extend(header_tips)

    print(f"Analyzing: {url}\n")
    print("Headers found:")
    for h in headers:
        print(f"- {h[0]}: {h[1]}")
    print("\nMain text (snippet):")
    print(main_text)
    print("\nSuggestions:")
    for tip in tips:
        print(tip)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        url = input("Enter the URL to analyze: ")
    else:
        url = sys.argv[1]

    analyze(url)
