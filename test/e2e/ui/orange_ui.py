from test.e2e.ui.base_ui import Ui
from playwright.sync_api import Locator

class OrangePageUi(Ui):
    """UI class for working with the main page of OrangeHRM"""
    def __init__(self, page):
        super().__init__(page)
    
    # Locators
    def _widget_button(self, name: str) -> Locator:
        return self.page.locator('.orangehrm-dashboard-widget-name').filter(has_text=name)
    
    # Actions
    def goto(self) -> None:
        """Transition to the main page"""
        self.page.goto('https://opensource-demo.orangehrmlive.com/')

    # Assertions
    def assert_widget_visible(self, name: str) -> None:
        """Checking widget visibility"""
        self._widget_button(name).wait_for(state="visible") 