import json
import socket
import sys
from collections import deque
import time
import threading
import logging
import subprocess
from pathlib import Path
from waggle.plugin import Plugin
from jtop import jtop


def get_container_memory() -> int:
    """ Returns the memory usage of the container that this script is running in. """
    return int(open("/sys/fs/cgroup/memory/memory.usage_in_bytes").readline()[:-1])

class profiler:
    def __init__(self, filename, socket_path="/var/run/docker.sock"):

        """
        Init server with a dictionary of
            {metric_name: METRIC_TYPE}
        and host at the default socket path (unless otherwise specified as a str)
        """

        self.metric = {"ram_usage": []}
        self.filename = filename

        self.socket_path = socket_path
        self.socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self.connect_to_metrics_socket()

        self.server_thread = threading.Thread(target=self.runSystemProfile)
        self.server_thread.start()

    def connect_to_metrics_socket(self):
        """
        Block until the server connects to the metrics socket. NOTE: this file must be shared with the Docker container
        that this script runs inside.
        """
        self.socket.connect(self.socket_path)

    def runTau(self):
        """ Provided Tau is installed in docker container this function will run Tau on the file to profile"""

        if Path(self.filename).is_file():
            cmd = "tau_python"
            temp = subprocess.Popen(
                "tau_python -ebs -T serial,python firstprime.py", shell=True, stdout=subprocess.PIPE
            )
            print(str(temp.communicate()))
        else:
            print("Cannot run Tau because ", self.filename, " not in directory")

    def runSystemProfile(self):
        """ This function looks for the Tau subprocess
            and records system utilization.
        """

        ## code reuse from luke's code
        report_cycle = 0
        while True:
            time.sleep(0.5)  # A little delay so that this thread doesn't fry the CPU

            # Every half-second report RAM usage of the currently-running container
            if report_cycle % 5 == 0:
                self.metric["ram_usage"].append(get_container_memory())
            report_cycle += 1
            print(self.metric)


    def run_tegrastats(self):

        print("Simple jtop reader")

        with jtop() as jetson:
            # jetson.ok() will provide the proper update frequency
            while jetson.ok():
                # Read tegra stats
                print(jetson.stats)

    # def parseData():

    #     """ Parses the data from Tau and System Utilization
    #         sends to beehive via pywaggle
    #     """


### 1 - run tau ??
### 2 - run captures system utilization while profiling
### 3 - parse data
