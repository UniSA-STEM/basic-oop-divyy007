"""
File: Asset.py
Description: <Digital Asset>
Author: <Divyesh>
ID: <110449639>
Username: <divyy007>
This is my own work as defined by the University's Academic Misconduct Policy.
"""

# creating class and encapsulating attributes
class Asset:
    def __init__(self, name, description):
        self.__name = name
        self.__description = description
        self.__isencrypted = False #default

    # getters
    def get_name(self):
        return self.__name

    def get_description(self):
        return self.__description

    def get_isencrypted(self):
        return self.__isencrypted
    
    # setters
    def set_name(self, name):
        self.__name = name

    def set_description(self, description):
        self.__description = description

    def set_isencrypted(self, status):
        self.__isencrypted = status
 