from po_homework.po.contact_page import ContactPage
from po_homework.po.main_page import MainPage


class TestAddDepartment:
    def setup(self):
        self.main_page = MainPage()
        self.contact_page = ContactPage()
        # pass

    def test_add_single_department(self):
        self.main_page.go_to_contact().click_add_button()
        self.contact_page.add_department()
        department=self.contact_page.get_department()
        assert department == '测试1'