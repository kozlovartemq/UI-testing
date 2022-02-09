import allure
from allure_commons.types import AttachmentType
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as GoogleOptions
from selenium.webdriver.chrome.service import Service as GoogleService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
import pathlib
from pathlib import Path

set_environment = True  # The quantity limit of the 'set_allure_environment_properties' func calls
                        # if "True": environment.properties file will be created before the first test
                        # if "False": NEW environment.properties file will not be created


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")


def set_allure_environment_properties(browser_name, allure_dir, driver, status=set_environment):
    """This function creates environment.properties file for Allure reports once per session."""
    if status is False:
        return None, False
    else:
        status = False
        if allure_dir is None:
            return "\n\nAllure directory didn't select. To select add option --alluredir='directory_name'", status
        else:
            browser_version = driver.capabilities['browserVersion']
            driver_version = None
            if browser_name == "chrome":
                driver_version = driver.capabilities['chrome']['chromedriverVersion'].split(' ')[0]
            elif browser_name == "firefox":
                driver_version = driver.capabilities['moz:geckodriverVersion']
            with open(f'{allure_dir}{pathlib.os.sep}environment.properties', 'w') as file:  # str(Path(
                file.write(f'Browser={browser_name.capitalize()}')
                file.write(f'\nBrowser.Version={browser_version}')
                file.write(f'\nDriver.Version={driver_version}')  # browser_name will exactly be in IF or ELIF
            return "\n\nEnvironment properties for Allure (environment.properties file) was successfully set", status


def get_chrome_options():
    options = GoogleOptions()
    options.add_argument("--start-maximized")

    """for performance improvement in '--headless' mode"""
    # options.add_argument('--headless')
    options.add_argument("--no-proxy-server")
    options.add_argument("--proxy-server='direct://'")
    options.add_argument("--proxy-bypass-list=*")
    return options


def get_firefox_options():
    profile = webdriver.FirefoxProfile()
    # profile.set_preference("general.useragent.override",
    #                        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36")
    options = FirefoxOptions()
    options.add_argument("--start-maximized")
    # options.add_argument("--width=800")
    # options.add_argument("--height=600")
    # options.add_argument('--headless')
    return profile, options


def get_chrome_webdriver():
    options = get_chrome_options()
    service = GoogleService(str(Path(pathlib.Path.cwd() / 'chromedriver')))
    return service, options                  #  driver = webdriver.Chrome() is forbidden here,
                                             #  as this leads to premature opening of the Chrome


def get_firefox_webdriver():
    profile, options = get_firefox_options()
    service = FirefoxService(str(Path(pathlib.Path.cwd() / 'geckodriver')))
    return service, options, profile


@pytest.fixture
def web_driver_init(request):
    """Init before a test"""
    browser_name = request.config.option.browser_name
    allure_dir = request.config.option.allure_report_dir
    global set_environment
    if browser_name == "chrome":
        s, o = get_chrome_webdriver()
        driver = webdriver.Chrome(options=o)
    elif browser_name == "firefox":
        s, o, p = get_firefox_webdriver()
        driver = webdriver.Firefox(service=s, firefox_profile=p, options=o)
    else:
        raise ValueError("Wrong '--browser_name' option. Available: chrome, firefox.")
    if request.cls is not None:
        request.cls.driver = driver
    if set_environment is True:
        allure_environment_status, set_environment = set_allure_environment_properties(browser_name, allure_dir, driver, status=set_environment)
        print(allure_environment_status)
    yield driver
    """Actions after a test"""
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.outcome == 'failed':
        driver = item.funcargs["web_driver_init"]
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
