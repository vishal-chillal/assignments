#!/usr/bin/python

import logging
import sys
def class Logger():
    def __init__(self, log_level = logging.DEBUG):
        self.logger = = logging.getLogger()
        self.root.setLevel(log_level)

ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
root.addHandler(ch)
