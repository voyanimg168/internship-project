from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


SIGNIN_URL = 'https://soft.reelly.io/sign-in'
EMAIL = 'jackdaw_mg@yahoo.com'
PASSWORD = '*******'
SIGNIN_EMAIL = (By.CSS_SELECTOR, "[data-name='Email 2']")
SIGNIN_PASSWORD = (By.CSS_SELECTOR, "[data-name='Password']")
CONTINUE_PASSWORD_BTN = (By.CSS_SELECTOR, "[class='login-button w-button']")


@given('Open Reelly login page')
def open_reelly_signin_page(context):
    context.driver.get(SIGNIN_URL)
    sleep(5)


@when('Input signin email')
def input_signin_email(context):
    context.app.login_page.input_signin_email()
    # context.wait_until_visible(*SIGNIN_EMAIL)
    # context.EMAIL = context.SIGNIN_EMAIL
    # context.input_text(EMAIL, *SIGNIN_EMAIL)


@when('Input signin password')
def input_signin_password(context):
    context.app.login_page.input_signin_password()
    # context.wait_until_visible(*SIGNIN_PASSWORD)
    # context.PASSWORD = context.SIGNIN_PASSWORD
    # context.input_text(PASSWORD, *SIGNIN_PASSWORD)


@when('Click continue signin button')
def click_continue_signin_btn(context):
    context.app.login_page.click_continue_signin_btn()
    sleep(10)