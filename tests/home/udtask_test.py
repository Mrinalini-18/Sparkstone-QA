from pages.home.login_page import LoginPage
from pages.home.udtask_page import AddUdtaskPage
from utilities.teststatus import TestStatus
import unittest
import pytest
import time
time.sleep(5)
@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class AddUdtask(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp,):
        time.sleep(5)
        self.ts = TestStatus(self.driver)
        self.lp = LoginPage(self.driver)
        self.ud = AddUdtaskPage(self.driver)
        time.sleep(5)

    @pytest.mark.run(order=1)
    def test_validLogin(self):
        self.lp.login("test", "test")
        result1 = self.lp.verifyLoginSuccessful()
        self.ts.mark(result1, "Logged in")
        self.driver.maximize_window()

    @pytest.mark.run(order=2)
    def test_verifyUdTaskAdded(self):
        time.sleep(2)
        self.ud.clickStarIcon()
        window_before = self.driver.window_handles[0]
        self.ud.clickAdminSec()
        window_after = self.driver.window_handles[1]
        self.driver.switch_to_window(window_after)
        time.sleep(5)
        self.ud.clickMenuToggle()
        time.sleep(5)
        self.ud.clickTaskLink()
        time.sleep(2)
        self.ud.clickTaskTypes()
        time.sleep(2)
        self.ud.clickCreateTasktype()
        time.sleep(2)
        self.ud.enterTaskName("QA")
        time.sleep(2)
        self.ud.enterShortName("QA")
        time.sleep(4)
        self.ud.clickChooseGroup()
        time.sleep(4)
        self.ud.clickUserDefined()
        time.sleep(4)
        self.ud.enterAddDescription("Test")
        time.sleep(4)
        self.ud.clickSearchGroup()
        time.sleep(4)
        self.ud.clickChooseMeeting()
        time.sleep(4)
        self.ud.clickChooseType()
        time.sleep(4)
        self.ud.clickDefaultType()
        time.sleep(4)
        self.ud.clickSaveButton()
        time.sleep(4)
        result = self.ud.verifyUdTaskAdded()
        self.ts.mark(result, "Task Added!!")
        assert result