# Website Improver

Minimal tool to analyze a webpage’s content (headers, text, etc.) and suggest improvements using the MoSCoW prioritization method.

## Features

- Fetches and parses a single webpage
- Extracts all headers (`h1`–`h6`) and main text
- Outputs a list of actionable suggestions (suggestions are prioritized as Must, Should, or Could based on their impact on website quality)

## Usage

### CLI

```bash
python main.py <URL>
```

### Output
- List of headers found
- Main text snippet
- MoSCoW-classified improvement tips

## Requirements
- Python 3.13.5
- requests
- beautifulsoup4

Install dependencies:
```bash
pip install -r requirements.txt
```

## Roadmap
- Support for batch/multi-page analysis
- Advanced recommendations (SEO, accessibility, etc.)
- Web interface

License
MIT License