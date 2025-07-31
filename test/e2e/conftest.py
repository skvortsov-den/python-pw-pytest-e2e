import pytest
from dataclasses import dataclass
from playwright.sync_api import Page
from test.e2e.api.orange_api import OrangeApi
from test.e2e.ui.orange_ui import OrangePageUi
from test.e2e.ui.orange_pim_ui import OrangePimUi

# Define fixtures for API and UI
@dataclass
class ApiFixtures:
    orange: OrangeApi

@dataclass
class UiFixtures:
    page: Page
    orange_page: OrangePageUi
    orange_pim: OrangePimUi

# Base fixtures that return instances of classes
@pytest.fixture
def api(context) -> ApiFixtures:
    """API fixture for working with API requests"""
    return ApiFixtures(
        orange=OrangeApi(context.request)
    )

@pytest.fixture
def ui(page: Page) -> UiFixtures:
    """UI fixture for working with web pages"""
    return UiFixtures(
        page=page,
        orange_page=OrangePageUi(page),
        orange_pim=OrangePimUi(page)
    )
# Short aliases for typing
Api = ApiFixtures
Ui = UiFixtures

# Export for convenience
__all__ = ['api', 'ui']