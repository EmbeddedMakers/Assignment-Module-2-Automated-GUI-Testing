"""
This module is used to define a class AmazonSearchTest
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.amazon import AmazonBase


class AmazonSearchTest(AmazonBase):
    """AmazonSearchTest"""

    def test_search_for_item(self):
        """test_search_for_item"""
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

        # Click on the first search result to go to its details page
        first_result = self.driver.find_element(By.XPATH,
                                                "//div[@data-component-type='s-search-result']\
                                                 [1]//a[@class='a-link-normal s-no-outline']")
        first_result.click()

        # Wait for the details page to load
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "productTitle"))
        )
        return True

    def run_test(self):
        """The method that runs the test implemented by inherited class."""
        self.set_up()
        ret = self.test_search_for_item()
        self.tear_down()
        return ret

    def announce_test(self) -> None:
        """The method that prints what test will be run."""
        print("\n### Validating Search for Item ###")
