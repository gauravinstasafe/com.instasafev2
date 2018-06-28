
import pytest
from base.webdriverfactory import WebDriverFactory
from pages.loginPage import LoginPage



#URL = "http://automationtesting.instasafe.in"
#USERNAME = "gaurav"
#PASSWORD ="gaurav@123"

URL = "http://safehats.instasafe.in"
USERNAME = "richard"
PASSWORD ="Richard@999"

@pytest.yield_fixture(scope="class")
#@pytest.fixture()
def setUp(request,browser):
    print("Running setUp")
    print("Running method level setUp")
    yield 
    print("Running method level tearDown")

@pytest.yield_fixture(scope="class")
#@pytest.fixture(scope="class")
def oneTimeSetUp(request, browser):
    global URL,USERNAME,PASSWORD
    print("Running one time setUp")
    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance()
    driver.set_page_load_timeout(30)
    driver.get(URL)
    #time.sleep(20)  
    driver.implicitly_wait(30000)
    lp = LoginPage(driver)
    lp.login(USERNAME, PASSWORD)

    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    driver.quit()
    print("Running one time tearDown")

@pytest.yield_fixture(scope="session")
def universalSetUp(browser):
    print("Running universalSetUp")
    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance()
    driver.set_page_load_timeout(30)
    driver.get(URL)
    lp = LoginPage(driver)
    lp.login(USERNAME,PASSWORD)
    yield driver
    driver.quit()
    print("Running universalSetUp")

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")