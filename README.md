# E2E tests with python + playwright + pytest

Framework for automated web application testing. Testing https://opensource-demo.orangehrmlive.com/ through API and UI

## Architecture

- **Pytest** — runs tests and manages fixtures
- **Playwright** — automates browser (clicks, form filling, checks)
- **Feature Object Model** — all elements and locators for one feature are collected in a separate class
- **API layer** — separate API layer for data creation and management
- **Dataclass fixtures** — convenient access to testing objects
- **Faker** — generates random test data

## Project Structure

```
test-repo-python/
├── test/
│   └── e2e/
│       ├── api/                    # API work
│       │   ├── base_api.py         # Base API class
│       │   └── orange_api.py       # OrangeHRM API
│       ├── ui/                     # Interface work
│       │   ├── base_ui.py          # Base UI class
│       │   ├── orange_ui.py        # Main page + locators
│       │   └── orange_pim_ui.py    # Employee page + locators
│       ├── tests/
│       │   └── test_orange.py      # Tests
│       ├── test-data/
│       │   └── test_avatar.jpg     # File for upload
│       └── conftest.py             # Test settings
├── pytest.ini                      # Pytest configuration
├── playwright.config.py            # Browser configuration
├── requirements.txt                # Libraries
└── README.md                       # Documentation
```

## Quick Start

### Installation
```bash
# Install Python 3.8+ (if not installed)
# https://www.python.org/downloads/

# Install libraries
pip install -r requirements.txt

# Install browsers
playwright install
```

### Running Tests

#### All tests
```bash
python3 -m pytest --headed
```

#### Individual tests
```bash
python3 -m pytest -m test1 --headed  # Authentication
python3 -m pytest -m test2 --headed  # Create employee
python3 -m pytest -m test3 --headed  # Upload avatar
```

#### Without opening browser
```bash
python3 -m pytest -m test1
```

## How it works

### Convenient access to objects
```python
from test.e2e.conftest import Api, Ui

def test_example(api: Api, ui: Ui):
    # Convenient access to objects via dot notation
    api.orange.auth()
    ui.orange_page.goto()
    ui.orange_pim.find_employee("123")
```

### Creating data through API
```python
def test_create_user_and_employee(api: Api, ui: Ui):
    # Quickly create employee through API
    user = api.orange.create_employee_and_user()
    
    # Check that it appeared in interface
    ui.orange_pim.goto()
    ui.orange_pim.find_employee(user['employeeData']['employeeId'])
    ui.orange_pim.assert_employee_visible(user['employeeData']['firstName'])
```

## What we test

| Test | What it does | Why needed |
|------|-------------|------------|
| `test1` | UI authentication after API | Check that API authentication works |
| `test2` | Create employee through API, check in UI | Test API and UI integration |
| `test3` | Upload employee avatar | Check file upload |

## 🔧 Configuration

### pytest.ini - test settings
```ini
[pytest]
testpaths = test/e2e              # Where to look for tests
python_files = test_*.py          # Which files to test
addopts = 
    --tb=short                    # Short errors
    -v                           # Verbose output
markers =                        # Tags for grouping tests
    test1: mark test as test1
    test2: mark test as test2
    test3: mark test as test3
```

## 🛠️ Debugging

### Playwright Inspector - step-by-step debugging
```bash
PWDEBUG=1 python3 -m pytest -m test1 --headed
```

### Developer Tools - like in browser
```bash
PWDEBUG=console python3 -m pytest -m test1 --headed
```

### Pause in test
```python
def test_example(api: Api, ui: Ui):
    api.orange.auth()
    ui.page.pause()  # Stop for debugging
    ui.orange_page.goto()
```

## Why exactly this way?

### API layer
- **Faster** - API works faster than UI
- **More stable** - less dependent on interface
- **More reliable** - fewer random errors

### Feature Object Model
- **Locators in one place** - all selectors for feature are collected in class
- **Reusability** - one class for all feature tests
- **Maintenance** - easy to change locator in one place
- **Readability** - clear what each method does

### Dataclass fixtures
- **Convenience** - access to objects via dot notation
- **Typing** - IDE suggests methods
- **Compactness** - less code in tests

## 🔗 Useful links

- [Playwright Python](https://playwright.dev/python/)
- [Pytest](https://docs.pytest.org/)
- [Faker](https://faker.readthedocs.io/)

---

**Ready to use! 🚀** 