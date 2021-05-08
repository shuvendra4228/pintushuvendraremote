from selenium import webdriver
from selenium.webdriver.support.select import Select
import pytest

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass
from TestData.HomePageData import HomePageData

# debug:put a breakpoint,if we want to debug,then we have run through test runner of pycharm
# go to edit configuration,click on +,select pytest of python test,and in the script path we have to give the
# specific path that we are running
# D:\seleniumpython_workspace\selenium_automation\tests\test_HomePage.py
# now click on debug btn,test stop ta break point

class TestHomepage(BaseClass):
    def test_formSubmission(self, getData):
        # driver = Webdriver.Chrome(executable_path="D:\\Seleniumpython_workspace\\library\\chromedriver.exe")
        # driver.get("https://rahulshettyacademy.com/angularpractice/")
        # driver.maximize_window()
        # every element of Homepage should be sent to page object of Homepage
        homepage = HomePage(self.driver)
        # homepage.getName().send_keys("rahul")
        # homepage.getEmail().send_keys("Shetty")
        homepage.getName().send_keys(getData["firstname"])
        homepage.getName().send_keys(getData["lastname"])
        # homepage.getName().send_keys(getData[0])
        # homepage.getName().send_keys(getData[1])
        # now i can able to run this test on multiple sets of data
        homepage.getCheckBox().click()
        # sel = Select(homepage.getGender())
        # sel.select_by_visible_text("Male")
        self.selectOptionByText(homepage.getGender(), getData["gender"])
        homepage.submitForm().click()

        alertText = homepage.getSuccessMessage().text
# if some where testcase fails then automatically screenshot generate in our htmlreports
# by adding  screenshots code in conftest file(define screenshot method where driver is created in conftest file )
        assert ("Success" in alertText)
        self.driver.refresh()  # refreshed or else rahulmonaasu will get..no empty text field we get


# @pytest.fixture(params=[("rahul", "shetty", "male"), ("mona", "lisa", "female"), ("asu", "tosh", "male")])
# @pytest.fixture(params=HomePageData.test_HomePageData)
@pytest.fixture(params=HomePageData.getTestData("TestData2"))
# Testcase2 is on excel file based on that it will filter only TC2 data
def getData(self, request):t
    return request.param
# we didn't write this fixture inside confest
# Bcoz its not common to all test case only required for this