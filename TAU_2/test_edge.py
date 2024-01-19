import logging
from time import sleep

from selenium import webdriver
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logger = logging.getLogger('mylogger')
logger.setLevel(logging.INFO)

ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

def google_search_test_edge():
    try:
        logger.info('Starting Google Search Test with Edge browser')
        edge_options = EdgeOptions()
        driver = webdriver.Edge(options=edge_options)

        driver.get('https://www.google.com')

        # Akceptuj popup z informacją o cookies
        try:
            cookie_popup = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.ID, 'L2AGLb'))
            )
            cookie_popup.click()
        except Exception as e:
            logger.warning('Cookie popup not found or not needed.')

        sleep(2)

        # Wprowadź zapytanie "github" do pola wyszukiwania
        search_box = driver.find_element(By.NAME, 'q')
        search_box.send_keys('github')
        search_box.submit()

        sleep(2)

        # Sprawdź, czy fraza "github" występuje w tytule strony
        if "github" in driver.title.lower():
            logger.info("Google search successful")
        else:
            logger.error("Google search failed")

    except Exception as e:
        logger.error(f'An error occurred: {e}')

    finally:
        logger.info('End Google Search Test for Edge browser')
        driver.quit()

if __name__ == '__main__':
    google_search_test_edge()
