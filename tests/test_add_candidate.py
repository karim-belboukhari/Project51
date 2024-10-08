from pages.login_page import Login
from pages.add_candidatepage import AddCandidate
from utilities.custom_logger import LoggingGenerator
from utilities.read_properties import ReadConfig
import time
from selenium.webdriver.common.by import By
import random
import string
import pytest
import os
import allure

@allure.severity(allure.severity_level.CRITICAL)
class TestAddCandidate:
   
   email= ReadConfig.get_email()
   password=ReadConfig.get_password()
   loggin= LoggingGenerator.log_gen()
   screen2 = os.path.join(os.path.dirname(__file__), '..', 'Screenshots', 'addUser.png')
   @pytest.mark.Sanity
   def test_addcandidate(self, setup):
       self.loggin.info("***********************test_addcandidate started**********************")
       driver = setup
       Lp = Login(driver)
       Lp.set_username(self.email)
       Lp.set_password(self.password)
       Lp.click_login()
       self.loggin.info("***********************logging passed**********************")
       AddCand = AddCandidate(driver)
       AddCand.set_candidate()
       AddCand.set_firstname("karim")
       AddCand.set_lastname("belboukhari")
       AddCand.set_v_role("Senior QA Lead")
       self.emaill = random_generator() +"@gmail.com"
       AddCand.set_email(self.emaill)
       time.sleep(3)
       #AddCand.set_datepiker("2023-26-08")
       AddCand.set_note("Test for the note section")
       AddCand.set_checkbox()
       AddCand.save_candidate()
       time.sleep(5)
       expectedresult = "karim belboukhari"
       
       expectedfild = driver.find_element(By.XPATH, '//*[@data-v-7b563373 and @class="oxd-text oxd-text--p" and text()="karim  belboukhari"]')
    
       print(expectedfild.text)
       if expectedfild.text == expectedresult :
           
           assert True
           self.loggin.info("***********************test_addcandidate Passed**********************")
       else:
           driver.save_screenshot("Screenshots\\addUser.png")
           self.loggin.info("***********************test_addcandidate Failed **********************")
           assert False

def random_generator(size=8, chars= string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))