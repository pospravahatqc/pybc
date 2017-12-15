# selenium driver
import pytest

from pbc.sg.ssh import Ssh
from pbc.sg.sg_setup import GridSetup

# remote grid driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

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

@pytest.mark.gridpage_testinitsetup
def test_is_java_run(selenium_precondition):
    grid = GridSetup(selenium_precondition)
    grid.download(downloadlist)
    grid.start_hub(hablist)
    grid.add_node(nodelist)
    client = selenium_precondition
    client.start()
    stdin, stdout, stderr = client.exec_command("pgrep java")
    stdin.write('lol\n')
    stdin.flush()
    result = []
    for line in stdout:
        result.append(line)
    assert (len(result)) == 2
    client.close()

@pytest.mark.gridpage_test
def test_check_grid_is_run(ffox_driver, selenium_precondition):
    grid = GridSetup(selenium_precondition)
    grid.download(downloadlist)
    grid.start_hub(hablist)
    grid.add_node(nodelist)
    ffox_driver.get("http://127.0.0.1:4444/grid/console")
    assert ffox_driver.find_element(By.XPATH,
                               '//title[text()="Grid Console"]')  # "seleniumProtocol=WebDriver -> found 5 times"
    assert len(ffox_driver.find_elements(By.XPATH,
                                '//*[@id="left-column"]/div/div[2]/div[1]/p[2]/img')) == 5  # "seleniumProtocol=WebDriver Not found five times"

@pytest.mark.grid_node
def testGridTest(selenium_precondition):
    grid = GridSetup(selenium_precondition)
    grid.download(downloadlist)
    grid.start_hub(hablist)
    grid.add_node(nodelist)
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Remote(
        command_executor='http://192.168.33.10:4444/wd/hub',
        desired_capabilities={'browserName': 'firefox'},
        # desired_capabilities={'browserName': 'opera'},
        options=options
    )
    try:
        driver.get("http://www.python.org")
        driver.save_screenshot('python.png')
        assert "Python" in driver.title
        elem = driver.find_element_by_name("q")
        elem.clear()
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        driver.save_screenshot('pycon.png')
        driver.get("http://www.python.org")
        # assert "No results found." not in driver.page_source
    except Exception as a:
        print a.message
        raise a
    finally:
        print 'close'
        driver.close()
