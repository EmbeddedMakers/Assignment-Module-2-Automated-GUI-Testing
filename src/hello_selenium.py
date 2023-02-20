"""This module is used to define a class AmazonCartTest"""
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService



class AmazonCartTest:
    """AmazonCartTest
    """
    def __init__(self):
        """ Setup function
        """
        # Setting up Chrome options
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-setuid-sandbox")
        chrome_options.add_argument(r"user-data-dir=C:\environments\selenium")
        chrome_options.add_argument("--remote-debugging-port=9222")
        chrome_options.add_argument("--disable-dev-shm-using")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("start-maximized")

        # Initializing the Chrome driver
        self.driver = webdriver.Chrome(options=chrome_options,
                                       service=ChromeService(ChromeDriverManager().install()))

        # Accessing the Amazon website
        self.driver.get("https://www.amazon.com/")

    # Defining a method test_add_item_to_cart which is used to add an item to cart
    def test_add_item_to_cart(self):
        """test_add_item_to_cart
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
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH,
                                             '/html/body/div[4]/div[3]/div/div/div[1]'))
        )

    # Defining a method tearDown which is used to clean up the environment after test execution
    def tear_down(self):
        """tearDown
        """
        self.driver.quit()


def main() -> None:
    """main
    """
    amazon_cart_obj = AmazonCartTest()
    amazon_cart_obj.test_add_item_to_cart()
    amazon_cart_obj.tear_down()



if __name__ == '__main__':
    main()
