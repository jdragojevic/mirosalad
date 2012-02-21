#!/usr/bin/python
from lettuce import *

@step('I am on the "(.*?)" sidebar tab')
def display_library_tab(self, tab):
    world.sidebar.click_library_tab(tab)

@step('I am on the "(.*?)" source')
def display_source(self, tab):
    world.sidebar.click_source(source)

@step('I am on the "(.*?)" podcast')
def display_podcast(self, podcast):
    world.sidebar.click_podcast(podcast)

@step('I am on the "(.*?)" playlist')
def display_playlist(self, playlist):
    world.sidebar.click_podcast(playlist)


@step('I am on the "(.*?)" store')
def display_store(self, store):
    world.sidebar.click_store(store)

