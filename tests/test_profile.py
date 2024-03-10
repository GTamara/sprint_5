from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from constants.locators import Locators
from shared_methods import SharedMethods
from constants.constants import Constants


class TestProfile:

    # если пользователь залогинен, то ему доступна страница профиля.
    def test_go_to_profile_by_clicking_on_profile_link_logged_in_user_success(
        self,
        driver: WebDriver,
        logged_in_user: dict[str, str]
    ):
        SharedMethods.go_to_profile(driver)
        assert driver.find_element(*Locators.PROFILE_MENU_ACTIVE_LINK).text == 'Профиль'

    # если пользователь незалогинен, то ему НЕ доступна страница профиля.
    def test_go_to_profile_by_clicking_on_profile_link_unlogged_user_failure(self, driver: WebDriver):
        SharedMethods.go_to_main_page(driver)
        driver.find_element(*Locators.TOOLBAR_NAV_ACCOUNT_LINK).click()
        WebDriverWait(driver, Constants.TIMEOUT).until(
            expected_conditions.visibility_of_element_located(
                Locators.LOGIN_PAGE_HEADING
            )
        )
        assert len(
            driver.find_elements(*Locators.PROFILE_MENU_PROFILE_LINK)
        ) == 0

    # Если пользователь залогинен то он успешно разлогинивается кликом по кнопке "Выход"
    def test_logout_logged_in_user_success(self, driver: WebDriver, logged_in_user: dict[str, str]):
        SharedMethods.go_to_profile(driver)
        driver.find_element(*Locators.PROFILE_MENU_LOGOUT_BTN).click()
        WebDriverWait(driver, Constants.TIMEOUT).until(
            expected_conditions.visibility_of_element_located(
                Locators.LOGIN_PAGE_HEADING
            )
        )
        assert len(
            driver.find_elements(*Locators.PROFILE_MENU_LOGOUT_BTN)
        ) == 0

    # если пользователь не залогинен, то после клика по ссылке профиля он не увидит кнопку "Выход"
    def test_logout_unlogged_user_failure(self, driver: WebDriver):
        SharedMethods.go_to_main_page(driver)
        driver.find_element(*Locators.TOOLBAR_NAV_ACCOUNT_LINK).click()
        WebDriverWait(driver, Constants.TIMEOUT).until(
            expected_conditions.visibility_of_element_located(
                Locators.LOGIN_PAGE_HEADING
            )
        )
        assert len(
            driver.find_elements(*Locators.PROFILE_MENU_LOGOUT_BTN)
        ) == 0
