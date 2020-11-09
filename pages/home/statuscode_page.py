import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
import time


class StatusCodePage(BasePage):
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
    _task_link = "/html/body/section/aside/ul/li[3]/span/span"
    _task_code = "/html/body/section/aside/ul/li[3]/ul/li[2]/a"
    _create_code = "/html/body/section/div/section/section/ul/li[1]/button"
    _status_code = "TCC_CODE"
    _code_description = "TCC_DESCRIPTION"
    _followup_task = "/html/body/section/div/section/div[1]/div/div/section[2]/div/div/form/div/div/div/div[4]/div[1]/div[2]/span/span/span[2]"
    _save_button = "/html/body/section/div/section/div[1]/div/div/section[2]/div/div/form/div/div/div/div[6]/section/div/button"

    def clickStarIcon(self):
        self.elementClick(self._star_icon, locatorType="xpath")
        time.sleep(4)

    def clickAdminSec(self):
        self.elementClick(self._admin_sec, locatorType="xpath")
        time.sleep(2)

    def clickMenuToggle(self):
        self.elementClick(self._menu_toggle, locatorType="xpath")
        time.sleep(2)

    def clickTaskLink(self):
        
        self.elementClick(self._task_link, locatorType="xpath")
        time.sleep(2)
    def clickTaskCode(self):
        self.elementClick(self._task_code, locatorType= "xpath")

    def enterCreateCode(self,ATSC):
        self.sendKeys(ATSC, self._create_code, locatorType="xpath")
