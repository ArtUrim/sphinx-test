 # Sphinx Test Cases Documentation Extension

A Sphinx extension for comprehensive test case documentation that bridges the gap between test code and documentation. This extension allows you to document test cases either through reStructuredText files or directly from Python test function docstrings.

## Features

- Document test cases using reStructuredText or Python docstrings
- Auto-generate test documentation from pytest functions
- Create organized test suites with requirement traceability
- Generate comprehensive test indices
- Support for detailed test case documentation including:
  - Test suites grouping
  - Requirements coverage
  - Initial conditions
  - Test steps
  - Pass/fail criteria

## Installation

Install via pip:

```bash
pip install sphinx_test_cases
```

## Quick Start

1. Add 'sphinx_test_cases' to your Sphinx extensions in conf.py:

```python
extensions = [
    'sphinx_test_cases'
]
```

2. Document your tests using the directive:

```rst
.. test:test:: my_test_name
   :suite: regression, integration
   :reqs: REQ001, REQ002

   Test description here...
```

## Documentation Formats

### reStructuredText Format

Create dedicated .rst files for test documentation:

```rst
.. test:test:: login_validation
   :suite: security, user-management
   :reqs: SEC001, AUTH002
   :init:
      - System is running
      - Database is accessible
   :step:
      - Enter invalid credentials
      - Click login button
   :pass: System shows error message
```

### Python Docstring Format

Document tests directly in your pytest functions:

```python
def test_login_validation():
    """Test login validation

    :suite: security, user-management
    :reqs: SEC001, AUTH002
    :init: System is running
           Database is accessible
    :step: Enter invalid credentials
           Click login button
    :pass: System shows error message
    """
    # Test implementation
```

## Available Fields

- **suite**: Test suite categories (comma-separated)
- **reqs**: Requirements covered (comma-separated)
- **init**: Initial conditions (multiple allowed)
- **step**: Test steps (automatically enumerated)
- **pass**: Pass/fail criteria (can be labeled for multiple criteria)

## Generated Indices

The extension automatically generates three indices:

- **Requirements Index**: Lists all requirements and their test coverage
- **Test Cases Index**: Alphabetical listing of all test cases
- **Test Suites Index**: Organized view of test suites and their tests

Access indices using:
- :ref:`test-requirement`
- :ref:`test-test`
- :ref:`test-suite`

## Examples

The repository includes two example implementations:

1. **Standalone Example**: Test documentation using pure reStructuredText
2. **Docstring Example**: Test documentation within Python test functions

## Source Code

Access the source code and examples on GitHub:

```bash
git clone https://github.com/ArtUrim/sphinx-test
```

## Development Setup

For development, it's recommended to use Python virtual environments:

1. Create and activate a virtual environment
2. Install development dependencies
3. Run tests and build documentation

## Acknowledgments

This extension is based on examples from the Sphinx documentation:
- Recipes tutorial
- Intenum tutorial
