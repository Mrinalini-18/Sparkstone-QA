from pages.home.login_page import LoginPage
from utilities.teststatus import TestStatus
import unittest
import pytest
from utilities.read_data import getCSVData
from ddt import ddt, data, unpack
import time

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)


    @pytest.mark.run(order=1)
    @data(*getCSVData("C:/Users/mrina/PycharmProjects/Sparkstone/logindata.csv"))
    @unpack

    def test_invalidLogin(self, email, password):
            self.lp.login(email, password)
            time.sleep(5)
            result1 = self.lp.verifyInvalidcheck()
            time.sleep(5)
            self.ts.mark(result1, "Title Verified")
            assert result1

    @pytest.mark.run(order=2)
    @data(*getCSVData("C:/Users/mrina/PycharmProjects/Sparkstone/validcred.csv"))
    @unpack
    def test_validLogin(self, email, password):
            self.lp.login(email, password)
            time.sleep(5)
            result1 = self.lp.verifyLoginSuccessful()
            time.sleep(5)
            self.ts.mark(result1, "Title Verified")
            assert result1


