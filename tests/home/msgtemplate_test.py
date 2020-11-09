from pages.home.login_page import LoginPage
from pages.home.msgtemplate_page import AddMessagePage
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
        self.am = AddMessagePage(self.driver)
        time.sleep(5)

    @pytest.mark.run(order=1)
    def test_validLogin(self):
        self.lp.login("test", "test")
        result1 = self.lp.verifyLoginSuccessful()
        self.ts.mark(result1, "Logged in")
        self.driver.maximize_window()

    @pytest.mark.run(order=2)
    def test_verifyTemplateAdded(self):
        time.sleep(2)
        self.am.clickStarIcon()
        window_before = self.driver.window_handles[0]
        self.am.clickAdminSec()
        window_after = self.driver.window_handles[1]
        self.driver.switch_to_window(window_after)
        time.sleep(5)
        self.am.clickMenuToggle()
        time.sleep(5)
        self.am.clickOpenMessaging()
        time.sleep(2)
        self.am.clickMessageTemplate()
        time.sleep(5)
        self.am.clickCreateTemplate()
        time.sleep(2)
        self.am.enterTemplateName("AAA Template")
        time.sleep(2)
        self.am.enterTemplateSubject("AutomatedEmail")
        time.sleep(10)
        # self.driver.switch_to.frame(self.driver.find_element_by_xpath("/html/body/section/div/section/section[2]/div/div/section[2]/div/div/div/form/div[1]/div/div[1]/div/div/div/div[5]/div/div/div/div/div[2]/div/table/tbody/tr[2]/td/iframe"))
        time.sleep(5)
        self.am.clickSwitchCode()
        self.am.enterEditorAdd(data="<p>&nbsp;</p><p>[EmailHistory]</p>")
        time.sleep(2)
        self.am.clickSaveButton()
        time.sleep(2)
        self.am.clickSwitchSetting()
        time.sleep(2)
        self.am.enterAddDescription("Description001")
        time.sleep(2)
        self.am.clickSelectSave()
        time.sleep(2)
        self.driver.switch_to_window(window_before)
        self.am.clickDashboardsec()
        time.sleep(2)
        self.am.clickMyContact()
        time.sleep(2)
        self.am.clickSelectRow()
        time.sleep(2)
        self.am.clickAddTask()
        time.sleep(5)
        self.am.clickMaximizeModal()
        time.sleep(5)
        self.am.clickWriteTemplate()
        time.sleep(2)
        self.am.enterTemplateAAA('AAA')
        time.sleep(2)
        self.am.clickSendButton()
        time.sleep(2)
        # self.clickSearchTemplate()
        # time.sleep(2)
        result = self.am.verifyTemplateAdded()
        self.ts.mark(result, "Template Found!!")
        assert result



