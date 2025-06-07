from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        return self

    def enter_username(self, username):
        username_field = self.wait.until(EC.presence_of_element_located((By.NAME, "username")))
        username_field.clear()
        username_field.send_keys(username)
        return self

    def enter_password(self, password):
        password_field = self.wait.until(EC.presence_of_element_located((By.NAME, "password")))
        password_field.clear()
        password_field.send_keys(password)
        return self

    def click_login(self):
        login_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.orangehrm-login-button")))
        login_button.click()
        return self

    def get_error_message(self):
        """Отримує повідомлення про помилку при вході"""
        return self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".oxd-alert-content-text"))
        ).text

    def is_dashboard_visible(self):
        """Перевіряє, чи видима панель інструментів після входу"""
        try:
            self.wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".oxd-topbar-header-breadcrumb-module"))
            )
            return True
        except:
            return False