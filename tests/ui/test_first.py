from pages.homePage import Homepage
from pages.login import Login

def test_example_one(page):
    obj_login = Login(page)
    obj_homepage = Homepage(page)
    
    page.goto("https://www.saucedemo.com/")
    obj_login.login(obj_login.get_username_credentials(), obj_login.get_password_credentials())
    obj_homepage.validate_homepage()
    
    