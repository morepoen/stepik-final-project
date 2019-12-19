from .base_page import BasePage
from .locators import ProductPagelocators

class ProductPage(BasePage):
    def add_to_cart(self):
        add_to_cart_button = self.browser.find_element(*ProductPagelocators.ADD_TO_CART_BUTTON)
        add_to_cart_button.click()

    def should_be_added_to_cart_message(self):
        added_to_cart_message = self.browser.find_element(*ProductPagelocators.ADDED_TO_CART_MESSAGE)
        text_added_to_cart_message = added_to_cart_message.text
        product_name = (self.browser.find_element(*ProductPagelocators.PRODUCT_NAME)).text
        print(product_name)
        needed_added_to_cart_message = "{} has been added to your basket.".format(product_name)
        assert text_added_to_cart_message == needed_added_to_cart_message, "Wrong added_to_basket message"

    def should_be_cost_message(self):
        cart_cost_message = self.browser.find_element(*ProductPagelocators.CART_COST_MESSAGE)
        text_cart_cost_message = cart_cost_message.text
        product_cost = self.browser.find_element(*ProductPagelocators.PRODUCT_PRICE)
        product_cost_text = product_cost.text
        assert product_cost_text in text_cart_cost_message