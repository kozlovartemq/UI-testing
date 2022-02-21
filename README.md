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

**/reports** — Allure directory with old test results

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
Specify launch options in **pytest.ini** file and/or using command line.

Pytest documentation can be found at https://docs.pytest.org/

Custom options: 
- --browser_name (chrome or firefox) — to choose a browser (default is **_chrome_**)
- --headless — to launch browsers in 'headless' mode

#Make an Allure report

If tests were run with --alluredir="allure-results" (by default) option, it is possible to generate an Allure report:

    allure serve allure-results

Allure documentation can be found at https://docs.qameta.io/allure/

If the website is down, it is possible to generate an Allure report using old test results:

    allure serve reports

#Test Cases
1. Verify that contact us form sends successfully
   1. Go to the Contact Us page;
   2. fill in all the required fields (attach txt file); 
   3. Press 'Send' button; 
   4. Make sure that a message about successful sending is displayed.
2. Verify that error message appears if Message area is empty
   1. Go to the Contact Us page;
   2. fill in all the required fields (attach txt file), except the 'Message' field;
   3. Press 'Send' button;
   4. Make sure that the error message 'The message cannot be blank.' is displayed.
3. Verify the ability to register
   1. Go to the Register page;
   2. Complete registration on the website by filling in all the required fields;
   3. Press 'Register' button;
   4. Verify that 'My Account' page is displayed.
4. Verify the ability to search items
   1. Go to the Home page;
   2. Search for 'Blouse';
   3. Make sure this product appears in the search results.
5. Verify the ability to add and remove items from the cart
   1. Go to the Home page;
   2. Search for some product;
   3. Add a product to the cart;
   4. Make sure this product appears in the cart;
   5. Remove this product from the cart;
   6. Make sure the cart is empty.
6. Verify that products appears in a catalog
   1. Go to the Home page;
   2. Go to the Catalog Page (Women -> T-Shirts);
   3. Make sure the 'T-Shirt' product appears.
7. Verify the ability to order a product
   1. Go to the Home page;
   2. Search for some product;
   3. Add a product to the cart;
   4. Complete the order of the product by going through all the required steps.
   5. Make sure the product appears in the Order History Page.
8. Verify header navigation links text
   1. Go to the Home page;
   2. Make sure that header links have "WOMEN", "DRESSES" and "T-SHIRTS" text respectively.