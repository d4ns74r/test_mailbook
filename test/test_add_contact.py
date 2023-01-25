from model.contact import Contact


def test_addcustomer(app):
    app.session.Login(email="denisprokofyev88@gmail.com", password="Probka98")
    app.contact.Add(Contact(header="Denis", firstname="Denis", lastname="Prokofyev", number="79255712456", street="Petrozavodskaya"))
    app.session.Logout()


def test_addcustomer_one_symbol(app):
    app.session.Login(email="denisprokofyev88@gmail.com", password="Probka98")
    app.contact.Add(Contact(header="D", firstname="D", lastname="P", number="7", street="P"))
    app.session.Logout()