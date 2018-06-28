'''
Created on 11-Sep-2017

@author: user
'''
import os
from symbol import parameters

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import utilities.custom_logger as cl
import logging 


class WebDriverFactory():
     
    log = cl.customLogger(logging.DEBUG)
        
    def __init__(self, browser):
        self.browser = browser
    
#logging.error(msg)
    def getWebDriverInstance(self,browser = 'firefox'):    
        if browser == 'firefox' :
            driver = self.get_firefox()
        elif self.browser == 'chrome' :        
            driver = self.get_chrome()
        elif browser == 'EI' :
            driver = self.get_ei()
        elif self.browser == 'opera' :
            driver = self.get_opera()
        else:
            driver = self.get_firefox()
        self.log.info(browser+ "browser  open")    
        driver.delete_all_cookies()
        self.log.info("All cookies clear")
        driver.set_page_load_timeout(3)
        self.log.info("wait for 10 seconds")
        driver.implicitly_wait(10)
        self.log.info("maximize browser window")
        #driver.maximize_window()
        return driver
    
    def get_firefox(self):
        # Locate firFox from the default directory otherwise use FIREFOX_BIN #
        try:
            driver = webdriver.Firefox("D:\\geckodriver")
            self.log.info("")
        except Exception:
            my_local_firefox_bin = os.environ.get('FIREFOX_BIN')
            firefox_binary = FirefoxBinary(my_local_firefox_bin)
            driver = webdriver.Firefox(firefox_binary=firefox_binary)
        return driver
    
    def get_chrome(self):
        # Locate chrome from the default directory otherwise use FIREFOX_BIN #
        try:
            driver = webdriver.Chrome("D:\\software\\chromedriver.exe")
            self.log.info("browser ---- Chrome")
        except Exception:
            my_local_firefox_bin = os.environ.get('FIREFOX_BIN')
            firefox_binary = FirefoxBinary(my_local_firefox_bin)
            driver = webdriver.Firefox(firefox_binary=firefox_binary)
        return driver
    
    def get_ei(self):
        # Locate EI from the default directory otherwise use FIREFOX_BIN #
        try:
            capabilities = DesiredCapabilities.INTERNETEXPLORER
            capabilities.pop("platform", None)
            capabilities.pop("version", None)
            iepath="D:\\software\\IEDriverServer.exe"
            driver = webdriver.Ie(iepath,capabilities = capabilities )        
        except Exception:
            my_local_firefox_bin = os.environ.get('FIREFOX_BIN')
            firefox_binary = FirefoxBinary(my_local_firefox_bin)
            driver = webdriver.Firefox(firefox_binary=firefox_binary)
        return driver
    def get_opera(self):
        # Locate opera from the default directory otherwise use FIREFOX_BIN #
        try:
            capabilities = DesiredCapabilities.OPERA
            capabilities.pop("platform", None)
            capabilities.pop("version", None)
            iepath="D:\\software\\operadriver_win32\\operadriver.exe"
            driver = webdriver.Ie(iepath,capabilities = capabilities )        
            driver = webdriver.Firefox()
        except Exception:
            my_local_firefox_bin = os.environ.get('FIREFOX_BIN')
            firefox_binary = FirefoxBinary(my_local_firefox_bin)
            driver = webdriver.Firefox(firefox_binary=firefox_binary)
        return driver


def close_drivers(driver):
    driver.close()
    
