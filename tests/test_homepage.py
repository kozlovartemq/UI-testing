import pytest
from pages.homepage import HomePage
import allure


@allure.feature("Тесты при взаимодействии с товарами")
@pytest.mark.usefixtures('web_driver_init')
class TestHomePage:

    # @pytest.mark.runthis
    @allure.severity(allure.severity_level.NORMAL)
    @allure.story("Проверка текста на кнопоках навигации")
    def test_header_nav_links_exist(self):
        """Validating header navigation links text"""
        homepage_nav = HomePage(self.driver)
        expected_links = homepage_nav.expected_nav_links_text
        actual_links = homepage_nav.get_nav_links_text()
        allure.step("Проверка: текст на кнопках навигации совпадает со спецификацией.")
        # assert ACTUAL == EXPECTED (для корректного вывода AssertationError)
        assert actual_links == expected_links, 'Header navigation links text is not correct'

    # @pytest.mark.runthis
    @allure.severity(allure.severity_level.NORMAL)
    @allure.story("Проверка возможности искать товар через строку поиска")
    @pytest.mark.parametrize('s_text', ['Blouse', 'Dress',
                                        pytest.param('Nothing', marks=pytest.mark.xfail(reason='Searching for nonexistent item'))],
                             ids=['1_result', 'Multiple_results', '0_results'])
    def test_search_items(self, s_text):
        """Verifying the ability to search items"""
        search = HomePage(self.driver)
        search_text = s_text
        search.search_by_text(search_text)
        search.click_search_button()
        assert search.check_results_exists(), 'There are no items in results found'
        assert search.find_inside_results(search_text), 'There is no such text in result block'


    @pytest.mark.runthis
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Проверка возможности добавлять и удалять продукты из корзины")
    def test_add_del_from_cart(self):
        """Verifying the ability to add and delete items from a cart"""
        item = HomePage(self.driver)
        item.search_by_text("Dress")
        item.click_search_button()
        assert item.check_results_exists(), 'There are no items in results found'
        number_of_product = 7  # The number of a product you want to use
        product_name = item.store_name_of_an_added_product(number_of_product)
        item.click_add_to_cart(number_of_product)
        item.click_proceed_to_checkout()
        assert item.check_product_in_cart_exists(product_name), 'There is no added product in a cart'
        item.delete_all_items_in_a_cart()
        assert item.check_cart_is_empty(), 'The "Your shopping cart is empty." message didn\'t show up'

    @pytest.mark.runthis
    @allure.severity(allure.severity_level.MINOR)
    @allure.story("Проверка корректного открытия каталога")
    def test_catalog(self):
        """Verifying that products appears in a catalog"""
        catalog = HomePage(self.driver)
        catalog.move_to_women_button()
        catalog.click_tshirt_button_in_women_droplist()
        assert catalog.find_inside_results("t-shirt"), 'There is no product you are searching.'

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Проверка возможности оформления продукта")
    def test_order_product(self):
        """Verifying the ability to order a product"""
        order = HomePage(self.driver)
        order.search_by_text("Dress")
        order.click_search_button()
        assert order.check_results_exists(), 'There are no items in results found'
        number_of_product = 1
        product_name = order.store_name_of_an_added_product(number_of_product)
        order.click_add_to_cart(number_of_product)
        order.click_proceed_to_checkout()
        assert order.check_product_in_cart_exists(product_name), 'There is no added product in a cart'
        order.click_proceed_to_checkout_button_in_a_cart()
        order.login(email="randomemail1056@gmail.com", password="QwErTyUi")
        order.click_proceed_to_checkout_button_in_address()
        order.click_agree_to_the_terms_checkbox()
        order.click_proceed_to_checkout_button_in_shipping()
        order.click_pay_by_check_button()
        order.click_confirm_order_button()
        order.click_account_button()
        order.click_order_history_button()
        order.click_details_button()
        assert order.check_product_in_order_history_exists(product_name), 'Ordered product not found.'

