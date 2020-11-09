import pytest
from selenium import webdriver
from pages.home.login_page import LoginPage
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


@pytest.yield_fixture()
def setUp():
    print("Running method level setUp")
    yield
    print("Running method level tearDown")


@pytest.yield_fixture(scope="class")
def oneTimeSetUp(request, browser):
    print("Running one time setUp")
    if browser == 'firefox':
        baseURL = "https://crm-staging-b2b.sparkstone.co.uk"
        driver = webdriver.Firefox(executable_path='C:\\Users\mrina\PycharmProjects\AutomatedFairsale\geckodriver.exe')
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)
        lp = LoginPage(driver)
        lp.login("test", "test")
        print("Running tests on FF")
    else:
        baseURL = "https://crm-staging-b2b.sparkstone.co.uk"
        driver = webdriver.Chrome(executable_path='C:\\Users\mrina\PycharmProjects\AutomatedFairsale\\chromedriver.exe')
        driver.get(baseURL)

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
    print("Running one time tearDown")

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")
