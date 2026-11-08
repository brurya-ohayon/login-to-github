from playwright.sync_api import Page, expect
from pages.login_github import LoginPage
from utilities.config import TEST_PASSWORD_GITHUB, TEST_EMAIL_GITHUB


def test_sign_in_to_github(page: Page):
    login = LoginPage(page)
    login.open()
    login.clickOnSignButton()
    login.waitForLoginPageLoad()

    assert TEST_EMAIL_GITHUB is not None
    assert TEST_PASSWORD_GITHUB is not None



    login.emailField().fill(TEST_EMAIL_GITHUB)
    login.PasswordField().fill(TEST_PASSWORD_GITHUB)
    login.singInWithCredent().click()

    # login.expectNotOnLoginPage()
    # expect(login.userMenu()).to_be_visible()