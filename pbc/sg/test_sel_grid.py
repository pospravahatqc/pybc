from selenium.webdriver.common.by import By

def testJavaRun(selenium_precondition):
    client = selenium_precondition
    stdin, stdout, stderr = client.exec_command("pgrep java")
    stdin.write('lol\n')
    stdin.flush()
    result = []
    for line in stdout:
        result.append(line)
    assert (len(result)) == 2
    client.close()

def test_check_grid(ffox_driver):
    ffox_driver.get("http://127.0.0.1:4444/grid/console")
    assert ffox_driver.find_element(By.XPATH,
                               '//title[text()="Grid Console"]')  # "seleniumProtocol=WebDriver -> found 5 times"
    assert len(ffox_driver.find_elements(By.XPATH,
                                '//*[@id="left-column"]/div/div[2]/div[1]/p[2]/img')) == 5  # "seleniumProtocol=WebDriver Not found five times"