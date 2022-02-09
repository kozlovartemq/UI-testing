import allure
import pytest
from pages.register_page import RegisterPage
from testdata.testdata import User1


@allure.feature("Тест формы регистрации")
@allure.severity(allure.severity_level.BLOCKER)
@pytest.mark.usefixtures('web_driver_init')
class TestRegisterPage:

    # @pytest.mark.runthis
    @allure.story("Проверка возможности регистрации пользователя при корректно заполненных данных")
    def test_register_form(self):
        """Verifying the ability to register"""
        register = RegisterPage(self.driver)
        register.fill_email(User1.email)
        register.click_create_button()
        assert register.check_register_form_appears(), "A Register form didn't appear."
        register.select_sex()
        register.fill_first_name(User1.first_name)
        register.fill_last_name(User1.last_name)
        register.fill_password(User1.password)
        register.select_day_dropdown_list_by_random_value()
        register.select_month_dropdown_list_by_random_value()
        register.select_year_dropdown_list_by_text(User1.birth_year)
        register.fill_address(User1.address)
        register.fill_city(User1.city)
        register.select_state_dropdown_list_by_random_value()
        register.fill_postcode(User1.postcode)
        register.select_country_dropdown_list_by_text(User1.country)
        register.fill_phone(User1.phone)
        register.click_submit_button()
        assert register.check_my_account_head_appears(), "My account page didn't appear."
