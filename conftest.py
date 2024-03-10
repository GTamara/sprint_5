import pytest
from selenium.webdriver.chrome.options import Options
from shared_methods import SharedMethods
from selenium import webdriver
from data.login_data import valid_login_user_data


@pytest.fixture(scope="function")
def logged_in_user(driver):
    SharedMethods.get_login_page(driver)
    SharedMethods.fill_and_submit_login_form(driver, valid_login_user_data)
    return valid_login_user_data


@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument('--window-size=1920, 1080')
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()
