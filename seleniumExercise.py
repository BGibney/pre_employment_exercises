from selenium.webdriver import Chrome

driver = Chrome()
driver.get("https://google.com")

searchbox = driver.find_element_by_name("q")
searchbox.send_keys('RTS Labs')
searchbox.submit()

results = driver.find_elements_by_xpath("//*[@id='rso']//a")
results[0].click()
