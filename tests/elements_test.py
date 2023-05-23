import sys; sys.path.append('../automation_qa_course/')
from pages.elements_page import *
import time

class TestElements:
    class TestTextBox:

        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, TextBoxPage.URL)
            text_box_page.open_url()
            input_data = text_box_page.fill_all_fields()
            output_data = text_box_page.check_filled_form()
            assert input_data == output_data, 'Данные не сходятся'
            
            time.sleep(3)


    class TestCheckBox:

        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, CheckBoxPage.URL)
            check_box_page.open_url()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            input_checkbox = check_box_page.get_checked_checkbox()
            output_result = check_box_page.get_output_result()
            assert input_checkbox == output_result, 'Значения не совпадают'
            
            time.sleep(3)


    class TestRadioButton:
        
        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, RadioButtonPage.URL)
            radio_button_page.open_url()
            radio_button_page.click_radio_btn('yes')
            output_yes = radio_button_page.get_output_result()
            radio_button_page.click_radio_btn('impressive')
            output_impressive = radio_button_page.get_output_result()
            radio_button_page.click_radio_btn('no')
            output_no = radio_button_page.get_output_result()
            
            assert output_yes == 'Yes'
            assert output_impressive == 'Impressive'
            assert output_no == 'No'


    class TestWebTable:
        
        def test_web_table_add_person(self, driver):
            web_table_page = WebTablePage(driver, WebTablePage.URL)
            web_table_page.open_url()
            new_person = web_table_page.add_new_person()
            table_result = web_table_page.check_new_added_person()
            for item in new_person:
                assert item in table_result, 'Данные не совпадают'


        def test_web_table_search_person(self, driver):
            web_table_page = WebTablePage(driver, WebTablePage.URL)
            web_table_page.open_url()
            key_word = web_table_page.add_new_person()[random.randint(0, 5)]
            result = web_table_page.search_some_person(key_word)
            assert result, 'Человек не найден'
            
