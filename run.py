#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

import os

DESU_PATH = os.path.dirname(os.path.abspath(__file__))
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] =  DESU_PATH + "/Glamour-66c3d59d0a86.json"
os.system("./interface.py")