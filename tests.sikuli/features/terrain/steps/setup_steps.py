#!/usr/bin/python
from lettuce import *
import config
import os

def db_path(database):
    db_path = os.path.join(os.getcwd(), 'features', 'terrain', 'TestData', 'databases', database)
    return db_path

databases = {"corrupt": db_path("corrupt_db"),
             "empty": db_path("empty_db"),
             "351": db_path("351sqlitedb"),
             "bz17556": db_path("bz17556_backup_80")
            }

@step('I have (a|an|the) "(.*?)" miro db')
def reset_database(self, db):
    if db == "fresh": 
        world.config.set_def_db_and_prefs()
    else:
        world.config.replace_database(databases[db])

