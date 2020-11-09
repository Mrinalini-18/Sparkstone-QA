from pages.home.login_page import LoginPage
from pages.home.editcontact_page import EditContactPage
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
        self.uc = EditContactPage(self.driver)
        time.sleep(5)

    @pytest.mark.run(order=1)
    def test_validLogin(self):
        self.lp.login("test", "test")
        result1 = self.lp.verifyLoginSuccessful()
        self.ts.mark(result1, "Logged in")
        self.driver.maximize_window()

    @pytest.mark.run(order=2)
    @data(*getCSVData("C:/Users/mrina/PycharmProjects/Sparkstone/editcontact.csv"))
    @unpack
    def test_verifyUpdateSuccessful (self, company, address1, town, postcode, country):
        self.uc.clickMycontactLink()
        time.sleep(2)
        self.uc.clickContactRow()
        self.uc.clickEditAddress()
        time.sleep(5)
        # self.uc.clickSelectContact()
        # self.uc.enterSelectCompany(company)
        self.uc.enterAddressLine1(address1)
        self.uc.enterAddTown(town)
        time.sleep(2)
        self.uc.enterAddPostcode(postcode)
        self.uc.enterAddCountry(country)
        time.sleep(5)
        self.uc.clickClickUpdate()
        time.sleep(2)
        result = self.co.verifyUpdateSuccessful()
        self.ts.mark(result, "Contact updated")
        assert result
