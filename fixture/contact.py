from selenium.webdriver.common.by import By

class ContactHelper:
    def __init__(self, app):
        self.app = app


    def Add(self, contact):
        self.driver = self.app.driver
        self.Fill_group_form(contact)

    def Fill_group_form(self, contact):
        # Add contact
        self.driver = self.app.driver
        self.Fill_contact_form(contact)
        self.driver.find_element(By.CSS_SELECTOR, "span > span").click()

    def Fill_contact_form(self, contact):
        self.driver = self.app.driver
        self.Change_field_value("to", contact.header)
        self.Change_field_value("firstName", contact.firstname)
        self.Change_field_value("lastName", contact.lastname)
        self.Change_field_value("phone", contact.number)
        self.Change_field_value("streetname", contact.street)


    def Change_field_value(self, field_header, text):
        self.driver = self.app.driver
        if text is not None:
            self.driver.find_element(By.ID, field_header).click()
            self.driver.find_element(By.ID, field_header).clear()
            self.driver.find_element(By.ID, field_header).send_keys(text)

    def Delete_first_contact(self):
        self.driver = self.app.driver
        self.select_first_contact()
        self.driver.find_element(By.CSS_SELECTOR, "div.field.row.end>a").click()
        self.driver.switch_to.alert.accept()

    def select_first_contact(self):
        self.driver = self.app.driver
        self.driver.find_element(By.CSS_SELECTOR, "tbody>tr:nth-child(2)").click()

    def Modify_first_contact(self, new_contact_data):
        self.driver = self.app.driver
        # open contact to modify
        self.select_first_contact()
        # fill form
        self.Fill_contact_form(new_contact_data)
        # submit modify
        self.driver.find_element(By.CSS_SELECTOR, "span > span").click()






