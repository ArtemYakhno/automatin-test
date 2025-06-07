import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages import login_page


class TestLogin:
    def test_successful_login(self, login_page):
        (login_page.open()
         .enter_username("Admin")
         .enter_password("admin123")
         .click_login())

        assert login_page.is_dashboard_visible(), "Dashboard is not visible after successful login"

    def test_failed_login_wrong_password(self, login_page):
        (login_page.open()
         .enter_username("Admin")
         .enter_password("wrong_password")
         .click_login())

        error_message = login_page.get_error_message()
        assert "Invalid credentials" in error_message, "Expected error message not displayed"

    def test_navigation_after_login(self, login_page):
        (login_page.open()
         .enter_username("Admin")
         .enter_password("admin123")
         .click_login())

        WebDriverWait(login_page.driver, 10).until(
            EC.url_contains("dashboard/index")
        )
        assert "/dashboard/index" in login_page.driver.current_url.lower()