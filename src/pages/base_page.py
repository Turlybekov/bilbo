import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver: WebDriver, timeout: int = 10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def take_screenshot(self, name="Screenshot"):
        """Captures a screenshot and attaches it directly to the Allure report."""
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name=name,
            attachment_type=allure.attachment_type.PNG
        )

    def open(self, url: str):
        self.driver.get(url)

    def get_title(self):
        return self.driver.title

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def click(self, locator):
        self.find_element(locator).click()

    def send_keys(self, locator, text: str):
        self.find_element(locator).send_keys(text)

    def find_visible(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    def find_clickable(self, locator):
        return self.wait.until(
            EC.element_to_be_clickable(locator)
        )
