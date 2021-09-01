import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from robot.api.deco import keyword, library


@library
class myLibrary():
    ROBOT_AUTO_KEYWORDS = False

    @keyword('I open Chrome browser')
    def init_tests(self):
        self.chrome_driver = webdriver.Chrome(ChromeDriverManager().install())

    @keyword('I wait ${timespan_in_sec} seconds')
    def im_waiting(self, timespan_in_sec):
        print("this is waiting text print!")
        print("this is waiting text print!")
        print("this is waiting text print!")
        print("this is waiting text print!")
        print("this is waiting text print!")
        print("this is waiting text print!")
        # logger.debug("this is waiting text log debug!!")
        time.sleep(float(timespan_in_sec))
        print("this is waiting text print!")

    @keyword('I open webpage "${web_address}"')
    def open_page(self, web_address):
        self.chrome_driver.get(web_address)

    @keyword('I close Chrome browser')
    def end_tests(self):
        self.chrome_driver.close()
