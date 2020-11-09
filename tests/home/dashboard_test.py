from pages.home.login_page import LoginPage
from pages.home.dashbaord_page import DashboardPage
from utilities.teststatus import TestStatus
import unittest
import pytest
import time
time.sleep(5)
@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class Dashboard(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp,):
        time.sleep(5)
        self.ts = TestStatus(self.driver)
        self.lp = LoginPage(self.driver)
        self.ad = DashboardPage(self.driver)
        time.sleep(5)

    @pytest.mark.run(order=1)
    def test_validLogin(self):
        self.lp.login("test", "test")
        result1 = self.lp.verifyLoginSuccessful()
        self.ts.mark(result1, "Logged in")
        self.driver.maximize_window()

    @pytest.mark.run(order=2)
    def test_verifyDashboardAdded(self):
        time.sleep(2)
        self.ad.clickStarIcon()
        window_before = self.driver.window_handles[0]
        self.ad.clickAdminSec()
        window_after = self.driver.window_handles[1]
        self.driver.switch_to_window(window_after)
        time.sleep(5)
        self.ad.clickMenuToggle()
        time.sleep(5)
        self.ad.clickWidgetDashboard()
        time.sleep(2)
        self.ad.clickDashboardLink()
        time.sleep(5)
        self.ad.clickCreateDashboard()
        time.sleep(5)
        self.ad.enterDashboardName("DashboardQA1")
        time.sleep(5)
        # self.ad.clickSave1()
        time.sleep(5)
        self.ad.clickDashboardBuilder()
        time.sleep(5)
        self.ad.clickWidgetGroup()
        time.sleep(5)
        self.ad.clickInputContact()
        time.sleep(2)
        self.ad.clickContactGroup()
        time.sleep(5)
        self.ad.clickChooseWidget()
        time.sleep(5)
        self.ad.clickNewMonths()
        time.sleep(5)
        self.ad.clickAddRow()
        time.sleep(2)
        self.ad.clickAddColumn()
        time.sleep(2)
        self.ad.clickAddWidget()
        time.sleep(5)
        # self.ad.clickSave2()
        time.sleep(5)
        self.ad.clickSearchQuicklinks()
        time.sleep(5)
        self.ad.clickSmartSearch()
        time.sleep(5)
        self.ad.clickContactSearch()
        time.sleep(5)
        self.ad.clickChoosePosition()
        time.sleep(5)
        self.ad.clickTopLeft()
        time.sleep(5)
        self.ad.clickAddContact()
        time.sleep(5)
        self.ad.clickLastContact()
        time.sleep(5)
        self.ad.clickMyDashboard()
        time.sleep(5)
        self.ad.clickChoosePosition2()
        time.sleep(5)
        self.ad.clickTopRight()
        time.sleep(5)
        # self.ad.clickSave3()
        # time.sleep(5)
        result = self.ad.verifyDashboardAdded()
        self.ts.mark(result, "Dashboard Found!!")
        assert result