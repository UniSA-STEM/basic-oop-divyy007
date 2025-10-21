"""
File: Rig.py
Description: <Hacker's computer>
Author: <Divyesh>
ID: <110449639>
Username: <divyy007>
This is my own work as defined by the University's Academic Misconduct Policy.
"""
class Rig:
    def __init__(self, name):
        self.__name = name
        self.__damage = 0
        self.__level = 0
        self.__broken = False
        self.__store_asset = []

    def get_name(self):
        return self.__name

    def get_damage(self):
        return self.__damage

    def get_level(self):
        return self.__level

    def get_broken(self):
        return self.__broken

    def get_assets(self):
        return self.__store_asset