from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    VIEW_BASKET = (By.CSS_SELECTOR, ".basket-mini.pull-right.hidden-xs>span>a")

class BasketPageLocators():
    BASKET_TOTAL = (By.CSS_SELECTOR, "tr:nth-child(2)>th.total.align-right")
    ITEMS_TO_BUY = (By.CSS_SELECTOR, ".col-sm-6.h3")
    MSG_EMPTY_BASKET = (By.XPATH, "//*[@id='content_inner']/p")


class MainPageLocators():
    pass

class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")

    PRODUCT_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main>h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")

    PURCHASE_NAME = (By.XPATH, "//*[@id='messages']/div[1]/div/strong")
    PURCHASE_PRICE = (By.XPATH, "//*[@id='messages']/div[3]/div/p[1]/strong")

