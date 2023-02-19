from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class AmazonCartTest():

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.amazon.com/")

    def test_add_item_to_cart(self):
        # Find the search bar and enter a query
        search_bar = self.driver.find_element(By.ID, "twotabsearchtextbox")
        search_bar.send_keys("Samsung Galaxy S21")
        search_bar.send_keys(Keys.RETURN)

        # Wait for the search results page to load
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@data-component-type='s-search-result']"))
        )

        # Click on the first search result to go to its details page
        first_result = self.driver.find_element(By.XPATH,
            "//div[@data-component-type='s-search-result'][1]//a[@class='a-link-normal s-no-outline']")
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
            EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div[3]/div/div/div[1]'))
        )

    def tearDown(self):
        self.driver.quit()

def main() -> None:
    AmazonCartTestObj =  AmazonCartTest()
    AmazonCartTest.setUp(AmazonCartTestObj)
    AmazonCartTest.test_add_item_to_cart(AmazonCartTestObj)
    AmazonCartTest.tearDown(AmazonCartTestObj)


if __name__ == '__main__':
    main()