from selenium.webdriver.common.by import By


class MainPageLocators():

    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')

class LoginPageLocators():

    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form_inv')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form_inv')

    REGISTER_FORM_EMAIL = (By.CSS_SELECTOR, '#id_registration - email')
    REGISTER_FORM_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTER_FORM_REPEAT_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password2')

    LOGIN_FORM_EMAIL = (By.CSS_SELECTOR, '#id_login-username')
    LOGIN_FORM_PASSWORD = (By.CSS_SELECTOR, '#id_login-password')
