from selenium.webdriver.common.by import By
from time import sleep
from features.steps.reelly_login_steps import SIGNIN_PASSWORD, SIGNIN_EMAIL
from pages.base_page import Page


class LoginPage(Page):
    SIGNIN_URL = 'https://soft.reelly.io/sign-in'
    EMAIL = 'jackdaw_mg@yahoo.com'
    PASSWORD = 'Percival'
    SIGNIN_EMAIL = (By.CSS_SELECTOR, "[data-name='Email 2']")
    SIGNIN_PASSWORD = (By.CSS_SELECTOR, "[data-name='Password']")
    CONTINUE_SIGNIN_BTN = (By.CSS_SELECTOR, "[class='login-button w-button']")


    def open_reelly_signin_page(self):
        self.driver.get(self.SIGNIN_URL)


    def input_signin_email(self):
        self.wait_until_visible(*self.SIGNIN_EMAIL)
        self.input_text(self.EMAIL, *self.SIGNIN_EMAIL)
        EMAIL = self.SIGNIN_EMAIL
        assert EMAIL == self.SIGNIN_EMAIL, \
            f'Expected text {EMAIL} does not match actual {self.SIGNIN_EMAIL}'


    def input_signin_password(self):
        self.wait_until_visible(*self.SIGNIN_PASSWORD)
        sleep(10)
        self.input_text(self.PASSWORD, *self.SIGNIN_PASSWORD)

        PASSWORD = SIGNIN_PASSWORD
        assert PASSWORD == SIGNIN_PASSWORD, \
           f'Expected text {PASSWORD} does not match actual {SIGNIN_PASSWORD}'


    def click_continue_signin_btn(self):
        sleep(10)
        self.click(*self.CONTINUE_SIGNIN_BTN)
        sleep(5)



