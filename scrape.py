from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome('./chromedriver')

# surf Incognito
option = webdriver.ChromeOptions()
option.add_argument("--incognito")

# launch Chrome
browser = webdriver.Chrome(executable_path='./chromedriver', chrome_options=option)
# surf to this URL
browser.get("https://github.com/Adjectival")

### timeout, error handling ###
timeout = 10
try:
	# waiting for avatar image to load, likely last element
	WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//img[@class='avatar width-full rounded-2']")))
except TimeoutException:
	print("Page takes too long to load-- try again")
	browser.quit()

# grabbing repo titles from URL
titles_element = browser.find_elements_by_xpath("//a[@class='text-bold']")

# parsing returned objects into desired items ('list comprehension')
titles = [x.text for x in titles_element]

# display title items in terminal
print('Repo titles:')
print(titles, '\n')