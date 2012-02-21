# All actions on the preferences panel
#!/usr/bin/python
from lettuce import world 
from sikuli.Sikuli import *
from miro_app import MiroApp
import yaml

class MainView(MiroApp):
  
    _ITEM_BADGES = {'download error': "badge_dl_error.png",
                    'currently playing': "item_currently_playing.png",
                    'download': 'button_download.png'}

    _VIEW_TOGGLES = {'normal': ["standard-view.png"],
                     'list': ["list-view.png"],
                     'hybrid': ["hybrid-view.png"] }
    _CONVERSION_PROGRESS = "item-renderer-conversion-progress-left.png"
    _CLEAR_FINISHED_CONVERSIONS = "button_clear_finished.png"
    
    _BUTTONS = {'Autodownload': 'button_autodownload.png', 
                'Remove Podcast': 'button_remove_podcast.png',
                'Settings': 'button_settings.png',
                'Save as Podcast': 'button_save_as_podcast.png'}
                
    _SEARCH = {'clear': 'tabsearch_clear.png',
               'inactive': 'tabsearch_inactive.png'}

    def locate_image(self):
        pass
         

    def multi_select(self,region,item_list):
        """Use the CTRL or CMD key as os appropriate to select items in a region.

        Return a list of the items that we successfully selected.
        """
        selected_items = []
        #press the ctrl / cmd key
        if config.get_os_name() == "osx":
                keyDown(Key.CMD)
        else:
            keyDown(Key.CTRL)
        #select each item in the list if it is found
        time.sleep(2)
        for x in item_list:
            print x
            if region.exists(x):
                region.click(x)
                time.sleep(2)
                selected_items.append(x)           
            
        #release the ctrl /cmd key         
        if config.get_os_name() == "osx":
                keyUp(Key.CMD)
        else:
            keyUp(Key.CTRL)
 
    def set_podcast_autodownload(self, reg, setting="Off"):
        """Set the feed autodownload setting using the button at the bottom of the mainview.

        """
        """Based on the position of the Playlists tab, click on the last podcast in the list.

        This is useful if the title isn't displayed completely or you have other chars to don't work for text recognition.
        """
        
        b = Region(reg.m.getX(),reg.m.getY()+500,reg.m.getW(), reg.m.getH())
        b.highlight(2)
        b.find("button_autodownload.png")
        b1 = Region(b.getLastMatch().right(80))
        b1.highlight(2)
        for x in range(0,3):
            if not b1.exists(setting,2):
                   b.click("button_autodownload.png")
                   time.sleep(2)

    def open_podcast_settings(self, reg):
        b = Region(reg.s.getX(),reg.m.getY()*2,reg.m.getW(), reg.m.getH())
        b.find(Pattern("button_settings.png"))
        click(b.getLastMatch())

    def click_remove_podcast(self, reg):
        reg.m.click(Pattern("button_remove_podcast.png"))

    def change_podcast_settings(self, reg, option, setting):
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
    
    def delete_items(self, reg, title, item_type):
        """Remove video audio music other items from the library.

        """
        type(Key.ESC)
        self.click_sidebar_tab(reg, item_type)
        self.tab_search(reg, title)
        if reg.m.exists(title,10):
            click(reg.m.getLastMatch())
            type(Key.DELETE)
            self.remove_confirm(reg, "delete_item")

    def delete_current_selection(self, reg):
        """Wherever you are, remove what is currently selected.

        """
        type(Key.DELETE)
        self.remove_confirm(reg, "remove")


  
    def tab_search(self, reg, title, confirm_present=False):
        """enter text in the search box.

        """
        print "searching within tab"
        time.sleep(3)
        if reg.mtb.exists("tabsearch_clear.png",5):
            print "found tabsearch_clear"
            click(reg.mtb.getLastMatch())
            click(reg.mtb.getLastMatch().left(10))
        elif reg.mtb.exists("tabsearch_inactive.png",5):
            print "found tabsearch_inactive"
            reg.mtb.click("tabsearch_inactive.png")
        else:
            print "can not find the search box"
        time.sleep(2)
        print "Entering search text"
        type(title.upper())
        time.sleep(3)
        if confirm_present != False:
            self.toggle_normal(reg)
            if reg.m.exists(title, 5):
                present=True
            elif reg.m.exists(Pattern("item-context-button.png")):
                present=True
            else:
                print("Item %s not found in the tab" % title)
            return present

    def clear_search(self, reg):
        if reg.mtb.exists("tabsearch_clear.png",5):
            print "found tabsearch_clear"
            click(reg.mtb.getLastMatch())
        


    def expand_item_details(self, reg):
        if reg.m.exists(Pattern("item_expand_details.png").exact()):
            click(reg.m.getLastMatch())
        
        
    def toggle_normal(self, reg):
        """toggle to the normal view.

        """
        print "toggling to normal view"
        # Find the search box to set the area.
        
        if reg.mtb.exists("tabsearch_clear.png",5): # this should always be found on gtk
            treg = Region(reg.mtb.getLastMatch().left(350))
        elif reg.mtb.exists("tabsearch_inactive.png",5):
            treg = Region(reg.mtb.getLastMatch().left(350))
        treg.setH(treg.getH()+14)
        treg.setY(treg.getY()-8)

        
        if treg.exists(Pattern("standard-view.png").similar(.91),3):
            click(treg.getLastMatch())
     

    def toggle_list(self, reg):
        """toggle to the list view.

        """
        print "toggling to list view"
        # Find the search box to set the area.
        
        if reg.mtb.exists("tabsearch_clear.png",5): # this should always be found on gtk
            treg = Region(reg.mtb.getLastMatch().left(350))
        elif reg.mtb.exists("tabsearch_inactive.png",5):
            treg = Region(reg.mtb.getLastMatch().left(350))
        treg.setH(treg.getH()+14)
        treg.setY(treg.getY()-8)
        if treg.exists(Pattern("list-view.png").similar(.91),3):
            click(treg.getLastMatch())
     


    def search_tab_search(self, term, engine=None):
        """perform a search in the search tab.

        Requires: search term (term), search engine(engine) and MainViewTopRegion (mtb)

        """
        print "starting a search tab search"
        # Find the search box and type in the search text
        
        if self.mtb.exists("tabsearch_clear.png",5): # this should always be found on gtk
            print "found the broom"
            click(self.mtb.getLastMatch())
            click(self.mtb.getLastMatch().left(10))
        elif self.mtb.exists("tabsearch_inactive.png",5):
            click(self.mtb.getLastMatch())
        type(term.upper())
        # Use the search text to create a region for specifying the search engine
        if engine != None:
            l = self.mtb.find(term.upper())
            l1= Region(int(l.getX()-20), l.getY(), 8, 8,)
            click(l1)
            l2 = Region(int(l.getX()-15), l.getY(), 300, 500,)
            
            if engine == "YouTube":
                l3 = Region(l2.find("YouTube User").above())
                l3.click(engine)
            else:
                l2.click(engine)
            type("\n") #enter the search 
                
        else:
            type("\n")
     

    def download_all_items(self, reg):
        print "downloading all the items"
        time.sleep(5)
        self.toggle_normal(reg)
        if reg.m.exists(Pattern("button_download.png"),3):       
            mm = []
            f = reg.m.findAll("button_download.png") # find all matches
            while f.hasNext(): # loop as long there is a first and more matches
                print "found 1"
                mm.append(f.next())     # access next match and add to mm
            for x in mm:
                click(x)
                time.sleep(1)
        else:
            print "no badges found, maybe autodownloads in progress"


      
    def confirm_download_started(self, reg,title):
        """Verifies file download started.

        Handles and already download(ed / ing) messages
        """
        print "in function confirm dl started"
        time.sleep(2)
        mr = Region(reg.mtb.above(50).below())
        if mr.exists("been downloaded",3) or \
           mr.exists("message_already_downloaded.png",1):
            downloaded = "downloaded"
            print "item already downloaded"
            type(Key.ESC)            
        elif mr.exists("downloading now",3) or \
             mr.exists("message_already_external_dl.png",1):
            downloaded = "in_progress"
            print "item downloading"
            type(Key.ESC)
        elif mr.exists("Error",3) or \
             mr.exists(Pattern("badge_dl_error.png"),1):
            downloaded = "failed"
            type(Key.ESC)
        else:
            self.click_sidebar_tab(reg, "Downloading")
            reg.mtb.click(Pattern("download-pause.png"))
            if mr.exists(Pattern("badge_dl_error.png"),2):
                downlaoded = "errors"
            elif self.tab_search(reg,title,confirm_present=True) == True:
                downloaded = "in_progress"
            else:
                    downloaded = "item not located"
            reg.mtb.click(Pattern("download-resume.png"))
        return downloaded


    def wait_download_complete(self, reg, title, torrent=False):
        """Wait for a download to complete before continuing test.

        provide title - to verify item present itemtitle_'title'.png

        """
        if not self.confirm_download_started(reg, title) == "downloaded":
            if torrent == False:
                if reg.m.exists(title):
                    reg.m.waitVanish(title,240)
            elif torrent == True:
        #break out if stop seeding button found for torrent
                for x in range(0,30):
                    while not reg.m.exists("item_stop_seeding.png"):
                        time.sleep(5)
                    
    def cancel_all_downloads(self, reg):
        """Cancel all in progress downloads.
        
        If the tab exists, cancel all dls and seeding.
        Click off downloads tab and confirm tab disappears.
        
        """
        self.click_sidebar_tab(reg, "Music")
        time.sleep(2)
        if reg.s.exists("Downloading",2):
            click(reg.s.getLastMatch())
            time.sleep(3)
            reg.mtb.click("download-cancel.png")
            if reg.m.exists("Seeding"):
                mm = []
                f = reg.m.findAll("button_download.png") # find all matches
                while f.hasNext(): # loop as long there is a first and more matches
                    print "found 1"
                    mm.append(f.next())     # access next match and add to mm
                for x in mm:
                    click(x)    
                    
    def wait_for_item_in_tab(self, reg, tab, item):
        self.click_sidebar_tab(reg, tab)
        self.tab_search(reg, item)
        self.toggle_normal(reg)
        for x in range(0,30):
            if not reg.m.exists(item):
                print ". waiting",x*5,"seconds for item to appear in tab:",tab
                time.sleep(5)
        
    def wait_conversions_complete(self, reg, title, conv):
        """Waits for a conversion to complete.

        Catches the status and copies the log to a more identifyable name.
        Then it clears out the finished conversions.

        """
        while reg.m.exists(title):
            if reg.m.exists(Pattern("item-renderer-conversion-progress-left.png")):
                waitVanish(reg.m.getLastMatch(),60)
            if reg.m.exists("Open log",5):
                sstatus = "fail"
            else:
                sstatus = "pass"
                
            #fix - it's possible that I am clicking the wrong button
            if reg.mtb.exists("button_clear_finished.png",2) or \
               reg.mtb.exists("Clear Finished",5):
                click(reg.mtb.getLastMatch())
            return sstatus




    def add_source_from_tab(self, reg, site_url):
        p = self.get_sources_region(reg)
        reg.m.find("URL")
        click(reg.m.getLastMatch().right(150))
        type(site_url+"\n")
 

             
        
    def verify_normalview_metadata(self, reg, metadata):
        i = reg.mtb.below(300)
        for k,v in metadata.iteritems():
            if not(i.exists(v,3)):
                print("expected metadata not found")

    def verify_audio_playback(self, reg, title):
        self.toggle_normal(reg)
        if reg.m.exists("item_currently_playing.png"):
            playback = True
        else:
            playback = False
        return playback

    def stop_audio_playback(self, reg, title):
        reg.m.click(title)
        self.shortcut("d")
        reg.m.waitVanish("item_currently_playing.png",20)
        self.log_result("102","stop audio playback shortcut verified.")

    def count_images(self, reg, img, region="screen", num_expected=None):
        """Counts the number of images present on the screen.

        It will either confirms that it is the expected value.
        Returns the number found.

        To narrow the search view - more reliable and efficient, specify the search region
        main: mainview
        sidebar: sidebar
        mainright: right half of mainview extended)

        
        """
        if region == "list":
            ly = reg.mtb.getY()-50
            lh = reg.mtb.getH()+800
            search_reg = Region(reg.mtb.getX(),ly,reg.mtb.getW(),lh)
        elif region == "main":
            search_reg = reg.m
        elif region == "mainright":
            lx = int(reg.m.getX())*4
            ly = int(reg.m.getY())
            wx = int(reg.m.getW()/2)  
            search_reg = Region(lx,ly,wx,reg.m.getH())
        elif region == "sidebar":
            search_reg = reg.s
        else:
            print "searching default SCREEN"
            search_reg = SCREEN
        search_reg.highlight(3)
        mm = []
        f = search_reg.findAll(img) # find all matches
        while f.hasNext(): # loop as long there is a first and more matches
            print "found 1"
            mm.append(f.next())     # access next match and add to mm
            f.destroy() # release the memory used by finder
        if num_expected != None:
            if not (len(mm) == int(num_expected)):
                print("Did not find the expected number of images")
        return len(mm)

        

