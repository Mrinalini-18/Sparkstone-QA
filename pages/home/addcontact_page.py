import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
import time


class AddContactPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    ################
    ### Locators ###
    ################
    _add_icon = "/html/body/div[1]/div[2]/header/nav/div[1]/ul[3]/li[2]/a/i"
    _company_name = "Company"
    _first_name = "companyContactFirstName"
    _last_name = "companyContactLastName"
    _contact_number = "companyContactTel"
    _contact_email = "companyContactEmail"
    _save_contact = "/html/body/div[1]/div[2]/div[1]/div/div/div/div/div/div/form/div[3]/div/div[2]/div/button[2]/span"


    def clickAddIcon(self):
        self.elementClick(self._add_icon, locatorType="xpath")

    def enterCompanyName(self, companyname):
        self.sendKeys(companyname, self._company_name, locatorType="id")

    def enterFirstName(self, firstname):
        self.sendKeys(firstname, self._first_name, locatorType="id")

    def enterLastName(self, lastname):
        self.sendKeys(lastname, self._last_name, locatorType="id")

    def enterContactEmail (self, email):
            self.sendKeys(email, self._contact_email, locatorType="id")

    def enterContactNumber(self, phone):
        self.sendKeys(phone, self._contact_number, locatorType="id")



    def clickSaveContact(self):
        self.elementClick(self._save_contact, locatorType="xpath")

    def Add(self, companyname="", firstname="", lastname="", phone="", email=""):
        self.clickAddIcon()
        time.sleep(5)
        self.enterCompanyName(companyname)
        self.enterFirstName(firstname)
        self.enterLastName(lastname)
        time.sleep(2)
        self.enterContactNumber(phone)
        self.enterContactEmail(email)
        time.sleep(5)
        self.clickSaveContact()


    def verifySubmitSuccessful(self):
        result = self.isElementPresent("Company", locatorType="id")
        return result
