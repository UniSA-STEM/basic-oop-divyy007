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
