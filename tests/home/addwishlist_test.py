from pages.home.login_page import LoginPage
from pages.home.addwishlist_page import AddWishlistPage
from utilities.teststatus import TestStatus
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import pytest
import time
time.sleep(5)
@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class AddWishlist(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp,):
        time.sleep(5)
        self.ts = TestStatus(self.driver)
        self.lp = LoginPage(self.driver)
        self.aw = AddWishlistPage(self.driver)
        time.sleep(5)

    @pytest.mark.run(order=1)
    def test_validLogin(self):
        self.lp.login("test", "test")
        result1 = self.lp.verifyLoginSuccessful()
        self.ts.mark(result1, "Logged in")
        self.driver.maximize_window()

    @pytest.mark.run(order=2)
    def test_verifyAddWishlistSuccessful(self):
        self.aw.clickMycontactLink()
        time.sleep(2)
        self.aw.clickSelectRow()
        time.sleep(2)
        self.aw.clickRowMenu()
        time.sleep(2)
        self.aw.clickPlusMenu()
        time.sleep(2)
        self.aw.clickAddWishlist()
        time.sleep(2)
        self.aw.enterWishlistName(wishlist="test2")
        time.sleep(2)
        self.aw.clickFullScreen()
        time.sleep(5)
        self.aw.clickSaveButton()
        result = self.aw.verifyAddWishlistSuccessful()
        time.sleep(2)
        self.ts.mark(result, "Wishlist Added")
        assert result



