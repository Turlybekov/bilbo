import allure

from src.ui.pages.base_page import BasePage


@allure.feature("Browser Test")
@allure.story("Google")
@allure.title("Check google page opens")
def test_browser(browser):
    with allure.step("Opening Google page"):
        page = BasePage(browser)
        page.open("https://www.google.com")
        page.take_screenshot("Google page opened")
    assert page.get_title() == "Google"
