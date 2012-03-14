#!/usr/bin/python
from lettuce import *
import os

def feed_path(feed):
    feed_path = os.path.join(os.getcwd(), 'features', 'terrain', 'TestData', 'feeds', feed)
    return feed_path

feeds = {"MIXED CATS": feed_path("MixedCats.xml"),
         "Short Cats": feed_path("ShortCats.xml"),
         "AL JAZEERA": feed_path("youtube-feed.rss"),
         "ONE DAY": feed_path("vimeo-feed"),
         "Dilbert": feed_path("dilbert-feed.xml")
        }

@step('I download the item "(.*?)"')
def download_item(self, url):
    world.menus.download_item(url)
    assert not world.dialog.download_dialogs() == "failed", "Download status is failed"
     

@step('I subscribe to the "(.*?)" feed')
def subscribe_feed(self, feed):
    url = feeds[feed]
    world.sidebar.add_feed(url, feed)
    world.sidebar.click_podcast(feed)

