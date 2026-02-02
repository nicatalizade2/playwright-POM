from pages.login_page import LoginPage
from playwright.sync_api import expect

import pytest
@pytest.mark.parametrize("username,password,should_pass", [
    ("standard_user", "wrong_pass", False),
    ("locked_out_user", "secret_sauce", False),
    ("standard_user", "secret_sauce", True),
])
def test_login_logic(login_page,username, password, should_pass):
    # login_page.open()
    login_page.login(username,password)
    if should_pass == False:
        login_page.assert_login_failed()
    else:
        expect(login_page.page).to_have_url("https://www.saucedemo.com/inventory.html")