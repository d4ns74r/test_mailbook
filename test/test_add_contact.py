from model.contact import Contact
import pytest
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_addcustomer(app):
    app.Login(email="denisprokofyev88@gmail.com", password="Probka98")
    app.Add_contact(Contact(header="Denis", firstname="Denis", lastname="Prokofyev", number="79255712456", street="Petrozavodskaya"))
    app.Logout()


def test_addcustomer_one_symbol(app):
    app.Login(email="denisprokofyev88@gmail.com", password="Probka98")
    app.Add_contact(Contact(header="D", firstname="D", lastname="P", number="7", street="P"))
    app.Logout()