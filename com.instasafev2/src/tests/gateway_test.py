'''
Created on 28-Jun-2018

@author: gaurav
'''

import logging
import unittest
import pytest
import utilities.custom_logger as cl
from pages.companyPortal.gateway_Page import GatewayPages


class Test_GatewayTests(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)
    
    @pytest.fixture(autouse=True)
    def objectSetup(self, universalSetUp):
        self.gp = GatewayPages(universalSetUp)
        
    @pytest.mark.run(order = 0)
    def test_t1AddGateway(self):
        self.log.info("*#" * 20)
        self.log.info("test_t1 Add Gateway start")
        self.log.info("*#" * 20)
        self.log.info("navigate to Gateway page")
        self.gp.navigate_to_gateway_Add_window()   
        self.log.info("navigate to Gateway Add page")
        self.gp.add_Single_Gateway("Gateway1", "Location1", "BackUpGateway", "20", "10.14.70.2")
        self.log.info("controller add process complete now verify newly added controller")
        result = self.gp.verify_gateway_entry("Gateway1")
        assert result == True
    
        
    @pytest.mark.run( after = "test_t1AddGateway")
    def test_delete_gateway(self):
        self.log.info("*#" * 20)
        self.log.info("test_delete_controller")
        self.log.info("*#" * 20) 
        self.log.info("navigate to controller page")
        self.gp.navigategatewayPage()
        result = self.gp.delete_Sigle_Gateway("test") 
        assert result == True