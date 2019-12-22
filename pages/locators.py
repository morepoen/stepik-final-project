from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "[href='/en-gb/basket/']")

class BasketPageLocators():
    EMPTY_BASKET = (By.CSS_SELECTOR, '#content_inner p')
    BASKET_ITEMS = (By.CSS_SELECTOR, '.basket-items')

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')

    REGISTER_FORM_EMAIL = (By.CSS_SELECTOR, '#id_registration - email')
    REGISTER_FORM_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTER_FORM_REPEAT_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password2')

    LOGIN_FORM_EMAIL = (By.CSS_SELECTOR, '#id_login-username')
    LOGIN_FORM_PASSWORD = (By.CSS_SELECTOR, '#id_login-password')

class ProductPagelocators():
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, '.btn.btn-lg.btn-primary.btn-add-to-basket')
    ADDED_TO_CART_MESSAGE = (By.CSS_SELECTOR, '.alertinner')
    CART_COST_MESSAGE = (By.CSS_SELECTOR, '#messages > div:nth-child(3) > .alertinner')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.price_color')
    PRODUCT_NAME =(By.CSS_SELECTOR, '.col-sm-6.product_main h1')
