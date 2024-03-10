import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import helper_funcs
from constants.locators import Locators
from constants.urls import Urls
from constants.constants import Constants
from data.register_data import valid_register_user_data


class TestRegistrationPage:

    # перейти на страницу регистрации
    @staticmethod
    def get_registration_page(driver: WebDriver):
        driver.get(Urls.REGISTER_PAGE_URL)
        WebDriverWait(driver, Constants.TIMEOUT).until(
            expected_conditions.visibility_of_element_located(
                Locators.REGISTRATION_PAGE_PASSWORD_FIELD
            )
        )

    # заполнить и отправить форму регистрации
    @staticmethod
    def fill_and_submit_registration_form(driver: WebDriver, data):
        driver.find_element(*Locators.REGISTRATION_PAGE_NAME_FIELD).send_keys(data['name'])
        driver.find_element(*Locators.REGISTRATION_PAGE_EMAIL_FIELD).send_keys(data['email'])
        driver.find_element(*Locators.REGISTRATION_PAGE_PASSWORD_FIELD).send_keys(data['password'])
        driver.find_element(*Locators.REGISTRATION_PAGE_SUBMIT_BTN).click()

    # регистрация, позитивный сценарий
    def register_success(self, driver, data):
        self.get_registration_page(driver)
        self.fill_and_submit_registration_form(driver, data)
        WebDriverWait(driver, Constants.TIMEOUT).until(
            expected_conditions.presence_of_element_located(Locators.LOGIN_PAGE_HEADING)
        )
        return '/login' in driver.current_url

    # регистрация с валидным форматом email
    def test_register_valid_format_email_success(self, driver):
        data = {
            **valid_register_user_data,
            'email': helper_funcs.generate_email(10)
        }
        assert self.register_success(driver, data)

    # регистрация с непустым именем
    def test_register_non_empty_name_success(self, driver: WebDriver):
        data = {
            **valid_register_user_data,
            'name': helper_funcs.generate_random_string(5)
        }
        assert self.register_success(driver, data)

    # регистрация с валидным паролем > 5 символов
    @pytest.mark.parametrize(
        'password',
        [
            helper_funcs.generate_password(6),  # 6 symbols,
            helper_funcs.generate_password(7),  # 7 symbols,
            helper_funcs.generate_password(10),  # 10 symbols,
        ]
    )
    def test_register_more_than_5_symbols_password_success(self, driver, password):
        data = {
            **valid_register_user_data,
            'password': password
        }
        assert self.register_success(driver, data)

    # регистрация с НЕвалидным паролем < 5 символов
    @pytest.mark.parametrize(
        'password',
        [
            helper_funcs.generate_password(1),  # 1 symbol,
            helper_funcs.generate_password(3),  # 3 symbols,
            helper_funcs.generate_password(4),  # 4 symbols,
            helper_funcs.generate_password(5),  # 5 symbols,
        ]
    )
    def test_register_less_than_6_symbols_password_failure(self, password, driver):
        data = {
            **valid_register_user_data,
            'password': password
        }
        self.get_registration_page(driver)
        self.fill_and_submit_registration_form(driver, data)
        WebDriverWait(driver, Constants.TIMEOUT).until(
            expected_conditions.text_to_be_present_in_element(
                Locators.REGISTRATION_PAGE_PASSWORD_FIELD_ERROR_TEXT,
                'Некорректный пароль'
            )
        )
        assert driver.find_element(*Locators.REGISTRATION_PAGE_HEADING).text.lower() == 'регистрация'
        assert '/register' in driver.current_url

    # регистрация с пустым паролем
    def test_register_empty_password_failure(self, driver):
        data = {
            **valid_register_user_data,
            'password': ''
        }
        self.get_registration_page(driver)
        self.fill_and_submit_registration_form(driver, data)
        assert driver.find_element(*Locators.REGISTRATION_PAGE_HEADING).text.lower() == 'регистрация'
        assert '/register' in driver.current_url
