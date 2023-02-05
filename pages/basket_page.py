from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_no_be_products(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS_TO_BUY), \
            "Total sum of purchases is present, but should not be"

    def should_be_msg_about_empty_basket(self):
        text = self.browser.find_element(*BasketPageLocators.MSG_EMPTY_BASKET).text
        assert "Your basket is empty." in text, "Basket is not empty or text is unavailable"