from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from pages.base_page import Page


class SettingPage(Page):
    SETTINGS_ICON = (By.CSS_SELECTOR, "[class='settings-code w-embed']")
    COMMUNITY_BTN = (By.CSS_SELECTOR, '[href="/community"]')
    COMMUNITY_PG_URL = 'https://soft.reelly.io/community'
    SUPPORT_BTN = (By.CSS_SELECTOR, "[class='support']")


    def click_on_settings(self):
        self.wait_until_clickable_click(*self.SETTINGS_ICON)


    def click_on_community(self):
        self.driver.execute_script("window.scrollBy(0,1000)", "")
        self.wait_until_clickable_click(*self.COMMUNITY_BTN)


    def click_contact_support_button(self):
        self.wait_until_clickable_click(*self.SUPPORT_BTN)