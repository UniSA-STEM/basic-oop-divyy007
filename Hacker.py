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
    def __init__(self, name):
        self.__name = name
        self.__trace_level = 0
        self.__rig = None          # hacker can have one rig at a time
        self.__inventory = [Asset("CryptoToken", "Used to get a rig")]  # currency in inventory

    # getters
    def get_name(self):
        return self.__name

    def get_trace_level(self):
        return self.__trace_level

    def get_rig(self):
        return self.__rig

    def get_inventory(self):
        return self.__inventory
    # setters
    def set_name(self, name):
        self.__name = name

    def set_trace_level(self, level):
        self.__trace_level = level

    def set_rig(self, rig):
        self.__rig = rig

    # adds asset object to hacker's inventory
    def collect_asset(self, asset):
        self.__inventory.append(asset)
    
    # acquire a rig by using cryptotoken
    def acquire_rig(self):
      for asset in self.__inventory:
        if asset.get_name() == "CryptoToken":
            # acquire new rig
            new_rig = Rig(f"{self.__name} Rig")
            self.__rig = new_rig
            self.__inventory.remove(asset)  # remove the CryptoToken after use
            print(f"{self.__name} has acquired a new rig: {new_rig.get_name()}")
            return
        # if no cryptotoken found
        print(f"{self.__name} does not have a CryptoToken to acquire a rig.")

    # increases trace
    def increase_trace(self):
        self.__trace_level += 1
        if self.__trace_level >= 5:
            print(f"Warning: {self._name}'s trace is very high ({self._trace_level})!")

    # reduces trace
    def reduce_trace(self):
        if self.__trace_level > 0:
            self.__trace_level -= 1
        print(f"{self._name}'s trace level reduced to {self.__trace_level}")

    # launching attack data spikes
    def launch_attack(self, target):
        if not self.__rig:
            print(f"{self.__name} cannot launch an attack without a rig!")
            return
        if self.__trace>= 5:
            print(f"{self._name} cannot launch an attack with high trace level ({self._trace_level})!")
            return
        print(f"{self._name} is launching an attack on {target} using {self._rig.get_name()}!")
        if target.get_rig():
            target.get_rig().damage_rig()
        else:
            print(f"{target.get_name()} does not have a rig to attack.")
        self.__trace_level += 1
    
    #upgrading rig
    def upgrade_rig(self):
        if not self.__rig:
            print(f"{self.__name} has no rig to upgrade.")
            return
        for asset in self.__inventory:
            if asset.get_name() == "Hardware Patch":
                self.__inventory.remove(asset)
                self.__rig.upgrade()
                print(f"{self._name} upgraded {self._rig.get_name()} successfully!")
                return
        print(f"{self.__name} has no Hardware Patch in inventory.")