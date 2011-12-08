#!/usr/bin/python
from lettuce import *


class SidebarTab(object):
    _FIXED_LIB_TABS_IMG = "sidebar_top.png"
    _FIXED_TABS = ["Miro", "Video", "Music"]
    _MOVEABLE_TABS = ["Misc", "Downloading", "Converting", "Search", "Connect"]
    _EXPANDABLE_TABS = ["Sources", "Stores", "Podcasts", "Playlists"] #in order from top to bottom  

    def _fixed_library_region(self):
        find(Pattern(_FIXED_LIB_TABS_IMG).similar(0.5))
        fl = Region(getLastMatch())
        return fl

    def _moveable_library_region(self):
        fl = self.fixed_library_region()
        ml = Region(fl.getX(),
                    fl.getY() - fl.getH(),
                    fl.getW(),
                    int(fl.getH() * 1.45)
                    )
        return ml
    
    def _expandable_tab_region(self, tab):
        """ Find the Region of the contents of expandible tabs.  

        May have to page down in the sidebar to find the tab if there are many items.
        """
        if not world.s.exists(tab, 2):
            sch_reg = self.click_static_library_tab("Search")
            type(Key.PAGE_DOWN)
            world.sidebar_pg_dn = True
        world.s.click(tab)    
        tab_rg = Region(world.s.getLastMatch())

        topx = int(tab_rg.getX() * .5)
        topy = tab_rg.getY()
        if self._EXPANDABLE_TABS.index(tab) + 1 >= len(self._EXPANDABLE_TABS):
            height = world.s.getH()
        else:
            world.s.find(self._EXPANDABLE_TABS[self._EXPANDABLE_TABS.index(tab)+1])
            height = Region(world.s.getLastMatch()).getH()
        width = world.s.getW()
                         
        tab_region = Region(topx, topy, width, height)
        tab_region.setAutoWaitTimeout(20)
        return tab_region

    def find_static_library_tab(self, tab):
        """Click any default tab in the sidebar.

        """
        if tab in _FIXED_TABS:
            m = self._fixed_library_region()
        elif m in self._MOVEABLE_TABS:
            m = self._moveable_library_region() 
        if m.exists(tab, 2):
            return Region(m.getLastMatch())
        else:  
            type(Key.DOWN)
            m.find(tab)
            return Region(m.getLastMatch())


    def click_library_tab(self, tab):
       tr =  self.find_static_library_tab(tab)
       click(tr.getLastMatch())
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
    

      
