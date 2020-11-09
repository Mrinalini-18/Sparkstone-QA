import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
import time


class EditContactPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    ################
    ### Locators ###
    ################
    _mycontact_link = "/html/body/div[1]/div[2]/div[1]/div/div/div/div/div/div/div[1]/div[2]/div/div/ul/li[4]/a/span"
    _contact_row = "/html/body/div[1]/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[2]/div[2]/table/tbody/tr[1]/td[4]"
    _edit_address = "/html/body/div[1]/div[2]/div[1]/div/div/div/div/div/div/div/div/div/form/div[2]/div/div/div[2]/div[2]/div/i"
    _select_contact = "/html/body/div[1]/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[2]/div[2]/div[1]/div[2]/div/div[2]/div/div/div/div[1]/div/div/div[3]"
    _select_company = "/html/body/div[1]/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[2]/div[2]/div[1]/div[2]/div/div[2]/div/div/div/div[1]/div/div/div[2]"
    _address_line1 = "CMA_ADDR1"
    _add_town = "CMA_ADDR4"
    _add_postcode = "CMA_POSTCODE"
    _add_country = "CMA_COUNTRY"
    _click_update = "/html/body/div[1]/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[2]/div[2]/div[2]/button[4]"

    def clickMycontactLink(self):
        self.elementClick(self._mycontact_link, locatorType="xpath")
        time.sleep(5)

    def clickContactRow(self):
        self.elementClick(self._contact_row, locatorType="xpath")
        time.sleep(5)

    def clickEditAddress(self):
        self.elementClick(self._edit_address, locatorType="xpath")
        time.sleep(5)

    def clickSelectContact(self):
        self.elementClick(self._select_contact, locatorType="xpath")
        time.sleep(5)
    def enterSelectCompany(self):
        self.sendKeys(company, self._select_company, locatorType="xpath")

    def enterAddressLine1(self, address):
        self.sendKeys(address, self._address_line1, locatorType="id")

    def enterAddTown(self, town):
        self.sendKeys(town, self._add_town, locatorType="id")

    def enterAddPostcode(self, postcode):
        self.sendKeys(postcode, self._add_postcode, locatorType="id")

    def enterAddCountry(self, country):
        self.sendKeys(country, self._add_country, locatorType="id")
        time.sleep(5)

    def clickClickUpdate(self):
        self.elementClick(self._click_update, locatorType="xpath")

    def Add(self, company="", address1="", town="", postcode="", country=""):
        self.clickMycontactLink()
        self.clickContactRow()
        self.clickEditAddress()
        time.sleep(5)
        self.clickSelectContact()
        self.enterSelectCompany(company)
        self.enterAddressLine1(address1)
        self.enterAddTown(town)
        time.sleep(2)
        self.enterAddPostcode(postcode)
        self.enterAddCountry(country)
        time.sleep(5)
        self.clickClickUpdate()
        time.sleep(2)

    def verifyUpdateSuccessful (self):
        result = self.isElementPresent("/html/body/div[1]/div[2]/div[1]/div/div/div/div/div/div/div/div/div/form/div[1]/div[2]/li[1]/a", locatorType="xpath")
        time.sleep(2)
        return result






