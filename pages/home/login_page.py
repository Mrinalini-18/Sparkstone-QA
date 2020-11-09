from base.basepage import BasePage
import utilities.custom_logger as cl
import logging

class LoginPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _user_name = "login-name"
    _password_field = "login-pass"
    _login_button = "login-submit"

    def enterUsername(self, username):
        self.sendKeys(username, self._user_name)

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="id")


    def login(self, username="", password=""):
        self.clearLoginForm()
        self.enterUsername(username)
        self.enterPassword(password)
        self.clickLoginButton()


    def clearLoginForm(self):
        self.driver.find_element_by_id(self._user_name).clear()
        self.driver.find_element_by_id(self._password_field).clear()

    def verifyLoginSuccessful(self):
        result = self.isElementPresent("/html/body/div[1]/div[2]/header/nav/div[1]/ul[2]/li/input", locatorType="xpath")

        return result
    def verifyInvalidcheck(self):
        result = self.isElementPresent("/html/body/div[1]/section/div/div[2]/form/div[2]/div", locatorType="xpath")
        return result
    