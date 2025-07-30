from setuptools import setup, find_packages

setup(
    name="python-pw-pytest-e2e",
    version="1.0.0",
    description="E2E Tests with Python + Playwright + Pytest",
    author="Denis Skvortsov",
    packages=find_packages(),
    install_requires=[
        "pytest>=7.4.3",
        "pytest-playwright>=0.4.3",
        "playwright>=1.40.0",
        "faker>=20.1.0",
        "pytest-html>=4.1.1",
        "pytest-xdist>=3.3.1",
    ],
    python_requires=">=3.8",
) 