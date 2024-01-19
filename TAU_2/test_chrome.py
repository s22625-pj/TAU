import logging
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By

logger = logging.getLogger('mylogger')
logger.setLevel(logging.INFO)

ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

def github_registration_test_chrome():
    try:
        logger.info('Starting GitHub Registration Test with Chrome browser')
        chrome_options = ChromeOptions()
        driver = webdriver.Chrome(options=chrome_options)

        driver.get('https://github.com')
        sleep(2)

        sign_up_btn = driver.find_element(By.LINK_TEXT, 'Sign up')
        sign_up_btn.click()

        logger.info("Move to registration page")
        sleep(2)

        # Add registration test steps here

        logger.info("Registration test successful")

    except Exception as e:
        logger.error(f'An error occurred: {e}')

    finally:
        logger.info('End GitHub Registration Test for Chrome browser')
        driver.quit()

if __name__ == '__main__':
    github_registration_test_chrome()
