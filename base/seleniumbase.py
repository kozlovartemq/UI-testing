from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from typing import List
from selenium.webdriver.support.ui import Select


class SeleniumBase:
    def __init__(self, driver):
        self._driver = driver
        self.__wait = WebDriverWait(driver, 10)  # Timeout = 10 secs

    @staticmethod
    def __get_selenium_by(find_by: str) -> dict:
        find_by = find_by.lower()
        locating = dict(xpath=By.XPATH,
                        css=By.CSS_SELECTOR,
                        linktext=By.LINK_TEXT,
                        part_of_linktext=By.PARTIAL_LINK_TEXT,
                        tagname=By.TAG_NAME)
        return locating[find_by]

    def _is_visible(self, find_by: str, locator: str) -> WebElement:
        return self.__wait.until(ec.visibility_of_element_located((self.__get_selenium_by(find_by), locator)))

    def _is_present(self, find_by: str, locator: str) -> WebElement:
        return self.__wait.until(ec.presence_of_element_located((self.__get_selenium_by(find_by), locator)))

    def _is_not_present(self, find_by: str, locator: str) -> WebElement:
        return self.__wait.until(ec.invisibility_of_element_located((self.__get_selenium_by(find_by), locator)))

    def _are_visible(self, find_by: str, locator: str) -> List[WebElement]:
        return self.__wait.until(ec.visibility_of_all_elements_located((self.__get_selenium_by(find_by), locator)))

    def _are_present(self, find_by: str, locator: str) -> List[WebElement]:
        return self.__wait.until(ec.presence_of_all_elements_located((self.__get_selenium_by(find_by), locator)))

    def _is_clickable(self, find_by: str, locator: str) -> WebElement:
        return self.__wait.until(ec.element_to_be_clickable((self.__get_selenium_by(find_by), locator)))

    @staticmethod
    def _get_text_from_list_of_webelements(list_of_elements: List[WebElement]) -> List[str]:
        return [link.text for link in list_of_elements]

    @staticmethod
    def _get_element_from_list_by_text(list_of_elements: List[WebElement], text: str) -> WebElement:
        """The method finds a certain WebElement from a given List of WebElements by text (case-insensitive).
            If several elements is found the method will return the first one."""
        text = text.lower()
        element = [element for element in list_of_elements if element.text.lower() == text]
        if element:             # len(element) != 0
            return element[0]
        else:
            print(f"\nYou wanted to find a WebElement with text '{text}', but there is no element with text like this.")
            assert False, 'There is no element with text like this'

    def _get_select_list(self, find_by: str, locator: str):
        return Select(self._is_present(find_by, locator))

    def find_text_on_page(self, text) -> bool:
        return text in self._driver.page_source

    @staticmethod
    def _find_text_inside_elements(element: List[WebElement], text: str) -> bool:
        a = [elem.text.lower() for elem in element]
        for arg in a:
            if arg.find(text) != -1:
                return True
        return False

    @staticmethod
    def _scroll_to_element(element: WebElement):
        return element.location_once_scrolled_into_view  # return None if element is not visible

    def _move_to_element(self, element: WebElement):
        if 'firefox' in self._driver.capabilities['browserName']:  # To prevent MoveTargetOutOfBoundsException
            self._scroll_to_element(element)
        ActionChains(self._driver).move_to_element(element).perform()
