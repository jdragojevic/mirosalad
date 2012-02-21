from steps import *
import miro_app
import main_view
import sidebar_tab

from sikuli.Sikuli import *
from lettuce import before, after
from lettuce import world 

#@before.each_feature
#@before.each_scenario


#@before.each_step

@before.all
def instantiate_pages():
    world.miro = miro_app.MiroApp()
    world.mainview = main_view.MainView()
    world.sidebar = sidebar_tab.SidebarTab()

@after.all
def teardown_browser(total):
    pass

