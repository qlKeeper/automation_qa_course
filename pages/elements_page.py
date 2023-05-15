from locators.elements_page_locators import TextBoxPageLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    
    URL = 'https://demoqa.com/text-box'
    
    locators = TextBoxPageLocators()

    
    def fill_all_fields(self):
        self.element_is_visible(self.locators.FULL_NAME).send_keys('Pasha')
        self.element_is_visible(self.locators.EMAIL).send_keys('as@sw.com')
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys('NY')
        self.element_is_visible(self.locators.PERMAMENT_ADDRESS).send_keys('LA')
        self.element_is_visible(self.locators.SUBMIT).click()

    
    def check_filled_form(self):
       full_name = self.element_is_present\
        (self.locators.CREATED_FULL_NAME).text.split(':')[1]
       
       email = self.element_is_present\
        (self.locators.CREATED_EMAIL).text.split(':')[1]
       
       current_address = self.element_is_present\
        (self.locators.CREATED_CURRENT_ADDRESS).text.split(':')[1]
       
       permament_address = self.element_is_present\
        (self.locators.CREATED_PERMAMENT_ADDRESS).text.split(':')[1]
       
       return full_name, email, current_address, permament_address