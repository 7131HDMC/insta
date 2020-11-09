
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
    try:
      WebDriverWait(self.driver,60).until(EC.presence_of_element_located((By.XPATH, self.select.BOX_ALERT)))
      campo_botao = self.driver.find_element_by_xpath(self.select.ALERT)
      campo_botao.click()
    except Exception:
      return None

  def save_pass(self):
    try:
      WebDriverWait(self.driver,60).until(EC.presence_of_element_located((By.XPATH, self.select.xBOX)))
      campo_botao = self.driver.find_element_by_xpath(self.select.xNO)
      campo_botao.click()
    except Exception:
      return None


