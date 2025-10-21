"""
File: Hacker.py
Description: <Represents hacker>
Author: <Divyesh>
ID: <110449639>
Username: <divyy007>
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from rig import Rig
from asset import Asset

class Hacker:
    def init(self, name):
        self.__name = name
        self.__trace_level = 0
        self.__rig = None          # hacker can have one rig at a time
        self.__inventory = [Asset("CryptoToken", "Used to get a rig")]  # currency in inventory
