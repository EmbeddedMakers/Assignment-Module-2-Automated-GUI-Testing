"""This module is used to define a class AmazonSearchTest"""
from src.Amazon import AmazonBase
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService



class AmazonSearchTest(AmazonBase):
    """AmazonSearchTest
    """
    # Defining a method test_add_item_to_cart which is used to add an item to cart
    def test_search_for_item(self):
        """test_search_for_item
        """
        # Find the search bar and enter a query
        search_bar = self.driver.find_element(By.ID, "twotabsearchtextbox")
        search_bar.send_keys("Samsung Galaxy S21")
        search_bar.submit()

        # Wait for the search results page to load
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                             "//div[@data-component-type='s-search-result']"))
        )

        # Get search result 
        results = self.driver.find_element(By.CSS_SELECTOR, ".s-result-list .s-result-item")

        assert results.text == 'RESULTS'

    def run_test(self):
        self.test_search_for_item()
        self.tear_down()

    def announce_test(self) -> None:
        print("\n### Validating Search for Item ###")


