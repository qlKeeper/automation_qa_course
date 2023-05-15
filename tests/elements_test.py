import sys; sys.path.append('../automation_qa_course/')
from pages.elements_page import TextBoxPage
import time

class TestElements:
    class TestTextBox:

        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, TextBoxPage.URL)
            text_box_page.open_url()
            text_box_page.fill_all_fields()
            output_name, output_email, output_cur_addr, output_per_addr = \
            text_box_page.check_filled_form()
            print(output_name, output_email, output_cur_addr, output_per_addr)
            time.sleep(3)