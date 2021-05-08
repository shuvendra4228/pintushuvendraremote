from selenium.webdriver.common.by import By
from selenium import webdriver

from pageObjects.CheckOutPage import CheckOutPage
from tests import *

"""
POM: for each page,each class created.
Per page whatever object(web elements+ locatiing web elements methods) seen,all objects in single page class.exp: homepage objects maintained in home page class
call that objects(web elements+locatiing web elements methods) in each page class instead of having them in out T.C.
create objects of this home page in actual test and pass driver.
"""


class HomePage:
    # passing the driver obj from T.C to Page class
    def __init__(self, driver):
        self.driver = driver  # assign local to instance var

    shop = (By.CSS_SELECTOR, "a[href='/angularpractice/shop']")
    name = (By.CSS_SELECTOR, "[name='name']")
    email = (By.NAME, "email")
    check = (By.ID, "exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    submit = (By.XPATH, "//input[@value='Submit']")
    successMessage = (By.CSS_SELECTOR, "[class='alert-success']")

    def shopItems(self):
        # driver.findelement(by.css_selector,"a[href='/angularpractice/shop']")
        # return self.driver.find_element(*HomePage.shop)
        self.driver.find_element(*HomePage.shop).click()
        checkOutPage = CheckOutPage(self.driver)
        return checkOutPage

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getCheckBox(self):
        return self.driver.find_element(*HomePage.check)

    def getGender(self):
        return self.driver.find_element(*HomePage.gender)

    def submitForm(self):
        return self.driver.find_element(*HomePage.submit)

    def getSuccessMessage(self):
        return self.driver.find_element(*HomePage.successMessage)


