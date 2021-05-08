import pytest
from selenium.webdriver.support.select import Select

from tests.conftest import setup
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass():
    # here no need to create constructor to assign self.driver = driver,bcoz Baseclass in inherited in test_e2e class
    # so automatically assigned...
    def verifyLinkPresence(self, text):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.LINK_TEXT, text))
        return element

    def selectOptionByText(self, locator, text):
        sel = Select(locator)
        sel.select_by_visible_text(text)
