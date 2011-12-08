import os
import sys
from sikuli.Sikuli import *
sys.path.append(os.path.join(os.getcwd(), lettuce))
import lettuce
newdir = os.path.join(os.getcwd(), 'tests.sikuli')
os.chdir(newdir)
lettuce.lettuce_cli.main()



    
    







