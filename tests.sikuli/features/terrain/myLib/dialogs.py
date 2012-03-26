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

    _REMOVE_CONFIRMATION_DIALOGS = ["dialog_are_you_sure.png", 
                                    "dialog_one_of_these.png", 
                                    "Remove",
                                    "Are you",
                                    "One of", 
                                    "Cancel"]


    def remove_confirm(self, action="remove"):
        """If the remove confirmation is displayed, remove or cancel.

        action = (remove_feed, remove_item or cancel)
        """
        time.sleep(3)       
        for dialog_text in self._REMOVE_CONFIRMATION_DIALOGS:
            if exists(dialog_text, 2):
                print 'got confimation dialog'
                continue
        else:
            print 'Dialog not found'

        if action == "remove":
            type(Key.ENTER)
        elif action == "delete_item":
            print "clicking delete button"
            if config.get_os_name() == "osx":
                self.t.click("button_delete_file.png")
            else:
                self.m.click("Delete File")
        elif action == "cancel":
            print "clicking cancel"
            type(Key.ESC)
        elif action == "keep":
                print "keeping"
                self.m.click("Keep")
                type(Key.ENTER)
        else:
            print "not sure what to do in this dialog"
  


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



    def edit_item_type(self, new_type, old_type):
        """Change the item's metadata type, assumes item is selected.

        """
        click("Rating")
        f = Region(getLastMatch())
        f.setW(200)
        f.setH(100)
        f.find("Type")
        click(f.getLastMatch().right(50))
        if old_type == "Video" and new_type == "Music":
            type(Key.UP)
        elif old_type == "Video" and new_type == "Misc":
            type(Key.DOWN)
        elif old_type == "Music" and new_type == "Video":
            type(Key.UP)
        else: 
            mouseDown(Button.LEFT)
            mouseMove(new_type)
            mouseUp(Button.LEFT)
        time.sleep(2)
        click("button_ok.png")

    def edit_item_rating(self, rating):
        """Change the item's metadata type, assumes item is selected.

        """
        click("Rating")
        click(getLastMatch().right(50))
        for x in range(0,int(rating)):
            type(Key.DOWN)
        type(Key.ENTER)
        click("button_ok.png")


    def edit_item_metadata(self, meta_field, meta_value):
        """Given the field and new metadata value, edit a selected item, or multiple items metadata.

        """
        metalist = ["name","artist","album","genre","track_num",
                         "track_of","year","about","rating","type",
                         "art","path","cancel","ok"]
        time.sleep(2)
        self.shortcut('i')
        time.sleep(2)

        for i in (i for i,x in enumerate(metalist) if x == meta_field.lower()):
            rep = i

        if meta_field == "rating":
            self.edit_item_rating(rating=meta_value)
        elif config.get_os_name() == "osx" and rep > 6: #stupid but the tab gets stuck on the about field
            if meta_field == "art":
                click("Click to")
                type(meta_value)
                type(Key.ENTER)
            else:
                click(meta_field)
                click(getLastMatch().right(50))
                type(meta_value)
            click(Pattern("button_ok.png"))
        else:    
            for x in range(0,rep): #tab to the correct field
                type(Key.TAB)
                time.sleep(.5)
            if meta_field == "art": #need a space bar to open the text entry field
                type(" ")
                type(meta_value)
                type(Key.ENTER)
                time.sleep(2)
                click("button_ok.png")
            else:
                type(meta_value) #enter the new value
                ok_but = len(metalist)
                for x in range(rep+1,ok_but):
                    type(Key.TAB)
                    time.sleep(.5)
                type(Key.ENTER) #Save the changes

    def edit_item_video_metadata_bulk(self,new_metadata_list):
        """Given the field and new metadata value, edit a selected item, or mulitple items metadata.

        """
        metalist = ["show","episode_id","season_no","episode_no",
                         "video_kind","cancel","ok"]
        self.shortcut('i')
        time.sleep(2)
        find("Rating")
        v = Region(getLastMatch().above(100).left(60))
        v.click("Video")
        
        if exists("Show"):
            top_tab = getLastMatch().right(200)
            click(top_tab)
            metar = Region(getLastMatch().below())
            metar.setW(metar.getW()+300)
        else:
            print("Can not find show field")
        for meta_field,meta_value,req_id in new_metadata_list:
            print meta_field,meta_value
            for i in (i for i,x in enumerate(metalist) if x == meta_field):
                rep = i
                print rep,meta_field
            for x in range(0,rep): #tab to the correct field
                type(Key.TAB)
                time.sleep(.5)
            if meta_field == "video_kind": #need a space bar to open the text entry field
                type(" ")
                metar.click(meta_value)
            else:
                type(meta_value) #enter the new value
                #go back to the top field, Show
            if req_id:
                self.log_result(req_id,"value edited in dialog")
            click(top_tab)
        ok_but = len(metalist)
        for x in range(1,ok_but):
            type(Key.TAB)
            time.sleep(.5)
        type(Key.ENTER) #Save the changes
       

    def store_item_path(self):
        """Get the items file path from the edit item dialog via clipboard and return it.

        """
        if config.get_os_name == "osx":
            self.m.find("Path")
            pr = Region(self.m.getLastMatch()).right(500)
            pr.setX(pr.getX()+15)
            pr.setY(pr.getY()-10)
            pr.setH(pr.getH()+20)
            pr.highlight(5)
            mypath = pr.text()
            print mypath
            filepath = mypath
        else:
            for x in range(0,11):
                type(Key.TAB)
            self.shortcut('c')
            filepath = Env.getClipboard()
            type(Key.ESC) #ESC to close the dialog
        return filepath

    def change_podcast_settings(self, option, setting):
        find("Expire Items")
        p1 = Region(getLastMatch().nearby(800))
        p1.find(option)
        click(p1.getLastMatch().right(100))
        if not p1.exists(setting):
            type(Key.PAGE_DOWN)
        if not p1.exists(setting):
            type(Key.PAGE_UP)
        if setting == "Keep 0":
            type(Key.DOWN)
            time.sleep(1)
            type(Key.ENTER)
        else:
            p1.click(setting)
        time.sleep(2)
        p1.click("button_done.png")





