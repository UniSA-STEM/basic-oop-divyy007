"""
File: main.py
Description: <Entry point for simulation>
Author: <Divyesh>
ID: <110449639>
Username: <divyy007>
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from Asset import Asset
from Rig import Rig
from Hacker import Hacker


print("INTO THE GRID")

# Create two hackers
hacker1 = Hacker("MRRobot")
hacker2 = Hacker("Heckler")

print("\n Initial Hacker Information")
print(hacker1)
print(hacker2)

# step 1- acquire rigs 
print("\n Step 1: Acquiring Rigs")
hacker1.acquire_rig()
hacker2.acquire_rig()

# Step 2: Add extra assets for testing
print("\n Step 2: Adding Assets")
hacker1.get_inventory().append(Asset("Hardware Patch", "Upgrade rigs."))
hacker1.get_inventory().append(Asset("Security Chip", "To encrypt or decrypt assets."))
hacker1.get_inventory().append(Asset("CryptoToken", "For repair."))
hacker2.get_inventory().append(Asset("Security Chip", "To encrypt or decrypt assets."))
