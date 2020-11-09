from pages.home.login_page import LoginPage
from pages.home.addtask_page import AddTaskPage
from utilities.teststatus import TestStatus
import unittest
import pytest
import time
time.sleep(5)
@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class AddTask(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp,):
        time.sleep(5)
        self.ts = TestStatus(self.driver)
        self.lp = LoginPage(self.driver)
        self.at = AddTaskPage(self.driver)
        time.sleep(5)

    @pytest.mark.run(order=1)
    def test_validLogin(self):
        self.lp.login("test", "test")
        result1 = self.lp.verifyLoginSuccessful()
        self.ts.mark(result1, "Logged in")
        self.driver.maximize_window()

    @pytest.mark.run(order=2)
    def test_verifyAddTaskSuccessful(self):
        self.at.clickMycontactLink()
        self.at.clickSelectRow()
        time.sleep(5)
        self.at.clickRowMenu()
        time.sleep(5)
        self.at.clcikOpenMenu()
        time.sleep(5)
        self.at.clickAddTask()
        time.sleep(5)
        self.at.clickClickNext()
        time.sleep(5)
        self.at.clickFullModal()
        time.sleep(5)
        self.at.clickCurrentStatus()
        time.sleep(5)
        self.at.clickSendContinue()
        time.sleep(2)
        self.at.clickSaveButton()
        time.sleep(2)
        self.at.clickFollowUp()
        time.sleep(2)
        self.at.clickFullConfirm()
        time.sleep(2)
        self.at.clickConfirmCurrent()
        time.sleep(2)
        result2 = self.at.verifyAddTaskSuccessful()
        time.sleep(5)
        self.ts.mark(result2, "Succsess")
        assert result2