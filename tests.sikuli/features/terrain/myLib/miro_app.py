import os
import time
import glob
import config
import testvars
import testsetup
from sikuli.Sikuli import *
from miro_regions import MiroRegions

#setBundlePath(config.get_img_path())

class MiroApp(object):
    """Tabs and dialogs inherit from MiroApp.

    """
    def __init__(self):
        '''
        Constructor
        '''

        self.os_name = config.get_os_name()
        self.SYS_TEXT_ENTRY_BUTTON = Pattern('type_a_filename.png')
        self.OPTION_EXPAND = Pattern("prefs_expand_option.png")
        AppRegion = MiroRegions()
        self.s = AppRegion.s
        self.sidebar_width = self.s.getW()
        self.m = AppRegion.m
        self.mtb = AppRegion.mtb
        self.t = AppRegion.t
        self.mr = AppRegion.mr


    def screen_region(self):
        myscreen = Screen()
        screen_region = Region(myscreen.getBounds())
        return screen_region
        
    
    def miro_focus(self):
        App.focus("Miro")


    def find_element(self, elements, region=None):
        """given a list of element locate the first instance return it's region.

        """
        if region == None:
                region = self.screen_region()
        for x in elements:
            if region.exists(x, 3): break 
            else:
                print ("Can't find: %s" % elements)
        element_region = Region(region.getLastMatch())
        return element_region

    def click_element(self, elements, region=None):
        """given a list of element locate the first instance and click.

        """
        if region == None:
            region = self.screen_region()
        for x in elements:
            if region.exists(x, 3): break 
            else:
                print ("Can't find: %s" % elements)
        click(region.getLastMatch())



    
    def shortcut(self, key, shift=False):
        """Keyboard press of the correct shortcut key

        for os x = cmd + key
        for win and linux = ctrl + key

        """
        if shift == False:
            if config.get_os_name() == "osx":
                type(key,KEY_CMD)
            elif config.get_os_name() == "win":
                type(key,KEY_CTRL)
            elif config.get_os_name() == "lin":
                type(key,KEY_CTRL)
            else:
                print config.get_os_name()
                type(key,KEY_CTRL)
        else:
            if config.get_os_name() == "osx":
                type(key,KEY_CMD+KEY_SHIFT)
            elif config.get_os_name() == "win":
                type(key,KEY_CTRL+KEY_SHIFT)
            elif config.get_os_name() == "lin":
                type(key,KEY_CTRL+KEY_SHIFT)
            else:
                print config.get_os_name()
                type(key,KEY_CTRL+KEY_SHIFT)
        
    def quit_miro(self):
        if exists("Miro",10):
            click(getLastMatch())
            self.shortcut("q")       
        if exists("in progress", 10) or \
              exists("Quit",5):
            type(Key.ENTER)
        time.sleep(20)
      

    def restart_miro(self):
        if self.os_name == "lin":
            config.start_miro_on_linux()
        else:
            App.open(testsetup.launch_cmd())
        wait("Miro",30)

        
    def open_prefs(self, reg, menu=None, option=None):
        """OS specific handling for Preferences menu, since it differs on osx and windows.

        """
        if reg.s.exists("icon-search.png",3) or \
           reg.s.exists("icon-video.png",3):
            click(reg.s.getLastMatch())
        time.sleep(3)
        if menu == None:
            option = 'Preferences'
            sc = 'f'
        else:
            sc = menu[0].lower()
        #Open the Preferences Menu based on the os with keyboard navigation
        if config.get_os_name() == "osx":
            self.shortcut(',')
        else:
            myscreen = Screen()
            pr = Region(myscreen.getBounds())
            type(sc,KEY_ALT)
            reg.s.click(option)
            time.sleep(2)

    def type_a_path(self, file_path):
        if config.get_os_name() == "osx":
            type(file_path +"\n")     
        else:
            if not exists("Location",5):
                click(self.SYS_TEXT_ENTRY_BUTTON)
                time.sleep(2)
            else:  #clear any text in the type box
                for x in range(0,15):
                    type(Key.DELETE)
            type(file_path +"\n")

#####################KEEPERS ABOVE THIS LINE ##############################################

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
        return selected_items
        
        
    def cmd_ctrl():
        """Based on the operating systems, returns the correct key modifier for shortcuts.
        
        """
        if config.get_os_name() == "osx":
            return "CMD"
        elif config.get_os_name() == "win":
            return "CTRL"
        else:
            print config.get_os_name()
            return "CTRL"


    def open_ff(self):
        """Returns the launch path for the application.

        launch is an os specific command
        """
        if self.os_name == "osx":
            return "/Applications/Firefox.app"
        elif self.os_name == "win":
            return os.path.join(os.getenv("PROGRAMFILES"),"Mozilla Firefox","firefox.exe")
        elif self.os_name == "lin":
            config.start_ff_on_linux()
            return "Firefox"
        else:
            print "no clue"

    def browser_to_miro(self, reg, url):
        """Opens the browser and copies in a url. Waits then closes the browser.

        This has the expectation that the browser is configured to open the url with miro, .torrent or feed item.
        """
        myFF = App.open(self.open_ff())
        if reg.t.exists("Firefox",45):
            click(reg.t.getLastMatch())
        time.sleep(5)
##        if config.get_os_name() == "osx":
##            self.shortcut('f', shift=True)
##        else:
##            type(Key.F11)
        time.sleep(3)
        self.shortcut("l")
        time.sleep(2)
        type(url + "\n")
        time.sleep(30)
        self.shortcut('w')


    def close_ff(self):
        for x in range(0,3):
            if exists("Firefox",1):
                print "ff is here"
                click(getLastMatch())
                self.shortcut('w')
                time.sleep(2)
            
    def close_window(self):
        if config.get_os_name() == "win":
            self.shortcut('w')
        else:
            self.shortcut('q')

    def toggle_radio(self,button):
        
        """Looks for the specified tab by image base name.
        Should be able to find the image if it is selected or not selected.
        """
        if noreg.t.exists (imagemap.Buttons[button +"_selected"]):
            click (imagemap.Buttons[(button)])   
     


    def close_one_click_confirm(self):
        """Close any os confirm dialogs when opening 1-click subscribe feeds."


        """
        if exists("sys_open_alert.png",30):
            click("sys_ok_button.png")


        
        
    def delete_site(self, reg, site):
        """Delete the video feed from the sidebar.
        feed = the feed name exact text that is displayed in the sidebar.
        m = Mainview Region, calculate in the testcase on launch.
        s = Sideview Region, calculated in the testcase on launch.

        """
        
        p = self.get_sources_region(reg)
        if p.exists(site,15):
            click(p.getLastMatch())
            time.sleep(2)
            type(Key.DELETE)
            self.remove_confirm(reg, "remove")
        else:
            print "site not present: ",site



    def add_playlist(self, reg, playlist, style="menu"):
        """Add a playlist miro using 1 of the following styles:

        1. style='menu' uses the Playlist menu option
        2. style='shortcut' uses the keyboard shortcut
        3. style='context' uses right-click context menu
        4. style='tab' uses the Playlists sidebar tab.
        
        Verify the playlist is added by clicking on it.
        """
        if style == "menu":
            find("Sidebar")
            mmr = Region(getLastMatch().right())
            print mmr
            mmr.setH(mmr.getH()*8)
            mmr.setW(mmr.getW()*4)
            print mmr
            mmr.click("Playlists")
            type(Key.DOWN)
            type(Key.ENTER)
        elif style == "shortcut":
            self.shortcut('p')
        elif style == "context":  # assumes the context menu is already open on the item
            reg.m.click("Add to Playlist")
        elif style == "tab":
            self.get_playlists_region(reg)
            reg.m.find("Name")
            click(reg.m.getLastMatch().right(150))
        else:
            print "new playlist style must be one if 'menu','shortcut','context' or 'tab'."
            
        time.sleep(2)
        type(playlist + "\n")
        time.sleep(10) #give it 10 seconds to add the playlist
        self.click_playlist(reg, playlist)
        time.sleep(3)



    def add_watched_folder(self, reg, folder_path, show=True):
        """Add a feed to miro, click on it in the sidebar.
        
        Verify the feed is added by clicking on the feed and verify the feed name is present
        in the main title bar.
        """
        reg.t.click("File")
        reg.t.click("Import")
        reg.t.click("Watch")
        time.sleep(4)
        if show == True:
            time.sleep(1)
            type(folder_path+"\n")
            time.sleep(10) #give it 10 seconds to add the feed
            self.click_last_podcast(reg)
        else:
            type(folder_path)
            reg.m.click("Show in")
            type(Key.TAB)
            type(Key.TAB)
            type(Key.ENTER)
        
    def click_last_source(self, reg):
        """Based on the position of the Playlists tab, click on the last podcast in the list.

        This is useful if the title isn't displayed completely or you have other chars to don't work for text recognition.
        """
        p = self.get_sources_region(reg)
        time.sleep(5)
        p.find("Stores")
        click(p.getLastMatch().above(38))


    def click_last_podcast(self, reg):
        """Based on the position of the Playlists tab, click on the last podcast in the list.

        This is useful if the title isn't displayed completely or you have other chars to don't work for text recognition.
        """
        p = self.get_podcasts_region(reg)
        time.sleep(5)
        reg.s.find("Playlists")
        click(reg.s.getLastMatch().above(35))


    def expand_feed_folder(self, reg, feed):
        p = self.get_podcasts_region(reg)
        if p.exists(feed):
            fr = Region(p.getLastMatch()).left()
            fr.setY(fr.getY()-10)
            fr.setH(fr.getH()+20)
        if fr.exists(Pattern("folder_closed.png")):
            click(fr.getLastMatch())
        else:
            print "not found"
        

    def delete_all_podcasts(self, reg):
        p = self.get_podcasts_region(reg)
        time.sleep(5)
        pody = p.getY()+40
        top_podcast = Location(p.getX(),pody)
        reg.s.find("Playlists")
        if (reg.s.getLastMatch().getY() - pody) > 100:
            click(reg.s.getLastMatch().above(35))
            keyDown(Key.SHIFT)
            click(top_podcast)
            keyUp(Key.SHIFT)
            if reg.m.exists("Delete",4) or reg.m.exists(Pattern("button_mv_delete_all.png"),4):
                click(reg.m.getLastMatch())
                time.sleep(2)
                type(Key.ENTER)
        
            
        


        

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


    def delete_feed(self, reg, feed):
        """Delete the video feed from the sidebar.
        feed = the feed name exact text that is displayed in the sidebar.
        m = Mainview Region, calculate in the testcase on launch.
        s = Sideview Region, calculated in the testcase on launch.

        """ 
        p = self.get_podcasts_region(reg)
        
        if p.exists(feed,4):
            click(p.getLastMatch())
            type(Key.DELETE)
            self.remove_confirm(reg, "remove")

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


    def add_source(self, reg, site_url, site, alt_site=None):
        reg.tl.click("Sidebar")
        reg.tl.click("Add Source")
        time.sleep(2)
        type(site_url+"\n")
        time.sleep(3)
        p = self.get_sources_region(reg)
        website = site[0:10].rstrip()
        if alt_site == None:
            p.find(website)
        else:
            if not exists(website,5):
                p.find(alt_site)
        click(p.getLastMatch())


    def add_source_from_tab(self, reg, site_url):
        p = self.get_sources_region(reg)
        reg.m.find("URL")
        click(reg.m.getLastMatch().right(150))
        type(site_url+"\n")
        
    def new_search_feed(self, reg, term, radio, source, defaults=False, watched=False):
        print "Opening the New Search Feed dialog."
        reg.t.click("Sidebar")
        reg.t.click("New Search")
        if defaults == True:
            print "Accepting defaults"
            time.sleep(2)
            type(Key.ENTER)
        elif watched == True: #special case for regression bug with watched folders
            print "Watched folder test case, should be no entry for the watched folder"
            if reg.m.exists(source):
                self.handle_crash_dialog(db=True, test=False)   
                print ("%s exists when it should not." % source)
            type(Key.ESC)
        else:
            print "Entering the search term"
            type(term)
            # Dialog appears in different locations on os x vs gtk
    ##        if config.get_os_name() == "osx":
    ##            reg.t.find("In this")
    ##            f = Region(reg.t.getLastMatch().right(600).below())
    ##        else:
    ##            reg.m.find("In this")
    ##            f = Region(reg.m.getLastMatch().right(600).above().below())
            reg.mr.find("Search for")
            f = Region(reg.mr.getLastMatch().right(600).below())
            f.setY(f.getY()-120)
            f.highlight(3)
            print "Clicking the %s radio button" %radio
            f.click(radio)
            click(f.getLastMatch().right(150))
            time.sleep(2)
            if radio == "URL":
                type(Key.TAB)
                print "Entering the search url"
                type(source)
            else:     
                if not f.exists(source,2):
                    f.click(self.OPTION_EXPAND)
                    f.click(source)
            f.click("Create")


            
        
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

    def verify_video_playback(self, reg):
        find(Pattern("playback_bar_video.png"))
        self.shortcut("d")
        waitVanish(Pattern("playback_bar_video.png"),20)
        self.log_result("102","stop video playback shortcut verified.")

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


    def http_auth(self, reg, username="tester", passw="pcfdudes"):
        mr = Region(reg.mtb.above(100).below())
        if not mr.exists("Username",30):
            print "http auth dialog not found"
        else:
            type(username)
            type(Key.TAB)
            type(passw)
            mr.click("button_ok.png")
            time.sleep(3)

    def remove_http_auth_file(self, reg):
        auth_file = os.path.join(config.get_support_dir(),"httpauth")
        self.quit_miro(reg)
        time.sleep(5)
        if os.path.exists(auth_file):
            auth_saved = True
            os.remove(auth_file)
            self.restart_miro()
        else:
            print "no auth file found"
            auth_saved = False
        return auth_saved

    def convert_file(self, reg, out_format):
        if self.os_name == "osx":
            reg.t.click("Convert")
        else:
           type('c',KEY_ALT)
        find("Folder")
        tmpr = Region(getLastMatch().above())
        tmpr.setX(tmpr.getX()-100)
        tmpr.setW(tmpr.getW()+150)
        if out_format == "MP3":
            tmpr.find("Theora")
            click(tmpr.getLastMatch().above(80))
        else:
            tmpr.find(out_format)
            click(tmpr.getLastMatch())
        

    def import_opml(self, reg, opml_path):
        self.click_sidebar_tab(reg, "Music")
        reg.tl.click("Sidebar")
        time.sleep(2)
        reg.tl.click("Import")
        time.sleep(2)
        self.type_a_path(opml_path)
        if exists("OK", 15) or exists("Successfully") or exists("imported", 5):
            type(Key.ENTER)

    def click_next(self, dR):
        """Click the Next button in a dialog.

        Needs the Dialog region (dR) set, see first_time_startup for example
        """
        print dR
        if dR.exists(Pattern("button_next.png"),5) or \
        dR.exists(Pattern("button_next1.png"),5):
             click(dR.getLastMatch())
        else:
            print "Next button not found"

    def click_finish(self, dR):
        """Click the Finish button in a dialog.

        Needs the Dialog region (dR) set, see first_time_startup for example
        """
        if dR.exists(Pattern("button_finish.png"),5) or \
           dR.exists(Pattern("button_finish1.png"),5):
            click(dR.getLastMatch())
        else:
            print "Finish button not found"


    def first_time_startup_dialog(self,
                                  lang="Default",
                                  run_on_start="No",
                                  search="No",
                                  search_path="Everywhere",
                                  itunes="No"):
        """Walk throught the first time startup dialog, specifying defaults.

        """
        if exists(Pattern("button_System_default.png").similar(.90),45) or \
           exists("System default",45) or \
           exists("Language",5):
            print "In first time dialog"
            dR = Region(getLastMatch())
            dR.setX(dR.getX()-200)
            dR.setY(dR.getY()-20)
            dR.setH(dR.getH()+600)
            dR.setW(dR.getW()+600)
            dR.highlight(2)
            dR.setAutoWaitTimeout(15)
            
        #Language Setting
        print "setting lang:",lang
        if not lang == "Default":
            click(getLastMatch())
            for x in range(0,3):
                if not exists(lang,3):
                    type(Key.PAGE_DOWN)
            for x in range(0,4):
                if not exists(lang,3):
                    type(Key.PAGE_UP)
            click(lang)
            time.sleep(2)        
        self.click_next(dR)
        
        #Run on Startup
        print "run at startup? ",run_on_start
        time.sleep(3)
        if run_on_start == "Yes":
            dR.click("Yes")
        elif run_on_start == "No":
            dR.click("No")
        else:
            print "pref not set"
        self.click_next(dR)
        
        #Add itunes library
        time.sleep(3)
        if config.get_os_name() == "osx"  or \
           (config.get_os_name() == "win" and dR.exists("iTunes",3)):
            print "itunes? ",itunes
            if itunes == "Yes":
                dR.click("Yes")
            else:
                dR.click("No")
            self.click_next(dR)
        
        #Search for music and video files
        print "search for files? ",search
        time.sleep(3)
        if search == "Yes":
            dR.click("Yes")
            print "specifying search"
            if search_path == "Everywhere":
                print "searching everywhere"
                self.click_next(dR)
                time.sleep(5)
                waitVanish("parsed",900) #this can take a long time, giving 15 mins for search            
            else:
                print "searching specific dir: ",search_path
                dR.click("Just")
                dR.click(Pattern("button_choose.png"))
                self.type_a_path(search_path)
                self.click_next(dR)
                waitVanish("parsed",300)        
        time.sleep(2)
        self.click_finish(dR)
        
    def corrupt_db_dialog(self, action="start_fresh", db=False):
        """Handle the corrupt db dialog.

        'action' options are 'start_fresh', 'submit_crash' or 'quit'
        'db' is 'True' (submit db with crash report) or 'False'
        """
        if exists(Pattern("button_start_fresh.png").similar(.90),20):
            print "In corrupt db dialog"
            dR = Region(getLastMatch().nearby(350))
            dR.highlight(1)
            dR.setAutoWaitTimeout(30)
            if action == "quit":
                type(Key.ENTER)
            elif action == "start_fresh":
                dR.click(Pattern("button_start_fresh.png"))
                wait("Music")
            elif action == "submit_crash":
                dR.click("Submit Crash")
                time.sleep(5)
                if db == True:
                    type(Key.ENTER)
                else:
                    dR.click(Pattern("button_dont_include_db.png"))
                time.sleep(5)
                dR.waitVanish("Sending")
                ct = ct + 1               
        

    def log_result(self, result_id, runner_id, status="pass"):
        LOG_RESULT = """
        <result testid="%(testid)s"
        is_automated_result="0"
        resultstatus="%(status)s"
        exitstatus="0"
        timestamp="%(timestamp)s"
        >
        
            <comment><![CDATA[ %(msg)s]]>
            </comment>
        </result>
    """
        
        log = "Log_current.xml"
        logfile = os.path.join(os.getcwd(),log)
        f = open(logfile, 'a')
        f.write(LOG_RESULT % {"testid": result_id,
                         "status": status,
                         "timestamp": time.strftime("%Y%m%d%H%M%S", time.gmtime()),
                         "msg": "executed as part of "+runner_id
                             })
        f.close
       
    def handle_crash_dialog(self, test_id=None, db=True, test=False):
        """Look for the crash dialog message and submit report.
        
        """
        crashes = False
        count = 1
        print "checking if there was a crash"
        while exists(Pattern("internal_error.png"),5):
            if count > 1:
                click("Ignore")
                break
            else:
                crashes = True
                tmpr = Region(getLastMatch().nearby(800))
                if db == True:
                    click("Include")
                try:
                    time.sleep(3)
                    tmpr.find("Include")
                    click(tmpr.getLastMatch().below(120))
                    type("Sikuli Automated test crashed:" +str(test_id))
                finally:
                    if exists("button_submit_crash_report.png") or exists("Submit Crash"):
                        click(getLastMatch())
                time.sleep(5)
                count = count + 1
            
        if crashes == True and test == False:
            print "miro crashed"
            type(Key.ESC) # close any leftover dialogs
            time.sleep(20) #give it some time to send the report before shutting down.
            print("Got a crash report - check bogon")
        else:
            print "no crashes"
            

        
