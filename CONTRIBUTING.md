# Contributing

Thanks for helping improve Scientific Calculator. Keep contributions focused, readable, and easy to test.

## Local Setup

```bash
git clone https://github.com/Rvx0098/scientific_calculator.git
cd scientific_calculator
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Open `http://localhost:10000` in your browser.

## Contribution Ideas

- Add keyboard support
- Add more scientific operations
- Improve mobile layout
- Add unit tests for calculator expressions
- Improve accessibility labels and focus states
- Add deployment documentation

## Pull Request Checklist

- Keep the pull request focused on one improvement
- Test the UI locally
- Test `/calculate` with valid and invalid expressions
- Avoid committing secrets, virtual environments, caches, or generated files
- Add screenshots for UI changes

## Code Guidelines

- Keep backend expression evaluation restricted and explicit
- Avoid reintroducing unrestricted `eval`
- Use descriptive function names
- Prefer small, testable changes
