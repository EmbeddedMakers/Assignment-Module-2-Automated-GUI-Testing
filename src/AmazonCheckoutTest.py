"""This module is used to define a class AmazonCheckoutTest"""
from src.AmazonCartTest import AmazonCartTest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



class AmazonCheckoutTest(AmazonBase):
    """AmazonCheckoutTest
    """
    # Defining a method test_checkout_item which is used to add an item to cart
    def test_checkout_item(self):
        """test_checkout_item
        """
        # Find the search bar and enter a query
        search_bar = self.driver.find_element(By.ID, "twotabsearchtextbox")
        search_bar.send_keys("Samsung Galaxy S21")
        search_bar.send_keys(Keys.RETURN)

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

        # Wait for the details page to load
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "productTitle"))
        )

        # Click the "Add to Cart" button
        add_to_cart_button = self.driver.find_element(By.ID, "add-to-cart-button")
        add_to_cart_button.click()

        # Wait for the item to be added to the cart
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                             '/html/body/div[1]/div[2]/div/div[1]/div[1]/div[2]/div[1]'))
        )

        cart_icon = self.driver.find_element(By.ID, "nav-cart")
        cart_icon.click()
        
        # Wait for the cart page to load and click on the "Proceed to Checkout" button
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "/html/body/div[1]/div[2]/div[3]/div[3]/div/div[1]/div[1]/div/form/div/div/span/span/span/input")))
        proceed_to_checkout_button = self.driver.find_element(By.XPATH,
                                                              "/html/body/div[1]/div[2]/div[3]/div[3]/div/div[1]/div[1]/div/form/div/div/span/span/span/input")
        proceed_to_checkout_button.click()
        
        # Wait for the login page to load and enter the email and password
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "ap_email")))
        email_input = self.driver.find_element(By.ID, "ap_email")
        emailid = input("What is your emailid?(Press enter at the end to continue):")
        email_input.send_keys(
            emailid
        )

        self.driver.find_element(By.ID, "continue").click()
        password_input = self.driver.find_element(By.ID, "ap_password")
        password = input("What is your password?(Press enter at the end to continue):")
        password_input.send_keys(
            password
        )
        
        # Click on the "Sign in" button
        sign_in_button = self.driver.find_element(By.ID, "signInSubmit")
        sign_in_button.click()
        
        # Wait

    def run_test(self):
        self.test_checkout_item()
        self.tear_down()

    def announce_test(self) -> None:
        print("\n### Validating Item Added to Chart ###")

