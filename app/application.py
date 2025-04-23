from pages.base_page import Page
# from pages.header import Header
from pages.login_page import LoginPage
from pages.setting_page import SettingPage
# from pages.main_page import MainPage


class Application:
    def __init__(self, driver):
        self.driver = driver

        # self.app_page = AppPage(driver)
        self.base_page = Page(driver)
        # self.header = Header(driver)
        self.login_page = LoginPage(driver)
        # self.main_page = MainPage(driver)
        self.setting_page = SettingPage(driver)

# app = Application()
# app.header.search()
# app.search_results_page.verify_search_results