from base.seleniumbase import SeleniumBase
from locators.locators import HomePageLocators
from selenium.webdriver.remote.webelement import WebElement
from typing import List
import allure


class HomePage(SeleniumBase):
    __NAV_LINKS_TEXT = "WOMEN, DRESSES, T-SHIRTS"

    def __init__(self, driver):
        super().__init__(driver)
        self._driver.get('http://automationpractice.com/index.php')

    @property
    def expected_nav_links_text(self):
        return self.__NAV_LINKS_TEXT

    @allure.step('Сбор актуального текста на кнопоках навигации')
    def get_nav_links_text(self) -> str:
        nav_links: List[WebElement] = self._are_visible('xpath', HomePageLocators.nav_links)
        nav_links_text: List[str] = self._get_text_from_list_of_webelements(nav_links)
        return ", ".join(nav_links_text)

    @allure.step('Набор заданного текста в поле поиска')
    def search_by_text(self, text):
        self._is_present('xpath', HomePageLocators.search_field).send_keys(text)

    @allure.step('Клик по кнопке "Найти"')
    def click_search_button(self):
        self._is_present('xpath', HomePageLocators.search_button).click()

    @allure.step('Проверка: в результатах поиска есть заданный текст')
    def find_inside_results(self, text: str):
        elements = self._are_visible('xpath', HomePageLocators.result_product_containers)
        return self._find_text_inside_elements(elements, text.lower())

    @allure.step('Проверка: поиск выдал результаты')
    def check_results_exists(self):
        res_count = self._is_present('xpath', HomePageLocators.X_results_found)
        if res_count.text.find("0") == -1:
            return True
        else:
            return False

    @allure.step('Сохранение имени добавленного продукта')
    def store_name_of_an_added_product(self, number_of_product: int = 1):
        products = self._are_present('xpath', HomePageLocators.result_product_containers)
        assert number_of_product <= len(products), 'Products in result is less than your number of product'
        element = products[number_of_product - 1]
        return element.text.split("\n")[0]

    @allure.step('Клик по кнопке "Add to cart"')
    def click_add_to_cart(self, number_of_product: int = 1):
        """Add to cart first item in result block"""
        buttons = self._are_present('xpath', HomePageLocators.add_to_cart_buttons)
        assert number_of_product <= len(buttons), 'Products in result is less than your number of product'
        element = buttons[number_of_product - 1]
        #  move_to_element is necessary, because 'Add to cart' button disappears at a res of 1200xXXXX and more
        product_block = self._are_present('xpath', HomePageLocators.result_product_containers)[number_of_product - 1]
        self._move_to_element(product_block)
        element.click()

    @allure.step('Клик по кнопке "Proceed to checkout"')
    def click_proceed_to_checkout(self):
        self._is_visible('xpath', HomePageLocators.proceed_to_checkout_button).click()

    @allure.step('Проверка: в корзину добавился продукт')
    def check_product_in_cart_exists(self, product_name):
        added_element = self._are_present('xpath', HomePageLocators.products_in_cart)[-1]
        if added_element.text.split("\n")[0] == product_name:
            return True
        else:
            return False

    @allure.step('Полная очистка корзины')
    def delete_all_items_in_a_cart(self):
        products_in_cart_count = len(self._are_present('xpath', "//tbody/tr"))
        for _ in range(products_in_cart_count):
            self._are_present('xpath', HomePageLocators.delete_item_from_cart_buttons)[0].click()

    @allure.step("Проверка: Корзина пуста.")
    def check_cart_is_empty(self) -> bool:
        try:
            msg = self._is_visible('xpath', HomePageLocators.cart_is_empty_msg)
        except:
            return False
        else:
            return True

    @allure.step('Наведение мыши на кнопку "Woman" для открытия меню')
    def move_to_women_button(self):
        element = self._is_present('xpath', HomePageLocators.women_header_button)
        return self._move_to_element(element)

    @allure.step('Клик по кнопке "T-shirt" в контекстном меню')
    def click_tshirt_button_in_women_droplist(self):
        self._is_visible('xpath', HomePageLocators.t_shirts_button_in_women_droplist).click()

    @allure.step('Клик по кнопке "Proceed to checkout" в корзине')
    def click_proceed_to_checkout_button_in_a_cart(self):
        self._is_present('xpath', HomePageLocators.proceed_to_checkout_button_in_a_cart).click()

    @allure.step('Авторизация')
    def login(self, email: str, password: str):
        self._is_visible('xpath', HomePageLocators.email_enter).send_keys(email)
        self._is_visible('xpath', HomePageLocators.password_enter).send_keys(password)
        self._is_visible('xpath', HomePageLocators.sign_in_button).click()

    @allure.step('Клик по кнопке "Proceed to checkout" на странице выбора адреса')
    def click_proceed_to_checkout_button_in_address(self):
        self._is_present('xpath', HomePageLocators.proceed_to_checkout_button_in_address).click()

    @allure.step('Клик по чекбоксу "Agree to the terms"')
    def click_agree_to_the_terms_checkbox(self):
        self._is_present('xpath', HomePageLocators.agree_to_the_terms_of_service_checkbox).click()

    @allure.step('Клик по кнопке "Proceed to checkout" на странице выбора способа доставки')
    def click_proceed_to_checkout_button_in_shipping(self):
        self._is_present('xpath', HomePageLocators.proceed_to_checkout_button_in_shipping).click()

    @allure.step('Клик по кнопке "Pay by check"')
    def click_pay_by_check_button(self):
        self._is_present('xpath', HomePageLocators.pay_by_check_button).click()

    @allure.step('Клик по кнопке "Confirm order"')
    def click_confirm_order_button(self):
        self._is_present('xpath', HomePageLocators.confirm_order_button).click()

    @allure.step('Клик по кнопке "Account"')
    def click_account_button(self):
        self._is_present('xpath', HomePageLocators.account_button).click()

    @allure.step('Клик по кнопке "Order history"')
    def click_order_history_button(self):
        self._is_present('xpath', HomePageLocators.orders_history_button).click()

    @allure.step('Клик по кнопке "details"')
    def click_details_button(self):
        self._are_visible('xpath', HomePageLocators.details_buttons)[0].click()

    @allure.step('Проверка: продукт отображается в истории покупок')
    def check_product_in_order_history_exists(self, product_name):
        element = self._is_visible('xpath', HomePageLocators.ordered_product_name)
        if element.text.find(product_name) == -1:
            print(f'"{product_name}" does not exist is ordered products')
            return False
        else:
            return True


