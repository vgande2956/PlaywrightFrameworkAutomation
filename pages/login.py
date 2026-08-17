class Login:
    
    def __init__(self, page):
        self.page = page
        self.page_header = page.locator("div.login_logo")
        self.username_input = page.get_by_placeholder("Username")
        self.password_input = page.get_by_placeholder("Password")
        self.login_button = page.get_by_role("button")
        self.login_credentials_username = page.locator(".login_credentials")
        self.login_credentials_password = page.locator(".login_password")

    def get_username_credentials(self):
        user_name = self.login_credentials_username.text_content()
        print(user_name.split("user")[1].replace("names are:", "")+"user")
        return user_name.split("user")[1].replace("names are:", "")+ "user"

    def get_password_credentials(self):
        user_password = self.login_credentials_password.text_content()
        print(user_password.split(":")[1].strip())
        return user_password.split(":")[1].strip()

    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()