class SelectorsConts:
  GECKO_PATH = "/home/monkey/Desktop/insta/insta/geckodriver"
  #LOGIN
  USER =  "username"
  PASS =  "password"
  #notification modal
  BOX_ALERT = "/html/body/div[4]/div/div/div"
  ALERT = "html.js.logged-in.client-root.js-focus-visible.sDN5V body div.RnEpo.Yx5HN div.pbNvD.fPMEg div._1XyCr div.piCib div.mt3GC button.aOOlW.HoLwm"
  
  #est'a aparecendo 2 alertas, um de credential.store e outro de notificaion.helper -> criar uma classe que extende objetos modal e limpa eles, fazer necess'ario adicionar quantos sugirem mais
  #credential.store
  xBOX = "/html/body/div[1]/section/main/div/div/div/section"
  xNO = "/html/body/div[1]/section/main/div/div/div/div/button"


  #SEARCH
  SEARCH_FIELD = "XTCLo.x3qfX"
  WAIT_RESULTS = "yCE8d"
  TARGET_ELEMENT = "//div[@class='drKGC']/div/a[1]"

  #FOLLOWERS
  FOLLOWERS_FIELD = "/html/body/div[1]/section/main/div/header/section"
  FOLLOWERS_PATH = "/html/body/div[1]/section/main/div/header/section/ul/li[2]/a"

  #Users 
  BOX_USERS = "/html/body/div[5]/div/div/div[2]/ul/div/li[1]/div/div[2]/div[1]/div/div/span/a"
#
  LIST_UN = "html.js.logged-in.client-root.js-focus-visible.sDN5V body div.RnEpo.Yx5HN div.pbNvD.fPMEg.HYpXt div._1XyCr div.isgrP ul.jSC57._6xe7A div.PZuss li div.Igw0E.rBNOH.eGOV_.ybXk5._4EzTm.XfCBB.HVWg4 div.Igw0E.IwRSH.eGOV_._4EzTm.yC0tu div.Jv7Aj.mArmR.pZp3x div.RR-M-.h5uC0"# XPATH - "/html/body/div[5]/div/div/div[2]/ul"
