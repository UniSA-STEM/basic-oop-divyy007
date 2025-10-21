"""
File: Rig.py
Description: <Hacker's computer>
Author: <Divyesh>
ID: <110449639>
Username: <divyy007>
This is my own work as defined by the University's Academic Misconduct Policy.
"""

# class Rig with encapsulated attributes
class Rig:
    def __init__(self, name):
        self.__name = name
        self.__damage = 0
        self.__level = 0
        self.__broken = False
        self.__assets = []

    # getters
    def get_name(self):
        return self.__name

    def get_damage(self):
        return self.__damage

    def get_level(self):
        return self.__level

    def get_broken(self):
        return self.__broken

    def get_assets(self):
        return self.__assets

    # setters
    def set_name(self, name):
        self.__name = name

    def set_damage(self, damage):
        self.__damage = damage

    def set_level(self, level):
        self.__level = level

    def set_broken(self, status):
        self.__broken = status

    # increases rig's damage
    def damage_rig(self):
        self.__damage += 1
        if self.__damage >= 2 + self.__level:
            self.__broken = True

    # repairs rig
    def repair(self):
        if self.__broken:
            self.__damage = 0
            self.__broken = False

    # upgrades rig
    def upgrade(self):
        self.__level += 1

    # store an asset
    def store_asset(self, asset):
        self.__assets.append(asset)
    
    # displays current condition of rig
    def __str__(self):
        status = "Broken" if self.__broken else "Working"
        return f"{self.__name} [Level {self.__level}] - Status: {status}, Damage: {self.__damage}"