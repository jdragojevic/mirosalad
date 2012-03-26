#!/usr/bin/python
from lettuce import *
import os

def data_path(data):
    feed_path = os.path.join(os.getcwd(), 'features', 'terrain', 'TestData', 'feeds', data)
    return data_path




@step('I change the "(.*?)" field to "(.*?)"')
def edit_single_item_metadata(self, meta_field, meta_value):
    if meta_field == "art":
        meta_value = data_path(meta_value)
    world.menus.edit_item()
    world.dialogs.edit_item_metadata(meta_field, meta_value)
    


@step('I download the item "(.*?)"')
def download_item(self, url):
    world.menus.download_item(url)
    assert not world.dialog.download_dialogs() == "failed", "Download status is failed"
     

@step('I subscribe to the "(.*?)" feed')
def subscribe_feed(self, feed):
    url = feeds[feed]
    world.sidebar.add_feed(url, feed)
    world.sidebar.click_podcast(feed)

