import requests

class Stories:
  def __init__(self):
    self.source = "https://www.instagram.com/stories/"

  def watch(self):
    requests.get(self.source + self.userName)

  def setName(self, userName):
    self.userName = userName

