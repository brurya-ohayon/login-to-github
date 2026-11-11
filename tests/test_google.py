import pytest
from selenium.webdriver.common.by import By


# @pytest.fixture
# def driver():
#     driver = webdriver.Chrome()
#     yield driver
#     driver.quit()  # runs even if the test fails

@pytest.mark.selenuim
def test_google_title(driver):
    driver.get("https://www.google.com")
    print(f"Driver:{driver}")
    assert driver.title == "Google"
    driver.quit()

@pytest.mark.selenuim
def test_google_search(driver):
    driver.get("https://www.google.com")
    searchField = driver.find_element(By.NAME , "q")
    searchField.send_keys("TEST")
    searchField.submit()

@pytest.mark.selenuim
def test_google_search(driver):
    driver.get("https://www.google.com")
    searchField = driver.find_element(By.NAME , "q")
    searchField.send_keys("TEST")
    searchField.submit()

@pytest.mark.selenuim
def test_google_search(driver):
    driver.get("https://www.google.com")
    searchField = driver.find_element(By.NAME , "q")
    searchField.send_keys("TEST")
    searchField.submit()
    