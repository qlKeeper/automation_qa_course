import sys; sys.path.append('../automation_qa_course/')
from pages.elements_page import TextBoxPage
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