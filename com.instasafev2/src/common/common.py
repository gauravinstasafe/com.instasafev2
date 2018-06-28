'''
Created on 12-Sep-2017

@author: gaurav
'''
from selenium.common.exceptions import NoSuchElementException, \
    NoAlertPresentException


class abc():
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to.alert()
        except NoAlertPresentException as e:
            return False
        return True    

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
        
        
    def test_popup_windows(self):
        driver = self.driver
        driver.find_element_by_xpath("//a[contains(@href, 'smallPopup.html')]").click()
        driver.switch_to.window("notes")
        driver.find_element_by_name("FirstName").clear()
        element = driver.find_element_by_name("FirstName")
        element.send_keys("Hermione")
        self.assertTrue("Hermione", element.text)        
        
            