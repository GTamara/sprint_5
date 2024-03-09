import pytest
from selenium.webdriver.chrome.options import Options
from shared_methods import SharedMethods

import helper_funcs
from selenium import webdriver


@pytest.fixture(scope="function", autouse=True)
def valid_register_user_data():
    return {
        'name': 'Имя',
        'email': helper_funcs.generate_email(20),
        'password': 'password',
    }

@pytest.fixture(scope="function", autouse=True)
def valid_login_user_data():
    return {
        'email': 'qq@mail.ru',
        'password': '123123',
    }

@pytest.fixture(scope="function")
def logged_in_user(valid_login_user_data, driver):
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

