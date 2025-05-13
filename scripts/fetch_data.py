import json

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

from webdriver_manager.chrome import ChromeDriverManager

import time


options = webdriver.ChromeOptions()
options.set_capability(
	'goog:loggingPrefs', {"performance": "ALL", "browser": "ALL"}
)

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), 
	options=options)


driver.set_page_load_timeout(20)

try:
	driver.get("https://www.sofascore.com/football/match/inter-miami-cf-new-york-red-bulls/gabsccKc#id:11911622")
except:
	pass

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


logs_raw = driver.get_log("performance")
logs = [json.loads(log['message'])['message'] for log in logs_raw]


for log in logs:
	# if 'shotmap' in log['params'].get('headers', {}).get(':path', ''):
	# 	print(log['params'].get('headers', {}).get(':path', ''))
	# 	break
	pass


# input("Press enter to close the browser...")
# driver.quit()