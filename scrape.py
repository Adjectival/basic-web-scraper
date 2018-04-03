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
repos_element = browser.find_elements_by_xpath("//a[@class='text-bold']")

# parsing returned objects into desired items ('list comprehension')
repos = [x.text for x in repos_element]

# display repo items in terminal
print('Repo names:')
print(repos, '\n')

# grabbing repo languages from URL
languages_element = browser.find_elements_by_xpath("//p[@class='mb-0 f6 text-gray']")

# parsing returned objects into desired items ('list comprehension')
languages = [x.text for x in languages_element]

# display title items in terminal
print('Repo languages:')
print(languages, '\n')

# combine and match array elements
for repo, language in zip(repos, languages):
	print("Repo: Language")
	print(repo + ": " + language, '\n')



