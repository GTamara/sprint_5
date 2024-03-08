from selenium.webdriver.common.by import By
class Locators:
    # Registration page
    REGISTRATION_PAGE_HEADING = By.XPATH, './/h2[text()="Регистрация"]'
    REGISTRATION_PAGE_NAME_FIELD = By.XPATH, './/form//label[text()="Имя"]/following-sibling::input'
    REGISTRATION_PAGE_EMAIL_FIELD = By.XPATH, './/form//label[text()="Email"]/following-sibling::input'
    REGISTRATION_PAGE_PASSWORD_FIELD = By.XPATH, './/form//label[text()="Пароль"]/following-sibling::input'
    REGISTRATION_PAGE_SUBMIT_BTN = By.XPATH, './/form//button[text()="Зарегистрироваться"]'
    REGISTRATION_PAGE_PASSWORD_FIELD_ERROR_TEXT \
        = By.XPATH, './/form//label[text()="Пароль"]/parent::*/parent::*/*[contains(@class, "input__error")]'
    REGISTRATION_PAGE_LOGIN_LINK = By.XPATH, './/a[@href="/login"]'

    # Login page
    LOGIN_PAGE_HEADING = By.XPATH, './/h2[text()="Вход"]'
    LOGIN_PAGE_EMAIL_FIELD = By.XPATH, './/form//label[text()="Email"]/following-sibling::input'
    LOGIN_PAGE_PASSWORD_FIELD = By.XPATH, './/form//label[text()="Пароль"]/following-sibling::input'
    LOGIN_PAGE_SUBMIT_BTN = By.XPATH, './/form//button[text()="Войти"]'

    # Constructor page
    CONSTRUCTOR_PAGE_HEADING = (By.XPATH, './/h1[text()="Соберите бургер"]')
    CONSTRUCTOR_ORDER_SUBMIT_BTN = './/form//button[text()="Оформить заказ"]'

    # Toolbar navigation links
    TOOLBAR_NAV_LINK_PROFILE = By.XPATH, './/a[@href="/account"]'

    # Profile page
    PROFILE_MENU_ACTIVE_LINK = (By.XPATH, './/li/a[contains(@class, "_active")]')
    PROFILE_LOGIN_FIELD = By.XPATH, './/label[text()="Логин"]/following-sibling::input'

    # Reset password page
    RESET_PASSWORD_PAGE_HEADING = By.XPATH, './/h2[text()="Восстановление пароля"]'
    RESET_PASSWORD_PAGE_LOGIN_LINK = By.XPATH, './/a[@href="/login"]'



