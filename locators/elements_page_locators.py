from selenium.webdriver.common.by import By


class TextBoxPageLocators:

    # Form fields
    FULL_NAME = (By.XPATH, '//input[@id="userName"]')
    EMAIL = (By.XPATH, '//input[@id="userEmail"]')
    CURRENT_ADDRESS = (By.XPATH, '//textarea[@id="currentAddress"]')
    PERMAMENT_ADDRESS = (By.XPATH, '//textarea[@id="permanentAddress"]')
    SUBMIT = (By.XPATH, '//button[@id="submit"]')

    # Created form 
    CREATED_FULL_NAME = (By.XPATH, '//p[@id="name"]')
    CREATED_EMAIL = (By.XPATH, '//p[@id="email"]')
    CREATED_CURRENT_ADDRESS = (By.XPATH, '//p[@id="currentAddress"]')
    CREATED_PERMAMENT_ADDRESS = (By.XPATH, '//p[@id="permanentAddress"]')


class CheckBoxPageLocators:

    # Check boxes
    EXPAND_ALL_BTN = (By.XPATH, '//button[@title="Expand all"]')
    ITEM_LIST = (By.XPATH, '//span[@class="rct-checkbox"]')
    CHECKED_ITEMS = (By.XPATH, '//*[@class="rct-icon rct-icon-check"]')
    TITLE_ITEM = './/ancestor::span[@class="rct-text"]'
    OUTPUT_RESULT = (By.XPATH, '//span[@class="text-success"]')


class RadioButtonPageLocators:

    # Radio Button
    YES_BTN = (By.XPATH, '//label[@for="yesRadio"]')
    IMPRESSIVE_BTN = (By.XPATH, '//label[@for="impressiveRadio"]')
    NO_BTN = (By.XPATH, '//label[@for="noRadio"]')
    OUTPUT_RESULT = (By.XPATH, '//span[@class="text-success"]')


class WebTablePageLocators:
    
    # Add person form
    ADD_BUTTON = (By.XPATH, '//button[text()="Add"]')
    FIRSTNAME_INPUT = (By.XPATH, '//input[@id="firstName"]')
    LASTNAME_INPUT = (By.XPATH, '//input[@id="lastName"]')
    EMAIL_INPUT = (By.XPATH, '//input[@id="userEmail"]') 
    AGE_INPUT = (By.XPATH, '//input[@id="age"]')
    SALARY_INPUT = (By.XPATH, '//input[@id="salary"]')
    DEPARTMENT_INPUT = (By.XPATH, '//input[@id="department"]')
    SUBMIT = (By.XPATH, '//button[@id="submit"]')

    # Table
    FULL_PEOPLE_LIST = (By.XPATH, \
    '//div[@class="rt-tr -even" or @class="rt-tr -odd"]//div[@role="gridcell"]')
    SEARCH_BOX = (By.XPATH, '//input[@id="searchBox"]')
    DELETE_BUTTON = (By.XPATH, '//span[@title="Delete"]')
    EDIT_BUTTON = (By.XPATH, '//span[@title="Edit"]')
    ROW_COUNTS = (By.XPATH, '//div[@role="rowgroup"]')
    ROW_COUNTS_BTN = (By.XPATH, '//select[@aria-label="rows per page"]')
