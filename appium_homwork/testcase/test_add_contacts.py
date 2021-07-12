from appium_homwork.po.app import App



class TestAddContact:
    def setup(self):
        self.app = App()

    def teardown(self):
        self.app.app_close()
        # pass

    def test_add_contacts(self):
        self.app.start().go_to_main_page().go_to_contacts_page().go_to_add_people_page().go_to_edit_people_page().edit_people()
        # pass
