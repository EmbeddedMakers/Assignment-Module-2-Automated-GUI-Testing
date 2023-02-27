"""
This module is used to define a class AmazonFilterByCustomerReview
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from src.amazon import AmazonBase


class AmazonFilterByCustomerReview(AmazonBase):
    """AmazonFilterByCustomerReview"""

    def test_filter_by_customer_review(self):
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

        # Filter by Customer Reviews
        filter_dropdown = Select(self.driver.find_element(By.XPATH,
                                                          "//select[@id='s-result-sort-select']"))
        filter_dropdown.select_by_value("review-rank")

        # Wait for the search results page to load
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                            "//div[@data-component-type='s-search-result']"))
        )

        # Click on the first search result to go to its details page
        first_result = self.driver.find_element(By.XPATH,
                                                "//div[@data-component-type='s-search-result']\
                                                 [1]//a[@class='a-link-normal s-no-outline']")
        first_result.click()
        reviews_tab = self.driver.find_element(By.ID, "acrCustomerReviewText")
        reviews_tab.click()
        review_count_text = self.driver.find_element(By.ID, "acrCustomerReviewText").text
        review_count = int(review_count_text.split()[0].replace(",", ""))
        assert review_count > 0, f"First product has no customer reviews: {review_count_text}"
        return True

    def run_test(self):
        """The method that runs the test implemented by inherited class."""
        self.set_up()
        ret = self.test_filter_by_customer_review()
        self.tear_down()
        return ret

    def announce_test(self) -> None:
        """The method that prints what test will be run."""
        print("\n### Validating Filter Item by Customer Reviews ###")
