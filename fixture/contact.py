from selenium.webdriver.common.by import By

class ContactHelper:
    def __init__(self, app):
        self.app = app


    def Add(self, contact):
        # Add contact
        self.driver = self.app.driver
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
