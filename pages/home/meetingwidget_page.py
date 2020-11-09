import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
import time
import pytest



class MeetingWidgetPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    ################
    ### Locators ###
    ################

    _burger_menu = "/html/body/div[1]/div[2]/div[1]/div/div/div/div/div/div/div[2]/div[3]/div[2]/div/div/div/div/i"
    _map_view = "/html/body/div[1]/div[2]/div[3]/div/ul/li[1]/a"
    _my_location = "/html/body/div[1]/div[2]/div[1]/div/div/div/div/div/div[1]/button[4]/span"


    def clickBurgerMenu(self):
        self.elementClick(self._burger_menu, locatorType="xpath")
        time.sleep(5)

    def clickMapView(self):
        self.elementClick(self._map_view, locatorType="xpath")
        time.sleep(5)

    def clickMyLocation(self):
        self.elementClick(self._my_location, locatorType="xpath")
        time.sleep(5)


    def verifyViewMapworks(self):
        result = self.isElementPresent("/html/body/div[1]/div[2]/div[1]/div/div/div/div/div/div[2]/div/div[1]/div[1]/a/div/span", locatorType="xpath")
        return result

