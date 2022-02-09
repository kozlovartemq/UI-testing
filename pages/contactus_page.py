from base.seleniumbase import SeleniumBase
from locators.locators import ContactUsPageLocators
from selenium.webdriver.remote.webelement import WebElement
from typing import List
import allure

class ContactUsPage(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self._driver.get("http://automationpractice.com/index.php?controller=contact")

    @allure.step('Прикрепление файла')
    def attach_txt_file(self, file_path: str):
        self._is_present("xpath", ContactUsPageLocators.choose_file_button).send_keys(file_path)

    @allure.step('Клик по кнопке "Send"')
    def click_send_button(self):
        self._is_visible("xpath", ContactUsPageLocators.send_button).click()

    @allure.step('Выбор "Subject Heading"')
    def select_sh_dropdown_list_by_text(self, text: str):
        select = self._get_select_list('xpath', ContactUsPageLocators.subject_heading_select)
        select.select_by_visible_text(text)

    @allure.step('Заполнение email')
    def fill_email(self, email: str):
        self._is_present('xpath', ContactUsPageLocators.email).send_keys(email)

    @allure.step('Заполнение номера заказа')
    def fill_order(self, id_order: str):
        self._is_present('xpath', ContactUsPageLocators.id_order).send_keys(id_order)

    @allure.step('Заполнение сообщения')
    def fill_msg(self, msg: str):
        self._is_present('xpath', ContactUsPageLocators.massage).send_keys(msg)

    @allure.step("Проверка: Сообщение об успешной отпраке появилось")
    def check_success_msg_appears(self) -> bool:
        try:
            msg = self._is_visible('xpath', ContactUsPageLocators.success_msg)
        except:
            return False
        else:
            return True

    @allure.step("Проверка: Сообщение об ошибке появилось")
    def check_error_msg_appears(self) -> bool:
        try:
            msg = self._is_visible('xpath', ContactUsPageLocators.error_msg)
        except:
            return False
        else:
            return True
