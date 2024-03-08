import time

import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import helper_funcs
from constants.locators import Locators
from  constants.urls import Urls


class TestLogin:

    @staticmethod
    def get_login_page(driver: WebDriver):
        driver.get(Urls.LOGIN_PAGE_URL)
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(
                Locators.LOGIN_PAGE_HEADING
            )
        )

    @staticmethod
    def fill_and_submit_login_form(driver: WebDriver, data):
        driver.find_element(*Locators.LOGIN_PAGE_EMAIL_FIELD).send_keys(data['email'])
        driver.find_element(*Locators.LOGIN_PAGE_PASSWORD_FIELD).send_keys(data['password'])
        driver.find_element(*Locators.LOGIN_PAGE_SUBMIT_BTN).click()

    def login_success(self, driver: WebDriver, valid_login_user_data):
        # self.get_login_page(driver)
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(
                Locators.LOGIN_PAGE_HEADING
            )
        )
        self.fill_and_submit_login_form(driver, valid_login_user_data)
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(
                Locators.CONSTRUCTOR_PAGE_HEADING
            )
        )
        driver.find_element(*Locators.TOOLBAR_NAV_LINK_PROFILE).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(
                Locators.PROFILE_MENU_ACTIVE_LINK
            )
        )
        assert driver.find_element(*Locators.PROFILE_MENU_ACTIVE_LINK).text == 'Профиль'
        assert driver.find_element(*Locators.PROFILE_LOGIN_FIELD).get_attribute('value') \
               == valid_login_user_data['email']

    def test_login_from_login_page_valid_data_success(self, driver: WebDriver, valid_login_user_data):
        driver.get(Urls.LOGIN_PAGE_URL)
        self.login_success(driver, valid_login_user_data)

    def test_login_from_profile_btn_valid_data_success(self, driver: WebDriver, valid_login_user_data):
        driver.get(Urls.ORIGIN)
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable(
                Locators.TOOLBAR_NAV_LINK_PROFILE
            )
        )
        driver.find_element(*Locators.TOOLBAR_NAV_LINK_PROFILE).click()
        self.login_success(driver, valid_login_user_data)

    def test_login_from_registration_page_valid_data_success(self, driver: WebDriver, valid_login_user_data):
        driver.get(Urls.REGISTER_PAGE_URL)
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable(
                Locators.REGISTRATION_PAGE_LOGIN_LINK
            )
        )
        driver.find_element(*Locators.REGISTRATION_PAGE_LOGIN_LINK).click()
        self.login_success(driver, valid_login_user_data)

    def test_login_from_reset_password_page_valid_data_success(self, driver: WebDriver, valid_login_user_data):
        driver.get(Urls.RESET_PASSWORD_PAGE_URL)
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable(
                Locators.RESET_PASSWORD_PAGE_LOGIN_LINK
            )
        )
        driver.find_element(*Locators.RESET_PASSWORD_PAGE_LOGIN_LINK).click()
        self.login_success(driver, valid_login_user_data)

