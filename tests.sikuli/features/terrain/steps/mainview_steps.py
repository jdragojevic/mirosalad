#!/usr/bin/python
from lettuce import *

@step('"(.*?)" (?:items|items) (?:is|are) displayed in the "(.*?)" view')
def main_view_has_items(item_text, view):
    world.mainview.toggle_filter(view)
    world.mainview.items_displayed(item_text)


@step('I (see|click) the "(.*?)" button')
def find_or_click_mainview_button(action, button):
    loc = world.mainview.locate(button)
    if action == 'click':
        loc.click()

@step('I enter a search for "(.*?)" using the search engine "(.*?)"')
def search_engine_search(self, term, engine):
    world.mainview.search_tab_search(term, engine)


