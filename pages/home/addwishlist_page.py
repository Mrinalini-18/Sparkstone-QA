import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
import time
import pytest



class AddWishlistPage(BasePage):
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
    _plus_menu = "/html/body/div[1]/div[2]/header/nav/div[1]/ul[1]/li[6]/div/a/i"
    _add_wishlist = "/html/body/div[1]/div[2]/div[3]/div/ul/li[7]/a"
    _wishlist_name = "wishlist-modal-wishlistname"
    _full_screen = "/html/body/div[1]/div[2]/div[4]/div[1]/span/i[1]"
    _save_button = "/html/body/div[1]/div[2]/div[4]/div[2]/div/div[2]/button[1]"

    def clickMycontactLink(self):
        self.elementClick(self._mycontact_link, locatorType="xpath")
        time.sleep(5)

    def clickSelectRow(self):
        self.elementClick(self._select_row, locatorType="xpath")
        time.sleep(5)
    def clickRowMenu(self):
        self.elementClick(self._row_menu, locatorType="xpath")

    def clickPlusMenu(self):
        self.elementClick(self._plus_menu, locatorType="xpath")

    def clickAddWishlist(self):
        self.elementClick(self._add_wishlist, locatorType="xpath")

    def enterWishlistName(self, wishlist):
        self.sendKeys(wishlist, self._wishlist_name, locatorType="id")

    def clickFullScreen(self):
        self.elementClick(self._full_screen, locatorType="xpath")
        time.sleep(10)

    def clickSaveButton(self):
        self.elementClick(self._save_button, locatorType="xpath")
        time.sleep(5)

    def verifyAddWishlistSuccessful(self):
        result = self.isElementPresent(
            "/html/body/div[1]/div[2]/div[1]/div/div/div/div/div/div/div/div/div/form/div[1]", locatorType="xpath")
        return result

