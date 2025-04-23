from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.firefox import GeckoDriverManager
from app.application import Application
from support.logger import logger


def browser_init(context):
    """
    :param context: Behave context
    """
    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    context.driver = webdriver.Chrome(service=service)

    context.driver.maximize_window()
    context.driver.implicitly_wait(4) #only shows up in environment.py file
    context.driver.wait = WebDriverWait(context.driver, 10)
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    logger.info(f'\nStarted scenario: {scenario.name}')
    browser_init(context)

def before_step(context, step):
    logger.info(f'Started step: {step}')
    print('\nStarted step: ', step)

def after_step(context, step):
    if step.status == 'failed':
        logger.warning(f'Step failed {step}')
        print('\nStep failed: ', step)

def after_scenario(context, feature):
    context.driver.quit()
    # Add browser logs:
    # browser_logs = context.driver.get_log('browser')
    # with open ('browser_logs.txt', 'w') as log_file:
    #     for log_entry in browser_logs:
    #         log_file.write(f"{log_entry['level']}) - {log_entry['timestamp']} - {log_entry['message']}\n")
    # print("Browser logs saved to browser_logs.txt")
