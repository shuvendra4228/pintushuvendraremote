import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", dafault="firefox")


# first add cmdline options
# passing browser name form Clargs:py.test -s -v --browser_name firefox
driver = None  # to make available for all methods(then global driver)


# only once per class executed
# contest file and testcase all should be  under same path means under one python package
# and no need to imoort the confest file in testcase file bcoz itsin the same directory of test case file
@pytest.fixture(scope="class")
def setup(request):  # its an bydefault arguement
    global driver
    browser_name = request.config.getoption("browser_name")  # to retrieve value in that option
    if browser_name == "firefox":
        driver = webdriver.Firefox(executable_path="D:\\seleniumpython_workspace\\library\\geckodriver.exe")
    elif browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="D:\\seleniumpython_workspace\\library\\chromedriver.exe")
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    # here driver object created how to give driver connection to our test files..return driver and access in TC as
    # argument is not the permanent solutions bcoz yield after that driver.close()
    # so driver is closed we cannot return by using request we can return so using request we establish connection
    request.cls.driver = driver  # requests transfer the driver object
    yield
    driver.close()
