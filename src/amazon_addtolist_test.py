"""
This module is used to define a class AmazonAddToListTest
"""

import configparser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import NoSuchElementException

from src.amazon import AmazonBase


class AmazonAddToListTest(AmazonBase):
    """AmazonAddToListTest"""

    # Defining a method test_sign_in which is used to add an item to cart
    def test_add_item_to_list(self):
        """test_add_item_to_list"""
        config = configparser.ConfigParser()
        config.read(r'src/config.ini')
        ap_email = config['amazon_test']['email']
        password = config['amazon_test']['password']
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

        # Add the product to a list
        list_button = self.driver.find_element(By.ID, "wishListMainButton")
        list_button.click()

        # Sign in (if necessary)
        try:
            self.driver.find_element(By.XPATH,
                                     '//*[@id="authportal-main-section"]\
                                     /div[2]/div/div[1]/form/div/div/div/h1')
            # Wait for the login page to load and enter the email and password
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "ap_email"))
            )
            email_input = self.driver.find_element(By.ID, "ap_email")
            email_input.send_keys(ap_email)

            self.driver.find_element(By.ID, "continue").click()
            password_input = self.driver.find_element(By.ID, "ap_password")
            password_input.send_keys(password)

            # Click on the "Sign in" button
            sign_in_button = self.driver.find_element(By.ID, "signInSubmit")
            sign_in_button.click()

            # Add the product to a list
            list_button = self.driver.find_element(By.ID, "wishListMainButton")
            list_button.click()

        except NoSuchElementException:
            pass

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="list-name"]')))

        # Select a list to add the product to
        select_list_dropdown = self.driver.find_element(By.XPATH, '//*[@id="list-name"]')
        select_list_dropdown.click()
        select_list_option = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="list-name"]'))
        )
        select_list_option.click()
        save_button = self.driver.find_element(By.ID, 'wl-redesigned-create-list')
        save_button.click()

        # Continue shopping
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,
                                        '//*[@id="wl-huc-post-create-msg"]\
                                        /div[2]/span[2]/span/span/button')))
        continue_shopping_button = self.driver.find_element(By.XPATH,
                                                            '//*[@id="wl-huc-post-create-msg"]\
                                                            /div[2]/span[2]/span/span/button')
        continue_shopping_button.click()
        return True

    def run_test(self):
        """Run the test"""
        self.set_up()
        ret = self.test_add_item_to_list()
        self.tear_down()
        return ret

    def announce_test(self) -> None:
        """Announce the test"""
        print("\n### Validating Amazon Adding Item To List ###")
