from model.contact import Contact

def test_modify_contact_header(app):
    app.session.Login(email="denisprokofyev88@gmail.com", password="Probka98")
    app.contact.Modify_first_contact(Contact(header='New name'))
    app.session.Logout()


#def test_modify_contact_firstname(app):
    #app.session.Login(email="denisprokofyev88@gmail.com", password="Probka98")
    #app.contact.Modify_first_contact(Contact(firstname='New name'))
    #app.session.Logout()

