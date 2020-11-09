import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
import time


class FormEditPage(BasePage):
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
    _contact_menu = "/html/body/section/aside/ul/li[4]/span/span"
    _form_mgmt = "/html/body/section/aside/ul/li[4]/ul/li[1]/a"
    _business_contact = "html/body/section/div/section/section[2]/div/div/section[1]/div/div/div[2]/div/div/ul/li[7]/div/span"
    _custom_tab = "/html/body/section/div/section/section[2]/div/div/section[2]/div/div/div/div/div/ul/li[2]/span[2]"
    _add_tab = "/html/body/section/div/section/section[2]/div/div/section[2]/div/div/div/div/div/div[2]/div/div/div/div/div/div/div/a"
    _add_title = "UDT_TITLE"
    _make_visible = "Visible"
    _add_position = "UDT_POSITION"
    _create_tab = "/html/body/section/div/section/section[2]/div/div/section[2]/div/div/div/div/div/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[5]/a[1]/span"

    def clickStarIcon(self):
        self.elementClick(self._star_icon, locatorType="xpath")
        time.sleep(4)

    def clickAdminSec(self):
        self.elementClick(self._admin_sec, locatorType="xpath")
        time.sleep(2)

    def clickMenuToggle(self):
        self.elementClick(self._menu_toggle, locatorType="xpath")
        time.sleep(2)

    def clickContactMenu(self):
        self.elementClick(self._contact_menu, locatorType="xpath")
        time.sleep(2)

    def clickFormMgmt(self):
        self.elementClick(self._form_mgmt, locatorType="xpath")
        time.sleep(2)

    def clickBusinessContact(self):
        self.elementClick(self._business_contact, locatorType="xpath")
        time.sleep(2)

    def clickCustomTab(self):
        self.elementClick(self._custom_tab, locatorType="xpath")
        time.sleep(2)

    def clickAddTab(self):
        self.elementClick(self._add_tab, locatorType="xpath")
        time.sleep(2)

    def enterAddTitle(self, Test):
        self.sendKeys(Test, self._add_title, locatorType="id")
        time.sleep(2)

    def clickMakeVisible(self):
        self.elementClick(self._make_visible, locatorType="id")
        time.sleep(2)

    def enterAddPosition(self):
        self.sendKeys(6, self._add_position, locatorType="id")
        time.sleep(2)

    def clickCreateTab (self):
        self.elementClick(self._create_tab, locatorType="xpath")
        time.sleep(2)

    def verifyTabCreated(self):
        result = self.isElementPresent("/html/body/section/div/section/section[2]/div/div/section[2]/div/div/div/div/div/div[2]/div/div/div/div/div/div/div/a", locatorType="xpath")
        return result
