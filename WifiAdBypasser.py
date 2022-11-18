import time
from urllib import request
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from urllib3.exceptions import ReadTimeoutError
from requests.exceptions import ReadTimeout
import requests


class WifiAdBypasser:

    def __init__(self):
        self.driver = self.__initialize_selenium()

    def __initialize_selenium(self):
        WINDOW_SIZE = "1920,1080"
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--mute-audio")
        chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
        return webdriver.Chrome(options=chrome_options)

    def bypassByClassAndIndex(self,gatewayIp,videoElementClass,index,videoLength):
        while (True) :
            try :
                res =  requests.get(gatewayIp,timeout=1)
                if res.ok:
                    print("Connection lost")
                    print("Trying to reconnect ...")
                    self.driver.get(gatewayIp)
                    #play the video
                    self.driver.find_elements_by_class_name(videoElementClass)[index].click()   
                    time.sleep(videoLength)
                    self.driver.close()
                    print("connected")
            except (ReadTimeoutError,ReadTimeout) :
                print("Connection is working well ")
                time.sleep(10)        