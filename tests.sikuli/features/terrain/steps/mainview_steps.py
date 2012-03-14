#!/usr/bin/python
from lettuce import *

@step('"(.*?)" (?:items|items) (?:is|are) displayed in the "(.*?)" view')
def main_view_has_items(self, item_text, view):
    world.mainview.toggle_filter(view)
    world.mainview.items_displayed(item_text)


@step('I (see|click) the "(.*?)" button')
def find_or_click_mainview_button(self, action, button):
    loc = world.mainview.locate(button)
    if action == 'click':
        loc.click()

@step('I enter a search for "(.*?)" using the search engine "(.*?)"')
def search_engine_search(self, term, engine):
    world.mainview.search_tab_search(self, term, engine)

@step('I have "(.*?)" in the "(.*?)" tab')
def wait_for_item_in_tab(self, item, tab):
    world.sidebar.click_library_tab(tab)
    world.mainview.wait_for_item_in_tab(item)

@step('I set the feed "(.*?)" setting to "(.*?)"')
def set_podcast_preference(self, setting, value):
    feed_setting = "podcast_"+setting.lower()
    getattr(world.mainview, feed_setting)(value)

@step('I can verify the video "([^"]*)" is playable')
def verify_video_playback(self, title):
    assert world.mainview.verify_video_playback(title) == True, \
        "Can not verify playback started for %s" % title
