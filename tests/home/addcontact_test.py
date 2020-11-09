from pages.home.login_page import LoginPage
from pages.home.addcontact_page import AddContactPage
from utilities.teststatus import TestStatus
import unittest
import pytest
import time
from utilities.read_data import getCSVData
from ddt import ddt, data, unpack

time.sleep(5)
@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class AddContact(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp,):
        time.sleep(5)
        self.ts = TestStatus(self.driver)
        self.lp = LoginPage(self.driver)
        self.ac = AddContactPage(self.driver)
        time.sleep(5)

    @pytest.mark.run(order=1)
    def test_validLogin(self):
        self.lp.login("test", "test")
        result1 = self.lp.verifyLoginSuccessful()
        self.ts.mark(result1, "Logged in")
        self.driver.maximize_window()

    @pytest.mark.run(order=2)
    @data(*getCSVData("C:/Users/mrina/PycharmProjects/Sparkstone/addcontact.csv"))
    @unpack
    def test_verifySubmitSuccessful(self, companyname, firstname, lastname, phone, email):
        self.ac = AddContactPage(self.driver)
        self.ac.clickAddIcon()
        time.sleep(10)
        self.ac.Add(companyname, firstname, lastname, phone, email)
        time.sleep(5)
        self.ac.clickSaveContact()
        time.sleep(10)
        result = self.ac.verifySubmitSuccessful()
        self.ts.mark(result , "Succsess")
        assert result

