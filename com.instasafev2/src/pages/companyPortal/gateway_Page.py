'''
Created on 28-Jun-2018

@author: gaurav
'''
import logging
import time
from base.basepage import BasePage
from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl



class GatewayPages(BasePage,SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        #Locator
    _gateways_menu = ".//span[contains(text(),'Gateways')]"    
    _Page_heading_text = ".//a[contains(text(),'Gateway')]"
    _add_button = ".//button[contains(text(),'Add Gateway')]"
    _bulk_add_button = ".//button[contains(text(),'Bulk')]"
    _delete_button = ".//button[contains(text(),'Delete')]"
    _select_dropdown=".//select[@name='pageselect']"
    _prev_button=".//span[contains(text(),'Prev')]"
    _next_button = ".//span[contains(text(),'Next')]"
    _search_box = ".//input[@placeholder='Type keyword and enter to search']"
    _checkBox_single = ".//a[contains(text(),'gateway')]/parent::*/..//input[@type='checkbox']"
    _checkBox_selectAll = ".//input[@ng-model='selectedAll']"
    _add_window_heading = ".//h2[contains(text(),'Add new gateway details to setup')]"
    _name_field = ".//input[@name='name']"
    _location_field = ".//input[@name='location']"
    _backup_field = ".//input[@name='backup_name']"
    _bandwith_field = ".//input[@name='bandwidth_limit']"
    #div[x] x change with newly added network address text box. value of x started from 1
    _protected_network_field = ".//div[1][@ng-repeat='net in Gateway.gateway.networks']//input[@name='value']"
    _add_more_button = ".//button[contains(text(),'Add more')]"
    _save_button =".//button[@type='submit']"
    _reset_button = ".//span[contains(text(),'Reset')]"
    _add_window_close_button = ".//i[@ng-click='closeThisDialog(0)']"

    _gateway_entry = ".//a[contains(text(),'gateway')]"
    _close_addwindow = ".//a[@class='close_slide ion-android-close']"

    
            
    def clickAddButton(self):
        self.waitForElement(self._add_button, locatorType="Xpath", pollFrequency=1) 
        self.elementClick(self._add_button, locatorType="xpath")
        
    def clickonBulkAddButton(self):    
        self.waitForElement(self._bulk_add_button, locatorType="Xpath",timeout=3, pollFrequency=1) 
        self.elementClick(self._bulk_add_button, locatorType="xpath")
          
    def verifyAddWindow(self,verificationText):
        heading = self.isElementPresent(verificationText, locatorType="Xpath")
        self.log.info("Add window appear status is " + str(heading))
    
    def enterGatewayName(self, gateway):
        self.sendKeys(gateway, self._name_field, locatorType="xpath", element="gateway name")
    
    def enterLocation(self, gateway):
        self.sendKeys(gateway, self._location_field, locatorType="xpath", element="gateway name")
    
    def enterBackupGatewayName(self, gateway):
        self.sendKeys(gateway, self._backup_field, locatorType="xpath", element="gateway name")
    
    def enterBandwithLimit(self, gateway):
        self.sendKeys(gateway, self._bandwith_field, locatorType="xpath", element="gateway name")
     
    def enterProtectedNetwork(self, gateway):
        self.sendKeys(gateway, self._protected_network_field, locatorType="xpath", element="gateway name")
    
    def clickAddMoreButton(self):
        self.elementClick(locator =self._add_more_button, locatorType="Xpath") 

    def clickResetButton(self):
        self.elementClick(locator =self._reset_button, locatorType="Xpath")
                      
    def clickSaveButton(self):
        self.elementClick(locator =self._save_button, locatorType="Xpath")    

    def closeAddWindow(self):
        self.elementClick(locator= self._add_window_close_button, locatorType="Xpath", element="closeAddWindow")
            
    def verify_gateway_entry(self, name):
        gateway_entry = self._gateway_entry.replace("gateway", name)
        self.log.info("new Xpath of gateway :- " + gateway_entry)
        self.waitForElement(locator= gateway_entry, locatorType="Xpath", timeout=20, pollFrequency=1)
        result = self.isElementPresent(locator= gateway_entry, locatorType="Xpath", element= "none")
        if (result == False):
            self.closeAddWindow()
        
        return result
        
    def clearFields(self):
        Field = self.getElement(locator=self._portNumber_field,locatorType="xpath")
        Field.clear()
    
    def deleteAll(self,locator):
        self.elementClick(self._checkBox_selectAll, locatorType="Xpath", element="checkBox")
        self.elementClick(self._delete_button, locatorType="Xpath", element="checkBox")

    def update_xpath(self,old_xpath,text_to_update,name):
        new_xpath = old_xpath.replace("text_to_update", name)
        self.log.info("Updated Xpath is as follow " + new_xpath)        
        return new_xpath
            
    def select_check_box(self,new_xpath,name):
        self.waitForElement(locator= new_xpath, locatorType="Xpath", timeout=20, pollFrequency=1)
        #self.isElementPresent(locator= new_xpath, locatorType="Xpath", element= "name"):
        self.elementClick(locator=new_xpath, locatorType="Xpath", element=name)
        self.log.info(name+ "related check box selected successfully")  
                
    def delete_entries(self,new_xpath):
        self.waitForElement(locator= new_xpath, locatorType="Xpath", element= "xpath of new entry")
        self.elementClick(locator=self._delete_button, locatorType="Xpath", element="delete button") 
        self.log.info("successfully clicked on delete button")     
 ##--------------------------------------------------------------------------------------------------------------------##
 
    def close_Whatfix_Windows(self):
        self.log.info("waiting for the element")
        time.sleep(10)
        self.switch_to(locator=self._iframe,locatorType="Xpath")
        self.log.info("switching frame now")        
        self.elementClick(locator=self._whatfix, locatorType="Xpath", element="whatfix")
        self.switch_to_default()

    def navigategatewayPage(self):
        time.sleep(1)
        '''
        self.waitForElement(self._gateways_gateways_menu, locatorType="Xpath", pollFrequency=1) 
        self.elementClick(self._gateways_gateways_menu, locatorType="Xpath", element="gateway_&_gateway_button")
        '''
        self.waitForElement(self._gateways_menu, locatorType="Xpath", pollFrequency=1)         
        self.elementClick(self._gateways_menu, locatorType="Xpath", element = "gateway_button")
        self.verifyPageTitle("Gateways - SafeHats | MyInstaSafe")

    def navigate_to_gateway_Add_window(self):    
        self.navigategatewayPage()
        self.clickAddButton()
        time.sleep(1)
        self.verifyAddWindow(self._add_window_heading)           
      
    def add_Single_Gateway(self, gatewayName="", location="", backUpGateway="", bandwidth="", protectedNetwork=""):    
        time.sleep(1)
        self.log.info("clear all data field")
        #self.clearFields()
        self.log.info("Enter gateway name")
        self.enterGatewayName(gatewayName)
        self.log.info("gateway name entered successfully")
        self.enterLocation(location)
        self.log.info("gateway location entered successfully")
        self.enterBackupGatewayName(backUpGateway)
        self.log.info("Backup Gateway Name entered successfully")
        self.enterBandwithLimit(bandwidth)
        self.log.info("Band width entered successfully")
        self.enterProtectedNetwork(protectedNetwork)
        self.log.info("Protected Network Address entered successfully")
        self.clickSaveButton()
        self.log.info("Save button clicked successfully")
        #self.closeAddWindow()
        #self.log.info("refresh gateway page")
        #self.driver.refresh()
        self.log.info("reload page and wait up to 30 second ")
        self.driver.set_page_load_timeout(10)
        self.log.info("")
                
    def addMultiplegateway(self, gatewayName="", location="", backUpGateway="", bandwidth="", protectedNetwork=""):
        self.log.info("Enter gateway name")
        self.enterGatewayName(gatewayName)
        self.log.info("gateway name entered successfully")
        self.enterLocation(location)
        self.log.info("gateway location entered successfully")
        self.enterBackupGatewayName(backUpGateway)
        self.log.info("Backup Gateway Name entered successfully")
        self.enterBandwithLimit(bandwidth)
        self.log.info("Band width entered successfully")
        self.enterProtectedNetwork(protectedNetwork)
        self.log.info("Protected Network Address entered successfully")
        self.clickSaveButton()
        self.log.info("Save button clicked successfully")
        self.log.info("reload page and wait up to 30 second ")
        self.driver.set_page_load_timeout(10)
                       
    def delete_Sigle_Gateway(self,name):
        # change Xpath at run time
        new_xpath = self.update_xpath(self._gateway_entry, "gateway", name)
        # search what to delete
        value = self.verify_gateway_entry(name)
        if value:
            self.select_check_box(new_xpath, name)
            self.delete_entries(new_xpath,name)
            value1 = self.verify_gateway_entry(self,name)
            if value1 :
                self.log.info("Fail to delete ("+name+") gateway")
                return False
            else :
                self.log.info(name+ " gateway successfully deleted")
            return True
        else :
            self.log.info("desire gateway " + name + " doesn't found")
            return False
      #   
     
      # select delete button
      # click on delete button
      
      
        
 #   def deleteMultipalegateway(self,):
        
        
          #  def deleteAll gateway(self):
            



   # def single_Delete(self):




