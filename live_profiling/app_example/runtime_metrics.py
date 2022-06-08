import json
import socket
import sys
from collections import deque
import time
import threading
import logging
from pathlib import Path


from waggle.plugin import Plugin


class profiler:

    def runTau(filename):
        if Path(filename).is_file():
            tau_python -ebs -T serial,python firstprime.py 
        else:
            print ("File not in directory")



    

    def runSystemProfile():


    def parseData():

        """ Parses the data from Tau and System Utilization sends to beehive via pywaggle """

