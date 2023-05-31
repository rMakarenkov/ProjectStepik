from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def test_guest_can_go_to_login_page(browser):
    URL = "https://selenium1py.pythonanywhere.com/"
    browser.get(URL)
    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    login_link.click()
