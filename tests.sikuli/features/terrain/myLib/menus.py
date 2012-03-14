# All actions on the preferences panel
#!/usr/bin/python
from lettuce import world 
from sikuli.Sikuli import *
from miro_app import MiroApp

class Menu(MiroApp):
 
    def download_item(self, url):
        self.t.click("File")
        self.t.click("Download from")
        time.sleep(2)
        type(url+"\n")        

