import re
from typing import Dict, Any, Optional
from faker import Faker
from playwright.sync_api import APIResponse
from test.e2e.api.base_api import Api

class OrangeApi(Api):
    """API class for working with OrangeHRM"""
    
    def __init__(self, request):
        super().__init__(request)
        self.base_url = 'https://opensource-demo.orangehrmlive.com'
        self.endpoints = {
            'login': '/web/index.php/auth/login',
            'validate': '/web/index.php/auth/validate'
        }
        self.fake = Faker()
    
    def generate_fake_employee(self) -> Dict[str, Any]:
        """Generates fake employee data"""
        return {
            'empPicture': None,
            'employeeId': self.fake.numerify(text='####'),
            'firstName': self.fake.first_name(),
            'lastName': self.fake.last_name(),
            'middleName': self.fake.last_name()
        }
    
    def generate_fake_user(self) -> Dict[str, Any]:
        """Generates fake user data"""
        return {
            'username': self.fake.user_name().lower(),
            'password': self.fake.password(length=8),
            'status': True,
            'userRoleId': 2,
            'empNumber': int(self.fake.numerify(text='###'))
        }
    
    def auth(self, credentials: Optional[Dict[str, str]] = None) -> APIResponse:
        """Authentication in the system"""
        if credentials is None:
            credentials = {'username': 'Admin', 'password': 'admin123'}
        
        token = self.get_token()
        
        return self.request.post(
            f"{self.base_url}{self.endpoints['validate']}",
            headers={'Content-Type': 'application/x-www-form-urlencoded'},
            form={'_token': token, **credentials}
        )
    
    def get_token(self) -> str:
        """Gets the authentication token"""
        response = self.request.get(f"{self.base_url}{self.endpoints['login']}")
        html = response.text()
        
        token_match = re.search(r':token="([^"]+)"', html)
        if token_match:
            token = token_match.group(1).replace('&quot;', '')
            return token
        else:
            raise Exception('[API] Auth token not found')
    
    def create_employee(self, employee_data: Optional[Dict[str, Any]] = None) -> APIResponse:
        """Creates an employee through API"""
        if employee_data is None:
            employee_data = self.generate_fake_employee()
        
        return self.request.post(
            f"{self.base_url}/web/index.php/api/v2/pim/employees",
            headers={'Content-Type': 'application/json'},
            data=employee_data
        )
    
    def create_user(self, user_data: Dict[str, Any]) -> APIResponse:
        """Creates a user through API"""
        return self.request.post(
            f"{self.base_url}/web/index.php/api/v2/admin/users",
            headers={'Content-Type': 'application/json'},
            data=user_data
        )
    
    def create_employee_and_user(
        self, 
        employee_data: Optional[Dict[str, Any]] = None,
        user_data: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Creates an employee and a user"""
        if employee_data is None:
            employee_data = self.generate_fake_employee()
        if user_data is None:
            user_data = self.generate_fake_user()
        
        self.create_employee(employee_data)
        self.create_user(user_data)
        
        return {'employeeData': employee_data, 'userData': user_data} 