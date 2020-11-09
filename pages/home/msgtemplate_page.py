import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
import time


class AddMessagePage(BasePage):
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
    _open_messaging = "/html/body/section/aside/ul/li[6]/span/span"
    _message_template = "/html/body/section/aside/ul/li[6]/ul/li[1]/a"
    _create_template = "/html/body/section/div/section/section[1]/ul/li/button"
    _template_name = "EmailTemplateName"
    _template_subject = "EmailTemplateSubject"
    _choose_object = "/html/body/section/div/section/section[2]/div/div/section[2]/div/div/div/form/div[1]/div/div[1]/div/div/div/div[4]/div[1]/div/span/span/span[2]/span"
    _choose_opp = "6fc3d262-6c15-4197-ad8d-dd1da332bbf1"
    _switch_code = "/html/body/section/div/section/section[2]/div/div/section[2]/div/div/div/form/div[1]/div/div[1]/div/div/div/div[5]/div/div/div/div/ul/li[1]/span[2]"
    _editor_add = "/html/body/section/div/section/section[2]/div/div/section[2]/div/div/div/form/div[1]/div/div[1]/div/div/div/div[5]/div/div/div/div/div[1]/div/div[2]/div"
    _iframe_path = " /html/body/section/div/section/section[2]/div/div/section[2]/div/div/div/form/div[1]/div/div[1]/div/div/div/div[5]/div/div/div/div/div[2]/div/table/tbody/tr[2]/td/iframe"
    _save_button = "/html/body/section/div/section/section[2]/div/div/section[2]/div/div/div/form/div[2]/section/div/button/i"
    _switch_setting = "/html/body/section/div/section/section[2]/div/div/section[2]/div/div/div/form/div[1]/div/ul/li[2]/span[2]"
    _add_description = "EmailTemplateDescription"
    _select_save = "/html/body/section/div/section/section[2]/div/div/section[2]/div/div/div/form/div[2]/section/div/button/i"
    _dashboard_sec = "sidenav-overlay"
    _my_contact = "/html/body/div[1]/div[2]/div[1]/div/div/div/div/div/div/div[1]/div[2]/div/div/ul/li[4]/a/span"
    _select_row = "/html/body/div[1]/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[2]/div[2]/table/tbody/tr[3]/td[88]/a/span"
    _add_task = "/html/body/div[1]/div[2]/div[3]/div/ul/li[8]/a"
    _maximize_modal = "/html/body/div[1]/div[2]/div[4]/div[1]/span/i[1]"
    _write_template = "/html/body/div[1]/div[2]/div[4]/div[2]/div/div/form/div[2]/div/div/div[13]/div/div/div[1]"
    _add_subject = "Subject"
    _send_button = "/html/body/div[1]/div[2]/div[1]/div/div/div/div/div/div/div/div/div[2]/div/di]v/div[3]/div/div[3]/button/span"


    def clickStarIcon(self):
        self.elementClick(self._star_icon, locatorType="xpath")
        time.sleep(4)

    def clickAdminSec(self):
        self.elementClick(self._admin_sec, locatorType="xpath")
        time.sleep(2)

    def clickMenuToggle(self):
        self.elementClick(self._menu_toggle, locatorType="xpath")
        time.sleep(2)

    def clickOpenMessaging(self):
        self.elementClick(self._open_messaging, locatorType="xpath")
        time.sleep(2)

    def clickMessageTemplate(self):
        self.elementClick(self._message_template, locatorType="xpath")
        time.sleep(2)

    def clickCreateTemplate(self):
        self.elementClick(self._create_template, locatorType="xpath")
        time.sleep(2)

    def enterTemplateName(self, Template001):
        self.sendKeys(Template001, self._template_name, locatorType="id")
        time.sleep(2)

    def enterTemplateSubject(self, AutomatedEmail):
        self.sendKeys(AutomatedEmail, self._template_subject, locatorType="id")
        time.sleep(2)

    def clickChooseObject(self):
        self.elementClick(self._choose_object, locatorType="xpath")
        time.sleep(2)

    def clickChooseOpp(self):
        self.elementClick(self._choose_opp, locatorType="xpath")
        time.sleep(2)
    def clickSwitchCode(self):
        self.elementClick(self._switch_code, locatorType="xpath")

    def enterEditorAdd(self, data):
        self.sendKeys(data, self._editor_add, locatorType="xpath")
        time.sleep(2)

    def clickSaveButton(self):
        self.elementClick(self._save_button, locatorType="xpath")
        time.sleep(2)

    def clickSwitchSetting(self):
        self.elementClick(self._switch_setting, locatorType="xpath")

    def enterAddDescription(self, Description001):
        self.sendKeys(Description001, self._add_description, locatorType="xpath")
        time.sleep(2)

    def clickSelectSave(self):
        self.elementClick(self._select_save, locatorType="xpath")
        time.sleep(2)

    def clickDashboardsec(self):
        self.elementClick(self._dashboard_sec, locatorType="id")
        time.sleep(2)

    def clickMyContact(self):
        self.elementClick(self._my_contact, locatorType="xpath")
        time.sleep(2)
    def clickSelectRow(self):
        self.elementClick(self._select_row, locatorType="xpath")
        time.sleep(2)
    # def clickSendEmail(self):
    #     self.elementClick(self._send_email, locatorType="xpath")
    #     time.sleep(5)
    # def enterWriteTemplate(self):
    #     self.sendKeys(AAA, self._write_template, locatorType="xpath")
    #
    # def clickSendButton(self):
    #     self.elementClick(self._send_button, locatorType="xpath")
    #     time.sleep(2)

    def clickAddTask(self):
        self.elementClick(self._add_task, locatorType="xpath")
        time.sleep(2)

    def clickMaximizeModal(self):
        self.elementClick(self._maximize_modal, locatorType="xpath")
        time.sleep(5)

    def clickWriteTemplate(self):
        self.elementClick(self._write_template, locatorType="xpath")
        time.sleep(2)

    def enterTemplateAAA(self,AAA):
        self.sendKeys(AAA, self._write_template, locatorType="xpath")
        time.sleep(2)

    def clickSendButton(self):
        self.elementClick(self._send_button, locatorType="xpath")

    def verifyTemplateAdded (self):
        result = self.isElementPresent(self._message_body, locatorType="xpath")
        return result






