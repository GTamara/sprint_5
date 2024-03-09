from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from constants.locators import Locators
from constants.urls import Urls
from constants.constants import Constants


class SharedMethods:

    @staticmethod
    def get_login_page(driver: WebDriver):
        driver.get(Urls.LOGIN_PAGE_URL)
        WebDriverWait(driver, Constants.TIMEOUT).until(
            expected_conditions.visibility_of_element_located(
                Locators.LOGIN_PAGE_HEADING
            )
        )

    @staticmethod
    def fill_and_submit_login_form(driver: WebDriver, data):
        driver.find_element(*Locators.LOGIN_PAGE_EMAIL_FIELD).send_keys(data['email'])
        driver.find_element(*Locators.LOGIN_PAGE_PASSWORD_FIELD).send_keys(data['password'])
        driver.find_element(*Locators.LOGIN_PAGE_SUBMIT_BTN).click()
        WebDriverWait(driver, Constants.TIMEOUT).until(
            expected_conditions.visibility_of_element_located(
                Locators.CONSTRUCTOR_PAGE_HEADING
            )
        )

    @staticmethod
    def go_to_main_page(driver):
        driver.get(Urls.ORIGIN)
        WebDriverWait(driver, Constants.TIMEOUT).until(
            expected_conditions.element_to_be_clickable(
                Locators.TOOLBAR_NAV_ACCOUNT_LINK
            )
        )

    @staticmethod
    def go_to_profile(driver: WebDriver):
        driver.find_element(*Locators.TOOLBAR_NAV_ACCOUNT_LINK).click()
        WebDriverWait(driver, Constants.TIMEOUT).until(
            expected_conditions.visibility_of_element_located(
                Locators.PROFILE_MENU_PROFILE_LINK
            )
        )