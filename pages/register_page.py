import random
from locators.locators import RegisterPageLocators
from base.seleniumbase import SeleniumBase
from selenium.webdriver.remote.webelement import WebElement
from typing import List
import allure


class RegisterPage(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self._driver.get("http://automationpractice.com/index.php?controller=authentication")
        self.__REGISTRATION_SUBTITLE = "TITLE"

    @allure.step('Заполнение email')
    def fill_email(self, email: str):
        self._is_present('xpath', RegisterPageLocators.email).send_keys(email)
        print(f' Generated email: {email}')

    @allure.step('Клик по кнопке "Create an account"')
    def click_create_button(self):
        self._is_visible("xpath", RegisterPageLocators.create_button).click()

    @allure.step('Проверка: форма регистрации появилась')
    def check_register_form_appears(self):
        element = self._is_present('xpath', RegisterPageLocators.subtitle)
        if element.text.upper().find(self.__REGISTRATION_SUBTITLE) != -1:
            return True
        return False

    @allure.step('Выбор пола')
    def select_sex(self, sex="Male"):
        if sex == "Female" or sex == "2":
            self._is_present('xpath', RegisterPageLocators.mrs_radio).click()
        else:
            self._is_present('xpath', RegisterPageLocators.mr_radio).click()

    @allure.step('Заполнение имени')
    def fill_first_name(self, first_name: str):
        self._is_present('xpath', RegisterPageLocators.first_name).send_keys(first_name)

    @allure.step('Заполнение фамилии')
    def fill_last_name(self, second_name: str):
        self._is_present('xpath', RegisterPageLocators.second_name).send_keys(second_name)

    @allure.step('Заполнение пароля')
    def fill_password(self, password: str):
        """The password must be 5 characters minimum"""
        self._is_present('xpath', RegisterPageLocators.passwd).send_keys(password)

    @allure.step('Выбор дня рождения')
    def select_day_dropdown_list_by_random_value(self):
        select = self._get_select_list('xpath', RegisterPageLocators.select_days)
        select.select_by_value(str(random.randint(1, 28)))

    @allure.step('Выбор месяца рождения')
    def select_month_dropdown_list_by_random_value(self):
        """This method required a month number (1-12)"""
        select = self._get_select_list('xpath', RegisterPageLocators.select_month)
        select.select_by_value(str(random.randint(1, 12)))

    @allure.step('Выбор года рождения')
    def select_year_dropdown_list_by_text(self, year: str):
        select = self._get_select_list('xpath', RegisterPageLocators.select_years)
        select.select_by_value(year)

    @allure.step('Заполнение адреса')
    def fill_address(self, address: str):
        self._is_present('xpath', RegisterPageLocators.address).send_keys(address)

    @allure.step('Заполнение города')
    def fill_city(self, city: str):
        self._is_present('xpath', RegisterPageLocators.city).send_keys(city)

    @allure.step('Выбор штата')
    def select_state_dropdown_list_by_random_value(self):
        select = self._get_select_list('xpath', RegisterPageLocators.select_state)
        select.select_by_value(str(random.randint(1, 50)))

    @allure.step('Заполнение индекса')
    def fill_postcode(self, postcode: str):
        """The postcode must follow this format: 00000"""
        self._is_present('xpath', RegisterPageLocators.postcode).send_keys(postcode)

    @allure.step('Заполнение страны')
    def select_country_dropdown_list_by_text(self, country: str):
        select = self._get_select_list('xpath', RegisterPageLocators.select_country)
        select.select_by_visible_text(country)

    @allure.step('Заполнение номера телефона')
    def fill_phone(self, phone: str):
        self._is_present('xpath', RegisterPageLocators.mobile_phone).send_keys(phone)

    @allure.step('Клик по кнопке "Register"')
    def click_submit_button(self):
        self._is_visible("xpath", RegisterPageLocators.submit_button).click()

    @allure.step("Проверка: Страница 'Мой аккаунт' появилась.")
    def check_my_account_head_appears(self) -> bool:
        try:
            msg = self._is_visible('xpath', RegisterPageLocators.my_account_head)
        except:
            return False
        else:
            return True
