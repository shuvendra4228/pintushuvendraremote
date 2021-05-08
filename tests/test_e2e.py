import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from tests.conftest import setup
from utilities.BaseClass import BaseClass
from pageObjects.HomePage import HomePage
from pageObjects.CheckOutPage import CheckOutPage


# @pytest.mark.usefixtures("setup"),we define all fixtures in Baseclass for clean code,here also we can define
class TestOne(BaseClass):
    # pytest docs : https://docs.pytest.org/en/stable/contents.html
    def test_e2e(self):  # self points to request.cls.driver
        homepage = HomePage(self.driver)  # driver created in conftest file.So to access this here self.driver
        # homepage.shopItems().click() checkOutPage = CheckOutPage(self.driver) no need to create objects in test
        # case file.....bcoz if 10 pages in T.C(means 10 classes),we need to create 10 objects.... to avoid that,
        # first figure out what is the integration point between page create object for next page and return that
        # object
        checkoutpage = homepage.shopItems()  # shopitems returns objects of next page,so skipped creating object in T.C
        cards = checkoutpage.getCardTitles()
        i = -1
        for card in cards:
            i = i + 1
            print(card.text)
            if card.text == "Blackberry":
                checkoutpage.getCardFooter()[i].click()
        self.driver.find_element_by.css_selector("//a[@class*='btn-primary']").click()
        confirmPage = CheckOutPage.checkOutItems()
        self.driver.find_element_by(By.ID, "country").send_leys("ind")
        # its better to write explicit wait mech. in Baseclass(bcoz every T.C we are using it)..
        # called custom utilities.... T.C inherits Baseclass.
        self.verifyLinkPresence("india")  # as baseclass is inherited so baseclass object points to self...
        # using self we call baseclass properties
        assert ("abed" in cards)
