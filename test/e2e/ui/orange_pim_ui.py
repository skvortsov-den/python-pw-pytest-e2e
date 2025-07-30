import os
from test.e2e.ui.base_ui import Ui
from playwright.sync_api import Locator

class OrangePimUi(Ui):
    """UI класс для работы с PIM модулем OrangeHRM"""
    def __init__(self, page):
        super().__init__(page)
        # Используем абсолютный путь к файлу аватара
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.avatar_path = os.path.join(current_dir, '..', 'test-data', 'test_avatar.jpg')
        
    # Locators
    def _field_employee_id(self) -> Locator:
        return self.page.get_by_role('textbox').nth(2)
    def _button_search(self) -> Locator:
        return self.page.get_by_role('button', name='Search')
    def _row_employee(self, name: str) -> Locator:
        return self.page.get_by_role('row').filter(has_text=name).first
    def _pencil_button(self, name: str) -> Locator:
        return self._row_employee(name).locator('.oxd-icon.bi-pencil-fill')
    def _avatar_icon(self) -> Locator:
        return self.page.locator('.orangehrm-edit-employee-image')
    def _avatar_image(self) -> Locator:
        return self._avatar_icon().locator('img')
    def _file_input(self) -> Locator:
        return self.page.locator('input[type="file"]')
    def _save_button(self) -> Locator:
        return self.page.get_by_role('button', name='Save')


    # Actions
    def goto(self) -> None:
        """Transition to the employee list page"""
        self.page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList')
    
    def find_employee(self, employee_id: str) -> None:
        """Search for an employee by ID"""
        self._field_employee_id().fill(employee_id)
        self._button_search().click()
    
    def change_employee_data(self, name: str) -> None:
        """Editing employee data"""
        self._pencil_button(name).click()
    
    def update_avatar_employee(self) -> None:
        """Updating employee avatar"""
        self._avatar_icon().click()
        # File input may be hidden, but accessible for upload
        self._file_input().set_input_files(self.avatar_path)
        self._save_button().click()
        # Wait for UI update after file upload
        self.page.wait_for_timeout(5000)
        # Wait for avatar element stabilization
        self._avatar_icon().wait_for(state="visible")

    def get_avatar_screenshot(self) -> bytes:
        """Getting avatar screenshot"""
        # Wait for element stabilization before screenshot
        self._avatar_icon().wait_for(state="visible")
        return self._avatar_icon().screenshot()

    # Assertions
    def assert_employee_visible(self, name: str) -> None:
        """Checking employee visibility"""
        self._row_employee(name).wait_for(state="visible")
    
    def assert_avatar_updated(self, old_avatar: bytes) -> None:
        """Checking avatar update"""
        new_avatar = self.get_avatar_screenshot()
        assert new_avatar != old_avatar, "Avatar was not updated" 