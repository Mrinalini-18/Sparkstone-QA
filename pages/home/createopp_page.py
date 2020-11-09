import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
import time


class CreateOppPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    ################
    ### Locators ###
    ################
    _mycontact_link = "/html/body/div[1]/div[2]/div[1]/div/div/div/div/div/div/div[1]/div[2]/div/div/ul/li[4]/a/span"
    _select_row = "/html/body/div[1]/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[2]/div[2]/table/tbody/tr[1]/td[4]"
    _row_menu = "/html/body/div[1]/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[2]/div[2]/table/tbody/tr[1]/td[87]/a/span"
    _open_menu = "/html/body/div[1]/div[2]/div[1]/div/div/div/div/div/div/div/div/div/form/div[1]/div[1]/i"
    _create_opp = "/html/body/div[1]/div[2]/div[3]/div/ul/li[2]/a"
    _save_opp = "/html/body/div[1]/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/form/div[3]/div/div[2]/div/button[2]/i"

    def clickMycontactLink (self):
        self.elementClick(self._mycontact_link, locatorType="xpath")
        time.sleep(5)

    def clickSelectRow (self):
        self.elementClick(self._select_row, locatorType="xpath")
        time.sleep(5)

    def clickRowMenu (self):
        self.elementClick(self._row_menu, locatorType="xpath")

    def clickOpenMenu (self):
        self.elementClick(self._open_menu, locatorType="xpath")

    def clickCreateOpp(self):
        self.elementClick(self._create_opp, locatorType="xpath")
        time.sleep(5)
    def clickSaveOpp(self):
        self.elementClick(self._save_opp, locatorType="xpath")

    def verifyCreateOppSuccessful (self):
        result = self.isElementPresent("/html/body/div[1]/div[2]/header/nav/div[1]/ul[1]/li[6]/div/a/i", locatorType="xpath")
        return result