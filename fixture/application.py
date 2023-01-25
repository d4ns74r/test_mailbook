from selenium import webdriver
from selenium.webdriver.common.by import By
from fixture.session import SessionHelper
from fixture.contact import ContactHelper

class Application():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.vars = {}
        self.driver.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.contact = ContactHelper(self)


    def Open_home_page(self):
        self.driver.get("https://mailbook.app/")

    def destroy(self):
        self.driver.quit()
