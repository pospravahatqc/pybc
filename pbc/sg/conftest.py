import pytest
from pbc.sg.sg_setup import GridSetup
from pbc.sg.test_sel_grid import ssh_instance

from selenium import webdriver

from pbc.sg.test_sel_grid import cleanlist, downloadlist, hablist, nodelist


@pytest.fixture()
def ffox_driver(request):
    # create a new Firefox session
    driver = webdriver.Firefox()
    driver.implicitly_wait(30)
    driver.maximize_window()
    return driver


@pytest.fixture(scope="session")
def connect_precondition(client):
    client.start()

@pytest.fixture(scope="session")
def grid_precondition():
    from pbc.sg.ssh import Ssh
    connection = Ssh('192.168.33.10', 'vagrant', 'vagrant')
    connection.start()
    connection.executor(cleanlist)
    connection.executor(downloadlist)
    connection.executor(hablist)
    connection.executor(nodelist)
    yield connection
    connection.close()
