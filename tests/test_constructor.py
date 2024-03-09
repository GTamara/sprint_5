import time

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from constants.locators import Locators
from constants.urls import Urls
from constants.constants import Constants
from shared_methods import SharedMethods

class TestConstructor:

    @staticmethod
    def is_constructor_page(driver: WebDriver):
        WebDriverWait(driver, Constants.TIMEOUT).until(
            expected_conditions.visibility_of_element_located(
                Locators.CONSTRUCTOR_PAGE_HEADING
            )
        )
        assert len(
            driver.find_elements(*Locators.CONSTRUCTOR_INGREDIENTS_CONTAINER)
        ) == 1
        assert len(
            driver.find_elements(*Locators.CONSTRUCTOR_BASKET)
        ) == 1

    def test_go_to_constructor_from_profile_by_clicking_on_constructor_link(self, driver: WebDriver, logged_in_user):
        SharedMethods.go_to_profile(driver)
        driver.find_element(*Locators.TOOLBAR_NAV_CONSTRUCTOR_LINK).click()
        self.is_constructor_page(driver)

    def test_go_to_constructor_from_profile_by_clicking_on_logo(self, driver: WebDriver, logged_in_user):
        SharedMethods.go_to_profile(driver)
        driver.find_element(*Locators.LOGO).click()
        self.is_constructor_page(driver)

    def check_whether_ingredients_list_scrolls_to_their_heading_when_the_tab_is_clicked(
        self,
        driver: WebDriver,
        current_tab_locator: tuple[str, str],
        current_heading_locator: tuple[str, str],
    ):
        driver.find_element(*current_tab_locator).click()
        # ждем, пока закончится анимация скролла, которая запускается по клику на таб
        time.sleep(0.8)
        WebDriverWait(driver, Constants.TIMEOUT).until(
            expected_conditions.presence_of_element_located(current_heading_locator)
        )
        current_heading = driver.find_element(*current_heading_locator)
        js_script = '''
            currentHeading = arguments[0]
            // для того, чтобы оффсеты считались от родителя заголовка
            currentHeading.parentNode.style.position = 'relative'; 
            currentHeading.style.position = 'relative'
            return [
                Math.round(currentHeading.offsetTop),
                Math.round(currentHeading.parentNode.scrollTop)
            ]
        '''
        current_heading_offset_top, parent_node_scroll_top = driver.execute_script(
            js_script,
            current_heading
        )
        assert current_heading_offset_top == parent_node_scroll_top

    def test_filling_tab(self, driver, logged_in_user):
        filling_tab_locator = Locators.CONSTRUCTOR_FILLING_TAB
        filling__heading_locator = Locators.CONSTRUCTOR_LIST_FILLING_HEADING

        # e = driver.find_element(*filling__heading_locator)
        # e = driver.find_element(*Locators.CONSTRUCTOR_PAGE_HEADING)
        e = driver.find_element(*Locators.CONSTRUCTOR_INGREDIENTS_CONTAINER)
        location = e.location
        size = e.size
        w, h = size['width'], size['height']

        print(location)
        print(size)
        print(w, h)
        print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        driver.find_element(*filling_tab_locator).click()
        # ждем, пока закончится анимация скролла, которая запускается по клику на таб
        time.sleep(0.8)
        # e = driver.find_element(*filling__heading_locator)
        location = e.location
        size = e.size
        w, h = size['width'], size['height']

        print(location)
        print(size)
        print(w, h)
        # self.check_whether_ingredients_list_scrolls_to_their_heading_when_the_tab_is_clicked(
        #     driver,
        #     filling_tab_locator,
        #     filling__heading_locator
        # )
