from selenium import webdriver
import selenium
from selenium.webdriver.common.keys import Keys
import time
import chrome_driver_configs as chronfigs
import configs as conf
import sys
import os
disclaimer = """
This bot was created out of boredom the creator (@OnyyTheBest) does not take any responsibility for what you do with this bot
"""
start = """

██████╗░░█████╗░████████╗  ██████╗░██╗░░░██╗
██╔══██╗██╔══██╗╚══██╔══╝  ██╔══██╗╚██╗░██╔╝
██████╦╝██║░░██║░░░██║░░░  ██████╦╝░╚████╔╝░
██╔══██╗██║░░██║░░░██║░░░  ██╔══██╗░░╚██╔╝░░
██████╦╝╚█████╔╝░░░██║░░░  ██████╦╝░░░██║░░░
╚═════╝░░╚════╝░░░░╚═╝░░░  ╚═════╝░░░░╚═╝░░░

░█████╗░███╗░░██╗██╗░░░██╗██╗░░░██╗████████╗██╗░░██╗███████╗██████╗░███████╗░██████╗████████╗
██╔══██╗████╗░██║╚██╗░██╔╝╚██╗░██╔╝╚══██╔══╝██║░░██║██╔════╝██╔══██╗██╔════╝██╔════╝╚══██╔══╝
██║░░██║██╔██╗██║░╚████╔╝░░╚████╔╝░░░░██║░░░███████║█████╗░░██████╦╝█████╗░░╚█████╗░░░░██║░░░
██║░░██║██║╚████║░░╚██╔╝░░░░╚██╔╝░░░░░██║░░░██╔══██║██╔══╝░░██╔══██╗██╔══╝░░░╚═══██╗░░░██║░░░
╚█████╔╝██║░╚███║░░░██║░░░░░░██║░░░░░░██║░░░██║░░██║███████╗██████╦╝███████╗██████╔╝░░░██║░░░
░╚════╝░╚═╝░░╚══╝░░░╚═╝░░░░░░╚═╝░░░░░░╚═╝░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚══════╝╚═════╝░░░░╚═╝░░░
"""

class Oronzo :


                def __init__(self, base_url, driver):
            
                        self.base_url = base_url
                        self.driver = driver

                def lollo(self):
                        self.driver.get(conf.BASE_URL)
                time.sleep(2)

                def realbotxD(self):
                        self.driver.find_element_by_xpath(conf.X_PATH1).click()
                        #set the xpath of the button you want to click
                        time.sleep(1)
                        self.driver.find_element_by_xpath(conf.X_PATH2).click()
                        #set the xpath of the button you want to click
                        time.sleep(4)
                        self.driver.quit()
                        restart()
                        
                def run(self):
            
                        self.lollo()
                        self.realbotxD()
def restart():
        os.execv(sys.executable, ['python'] + sys.argv)
if __name__ == "__main__":
                                        
 print(disclaimer)
 time.sleep(3)
 print(start)
options = chronfigs.get_chromdriver_options()
chronfigs.set_ignore_certificate_error(options)
chronfigs.set_incognito_mode(options)
                                                                
driver = chronfigs.get_chrome_driver(options)
Oronzo1 = Oronzo(conf.BASE_URL, driver)
Oronzo1.run()