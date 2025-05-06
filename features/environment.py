from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.firefox import GeckoDriverManager

from app.application import Application
from support.logger import logger

# Command to run tests with Allure & Behave:
# behave -f allure_behave.formatter:AllureFormatter -o test_results/ features/tests/target_search.feature


def browser_init(context, scenario_name):
    """
    :param context: Behave context
    """
    # driver_path = ChromeDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Chrome(service=service)

    # driver_path = GeckoDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Firefox(service=service)

    # context.driver = webdriver.Safari()  #driver already built into Safari

    #Headless Mode
    # options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # service = Service(ChromeDriverManager().install())
    # context.driver = webdriver.Chrome(
    #   options=options,
    #   service=service
    # )

    # options = webdriver.FirefoxOptions()
    # options.add_argument('headless')
    # service = Service(GeckoDriverManager().install())
    # context.driver = webdriver.Firefox(
    #   options=options,
    #   service=service
    # )

    #Register for BrowserStack, then grab from https://www.browserstack.com/accounts/settings
    bs_user ='mg_Zgr37v'
    bs_key ='kjnLGnGdfsyGssbKspPQ'
    url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'

    options = Options()
    bstack_options = {
         "os" : "Windows",
         "osVersion" : "13.0",
         "deviceName": "Google Pixel 7",
         "realMobile": "true",
         "browserName" : 'chrome',
         "sessionName" : scenario_name,
         # "interactiveDebugging" : True,
    }
    options.set_capability('bstack:options', bstack_options)
    context.driver = webdriver.Remote(command_executor=url, options=options)


    # context.driver.maximize_window()
    context.driver.implicitly_wait(4) #only shows up in environment.py file
    context.driver.wait = WebDriverWait(context.driver, 10)
    context.app = Application(context.driver)

def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    logger.info(f'\nStarted scenario: {scenario.name}')
    browser_init(context, scenario.name)

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

