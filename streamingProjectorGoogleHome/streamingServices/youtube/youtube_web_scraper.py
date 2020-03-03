from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from streamingServices.youtube.element_has_tag import element_has_tag
from streamingServices.youtube.youtube_scraping_IDs import scraping_IDs


# from element_has_tag import element_has_tag
# from youtube_scraping_IDs import scraping_IDs


class youtube_web_scraper:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.yID = scraping_IDs()
        # self.driver.get("http://www.youtube.com")
        # self.search("hello")
        # self.select_ideal_video_from_list(0)


    def search (self, search_string):
        self.search_string = search_string
        self.begin_search(search_string)


    def begin_search(self, search_string):
        button_element = self.driver.find_element_by_id(self.yID.search_button_element_id)
        search_bar_element = self.driver.find_element_by_css_selector(self.yID.search_bar_css)

        search_bar_element.send_keys(search_string)         # set Text on search bar 
        button_element.click()                              # click search

    def wait_for_succesful_search(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(element_has_tag(self.yID.video_list_tag))


    def select_ideal_video_from_list(self, driver, list_index = 0):
        self.wait_for_succesful_search()

        video_list_elements = self.driver.find_elements_by_tag_name(self.yID.video_list_tag)
        video_list_elements[list_index].click()

