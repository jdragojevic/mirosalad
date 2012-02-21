import os
import sys
from sikuli.Sikuli import *
os.chdir(os.path.join(os.getcwd(), 'tests.sikuli'))
sys.path.append(os.getcwd())
sys.path.append(os.path.join(os.getcwd(), 'lettuce'))
sys.path.append(os.path.join(os.getcwd(), 'features', 'terrain', 'myLib'))
import lettuce
lettuce.lettuce_cli.main()

