import logging
import unittest
import time
from ddt import ddt, data, unpack
import pytest

from pages.loginPage import LoginPage
import utilities.custom_logger as cl
from utilities.read_data import getCSVData
from utilities.teststatus import Status


@pytest.mark.usefixtures("setUp")
@ddt
class LoginTests(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)
    
    result_set = {}
    _username = "richard"
    _password = "Richard@999"

    @pytest.fixture(autouse=True)   
    def objectSetup(self, setUp):
        self.lp = LoginPage(self.driver)
        #self.ts = Status(self.driver)
       # print("print lp "+str(self.lp))
    i=0
    @pytest.mark.run()  
    @data(*getCSVData("C:/Users/user/workspace/com.instasafev2/usource/usernamePassword.csv"))
    @unpack
    def test_t1invalidLogin(self, condition, username, password):
        self.i+=1
        self.log.info("*#" * 20)
        self.log.info("ID "+ str(self.i) +" test_t1_Login with " + condition + " credential where username is "+ username +" and password is " + password)
        self.log.info("*#" * 20)
        time.sleep(3)
        self.lp.multiple_login(condition, username, password)
'''        if condition=="valid":
            result = self.lp.verifyLogin()
            print("valid")
        if condition == "invalid" :
            result = not(self.lp.verifyLogin())
            print("Invalid")
        else :
            print("blank entry in CSV file")
            
      #  self.result_set[str(i)+"_"+condition]=result
        i+=1
        #self.assert_Result()
     
    def assert_Result(self):
        assert self.result.values() == True    
'''        
''' def test_t1invalidLogin(self, condition, username, password):
        self.log.info("*#" * 20)
        self.log.info("test_t1_invalidLogin when both field blank field")
        self.log.info("*#" * 20)
        #self.lp.logout()
        #time.sleep(3)
        self.lp.clickLoginButton()
        result1 = self.lp.verifyLoginFailed()
        assert result1 == False
        

    @pytest.mark.run(order=2)
    def test_t2invalidLogin(self):
        self.log.info("*#" * 20)
        self.log.info("test_t3invalidLogin started")
        self.log.info("*#" * 20)
        self.log.info("test with blank username and valid password field")
        self.lp.logout()
        self.lp.login("", "gaurav@123")
        result3 = self.lp.verifyLoginFailed()
        assert result3 == False
         
    @pytest.mark.run(order=3)
    def test_t3invalidLogin(self):
        self.log.info("*#" * 20)
        self.log.info("test_t3invalidLogin started")
        self.log.info("*#" * 20)
        self.log.info("test with blank username and invalid password field")
        self.lp.logout()
        self.lp.login("", "invalid")
        result3 = self.lp.verifyLoginFailed()
        assert result3 == False 
        
    @pytest.mark.run(order=4)
    def test_t4invalidLogin(self):
        self.log.info("*#" * 20)
        self.log.info("test_t3invalidLogin started")
        self.log.info("*#" * 20)
        self.log.info("test with invalid username and blank password field")
        self.lp.logout()
        self.lp.login("invalid", "")
        result3 = self.lp.verifyLoginFailed()
        assert result3 == False   
        
    @pytest.mark.run(order=5)
    def test_t5invalidLogin(self):
        self.log.info("*#" * 20)
        self.log.info("test_t3invalidLogin started")
        self.log.info("*#" * 20)
        self.log.info("test with invaid username and invalid password field")
        self.lp.logout()
        self.lp.login("invalid", "invalid")
        result3 = self.lp.verifyLoginFailed()
        assert result3 == False               

    @pytest.mark.run(order=6)
    def test_t6invalidLogin(self):
        self.log.info("*#" * 20)
        self.log.info("test_t3invalidLogin started")
        self.log.info("*#" * 20)
        self.log.info("test with invaid username and valid password field")
        self.lp.logout()
        self.lp.login("invalid", self._password)
        result3 = self.lp.verifyLoginFailed()
        assert result3 == False 
                
    @pytest.mark.run(order=7)
    def test_t7invalidLogin(self):
        self.log.info("*#" * 20)
        self.log.info("test_t2_invalidLogin started")
        self.log.info("*#" * 20)
        self.log.info("test with valid username and blank password field")
        self.lp.logout()
        self.lp.login(self._username, "")
        result2 = self.lp.verifyLoginFailed()
        assert result2 == False
        
    @pytest.mark.run(order=8)
    def test_t8invalidLogin(self):
        self.log.info("*#" * 20)
        self.log.info("test_t3invalidLogin started")
        self.log.info("*#" * 20)
        self.log.info("test with valid username and invalid password field")
        self.lp.logout()
        self.lp.login("self._username", "invalid")
        result3 = self.lp.verifyLoginFailed()
        assert result3 == False    

    @pytest.mark.run(order=9)
    def test_t9invalidLogin(self):
        self.log.info("*#" * 20)
        self.log.info("test_t4invalidLogin started")
        self.log.info("*#" * 20)
        self.log.info("test with invalid username and blank password field")
        self.lp.logout()
        self.lp.login("test@email.com", "Abc@122")
        result4 = self.lp.verifyLoginFailed()
        assert result4 == False    
        
    @pytest.mark.run(order=5)
    def test_t5validLogin(self):
        self.log.info("*#" * 20)
        self.log.info("test_t5invalidLogin started")
        self.log.info("*#" * 20)
        self.lp.logout()        
        self.lp.login("gaurav", "gaurav@123")
        time.sleep(3)
        result5 = self.lp.verifyLoginTitle()
        self.ts.mark(result5, "Title Verification")
        result6 = self.lp.verifyLoginSuccessful()
        print("Result5: " + str(result5))
        print("Result6: " + str(result6))
        self.ts.markFinal("test_t5validLogin", result6, "Login Verification")
        '''