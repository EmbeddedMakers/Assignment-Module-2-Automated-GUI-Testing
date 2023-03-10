"""This module is used to define a class AmazonCartTest"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from src.amazon import AmazonBase


class AmazonCartTest(AmazonBase):
    """AmazonCartTest
    """

    def test_add_item_to_cart(self):
        """test_add_item_to_cart
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

        # Click on the first search result to go to its details page
        first_result = self.driver.find_element(By.XPATH,
                                                "//div[@data-component-type='s-search-result']\
                                                 [1]//a[@class='a-link-normal s-no-outline']")
        first_result.click()

        # Wait for the details page to load
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "productTitle"))
        )

        # Click the "Add to Cart" button
        add_to_cart_button = self.driver.find_element(By.ID, "add-to-cart-button")
        add_to_cart_button.click()

        # Wait for the item to be added to the cart
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "attachDisplayAddBaseAlert"))
        )
        # Verify that the cart count has increased
        cart_count = self.driver.find_element(By.ID, "nav-cart-count")
        return int(cart_count.text) >= 1

    def run_test(self):
        """Run the test"""
        self.set_up()
        ret = self.test_add_item_to_cart()
        self.tear_down()
        return ret

    def announce_test(self) -> None:
        """Announce the test"""
        print("\n### Validating Item Added to Cart ###")
