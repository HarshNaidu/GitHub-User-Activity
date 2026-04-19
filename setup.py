from setuptools import setup, find_packages

setup(
    name = "github-activity-cli",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "requests",
        "python-dotenv"
    ],
    entry_points={
        "console_scripts": [
            "github-activity=github_activity.main:main"
        ]
    }
)