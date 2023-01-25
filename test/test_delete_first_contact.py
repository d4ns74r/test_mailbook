#self.driver.switch_to.alert.accept()

def test_addcustomer(app):
    app.session.Login(email="denisprokofyev88@gmail.com", password="Probka98")
    app.contact.Delete_first_contact()
    app.session.Logout()