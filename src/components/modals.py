
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from consts import SelectorsConts

class Modals: 
  def __init__(self, driver):
    self.driver = driver
    self.select = SelectorsConts()

  def ignore(self):
    self.save_pass()
    self.notification()
    

  #Get the notfication request modal 
  def notification(self):
    WebDriverWait(self.driver,60).until(EC.presence_of_element_located((By.XPATH, self.select.BOX_ALERT)))
    campo_botao = self.driver.find_elements_by_css_selector(self.select.ALERT)
    campo_botao.click()
    

  def save_pass(self):
    WebDriverWait(self.driver,60).until(EC.presence_of_element_located((By.XPATH, self.select.xBOX)))
    campo_botao = self.driver.find_element_by_xpath(self.select.xNO)
    campo_botao.click()



