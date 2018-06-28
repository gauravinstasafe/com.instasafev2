'''
Created on 15-Jun-2018

@author: Gaurav
'''
import logging

from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl


class Old_reset_new_password(SeleniumDriver):
    
    log = cl.customLogger(logging.DEBUG)
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _old_Password_Field = ".//input[@placeholder='Old Password']"
    _new_Password_Field = ".//input[@placeholder='new Password']"
    _signIn_Button = ".//button[contains(text(),'Sign In')]"
    
    def click_On_Old_Password_Field(self):
        self.elementClick(self._old_Password_Field, locatorType="xpath")

    def enter_Old_Password(self, username):
        self.sendKeys(username, self._old_Password_Field, locatorType="xpath")
        
    def click_On_New_Password_Field(self):
        self.elementClick(self._new_Password_Field, locatorType="xpath")

    def enter_New_Password(self, password):
        self.sendKeys(password, self._new_Password_Field, locatorType="xpath")

    def click_SignIn_Button(self):
        self.elementClick(self._signIn_Button, locatorType="xpath")

    def change_password(self, username="", password=""):
        self.clearFields()
        self.click_On_Old_Password_Field()
        self.enter_Old_Password(username)
        self.click_On_New_Password_Field()
        self.enter_New_Password(password)
        self.click_SignIn_Button()

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

    def clearFields(self):
        oldPasswordField = self.getElement(locator=self._old_Password_Field,locatorType="xpath")
        oldPasswordField.clear()
        newPasswordField = self.getElement(locator=self._old_Password_Field,locatorType="xpath")
        newPasswordField.clear()

