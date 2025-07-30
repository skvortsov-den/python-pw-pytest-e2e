from playwright.sync_api import APIRequestContext

class Api:
    """Base class for API objects"""
    def __init__(self, request: APIRequestContext):
        self.request = request 