import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
import time


class AddTaskPage(BasePage):
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
    _add_task = "/html/body/div[1]/div[2]/div[3]/div/ul/li[8]/a"
    _click_next = "/html/body/div[1]/div[2]/div[1]/div/div/div/div/div/div/div/div/div/form/div[3]/div/div[2]/div/button[2]/span"
    _click_inside = "/html/body/div[11]/div[1]/div[2]/div/div[1]/h4"
    _full_modal = "/html/body/div[11]/div[1]/div[1]/span/i[1]"
    _current_status = "/html/body/div[11]/div[1]/div[2]/div/div[2]/button[1]"
    _full_screen = "/html/body/div[1]/div[2]/div[4]/div[1]/span/i[1]"
    _send_continue = "/html/body/div[1]/div[2]/div[1]/div/div/div/div/div/div/div/div/div[2]/div/div/div[3]/div/div[3]/button/i"
    _save_button = "/html/body/div[1]/div[2]/div[1]/div/div/div/div/div/div/div/div/div/form/div[3]/div/div[2]/div/button[2]/i"
    _follow_up = "/html/body/div[1]/div[2]/div[1]/div/div/div/div/div/div/div/div/div/form/div[3]/div/div[2]/div/button[2]/i"
    _full_confirm = "/html/body/div[6]/div[1]/div[1]/span/i[1]"
    _confirm_current = "/html/body/div[6]/div[1]/div[2]/div/div[2]/button[1]"

    _task_added = "/html/body/div[1]/div[2]/header/nav/div[1]/ul[1]/li[6]/div/a/i"



    def clickMycontactLink(self):
        self.elementClick(self._mycontact_link, locatorType="xpath")
        time.sleep(5)

    def clickSelectRow(self):
        self.elementClick(self._select_row, locatorType="xpath")
        time.sleep(5)
    def clickRowMenu(self):
        self.elementClick(self._row_menu, locatorType="xpath")

    def clcikOpenMenu(self):
        self.elementClick(self._open_menu, locatorType="xpath")

    def clickAddTask(self):
        self.elementClick(self._add_task, locatorType="xpath")
        time.sleep(5)

    def clickClickNext(self):
        self.elementClick(self._click_next, locatorType="xpath")

    def clickFullModal(self):
        self.elementClick(self._full_modal, locatorType="xpath")
        time.sleep(2)

    def clickCurrentStatus(self):
        self.elementClick(self._current_status, locatorType="xpath")
        time.sleep(2)

    def clickSendContinue(self):
        self.elementClick(self._send_continue, locatorType="xpath")
        time.sleep(2)

    def clickSaveButton(self):
        self.elementClick(self._save_button, locatorType="xpath")
        time.sleep(2)

    def clickFollowUp(self):
        self.elementClick(self._follow_up, locatorType="xpath")
        time.sleep(2)

    def clickFullConfirm(self):
        self.elementClick(self._full_confirm, locatorType="xpath")
        time.sleep(2)

    def clickConfirmCurrent(self):
        self.elementClick(self._confirm_current, locatorType="xpath")
        time.sleep(2)

    def verifyAddTaskSuccessful (self):
        result2 = self.isElementPresent("/html/body/div[1]/div[2]/div[1]/div/div/div/div/div/div/div/div/div/form/div[1]/div[2]/li[1]/a", locatorType="xpath")
        return result2
