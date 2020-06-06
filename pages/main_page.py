from .base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    #funkcja przejścia na stronę główną
    def go_to_login_page(self):
        login_link = self.driver.find_element(By.CSS_SELECTOR, ".btn.btn-add-to-basket")
        login_link.click()