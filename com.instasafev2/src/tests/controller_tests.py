import logging
import unittest

from ddt import ddt, data, unpack
import pytest

from pages.companyPortal.controller_Page import ControllerPages
import utilities.custom_logger as cl
from utilities.read_data import getCSVData
#from utilities.teststatus import Status


#from pages.companyPortal.controller_Page import ControllerPage
#@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@pytest.mark.usefixtures("universalSetUp", "setUp")
@ddt
class Test_ControllerTests(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)
    
    @pytest.fixture(autouse=True)
    def objectSetup(self, universalSetUp):
        self.cp = ControllerPages(universalSetUp)
    #    self.cp = ControllerPages(self.driver)
    #    self.ts = Status(self.driver)
    
    
    
    #to handle whatfix #
    """    
    @pytest.mark.run(order = 0)
    def test_close_whatfix_window(self): 
        self.log.info("try to close whatfix_window")
        self.cp.close_Whatfix_Windows()
        self.log.info("close_whatfix_window") 
       """ 
    # @pytest.mark.run(after = "test_close_whatfix_window")
    # def test_open_add_window(self):
    # self.log.info("test_open_add_window")
    # self.cp.navigate_to_Controller_Add_window()              
         
    @pytest.mark.run(order = 0)
    def test_t1AddController(self):
        self.log.info("*#" * 20)
        self.log.info("test_t1Addcontroller start")
        self.log.info("*#" * 20)
        self.log.info("navigate to controller page")
        self.cp.navigate_to_Controller_Add_window()   
        self.log.info("navigate to controller Add page")
        self.cp.add_Single_Controller("isademo", "test", "TCP", "1470", "10.14.70.0", "27")
        self.log.info("controller add process complete now verify newly added controller")
        result = self.cp.verify_Controller_entry("test")
        assert result == True

        
        
    @pytest.mark.run( after = "test_t1AddController")
    def test_delete_controller(self):
        self.log.info("*#" * 20)
        self.log.info("test_delete_controller")
        self.log.info("*#" * 20) 
        self.log.info("navigate to controller page")
        self.cp.navigateControllerPage()
        result = self.cp.delete_Sigle_Controller("test") 
        assert result == True
        
'''
    #@pytest.mark.run(after='test_open_add_window')  
    @data(*getCSVData("C:/Users/user/workspace/com.instasafev2/usource/controllerlist.csv"))
    @unpack
    def test_AddMultipleControllers(self, cloudServer, name, protocol, port, internalNetwork, netmaskBits):
        self.log.info("*#" * 20)
        self.log.info("test_AddMultiplecontroller start")
        self.log.info("*#" * 20)
        self.cp.addMultipleController(cloudServer, name, protocol, port, internalNetwork, netmaskBits)
        result = self.cp.verifyAddController("test")'''            
        
        
        