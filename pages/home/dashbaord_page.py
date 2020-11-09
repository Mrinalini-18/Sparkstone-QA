import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
import time


class DashboardPage(BasePage):
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
    _widget_dashboard = "/html/body/section/aside/ul/li[15]/span"
    _dashboard_link = "/html/body/section/aside/ul/li[15]/ul/li[2]/a"
    _create_dashboard = "/html/body/section/div/section/section[1]/ul/li/button"
    _dashboard_name = "Name"
    _save_1 = "/html/body/section/div/section/section[2]/div/div/section[2]/div/div/div/form/div[2]/section/div/button"
    _dashboard_builder = "/html/body/section/div/section/section[2]/div/div/section[2]/div/div/div/form/div[1]/div/ul/li[2]/span[2]"
    _widget_group = "/html/body/section/div/section/section[2]/div/div/section[2]/div/div/div/form/div[1]/div/div[2]/div/div/div/div[1]/div[1]/div[2]/span/span/span[1]"
    _input_contact = "/html/body/div[2]/div/span/input"
    _contact_group = "/html/body/div[2]/div/div[3]/ul/li[1]"
    _choose_widget = "/html/body/section/div/section/section[2]/div/div/section[2]/div/div/div/form/div[1]/div/div[2]/div/div/div/div[1]/div[2]/div[2]/span"
    _add_row = "/html/body/section/div/section/section[2]/div/div/section[2]/div/div/div/form/div[1]/div/div[2]/div/div/div/div[2]/div/table/tbody/tr[2]/td[2]/input"
    _add_column = "/html/body/section/div/section/section[2]/div/div/section[2]/div/div/div/form/div[1]/div/div[2]/div/div/div/div[2]/div/table/tbody/tr[2]/td[3]/input"
    _new_months = "/html/body/div[3]/div/div[3]/ul/li"
    _add_widget = "addUserButton"
    _save_2 = "/html/body/section/div/section/section[2]/div/div/section[2]/div/div/div/form/div[2]/section/div/button"
    _search_quicklinks = "/html/body/section/div/section/section[2]/div/div/section[2]/div/div/div/form/div[1]/div/ul/li[3]/span[2"
    _smart_search = "SmartSearch"
    _contact_search = "ContactsSearch"
    _choose_position = "/html/body/section/div/section/section[2]/div/div/section[2]/div/div/div/form/div[1]/div/div[3]/div/div/div/div[2]/div/div[2]/span/span/span[1]"
    _top_left = "/html/body/div[4]/div/div[3]/ul/li[1]"
    _add_contact = "AddContact"
    _last_contact = "LastContact"
    _my_dashboard = "1"
    _choose_position2 = "/html/body/section/div/section/section[2]/div/div/section[2]/div/div/div/form/div[1]/div/div[3]/div/div/div/div[4]/div/div[2]/span/span/span[1]"
    _top_right = "/html/body/div[5]/div/div[3]/ul/li[2]"
    _save_3 = "/html/body/section/div/section/section[2]/div/div/section[2]/div/div/div/form/div[2]/section/div/button"
    _verify_added = "/html/body/div[10]/div/div"

    def clickStarIcon (self):
        self.elementClick(self._star_icon, locatorType="xpath")
        time.sleep(4)

    def clickAdminSec (self):
        self.elementClick(self._admin_sec, locatorType="xpath")
        time.sleep(2)

    def clickMenuToggle (self):
        self.elementClick(self._menu_toggle, locatorType="xpath")
        time.sleep(2)

    def clickWidgetDashboard (self):
        self.elementClick(self._widget_dashboard, locatorType="xpath")
        time.sleep(4)

    def clickDashboardLink (self):
        self.elementClick(self._dashboard_link, locatorType="xpath")
        time.sleep(2)

    def clickCreateDashboard (self):
        self.elementClick(self._create_dashboard, locatorType="xpath")
        time.sleep(2)

    def enterDashboardName(self, DashboardQA1):
        self.sendKeys(DashboardQA1, self._dashboard_name, locatorType="id")
        time.sleep(2)
    # def clickSave1(self):
    #     self.elementClick(self._save_1, locatorType="xpath")
    #     time.sleep(4)

    def clickDashboardBuilder (self):
        self.elementClick(self._dashboard_builder, locatorType="xpath")
        time.sleep(4)

    def clickWidgetGroup (self):
        self.elementClick(self._widget_group, locatorType="xpath")
        time.sleep(5)

    def clickInputContact(self):
        self.elementClick(self._input_contact, locatorType="xpath")
        self.sendKeys("Contact")
        time.sleep(3)

    def clickContactGroup (self):
        self.elementClick(self._contact_group, locatorType="xpath")
        time.sleep(5)

    def clickChooseWidget (self):
        self.elementClick(self._choose_widget, locatorType="xpath")
        time.sleep(4)

    def clickNewMonths (self):
        self.elementClick(self._new_months, locatorType="xpath")
        time.sleep(2)

    def clickAddRow (self):
        self.elementClick(self._add_row, locatorType="xpath")
        self.sendKeys(2, self._add_row, locatorType="xpath")
        time.sleep(2)

    def clickAddColumn (self):
        self.elementClick(self._add_column, locatorType="xpath")
        time.sleep(2)

    def clickAddWidget (self):
        self.elementClick(self._add_widget, locatorType="id")
        time.sleep(2)

    # def clickSave2 (self):
    #     self.elementClick(self._save_2, locatorType="xpath")
    #     time.sleep(4)

    def clickSearchQuicklinks(self):
        self.elementClick(self._search_quicklinks, locatorType="xpath")
        time.sleep(2)

    def clickSmartSearch (self):
        self.elementClick(self._smart_search, locatorType="id")
        time.sleep(2)

    def clickContactSearch (self):
        self.elementClick(self._contact_search, locatorType="id")
        time.sleep(4)

    def clickChoosePosition (self):
        self.elementClick(self._choose_position, locatorType="xpath")
        time.sleep(2)

    def clickTopLeft (self):
        self.elementClick(self._top_left, locatorType="xpath")
        time.sleep(2)

    def clickAddContact (self):
        self.elementClick(self._add_contact, locatorType="id")
        time.sleep(4)

    def clickLastContact (self):
        self.elementClick(self._last_contact, locatorType="id")
        time.sleep(2)

    def clickMyDashboard (self):
        self.elementClick(self._my_dashboard, locatorType="id")
        time.sleep(2)

    def clickChoosePosition2 (self):
        self.elementClick(self._choose_position, locatorType="xpath")
        time.sleep(4)

    def clickTopRight (self):
        self.elementClick(self._top_right, locatorType="xpath")
        time.sleep(2)

    # def clickSave3 (self):
    #     self.elementClick(self._save_3, locatorType="xpath")
    #     time.sleep(2)

    def verifyDashboardAdded (self):
        result = self.isElementPresent(self._verify_added, locatorType="xpath")
        return result



