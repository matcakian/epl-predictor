import json

from seleniumwire import webdriver
from webdriver_manager.chrome import ChromeDriverManager

import time


options = {
	'disable_encoding': True,
	'cache_path': None
}


driver = webdriver.Chrome(seleniumwire_options=options)


# driver.set_page_load_timeout(10)

try:
	driver.get("https://www.sofascore.com/football/match/inter-miami-cf-new-york-red-bulls/gabsccKc#id:11911622")
except:
	pass

for i in range(0, 5):
    driver.execute_script("window.scrollBy(0, 400);")
    time.sleep(1)


for request in driver.requests:
	if request.response and "shotmap" in request.url:
		print("URL:", request.url)
		# print("Response:", request.response)


driver.quit()