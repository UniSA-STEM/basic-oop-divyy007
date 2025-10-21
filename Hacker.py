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

    #getters
    def get_name(self):
        return self.__name

    def get_trace_level(self):
        return self.__trace_level

    def get_rig(self):
        return self.__rig

    def get_inventory(self):
        return self.__inventory
    #setters
    def set_name(self, name):
        self.__name = name

    def set_trace_level(self, level):
        self.__trace_level = level

    def set_rig(self, rig):
        self.__rig = rig