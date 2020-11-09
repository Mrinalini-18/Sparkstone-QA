from pages.home.login_page import LoginPage
from pages.home.meetingwidget_page import MeetingWidgetPage
from utilities.teststatus import TestStatus
import unittest
import pytest
import time

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class MeetingWidgetTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp,):
        time.sleep(5)
        self.ts = TestStatus(self.driver)
        self.lp = LoginPage(self.driver)
        self.mw = MeetingWidgetPage(self.driver)
        time.sleep(5)

    @pytest.mark.run(order=1)
    def test_validLogin(self):
        self.lp.login("test", "test")
        result1 = self.lp.verifyLoginSuccessful()
        self.ts.mark(result1, "Logged in")
        self.driver.maximize_window()
        time.sleep(5)

    @pytest.mark.run(order=2)
    def test_verifyViewMapWorks(self):
        self.mw.clickBurgerMenu()
        time.sleep(5)
        self.mw.clickMapView()
        time.sleep(5)
        self.mw.clickMyLocation()
        time.sleep(5)
        result = self.mw.verifyViewMapworks()
        self.ts.mark(result,"Map View Works")
        assert result