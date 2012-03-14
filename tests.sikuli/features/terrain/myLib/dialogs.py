# Dialogs that are displayed in Miro
#!/usr/bin/python
from lettuce import world 
from sikuli.Sikuli import *
from miro_app import MiroApp

class Dialogs(MiroApp):
  
    _DOWNLOAD_DIALOGS = {'downloaded': ["message_already_downloaded.png", "been downloaded"],
                         'in_progress': ["message_already_external_dl.png", "downloading now"],
                         'failed': ["badge_dl_error.png", "Error"]
                        }



    def download_dialogs(self):
        """Handles and already download(ed / ing) messages
        
        """
        downloaded = 'undetermined'
        print "in function confirm dl started"
        time.sleep(5)
        mr = Region(self.mtb.above(50).below())
        for status, messages in self._DOWNLOAD_DIALOGS.iteritems():
            for message in messages:
                if mr.exists(message, 1):
                    downloaded = status
                    type(Key.ESC)
        return downloaded

