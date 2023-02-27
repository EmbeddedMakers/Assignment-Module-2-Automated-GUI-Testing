"""This module is used to define a class AmazonCheckoutTest"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from src.amazon import AmazonBase


class AmazonCheckoutTest(AmazonBase):
    """AmazonCheckoutTest"""

    # Defining a method test_sign_in which is used to add an item to cart
    def test_checkout_item(self):
        """test_checkout_item"""
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

        # Wait for the side sheet to appear and click on the "Proceed to checkout" button
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.ID, "attach-accessory-pane")))

        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH,
                                        '//*[@id="attach-sidesheet-checkout-button"]/span/input')))

        checkout_button = self.driver.find_element(By.XPATH,
                                                   '//*[@id="attach-sidesheet-checkout-button"]\
                                                   /span/input')
        checkout_button.click()

        return True

    def run_test(self):
        """Run the test"""
        self.set_up()
        ret = self.test_checkout_item()
        self.tear_down()
        return ret

    def announce_test(self) -> None:
        """Announce the test"""
        print("\n### Validating Item Checkout to Amazon ###")
