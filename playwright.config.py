import pytest

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """Configure browser context arguments"""
    return {
        **browser_context_args,
        "ignore_https_errors": True,
        "viewport": {
            "width": 1920,
            "height": 1080,
        },
    }

@pytest.fixture(scope="session")
def browser_type_launch_args():
    """Configure browser launch arguments"""
    return {
        "headless": True,  # Changed to headless for stability
        "slow_mo": 500,    # Reduced delay time
    } 