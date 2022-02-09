import allure
import pytest
from pages.contactus_page import ContactUsPage
from testdata.testdata import ContactUsData


@allure.feature("Тест формы обратной связи")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.usefixtures('web_driver_init')
class TestContactUsPage:

    @pytest.mark.runthis
    @allure.story("Проверка корректной отправки формы обратной связи")
    def test_contactus_form_send(self):
        """Verifying that contact us form sends successfully"""
        contact_us = ContactUsPage(self.driver)
        contact_us.attach_txt_file(ContactUsData.file_path)
        contact_us.select_sh_dropdown_list_by_text(ContactUsData.subject_heading)
        contact_us.fill_email(ContactUsData.email)
        contact_us.fill_order(ContactUsData.order)
        contact_us.fill_msg(ContactUsData.message)
        contact_us.click_send_button()
        assert contact_us.check_success_msg_appears(), 'Сообщение об успешной отправке формы обратной связи не появилось'

    # @pytest.mark.runthis
    @allure.story("Проверка появления ошибки при отправки формы обратной связи с незаполненным полем 'Message'")
    def test_contactus_form_error(self):
        """Verifying that error message appears if Message area is empty"""
        contact_us_er = ContactUsPage(self.driver)
        contact_us_er.attach_txt_file(ContactUsData.file_path)
        contact_us_er.select_sh_dropdown_list_by_text(ContactUsData.subject_heading)
        contact_us_er.fill_email(ContactUsData.email)
        contact_us_er.fill_order(ContactUsData.order)
        contact_us_er.click_send_button()
        assert contact_us_er.check_error_msg_appears(), 'Сообщение об ошибке появилось'
