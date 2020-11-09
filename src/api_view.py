from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
from cookie import Login 
from consts import SelectorsConts
from components.modals import Modals


class Instagram:
  firefox = 0
  select = 0
  def  __init__(self, site):
    options = Options()
    options.add_argument(' -P InstaBot -headless')
    self.firefox = Firefox(executable_path='/home/monkey/Desktop/insta/InstagramAPI_QDA/geckodriver', options=options)
    self.firefox.get(site)
    self.select = SelectorsConts()
    self.modals = Modals(self.firefox)


  def execute(self):
    user_name_target = self.put_login()
    self.modals.ignore()
    self.busca(user_name_target)#search the target an so do something
    self.select_followers(user_name_target)
    self.getUserIndex()

  def select_followers(self, user):
    WebDriverWait(self.firefox,60).until(EC.presence_of_element_located((By.XPATH, self.select.FOLLOWERS_FIELD)))
    folowers_link = self.firefox.find_element_by_xpath(self.select.FOLLOWERS_PATH)
    folowers_link.click()

  def put_login(self):
    log =  Login()
    login_values = log.menu()
    user_name_target = self.get_user_name()
    campo_name = self.firefox.find_element_by_name(self.select.USER)#from pag
    campo_name.send_keys(login_values['user'])
    campo_pass = self.firefox.find_element_by_name(self.select.PASS)#from pag
    campo_pass.send_keys(login_values['pass'])
    campo_pass.send_keys(Keys.ENTER)
    return user_name_target

  def busca(self, user_name):
    campo_busca = self.firefox.find_element_by_class_name(self.select.SEARCH_FIELD)
    campo_busca.send_keys(user_name)
    WebDriverWait(self.firefox,60).until(EC.presence_of_element_located((By.CLASS_NAME, self.select.WAIT_RESULTS)))
    target = self.firefox.find_element_by_xpath(self.select.TARGET_ELEMENT)
    target.click()#

  def getUserIndex(self):
    WebDriverWait(self.firefox,60).until(EC.presence_of_element_located((By.XPATH, self.select.BOX_USERS)))
    users = self.firefox.find_element_by_xpath(self.select.LIST_UN)
    print(users.size())

  def ignore_alert(self):
    WebDriverWait(self.firefox,30).until(EC.presence_of_element_located((By.CLASS_NAME, self.select.BOX_ALERT)))
    campo_botao = self.firefox.find_element_by_class_name(self.select.ALERT)
    campo_botao.click() 

  def get_user_name(self):
    print("Type the user name than you would like spy:")
    user_name = input()
    return  user_name

p =  Instagram('https://www.instagram.com/accounts/login/?hl=pt-br&source=auth_switcher')
p.execute()
