#!/usr/bin/python
from lettuce import *

@step('I choose "(.*?)" from the "(.*?)" menu')
def menu_action(self, menu, menu_item):
   getattr(worlds.menus, menu)(menu_item)

    
            

