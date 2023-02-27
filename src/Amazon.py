"""This module is used to define the base amazon class"""
from abc import abstractmethod
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService


class AmazonBase:
    """Amazon base class"""

    def set_up(self):
        """Init function"""
        # Setting up Chrome options
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-setuid-sandbox")
        chrome_options.add_argument(r"user-data-dir=C:\environments\selenium")
        chrome_options.add_argument("--remote-debugging-port=9222")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("start-maximized")
        #chrome_options.binary_location = "C:/Program Files/Google/Chrome/Application/chrome.exe"

        # Initializing the Chrome driver
        self.driver = webdriver.Chrome(options=chrome_options,
                                       service=ChromeService(ChromeDriverManager().install()))

        # Accessing the amazon website
        self.driver.get("https://www.amazon.com/")

    def tear_down(self):
        """This method is used to clean up the environment after test execution"""
        self.driver.quit()

    @abstractmethod
    def announce_test(self) -> None:
        """The method that prints what test will be run"""

    @abstractmethod
    def run_test(self) -> bool:
        """The method that runs the test implemented by inherited class"""
