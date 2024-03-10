from selenium.webdriver.common.by import By
class Locators:
    # Registration page
    # Заголовок страницы Регистрация
    REGISTRATION_PAGE_HEADING = By.XPATH, './/h2[text()="Регистрация"]'
    # Текстовое поле Имя
    REGISTRATION_PAGE_NAME_FIELD = By.XPATH, './/form//label[text()="Имя"]/following-sibling::input'
    # Текстовое поле Почта
    REGISTRATION_PAGE_EMAIL_FIELD = By.XPATH, './/form//label[text()="Email"]/following-sibling::input'
    # Текстовое поле Пароль
    REGISTRATION_PAGE_PASSWORD_FIELD = By.XPATH, './/form//label[text()="Пароль"]/following-sibling::input'
    # Кнопка Зарегистрироваться
    REGISTRATION_PAGE_SUBMIT_BTN = By.XPATH, './/form//button[text()="Зарегистрироваться"]'
    # Текст ошибки для поля Пароль
    REGISTRATION_PAGE_PASSWORD_FIELD_ERROR_TEXT \
        = By.XPATH, './/form//label[text()="Пароль"]/parent::*/parent::*/*[contains(@class, "input__error")]'
    REGISTRATION_PAGE_LOGIN_LINK = By.XPATH, './/a[@href="/login"]'

    # Login page
    # Заголовок страницы Вход
    LOGIN_PAGE_HEADING = By.XPATH, './/h2[text()="Вход"]'
     # Текстовое поле Почта
    LOGIN_PAGE_EMAIL_FIELD = By.XPATH, './/form//label[text()="Email"]/following-sibling::input'
    # Текстовое поле Пароль
    LOGIN_PAGE_PASSWORD_FIELD = By.XPATH, './/form//label[text()="Пароль"]/following-sibling::input'
    # Кнопка Войти
    LOGIN_PAGE_SUBMIT_BTN = By.XPATH, './/form//button[text()="Войти"]'

    # Constructor page
    # Заголовок страницы Конструктор
    CONSTRUCTOR_PAGE_HEADING = (By.XPATH, './/h1[text()="Соберите бургер"]')
    # Кнопка Оформить заказ
    CONSTRUCTOR_ORDER_SUBMIT_BTN = By.XPATH, './/form//button[text()="Оформить заказ"]'
    # Секция с ингредиентами
    CONSTRUCTOR_INGREDIENTS_CONTAINER = \
        By.XPATH, '//div[contains(@class, "BurgerIngredients_ingredients__menuContainer")]'
    # Секция Корзина
    CONSTRUCTOR_BASKET = By.XPATH, '//section[contains(@class, "BurgerConstructor_basket")]'
    # Таб Булки
    CONSTRUCTOR_BUNS_TAB = \
        By.XPATH, '//span[text()="Булки"]/parent::div[contains(@class, "tab_tab__")][contains(@class, "noselect")]'
    # Заголовок Булки в списке ингредиентов
    CONSTRUCTOR_LIST_BUNS_HEADING = \
        By.XPATH, '//div[contains(@class, "BurgerIngredients_ingredients__menuContainer")]/h2[text()="Булки"]'
    # Таб Соусы
    CONSTRUCTOR_SAUCE_TAB = \
        By.XPATH, '//span[text()="Соусы"]/parent::div[contains(@class, "tab_tab__")][contains(@class, "noselect")]'
    # Заголовок Соусы в списке ингредиентов
    CONSTRUCTOR_LIST_SAUCE_HEADING = \
        By.XPATH, '//div[contains(@class, "BurgerIngredients_ingredients__menuContainer")]/h2[text()="Соусы"]'
    # Таб Начинки
    CONSTRUCTOR_FILLING_TAB = \
        By.XPATH, '//span[text()="Начинки"]/parent::div[contains(@class, "tab_tab__")][contains(@class, "noselect")]'
    # Заголовок Начинки в списке ингредиентов
    CONSTRUCTOR_LIST_FILLING_HEADING = \
        By.XPATH, '//div[contains(@class, "BurgerIngredients_ingredients__menuContainer")]/h2[text()="Начинки"]'

    # Toolbar navigation links
    # Ссылка на Аккаунт
    TOOLBAR_NAV_ACCOUNT_LINK = By.XPATH, './/a[@href="/account"]'
    # Ссылка на Конструктор
    TOOLBAR_NAV_CONSTRUCTOR_LINK = By.XPATH, './/p[text()="Конструктор"]/parent::a[@href="/"]'
    # Логотип
    LOGO = By.XPATH, './/*[contains(@class, "AppHeader_header__logo")]/a[@href="/"]'

    # Profile page
    # Активная ссылка в меню профиля
    PROFILE_MENU_ACTIVE_LINK = (By.XPATH, './/li/a[contains(@class, "_active")]')
    # Текстовое поле Логин
    PROFILE_LOGIN_FIELD = By.XPATH, './/label[text()="Логин"]/following-sibling::input'
    # Ссылка Профиль в меню профиля
    PROFILE_MENU_PROFILE_LINK = (By.XPATH, './/li/a[contains(@href, "/account/profile")]')
    # Кнопка Выход
    PROFILE_MENU_LOGOUT_BTN = (By.XPATH, './/button[text()="Выход"]')

    # Reset password page
    # Заголовок страницы Восстановление пароля
    RESET_PASSWORD_PAGE_HEADING = By.XPATH, './/h2[text()="Восстановление пароля"]'
    # Ссылка на страницу логина
    RESET_PASSWORD_PAGE_LOGIN_LINK = By.XPATH, './/a[@href="/login"]'



