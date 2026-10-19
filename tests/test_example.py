from src.pages.base_page import BasePage


def test_browser(browser):
    page = BasePage(browser)
    page.open("https://www.google.com")
    assert page.get_title() == "Google"
