from selenium import webdriver
from selenium.webdriver.common.by import By

class Application():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.vars = {}
        self.driver.implicitly_wait(5)

    def Logout(self):
        # Logout
        self.driver.find_element(By.CSS_SELECTOR, 'a[class*="name"]').click()
        self.driver.find_element(By.CSS_SELECTOR, 'ul>li:nth-child(5)').click()

    def Add_contact(self, contact):
        # Add contact
        self.driver.find_element(By.CSS_SELECTOR, "div>button:nth-child(3)").click()
        self.driver.find_element(By.ID, "to").click()
        self.driver.find_element(By.ID, "to").send_keys(contact.header)
        self.driver.find_element(By.ID, "firstName").click()
        self.driver.find_element(By.ID, "firstName").send_keys(contact.firstname)
        self.driver.find_element(By.ID, "lastName").click()
        self.driver.find_element(By.ID, "lastName").send_keys(contact.lastname)
        self.driver.find_element(By.ID, "phone").click()
        self.driver.find_element(By.ID, "phone").send_keys(contact.number)
        self.driver.find_element(By.ID, "streetname").click()
        self.driver.find_element(By.ID, "streetname").send_keys(contact.street)
        self.driver.find_element(By.CSS_SELECTOR, "span > span").click()

    def Login(self, email, password):
        # Login
        self.Open_home_page()
        self.driver.find_element(By.LINK_TEXT, "Login").click()
        self.driver.find_element(By.ID, "email").click()
        self.driver.find_element(By.ID, "email").send_keys(email)
        self.driver.find_element(By.ID, "password").click()
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, "div.field.end>button:nth-child(1)>span").click()

    def Open_home_page(self):
        # Open home page
        self.driver.get("https://mailbook.app/")

    def destroy(self):
        self.driver.quit()
