Feature: Edit Item Metadata
    As a user
    I want to change the file type setting


Scenario Outline: Drag an item to a Library tab to change the type

Given I have "<item name>" in the "<tab>" tab
When I drag "<item name>" to the "<new type>" tab
Then I can verify "<item name>" has the characteristics of a "<new type>" item

Examples:
    | tab | new type | item name |
    | Videos | Music | Tongue |
    | Music | Videos | Paris |


Scenario Outline: Use the Edit Item Details panel to change item type.

Given I have "<item name>" in the "<tab>" tab
When I edit the "<type>" metadata to "<new type>" for "<itme name>"
Then I can verify "<item name>" has the characteristics of a "<new type>" item

Examples:
    | tab | new type | item name |
    | Videos | Music | Tongue |
    | Music | Video | Sample|
    | Misc  | Video | CIRCUS |
 
 
Scenario Outline: Edit Album Art

Given I have "<item name>" in the "<tab>" tab
When I change the "art" field to "<art file>"
Then I can verify the "<item name>" has the "<art file>" thumbnail image

Examples:
    | item name | tab | art file | 
    | Pancakes  | Music | album_art1.jpg |
    | summer    | Videos | album_art1.jpg | 

          art_file = os.path.join(os.getenv("PCF_TEST_HOME"),"Miro","TestData","album_art1.jpg")    
        #add feed and download flip face item
        miro.toggle_normal(reg)
        miro.tab_search(reg, title)
        try:
            reg.m.click(title)
            miro.edit_item_metadata(reg, meta_field="art",meta_value=art_file)
            ## Verify new image here:
            reg.m.find(Pattern("album_art1.png"))
        finally:
            miro.open_prefs(reg)
            prefs = PreferencesPanel()
            folder_tab = prefs.open_tab("Folders")
            folder_tab.remove_watched_folder("ArtTest")
            folder_tab.close_prefs()
            
        
    def test_728(self):
        """http://litmus.pculture.org/show_test.cgi?id=728 edit metadata for mulitple items

        1. add Static List feed
        2. download the Earth Eats item
        3. Edit item metadata
       

        """
        reg = MiroRegions() 
        miro = MiroApp()
        miro.open_prefs(reg)
        prefs = PreferencesPanel()
        general_tab = prefs.open_tab("General")
        general_tab.show_audio_in_music("on")
        general_tab.close_prefs()
        
        url = "http://pculture.org/feeds_test/list-of-guide-feeds.xml"
        feed = "Static"
        term = "Earth Eats"
        title = "Mushroom" # item title updates when download completes
        new_type = "Video"

        edit_itemlist = [
            ["name", "Earth Day Everyday", "647"],
            ["artist", "Oliver and Katerina", "648"],
            ["album", "Barki Barks", "649"],
            ["genre", "family", "650"],
            ["track_num" ,"1", "673"],
            ["track_of" ,"2", "673"],
            ["year", "2010", "655"],
            ["rating", "5", "651"],
            ]
        
        #start clean
        miro.delete_feed(reg, feed)
        #add feed and download earth eats item
        miro.add_feed(reg, url,feed)
        miro.toggle_normal(reg)
        miro.tab_search(reg, term)
        if reg.m.exists("button_download.png",10):
            click(reg.m.getLastMatch())
        miro.wait_for_item_in_tab(reg, "Music",item=title)
        reg.m.click(title)
        for x in edit_itemlist:
            miro.edit_item_metadata(reg, meta_field=x[0],meta_value=x[1])
            try:
                miro.log_result(x[2],"test_647")
            finally:
                time.sleep(2)
        if not miro.tab_search(reg, "Earth Day",confirm_present=True) == True:
            self.fail("new title not saved")
        #cleanup
        miro.delete_feed(reg, feed)
