#!/usr/bin/python
from lettuce import *


class Sidebar(MiroApp):

    def click_library_tab(self, tab):
	
@step('I am on the "(.*?)" tab')
