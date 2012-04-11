from steps import *
import os
import config
import miro_app
import main_view
import sidebar_tab
import menus
import dialogs

from sikuli.Sikuli import *
from lettuce import before, after
from lettuce import world 


@before.all
def instantiate_pages():
    world.miro = miro_app.MiroApp()
    world.mainview = main_view.MainView()
    world.sidebar = sidebar_tab.SidebarTab()
    world.menus = menus.Menu()
    world.dialog = dialogs.Dialogs()


@before.each_feature
def setup_basic_data(feature):
    print "Running the feature %r, at file %s" % (
    feature.name,
    feature.described_at.file
    )
    if feature.name == "Edit Item Metadata":
        print "settting up some test data"
        # Add a feed that contains 1 of each item type (Music, Video, Misc) and set autodownload to All
        feed_path = os.path.join(os.getcwd(), 'features', 'terrain', 'TestData', 'feeds', "MixedCats.xml")
        world.sidebar.add_feed("file://"+feed_path, "MIXED CATS")
        world.mainview.set_podcast_autodownload("All")

@after.each_feature
def cleanup(feature):
    world.miro.quit_miro()
    config.set_def_db_and_prefs()
    world.miro.restart_miro()

#@before.each_scenario


#@before.each_step






