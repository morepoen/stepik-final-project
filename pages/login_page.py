from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        current_url = str(self.browser.current_url)
        login_url = 'login'
        assert login_url in current_url

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Rgister form is not presented"

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_EMAIL)
        password_field = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PASSWORD)
        repeat_password_field = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_REPEAT_PASSWORD)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_REGISTER_BUTTON)
        email_field.send_keys(email)
        password_field.send_keys(password)
        repeat_password_field.send_keys(password)
        register_button.click()



