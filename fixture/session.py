from selenium.webdriver.common.by import By

class SessionHelper:

    def __init__(self, app):
        self.app = app

    def Login(self, email, password):
        self.driver = self.app.driver
        self.app.Open_home_page()
        self.driver.find_element(By.LINK_TEXT, "Login").click()
        self.driver.find_element(By.ID, "email").click()
        self.driver.find_element(By.ID, "email").send_keys(email)
        self.driver.find_element(By.ID, "password").click()
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, "div.field.end>button:nth-child(1)>span").click()

    def Logout(self):
        self.driver = self.app.driver
        self.driver.find_element(By.CSS_SELECTOR, 'a[class*="name"]').click()
        self.driver.find_element(By.CSS_SELECTOR, 'ul>li:nth-child(5)').click()