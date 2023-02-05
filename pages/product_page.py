from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def correct_purchase(self):
        self.correct_purchase_name_in_basket()
        self.correct_basket_price()

    def add_product_to_basket(self):
        add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket.click()

    def correct_purchase_name_in_basket(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        purchase_name_in_basket = self.browser.find_element(*ProductPageLocators.PURCHASE_NAME).text
        assert purchase_name_in_basket == product_name, "Wrong purchase name for adding to basket msg"

    def correct_basket_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_price = self.browser.find_element(*ProductPageLocators.PURCHASE_PRICE).text
        assert basket_price == product_price, "Basket price is different with product price"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.PURCHASE_NAME), \
            "Success message is presented, but should not be"

    def should_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.PURCHASE_NAME), \
            "Success message is not disappeared, but should be"