# Website Improver

Minimal tool to analyze a webpage’s content (headers, text, etc.) and suggest improvements using the MoSCoW prioritization method.

## Features

- Fetches and parses a single webpage
- Extracts all headers (`h1`–`h6`) and main text
- Outputs a list of actionable suggestions (suggestions are prioritized as Must, Should, or Could based on their impact on website quality)

## Usage

### CLI

```bash
python analyse_page.py <URL>
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

## Branch Naming Conventions

The following branch prefixes are used to keep the Git history clean and descriptive:

| Prefix      | Purpose                                   | Example                    |
|-------------|-------------------------------------------|----------------------------|
| `feat/`     | New features                              | `feat/header-validation`   |
| `fix/`      | Bug fixes                                 | `fix/empty-header-bug`     |
| `refactor/` | Refactoring code, no functional change    | `refactor/modularize`      |
| `test/`     | Adding or updating tests                  | `test/header-analysis`     |
| `docs/`     | Documentation changes                     | `docs/readme-clarity`      |
| `chore/`    | Maintenance, tooling, dependency updates  | `chore/update-deps`        |

- Use descriptive branch names, e.g., `feat/scraper-cli` instead of just `feat/cli`.
- Always start a new branch from the latest `main`.

## License
MIT License