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

# Step 3: Upgrade Hacker1’s Rig
print("\nStep 3: Upgrading Rig")
hacker1.upgrade_rig()

# Step 4: Launch attacks from Hacker1 to Hacker2’s Rig
print("\nStep 4:Launch Attacks")
hacker1.launch_attack(hacker2)
hacker1.launch_attack(hacker2)

# Step 5: Check rig condition
print("\nStep 5: Rig Conditions")
print(hacker1.get_rig())
print(hacker2.get_rig())

# Step 6: Repair a broken rig using CryptoToken
print("\nStep 6: Repairing Rig")
hacker1.get_rig().repair()

# Step 7: Encrypt an asset in inventory
print("\nStep 7: Encrypting an Asset")
for asset in hacker1.get_inventory():
    if asset.get_name() == "CryptoToken":
        asset.set_isencrypted(True)
        print(f"{asset.get_name()} has been encrypted in inventory.")
        break
else:
    print("CryptoToken not found in inventory.")

# Step 8: Decrypt the asset back
print("\nStep 8: Decrypting the Asset")
for asset in hacker1.get_inventory():
    if asset.get_name() == "CryptoToken":
        asset.set_isencrypted(False)
        print(f"{asset.get_name()} has been decrypted in inventory.")
        break
else:
    print("CryptoToken not found in inventory.")