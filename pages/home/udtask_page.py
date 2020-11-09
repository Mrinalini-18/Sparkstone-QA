import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
import time


class AddUdtaskPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    ################
    ### Locators ###
    ################
    _star_icon = "/html/body/div[1]/div[2]/header/nav/div[1]/ul[1]/li[1]/a"
    _admin_sec = "/html/body/div[1]/div[2]/div[4]/ul/li[1]/div/div/a[2]/i"
    _menu_toggle = "/html/body/section/div/header/nav/ul[1]/li[1]/a/i"
    _task_link = "/html/body/section/aside/ul/li[3]/span"
    _task_types = "/html/body/section/aside/ul/li[3]/ul/li[1]/a"
    _create_tasktype = "/html/body/section/div/section/section/ul/li[1]/button"
    _task_name = "TKA_NAME"
    _short_name = "TKA_SHORT"
    _choose_group = "/html/body/section/div/section/div[1]/div/div/section[2]/div/div/div/div/div/div[1]/div/form/div/div/div[1]/div[3]/div[2]/span/span[1]/span[2]/span"
    _user_defined = "/html/body/div[2]/div/div[3]/ul/li[4]/span"
    _add_description = "TKA_DESCRIPTION"
    _search_group = "/html/body/section/div/section/div[1]/div/div/section[2]/div/div/div/div/div/div[1]/div/form/div/div/div[5]/div[1]/div[2]/span/span/span[2]/span"
    _choose_meeting = "/html/body/div[3]/div/div[3]/ul/li[2]"
    _choose_type = "/html/body/section/div/section/div[1]/div/div/section[2]/div/div/div/div/div/div[1]/div/form/div/div/div[5]/div[2]/div[2]/span/span[1]/span[1]"
    _default_type = "/html/body/div[4]/div/div[3]/ul/li[1]"
    _save_button = "submitTaskEdit"
    _confirm_add = "/html/body/section/div/section/div[1]/div/div/section[1]/div/div/div[2]/div/div/ul/li[1]/ul/li[22]/div/span"

    def clickStarIcon(self):
        self.elementClick(self._star_icon, locatorType="xpath")
        time.sleep(4)

    def clickAdminSec(self):
        self.elementClick(self._admin_sec, locatorType="xpath")
        time.sleep(5)

    def clickMenuToggle(self):
        self.elementClick(self._menu_toggle, locatorType="xpath")
        time.sleep(5)
    def clickTaskLink(self):
        self.elementClick(self._task_link, locatorType="xpath")
        time.sleep(5)
    def clickTaskTypes(self):
        self.elementClick(self._task_types, locatorType="xpath")
        time.sleep(2)
    def clickCreateTasktype(self):
        self.elementClick(self._create_tasktype, locatorType="xpath")
        time.sleep(2)

    def enterTaskName(self,QA):
        self.sendKeys(QA, self._task_name, locatorType="id")
        time.sleep(2)
    def enterShortName(self,QA):
        self.sendKeys(QA, self._short_name, locatorType="id")
        time.sleep(2)

    def clickChooseGroup(self):
        self.elementClick(self._choose_group, locatorType="xpath")
        time.sleep(2)

    def clickUserDefined(self):
        self.elementClick(self._user_defined, locatorType="xpath")
        time.sleep(2)

    def enterAddDescription(self, Test):
        self.sendKeys(Test, self._user_defined, locatorType="id")
        time.sleep(2)

    def clickSearchGroup(self):
        self.elementClick(self._search_group, locatorType="xpath")
        time.sleep(2)

    def clickChooseMeeting(self):
        self.elementClick(self._choose_meeting, locatorType="xpath")
        time.sleep(2)

    def clickChooseType(self):
        self.elementClick(self._choose_type, locatorType="xpath")
        time.sleep(2)

    def clickDefaultType(self):
        self.elementClick(self._default_type, locatorType="xpath")
        time.sleep(2)

    def clickSaveButton(self):
        self.elementClick(self._save_button, locatorType="id")
        time.sleep(2)

    def verifyUdTaskAdded (self):
        result = self.isElementPresent(self._confirm_add, locatorType="xpath")
        return result





