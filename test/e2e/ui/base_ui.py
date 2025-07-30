from playwright.sync_api import Page

class Ui:
    """Base class for UI objects"""
    def __init__(self, page: Page):
        self.page = page 