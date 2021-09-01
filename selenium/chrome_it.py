import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.opera import OperaDriverManager

driver1 = webdriver.Chrome(ChromeDriverManager().install())
driver1.get("http://www.python.org")

driver2 = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver2.get("http://www.python.org")

driver3 = webdriver.Opera(executable_path=OperaDriverManager().install())
driver3.get("http://www.python.org")

time.sleep(1)

driver1.close()
driver2.close()
driver3.close()


