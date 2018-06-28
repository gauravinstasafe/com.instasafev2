import logging
import time

from base.basepage import BasePage
from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl


class LoginPage(BasePage,SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
       

    # Locators
    # _login_link = ".//input[@class='form-control ng-pristine ng-valid ng-empty ng-touched']"
    _username_Field = ".//input[@placeholder='Username']"
    _password_field = ".//input[@placeholder='Password']"
    _login_button = ".//button[@type='submit']"
    
    result_list = []

    def clickUserName(self):
        self.elementClick(self._username_Field, locatorType="xpath")

    def enterUsername(self, username):
        self.sendKeys(username, self._username_Field, locatorType="xpath")
        
    def clickPassWord(self):
        self.elementClick(self._password_field, locatorType="xpath")

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field, locatorType="xpath")

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="xpath")

    def login(self, username="", password=""):
        self.clearFields()
        self.clickUserName()
        self.log.info("click on username field")
        self.enterUsername(username)
        self.log.info("username enter successfully")
        self.clickPassWord()
        self.log.info("click on Password field")
        self.enterPassword(password)
        self.log.info("password enter successfully")
        self.clickLoginButton()
        self.log.info("click on login button successfully")
        
        
        
    def multiple_login(self, condition="", username="", password=""):
        self.login(username,password)
        result1=True
        if condition=='valid':
            self.log.info("test 2")
            result1 = self.verifyLoginFailed()
            print('valid')
        elif condition == 'invalid' :
            self.log.info("test 3")
            res = self.verifyLoginFailed()
            self.log.info("test 3.1")
            result1 = not(res)
            self.log.info("test 3.1")
            print('invalid')
        else :
            print("blank entry in CSV file")  
            self.log.info("test 4")
        self.result_list.append(result1)
        self.log.info(self.result_list[0])
        self.driver.refresh()
        
    def verifyLogin(self):
        self.waitForElement("//*[contains(text(), 'Dashboard')]",
                                       locatorType="xpath")
        result = self.isElementPresent(locator="//*[contains(text(), 'Dashboard')]",
                                       locatorType="xpath")
        return result
        

    def verifyLoginSuccessful(self):
        self.waitForElement("//*[contains(text(), 'Dashboard')]",
                                       locatorType="xpath")
        result = self.isElementPresent(locator="//*[contains(text(), 'Dashboard')]",
                                       locatorType="xpath")
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent(locator="//*[contains(text(), 'Dashboard')]",
                                       locatorType="xpath")
        return result

    def verifyLoginTitle(self):
        return self.verifyPageTitle("Dashboard - Mumbai | MyInstaSafe")

    def logout(self):
        
        #self.nav.navigateToUserSettings()
        time.sleep(3)
        logoutDropDownLinkElement = self.waitForElement(locator=".//a[@class='dropdown-toggle']",
                          locatorType="xpath", pollFrequency=2)
        self.elementClick(element=logoutDropDownLinkElement)
        time.sleep(1)
        logoutLinkElement = self.waitForElement(locator=".//*[@class='list-inline list-unstyled navitem nav navbar-nav']//*[contains(text(),'Sign out')]",
                          locatorType="xpath", pollFrequency=2)

        self.elementClick(element=logoutLinkElement)

    def clearFields(self):
        self.waitForElement(locator=self._username_Field,locatorType="xpath", pollFrequency=2)
        usernameField = self.getElement(locator=self._username_Field,locatorType="xpath")
        usernameField.clear()
        self.log.info("Username field successfully clear")
        passwordField = self.getElement(locator=self._password_field,locatorType="xpath")
        self.log.info("Password field successfully clear")
        passwordField.clear()
