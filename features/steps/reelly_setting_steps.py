from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


SETTINGS_ICON = (By.CSS_SELECTOR, "[class='settings-code w-embed']")
COMMUNITY_BTN = (By.CSS_SELECTOR, "[class='setting-text']"[6])
COMMUNITY_PG_URL = 'https://soft.reelly.io/community'
SUPPORT_BTN = (By.CSS_SELECTOR, "[class='support']")


@when('Click on Settings')
def click_on_settings(context):
    context.app.setting_page.click_on_settings()


@when('Click on Community')
def click_on_community(context):
    # context.driver.click(*COMMUNITY_BTN)
    context.app.setting_page.click_on_community()


@then('Verify Community page opens')
def verify_community_page_opens(context):
    context.app.setting_page.verify_community_page_opens()


@then('Verify Contact Support button is clickable')
def verify_contact_support_button_clickable(context):
    context.app.setting_page.verify_contact_support_button_clickable()

