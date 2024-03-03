import pytest
from selenium.webdriver.chrome.options import Options

import helper_funcs
from selenium import webdriver


@pytest.fixture(scope="function", autouse=True)
def valid_register_user_data():
    return {
        'name': 'Имя',
        'email': helper_funcs.generate_email(20),
        'password': 'password',
    }


@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument('--window-size=1920, 1080')
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()
