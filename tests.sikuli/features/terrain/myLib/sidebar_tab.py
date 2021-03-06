# All actions on the preferences panel
#!/usr/bin/python
from sikuli.Sikuli import *
from lettuce import *
from miro_app import MiroApp


class SidebarTab(MiroApp):
    _FIXED_LIB_TABS_IMG = "sidebar_top.png"
    _FIXED_TABS = ["Miro", "Videos", "Music"]
    _MOVEABLE_TABS = ["Misc", "Downloading", "Converting", "Search", "Connect"]
    _EXPANDABLE_TABS = ["Sources", "Stores", "Podcasts", "Playlists"] #in order from top to bottom  

    def _fixed_library_region(self):
        find(Pattern(self._FIXED_LIB_TABS_IMG).similar(0.5))
        fl = Region(getLastMatch())
        fl.setX(fl.getX()-10)
        fl.setW(self.sidebar_width)
        fl.highlight(3)
        print fl
        return fl

    def _moveable_library_region(self):
        ml = self._fixed_library_region()
        ml.setY(ml.getY() + ml.getH())
        moveable_hgt = int(ml.getH()) * 1.45
        ml.setH(int(moveable_hgt))
        ml.highlight(3)
        return ml
    
    def _expandable_tab_region(self, tab):
        """ Find the Region of the contents of expandible tabs.  

        May have to page down in the sidebar to find the tab if there are many items.
        """
        if not self.s.exists(tab, 2):
            sch_reg = self.click_static_library_tab("Search")
            type(Key.PAGE_DOWN)
            world.sidebar_pg_dn = True
        self.s.click(tab)    
        tab_rg = Region(self.s.getLastMatch())

        topx = int(tab_rg.getX() * .5)
        topy = tab_rg.getY()
        if self._EXPANDABLE_TABS.index(tab) + 1 >= len(self._EXPANDABLE_TABS):
            height = self.s.getH()
        else:
            self.s.find(self._EXPANDABLE_TABS[self._EXPANDABLE_TABS.index(tab)+1])
            height = Region(self.s.getLastMatch()).getY() - tab_rg.getY()
        width = self.s.getW()
                         
        tab_region = Region(topx, topy, width, height)
        tab_region.setAutoWaitTimeout(20)
        tab_region.highlight(2)
        return tab_region

    def find_library_tab(self, tab):
        """Click any default tab in the sidebar.

        """
        if tab in self._FIXED_TABS:
            tabloc = self._fixed_library_region()
        elif tab in self._MOVEABLE_TABS:
            tabloc = self._moveable_library_region()
        elif tab in self._EXPANDABLE_TABS:
            tabloc = self._expandable_tab_region(tab) 
        else:
            print "%s is an unrecognized library tab" % tab
        click(Pattern(self._FIXED_LIB_TABS_IMG).similar(0.5))
        if tabloc.exists(tab, 2):
            return Region(tabloc.getLastMatch())
        else:  
            type(Key.DOWN)
            tabloc.find(tab)
            return Region(tabloc.getLastMatch())


    def click_library_tab(self, tab):
        tr =  self.find_library_tab(tab)
        click(tr)
        return tr

    def click_podcast(self, podcast):
        podcast_region = self._expandable_tab_region("Podcasts")
        podcast_region.click(podcast)
        return Region(podcast_region.getLastMatch())

    def click_playlist(self, playlist):
        playlist_region = self._expandable_tab_region("Playlists")
        playlist_region.click(playlist)
        return Region(playlist_region.getLastMatch())

    def click_source(self, source):
        source_region = self._expandable_tab_region("Source")
        source_region.click(source)
        return Region(source_region.getLastMatch())

    def click_store(self, store):
        store_region = self._expandable_tab_region("Store")
        store_region.click(store)
        return Region(store_region.getLastMatch())

    def add_feed(self, url, feed):
        """Add a feed to miro, click on it in the sidebar.
        
        """
        print "Adding the podcast: %s" % url
        self.t.click("Sidebar")
        self.shortcut('n')
        time.sleep(2)
        type(url + "\n")
        time.sleep(10) #give it 10 seconds to add and update the feed
        self.click_podcast(feed)
        time.sleep(3)


