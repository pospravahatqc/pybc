import pytest
from pbc.sg.ssh import Ssh
from pbc.sg.sg_setup import GridSetup

from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

downloadlist = [
    "wget -O selenium-server-standalone-3.8.0.jar https://goo.gl/SVuU9X",
    "wget -O sg-node.json https://gist.github.com/extsoft/aed4cb6e0b1ae3cd1d38cafffdd79310/raw/"
]

hablist = [
    "java -jar selenium-server-standalone-3.8.0.jar -role hub >> log.txt 2>&1 &"
]

nodelist = [
    "java -jar selenium-server-standalone-3.8.0.jar -role node  -nodeConfig sg-node.json >> log.txt 2>&1 &"
]

@pytest.fixture(scope="session")
def selenium_precondition(request):
    # initial setups
    client = Ssh('192.168.33.10', 'vagrant', 'vagrant')
    client.start()
    # preconditions -> ssh.connect('192.168.33.10', username='vagrant', password='vagrant')

    try:
        grid = GridSetup(client)
        grid.download(downloadlist)
        grid.start_hub(hablist)
        grid.add_node(nodelist)

    except Exception as a:
        print(a.message)
        raise a

@pytest.fixture()
def ffox_driver(request):
    # create a new Firefox session
    driver = webdriver.Firefox()
    driver.implicitly_wait(30)
    driver.maximize_window()
    return driver