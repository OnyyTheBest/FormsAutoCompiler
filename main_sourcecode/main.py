from selenium import webdriver
import selenium
from selenium.webdriver.common.keys import Keys
import time
import chrome_driver_configs as chronfigs
import configs as conf
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
                
                def run(self):
            
                        self.lollo()
                        self.realbotxD()
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
print("First part completed")
print("loading second part...")
class Pipposugovalsugo:


                def __init__(self, base_url, driver):
                        self.base_url = base_url
                        self.driver = driver

                time.sleep(2)

                def ciso(self):
                        self.driver.get(conf.YT_URL)
                time.sleep(3)

                def pippa(self):
                        self.driver.execute_script("window.scrollBy(0,500)","")
                        time.sleep(1)
                        self.driver.find_element_by_xpath('/html/body/c-wiz/div/div/div/div[2]/div[1]/div[4]/form/div/div/button/span')
                        time.sleep(5)
                        self.driver.find_element_by_xpath(conf.X_PATH3).click()
                        time.sleep(1)
                        self.driver.find_element_by_xpath(conf.X_PATH4).click()
                def run(self):
                        self.ciso()
                        self.pippa()

if __name__ == "__main__":
 options = chronfigs.get_chromdriver_options()
chronfigs.set_ignore_certificate_error(options)

driver = chronfigs.get_chrome_driver(options)
Oronzo2 = Pipposugovalsugo(conf.BASE_URL, driver)
Oronzo2.run()                        