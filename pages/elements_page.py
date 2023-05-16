from locators.elements_page_locators import TextBoxPageLocators
from pages.base_page import BasePage
from generator.generator import generated_person

class TextBoxPage(BasePage):
    
    URL = 'https://demoqa.com/text-box'
    
    locators = TextBoxPageLocators()

    
    def fill_all_fields(self):
        full_name = next(generated_person()).full_name
        email = next(generated_person()).email
        current_address = next(generated_person()).current_address
        permament_address = next(generated_person()).permament_address
        self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.locators.PERMAMENT_ADDRESS).send_keys(permament_address)
        self.element_is_visible(self.locators.SUBMIT).click()

        return full_name, email, current_address, permament_address
    
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