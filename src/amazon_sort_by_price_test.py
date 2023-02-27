"""
This module is used to define a class AmazonSortByPriceTest
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.amazon import AmazonBase


class AmazonSortByPriceTest(AmazonBase):
    """AmazonSortByPriceTest"""

    def test_sort_by_price_item(self):
        """test_search_for_item"""

        # Find the search bar and enter a query
        search_bar = self.driver.find_element(By.ID, "twotabsearchtextbox")
        search_bar.send_keys("Samsung Galaxy S21")
        search_bar.submit()

        # Wait for the search results page to load
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "div.s-result-list")
            )
        )

        # Sort the results by price (low to high)
        sort_dropdown = self.driver.find_element(By.ID, "a-autoid-0-announce")
        sort_dropdown.click()
        sort_price_low_to_high = self.driver.find_element(By.CSS_SELECTOR,
                                                        "option[value='price-asc-rank']")
        sort_price_low_to_high.click()

        # Wait for the page to reload with sorted results
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.s-result-list"))
        )

        # Verify that the results are sorted by price (low to high)
        prices = self.driver.find_elements(By.CSS_SELECTOR, "span.a-price-whole")
        for i in range(len(prices)-1):
            assert int(prices[i].text.replace(",", "")) <= int(prices[i+1].text.replace(",", ""))
        return True

    def run_test(self):
        """The method that runs the test implemented by inherited class."""
        self.set_up()
        ret = self.test_sort_by_price_item()
        self.tear_down()
        return ret

    def announce_test(self) -> None:
        """The method that prints what test will be run."""
        print("\n### Validating Sort Results by Price ###")
