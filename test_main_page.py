import time

import pytest
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage


@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com"
        page = MainPage(browser, link)
        page.open()
        page.go_to_basket()
        basket_page = BasketPage(browser, link)
        basket_page.should_no_be_products()
        basket_page.should_be_msg_about_empty_basket()


    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com"
        page = MainPage(browser, link)
        page.open()
        page.go_to_basket()
        basket_page = BasketPage(browser, link)
        basket_page.should_no_be_products()
        basket_page.should_be_msg_about_empty_basket()

def test_reg(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = LoginPage(browser, link)
    page.open()
    email = str(time.time()) + "@fakemail.org"
    page.register_new_user(email)

