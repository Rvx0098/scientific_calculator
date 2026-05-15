# Security Policy

## Supported Versions

Security updates are applied to the default branch.

| Version | Supported |
| --- | --- |
| Default branch | Yes |

## Reporting a Vulnerability

Please do not open a public issue with exploit details. Contact the maintainer privately through GitHub or the contact details on the maintainer profile.

Include:

- Description of the vulnerability
- Steps to reproduce
- Impact
- Suggested fix, if available

## Security Notes

- The current app does not require secrets or API keys
- `.env` files are ignored and should not be committed
- Expression evaluation is intentionally restricted through an AST allowlist
- Any future external integrations should use environment variables
- Avoid adding unrestricted `eval`, shell execution, or dynamic imports from user input
