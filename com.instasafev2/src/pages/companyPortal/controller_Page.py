import logging
import string
import time

from base.basepage import BasePage
from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
from asyncio.tasks import sleep


class ControllerPages(BasePage,SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        #Locator
    # _whatfix = ".//button[@class='WFSTCY']" 
    #_iframe =".//*[@id='wfx-frame-smartPopup']" 
    _controllers_gateways_menu = ".//i[@class='icons ion-gear-a']"    
    _controller_menu = ".//a[contains(text(),'Controllers')]"
    _add_button = ".//button[contains(text(),'Add')]"   
    _heading_text=".//h2[contains(text(),'Add Controller')]"
    _cloudServer_field = ".//div[@class='selectize-input']"
    _cloudServer_list = ".//div[@role='option']"
    _name_field = ".//*[@id='vpn_name']"    
    _protocol_field = ".//*[@id='protocol']/option"
    _portNumber_field = ".//*[@id='port']"
    _internalNetwork_field = ".//*[@id='network']"
    _netmaskBit_field = ".//div[@name='netmask_bits']/descendant::div[@class='selectize-input']"
    _netmaskBit_list = ".//div[@role='option']"
    _save_button =".//button[@type='submit']"
    _controller_entry = ".//a[contains(text(),'controller')]"
    _close_addwindow = ".//a[@class='close_slide ion-android-close']"
    _checkBox_single = ".//a[contains(text(),'controller')]/parent::*/..//input[@type='checkbox']"
    _checkBox_selectAll = ".//input[@ng-model='selectedAll']"
    _delete_button = ".//button[contains(text(),'Delete')]"
    
            
    def clickAddButton(self):
        self.waitForElement(self._add_button, locatorType="Xpath", pollFrequency=1) 
        self.elementClick(self._add_button, locatorType="xpath")
  
    def verifyAddWindow(self):
        heading = self.isElementPresent(self._heading_text, locatorType="Xpath")
        self.log.info("Add window appear status is " + str(heading))
        
    def selectCloudServerDropDown(self, cloudServer):
        self.elementClick( self._cloudServer_field, locatorType="xpath")
        self.singleSelect_set_selections( self._cloudServer_list, locatorType="xpath",searchfor=cloudServer )
        
    def enterControllerName(self, controller):
        self.sendKeys(controller, self._name_field, locatorType="xpath", element="controller name")
        
    def selectProtocol(self, protocol):
        self.singleSelect_set_selections(self._protocol_field, locatorType="xpath", searchfor=protocol)
     
    def enterPortNumber(self, port):
        self.sendKeys(port, self._portNumber_field, locatorType="xpath")
     
    def enterInternalNetwork(self, ip):
        self.sendKeys(ip, self._internalNetwork_field, locatorType="xpath")
     
    def enterNetmaskBit(self, netmaskBit):
        self.elementClick( self._netmaskBit_field, locatorType="xpath")
        self.singleSelect_set_selections(self._netmaskBit_list, locatorType="xpath", searchfor=netmaskBit)
        
    def clickSaveButton(self):
        self.elementClick(locator =self._save_button, locatorType="Xpath")    

    def closeAddWindow(self):
        self.elementClick(locator= self._close_addwindow, locatorType="Xpath", element="closeAddWindow")
            
    def verify_Controller_entry(self, name):
        controller_entry = self._controller_entry.replace("controller", name)
        self.log.info("new Xpath of controller :- " + controller_entry)
        self.waitForElement(locator= controller_entry, locatorType="Xpath", timeout=30, pollFrequency=1)
        return self.isElementPresent(locator= controller_entry, locatorType="Xpath", element= "none")
        
    def clearFields(self):
        portNumberField = self.getElement(locator=self._portNumber_field,locatorType="xpath")
        portNumberField.clear()
    
    def checkbox(self,locator):
        self.elementClick(locator="", locatorType="Xpath", element="checkBox")

    def update_xpath(self,old_xpath,text_to_update,name):
        new_xpath = old_xpath.replace("text_to_update", name)
        self.log.info("Updated Xpath is as follow " + new_xpath)        
        return new_xpath
    
    # def check_for_element_precence(self,):
            
    def select_check_box(self,new_xpath,name):
        self.waitForElement(locator= new_xpath, locatorType="Xpath", timeout=30, pollFrequency=1)
        #self.isElementPresent(locator= new_xpath, locatorType="Xpath", element= "name"):
        self.elementClick(locator=new_xpath, locatorType="Xpath", element=name)
        self.log.info("related check box selected successfully")  
                
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

    def navigateControllerPage(self):
        time.sleep(4)
        self.waitForElement(self._controllers_gateways_menu, locatorType="Xpath", pollFrequency=1) 
        self.elementClick(self._controllers_gateways_menu, locatorType="Xpath", element="controller_&_gateway_button")
        self.waitForElement(self._controller_menu, locatorType="Xpath", pollFrequency=1)         
        self.elementClick(self._controller_menu, locatorType="Xpath", element = "controller_button")
        #self.verifyPageTitle(self, "titleToVerify")

    def navigate_to_Controller_Add_window(self):    
        self.navigateControllerPage()
        self.clickAddButton()
        self.verifyAddWindow()           
      
    def add_Single_Controller(self, cloudServer="", controllerName="", protocol="", port ="", internalNetwork="", netmaskBit="" ):    
        time.sleep(2)
        self.log.info("clear all data field")
        self.clearFields()
        self.log.info("select cloud server")
        self.selectCloudServerDropDown(cloudServer)
        self.log.info("Enter controller name")
        self.enterControllerName(controllerName)
        self.log.info("select protocol")
        self.selectProtocol(protocol)
        self.log.info("enter port number")
        self.enterPortNumber(port)
        self.log.info("enter IP address / network address")
        self.enterInternalNetwork(internalNetwork)
        self.log.info("enter net mask bit")
        self.enterNetmaskBit(netmaskBit)
        self.log.info("click on save button to save data")
        self.clickSaveButton()
        self.log.info("close Add window")
        self.closeAddWindow()
        self.log.info("refresh controller page")
        self.driver.refresh()
        self.log.info("reload page and wait up to 30 second ")
        self.driver.set_page_load_timeout(30)
        self.log.info("")
                
    def addMultipleController(self, cloudServer, name, protocol, port, internalNetwork, netmaskBits):
        self.selectCloudServerDropDown(cloudServer)
        self.enterControllerName(name)
        self.selectProtocol(protocol)
        self.enterInternalNetwork(internalNetwork)
        self.enterNetmaskBit(netmaskBits)
        self.clickSaveButton()
                       
    def delete_Sigle_Controller(self,name):
        # change Xpath at run time
        new_xpath = self.update_xpath(self._controller_entry, "controller", name)
        # search what to delete
        value = self.verify_Controller_entry(name)
        if value:
            self.select_check_box(new_xpath, name)
            self.delete_entries(new_xpath,name)
            value1 = self.verify_Controller_entry(self,name)
            if value1 :
                self.log.info("Fail to delete ("+name+") controller")
                return False
            else :
                self.log.info(name+ " controller successfully deleted")
            return True
        else :
            self.log.info("desire controller " + name + " doesn't found")
            return False
      #   
     
      # select delete button
      # click on delete button
      
      
        
 #   def deleteMultipaleController(self,):
        
        
          #  def deleteAll Controller(self):
            



   # def single_Delete(self):




