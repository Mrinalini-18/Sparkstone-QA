from pages.home.login_page import LoginPage
from pages.home.createopp_page import CreateOppPage
from utilities.teststatus import TestStatus
import unittest
import pytest
import time
time.sleep(5)
@pytest.mark.usefixtures("oneTimeSetUp", "setUp")

class CreateOpp(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp,):
        time.sleep(5)
        self.ts = TestStatus(self.driver)
        self.lp = LoginPage(self.driver)
        self.co = CreateOppPage(self.driver)
        time.sleep(5)

    @pytest.mark.run(order=1)
    def test_validLogin(self):
        self.lp.login("test", "test")
        result1 = self.lp.verifyLoginSuccessful()
        self.ts.mark(result1, "Logged in")
        self.driver.maximize_window()

    @pytest.mark.run(order=2)
    def test_verifyCreateOppSuccessful(self):
        self.co.clickMycontactLink()
        time.sleep(2)
        self.co.clickSelectRow()
        time.sleep(2)
        self.co.clickRowMenu()
        time.sleep(2)
        self.co.clickOpenMenu()
        time.sleep(2)
        self.co.clickCreateOpp()
        time.sleep(2)
        self.co.clickSaveOpp()
        result =self.co.verifyCreateOppSuccessful()
        self.ts.mark(result, "Opportunity Added")
        assert result