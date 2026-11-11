import os
from dotenv import load_dotenv

load_dotenv()

GITHUB_URL = "https://github.com"
TEST_EMAIL_GITHUB = os.getenv("TEST_EMAIL_GITHUB")
TEST_PASSWORD_GITHUB = os.getenv("TEST_PASSWORD_GITHUB")
