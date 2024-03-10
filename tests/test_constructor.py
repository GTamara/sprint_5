import time
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from constants.locators import Locators
from constants.constants import Constants
from shared_methods import SharedMethods


class TestConstructor:

    # Переход в конструктор по клику на ссылку Конструктор
    def test_go_to_constructor_from_profile_by_clicking_on_constructor_link(self, driver: WebDriver, logged_in_user):
        SharedMethods.go_to_profile(driver)
        driver.find_element(*Locators.TOOLBAR_NAV_CONSTRUCTOR_LINK).click()
        assert SharedMethods.is_constructor_page(driver)

    # переход в конструктор по клику на Логотип
    def test_go_to_constructor_from_profile_by_clicking_on_logo(self, driver: WebDriver, logged_in_user):
        SharedMethods.go_to_profile(driver)
        driver.find_element(*Locators.LOGO).click()
        assert SharedMethods.is_constructor_page(driver)

    # клик по табу скроллит вверх соответствующий заголовок списка ингредиентов
    @staticmethod
    def check_whether_ingredients_list_scrolls_to_their_heading_when_the_tab_is_clicked(
            driver: WebDriver,
            current_tab_locator: tuple[str, str],
            current_heading_locator: tuple[str, str],
    ):
        current_heading_element: WebElement = driver.find_element(*current_heading_locator)
        ingredients_container: WebElement = driver.find_element(*Locators.CONSTRUCTOR_INGREDIENTS_CONTAINER)
        driver.find_element(*current_tab_locator).click()
        # ждем, пока закончится анимация скролла, которая запускается по клику на таб
        time.sleep(0.8)
        assert current_heading_element.location['y'] == ingredients_container.location['y']

    # клик по табу Начинки скроллит вверх заголовок Начинки
    def test_fillings_scrolls_to_top_when_filling_tab_is_clicked(self, driver, logged_in_user):
        filling_tab_locator = Locators.CONSTRUCTOR_FILLING_TAB
        filling__heading_locator = Locators.CONSTRUCTOR_LIST_FILLING_HEADING
        self.check_whether_ingredients_list_scrolls_to_their_heading_when_the_tab_is_clicked(
            driver,
            filling_tab_locator,
            filling__heading_locator
        )

    # клик по табу Соусы скроллит вверх заголовок Соусы
    def test_sauce_scrolls_to_top_when_sauce_tab_is_clicked(self, driver, logged_in_user):
        filling_tab_locator = Locators.CONSTRUCTOR_SAUCE_TAB
        filling__heading_locator = Locators.CONSTRUCTOR_LIST_SAUCE_HEADING
        self.check_whether_ingredients_list_scrolls_to_their_heading_when_the_tab_is_clicked(
            driver,
            filling_tab_locator,
            filling__heading_locator
        )

    # клик по табу Булки скроллит вверх заголовок Булки
    def test_buns_scrolls_to_top_when_sauce_tab_is_clicked(self, driver, logged_in_user):
        buns_tab_locator = Locators.CONSTRUCTOR_BUNS_TAB
        buns__heading_locator = Locators.CONSTRUCTOR_LIST_BUNS_HEADING
        ingredients_container: WebElement = driver.find_element(*Locators.CONSTRUCTOR_INGREDIENTS_CONTAINER)
        driver.execute_script('''
            containerScrollHeight = arguments[0].scrollHeight
            arguments[0].scrollTo({ top: containerScrollHeight, left:0, behavior: "instant"})
        ''', ingredients_container)
        self.check_whether_ingredients_list_scrolls_to_their_heading_when_the_tab_is_clicked(
            driver,
            buns_tab_locator,
            buns__heading_locator
        )
