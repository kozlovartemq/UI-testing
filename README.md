# Introduction
This is a pet-project of UI-testing automation framework with Python, Selenium, Pytest, Allure, Jenkins using POM (Page Object Model) design pattern.

Testing website: http://automationpractice.com/

#Files
**/base**
- seleniumbase.py — contains PageObject pattern implementation

**/locators**
- locators.py — contains helper classes to define web elements on web pages

**/pages**
- homepage.py — contains methods that interact with Home page web elements
- contactus_page.py — contains methods that interact with Contact Us page web elements
- register_page.py — contains methods that interact with Register page web elements

**/tests**
- conftest.py — contains the fixture that is used by tests, the plugin that makes screenshot when a test fail,
the function that creates a environment.properties file
- test_homepage.py — contains UI tests for Home page of the website
- test_contactus_page.py — contains UI tests for Contact Us page of the website
- test_register_page.py — contains UI tests for Register page of the website

**/testdata**
- testdata.py — contains data that is used while tests execution
- ContactUs form.txt — file that attached to the Contact Us form

**/allure-results** — default Allure directory. Can be changed via --alluredir="dir_name" command
- categories.json — file that fills the "categories" section in Allure report
- environment.properties — file that is created before a first test execution starts. 
It fills the "environment" section in Allure report

**pytest.ini** — configuration file. Contains pytest launch options

**requirements.txt** — requirements file

#Prerequisites
1. Install all requirements:


    pip install -r requirements.txt

2. Download and move to the repo directory WebDrivers compatible with your OS and browser's version:

- for Chrome: https://chromedriver.chromium.org/downloads
- for Firefox: https://github.com/mozilla/geckodriver/releases

Avoid chrome WebDriver ver. 98 as it may not work as expected.

3. To generate Allure reports install Allure:

https://docs.qameta.io/allure/#_installing_a_commandline

#How to run

Quickrun all the tests in the directory:

    pytest
Specify launch options in pytest.ini file and/or using command line.

Pytest documentation can be found at https://docs.pytest.org/

Custom options: 
- --browser_name (chrome or firefox) — to choose a browser (default is **_chrome_**)
- --headless — to launch browsers in 'headless' mode

#Make an Allure report

If tests were run with --alluredir="allure-results" (by default) option, it is possible to generate an Allure report:

    allure serve allure-results

Allure documentation can be found at https://docs.qameta.io/allure/
