import pytest
from test.e2e.conftest import Api, Ui

@pytest.mark.test1
def test_auth_after_api(api: Api, ui: Ui):
    """Test authentication in UI after API authentication"""
    api.orange.auth()
    
    ui.orange_page.goto()
    ui.orange_page.assert_widget_visible('My Actions')

@pytest.mark.test2
def test_create_user_and_employee(api: Api, ui: Ui):
    """Test creating a new user and employee through API and checking in UI"""
    api.orange.auth()
    user = api.orange.create_employee_and_user()

    ui.orange_pim.goto()
    ui.orange_pim.find_employee(user['employeeData']['employeeId'])
    ui.orange_pim.assert_employee_visible(user['employeeData']['firstName'])

@pytest.mark.test3
def test_update_avatar(api: Api, ui: Ui):
    """Test updating employee avatar through API and checking in UI"""
    api.orange.auth()
    user = api.orange.create_employee_and_user()

    ui.orange_pim.goto()
    ui.orange_pim.find_employee(user['employeeData']['employeeId'])
    ui.orange_pim.change_employee_data(user['employeeData']['firstName'])
    
    old_avatar = ui.orange_pim.get_avatar_screenshot()
    ui.orange_pim.update_avatar_employee()
    ui.orange_pim.assert_avatar_updated(old_avatar) 