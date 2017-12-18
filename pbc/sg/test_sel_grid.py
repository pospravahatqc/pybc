from webbrowser import browser

from selenium.webdriver.support.wait import WebDriverWait

from pbc.sg.sg_setup import GridSetup
from pbc.sg.ssh import Ssh
# remote grid driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
import requests
import time

ssh_instance = Ssh('192.168.33.10', 'vagrant', 'vagrant')

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

cleanlist = [
    "killall java",
    "rm -r selenium*",
    "rm -r sg-node*",
    "rm -r log*"
]

def test_is_machine_run():
    ssh_instance.start()
    assert ssh_instance.check()

def test_is_mashin_run2():
    assert ssh_instance.check()

def test_grid_is_setup(grid_precondition):
    connection = grid_precondition
    result = []
    stdin, stdout, stderr = connection._client.exec_command("pgrep java")
    for line in stdout:
        result.append(line)
    assert (len(result)) == 2

def test_check_grid_is_run(grid_precondition):
    try:
        driver = webdriver.Firefox()
        driver.get("http://192.168.33.10:4444/grid/console")
        # time.sleep(3)
        # print("Page is ready")
        assert driver.find_element(By.XPATH, '//title[text()="Grid Console"]')
        # "seleniumProtocol=WebDriver -> found 5 times"
        assert  5 == len(driver.find_elements(By.XPATH, '//*[@id="left-column"]/div/div[2]/div[1]/p[2]/img'))
    except Exception as a:
            print a.message
            raise a
    finally:
        pass
        # driver.close()

def test_grid_session_count_http(grid_precondition):
    response = requests.get('http://192.168.33.10:4444/grid/console')
    assert response.content.count('browserName=firefox') == 5

def test_grid_test(grid_precondition):
    try:
        options = Options()
        options.add_argument('--headless')
        driver = webdriver.Remote(
        command_executor='http://192.168.33.10:5555/wd/hub',
        desired_capabilities={'browserName': 'firefox'},
        # desired_capabilities={'browserName': 'opera'},
        options=options
            )
        time.sleep(3)
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
    except Exception as a2:
        print a2.message
        raise a2
    finally:
        pass
        # driver.close()