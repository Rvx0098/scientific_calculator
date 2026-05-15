# Scientific Calculator

![Status](https://img.shields.io/badge/status-active-brightgreen)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Flask](https://img.shields.io/badge/Flask-3.x-black)
![Frontend](https://img.shields.io/badge/frontend-HTML%20%7C%20CSS%20%7C%20JavaScript-orange)
![License](https://img.shields.io/badge/license-MIT-green)

> A lightweight Flask-powered scientific calculator with a clean browser UI and a safer backend expression evaluator.

## Overview

`scientific_calculator` is a compact web application that performs standard arithmetic and scientific calculations through a Flask API and a responsive HTML/CSS/JavaScript interface. It demonstrates frontend interaction, JSON API requests, Python routing, and secure server-side expression handling.

The project is intentionally small, making it easy to understand, deploy, and extend with more advanced calculator features.

## Features

- Browser-based calculator interface
- Flask backend endpoint for expression evaluation
- Basic arithmetic operations: addition, subtraction, multiplication, and division
- Scientific functions: `sin`, `cos`, `tan`, `log`, `ln`, and `sqrt`
- Mathematical constants: `pi` and `e`
- Clear/reset button for fast input correction
- JSON-based `/calculate` API
- AST-based expression parsing instead of unrestricted Python `eval`
- Deployment-ready `PORT` environment variable support

## Tech Stack

| Layer | Technology |
| --- | --- |
| Backend | Python, Flask |
| Frontend | HTML5, CSS3, JavaScript |
| API | JSON over HTTP |
| Runtime | Local Python server or hosted WSGI platform |
| Configuration | Environment variable based port configuration |

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Rvx0098/scientific_calculator.git
cd scientific_calculator
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it:

```bash
# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the App

```bash
python app.py
```

By default, the app runs on:

```text
http://localhost:10000
```

To use another port:

```powershell
$env:PORT=5000
python app.py
```

## Project Structure

```bash
scientific_calculator/
+-- app.py                  # Flask app, routes, and safe expression evaluator
+-- requirements.txt        # Python dependencies
+-- settings.json           # Local editor/server configuration
+-- templates/
|   +-- index.html          # Calculator page markup
+-- static/
|   +-- style.css           # Calculator styling
|   +-- script.js           # Frontend input handling and API calls
+-- .github/                # Issue and pull request templates
+-- .env.example            # Environment variable reference
+-- README.md               # Project documentation
+-- LICENSE                 # MIT license
```

## API Documentation

### `GET /`

Renders the calculator UI.

### `POST /calculate`

Evaluates a calculator expression and returns the result.

Request:

```json
{
  "expression": "sqrt(16)+log(100)"
}
```

Response:

```json
{
  "result": 6.0
}
```

Error response:

```json
{
  "result": "Error"
}
```

## Security

The calculator parses expressions with Python's `ast` module and only permits a defined set of numeric operations, constants, and math functions. This avoids exposing Python builtins or arbitrary code execution.

Security practices included:

- No API keys or credentials required
- Environment files ignored through `.gitignore`
- Restricted expression evaluation
- JSON request parsing with safe fallback behavior
- Clear guidance for future environment variables in `.env.example`

See [SECURITY.md](SECURITY.md) for the security policy.

## Performance

- Minimal dependency footprint
- Static frontend assets served by Flask
- Lightweight JSON API response cycle
- No database or external service dependency

## Screenshots

Add a screenshot or short demo GIF to improve recruiter and portfolio presentation:

```markdown
![Scientific Calculator UI](docs/calculator-preview.png)
```

## Roadmap

- Add keyboard input support
- Add parentheses and exponent buttons to the UI
- Add calculation history
- Add unit tests for expression evaluation
- Add deployment guide for Render, Railway, or PythonAnywhere
- Improve mobile responsiveness and accessibility states

## Contributing

Contributions are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## Suggested GitHub Description

Flask scientific calculator with a clean web UI, JSON calculation API, and safe Python expression evaluation.
