from .base_page import BasePage
from .locators import BasketPageLocators
from selenium.common.exceptions import NoSuchElementException


class BasketPage(BasePage):
    def should_not_be_elements_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "There is element in basket, but should not be"

    def should_be_empty_basket_message(self):
        try:
            empty_basket_message = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET)
            text_empty_basket_message = empty_basket_message.text
            needed_empty_basket_message = 'Your basket is empty. Continue shopping'
            assert text_empty_basket_message == needed_empty_basket_message, \
            "There is wrong empty basket message"
        except (NoSuchElementException):
            return "There is no empty basket message"


