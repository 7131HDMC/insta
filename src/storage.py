import os
import json

class Login:
  secret_file = "secret.json"
  data = {}
  def saveCredentials(self, password, user_name ):
    with open(self.secret_file, "w") as arq:
      self.data['credentials'].append({ 
        "user" : user_name , 
        "pass" :  password 
      })
      arq.write(json.dumps(self.data))
      arq.close()

  def __init__(self):
    self.data['credentials'] = []
    self.data['menu'] = ['Delete' , 'add' ]
    if os.path.exists(self.secret_file):
      self.load()

  def menu(self):
    if os.path.exists(self.secret_file):    
      print(self.data['menu'])
      print('O que quer fazer(ex: \'0\')?')
      k = int(input())
      if k == 1:
        self.add()
        self.load()
        self.menu()
      elif k == 0:
        self.delete()
        self.menu()
      
      return self.login(self.data['menu'][k])
    else:
      self.add()

  def load(self):
    with open(self.secret_file, "r") as arq:
      dt = json.load(arq)
      for cred in dt['credentials']:
        self.data['menu'].append(cred['user'])

  def delete(self):
    if os.path.exists(self.secret_file):
      os.remove(secret_file)


  def login(self, username):
    with open(self.secret_file, "r") as arq:
      data = json.load(arq)
      for cred in data['credentials']:
        if cred['user'] == username:
          credentials = {"user": cred['user'], "pass": cred['pass'] }
    return credentials

  def add(self):
    print("Type your user name: ")
    user = input()
    print("Type your password:  ")
    password = input()
    self.saveCredentials(password, user)
    self.menu()


