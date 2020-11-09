from pages.home.login_page import LoginPage
from pages.home.formedit_page import FormEditPage
from utilities.teststatus import TestStatus
import unittest
import pytest
import time
time.sleep(5)
@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class AddMessage(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp,):
        time.sleep(5)
        self.ts = TestStatus(self.driver)
        self.lp = LoginPage(self.driver)
        self.fe = FormEditPage(self.driver)
        time.sleep(5)

    @pytest.mark.run(order=1)
    def test_validLogin(self):
        self.lp.login("test", "test")
        result1 = self.lp.verifyLoginSuccessful()
        self.ts.mark(result1, "Logged in")
        self.driver.maximize_window()

    @pytest.mark.run(order=2)
    def test_verifyTabCreated(self):
        time.sleep(2)
        self.fe.clickStarIcon()
        window_before = self.driver.window_handles[0]
        self.fe.clickAdminSec()
        window_after = self.driver.window_handles[1]
        self.driver.switch_to_window(window_after)
        time.sleep(5)
        self.fe.clickMenuToggle()
        time.sleep(5)
        self.fe.clickContactMenu()
        time.sleep(2)
        self.fe.clickFormMgmt()
        time.sleep(5)
        self.fe.clickBusinessContact()
        time.sleep(2)
        self.fe.clickCustomTab()
        time.sleep(2)
        self.fe.clickAddTab()
        time.sleep(2)
        self.fe.enterAddTitle("Test")
        time.sleep(2)
        self.fe.clickMakeVisible()
        time.sleep(2)
        # self.fe.enterAddPosition("6")
        time.sleep(2)
        self.fe.clickCreateTab()
        result = self.fe.verifyTabCreated()
        self.ts.mark(result, "Template Found!!")
        assert result
