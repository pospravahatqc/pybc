import pytest
from pbc.sg.ssh import Ssh
from pbc.sg.sg_setup import GridSetup

from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

@pytest.fixture()
def ffox_driver(request):
    # create a new Firefox session
    driver = webdriver.Firefox()
    driver.implicitly_wait(30)
    driver.maximize_window()
    return driver

@pytest.fixture(scope="session")
def selenium_precondition(request):
    # initial setups
    client = Ssh('192.168.33.10', 'vagrant', 'vagrant')
    client.start()
    # preconditions -> ssh.connect('192.168.33.10', username='vagrant', password='vagrant')