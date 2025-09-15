import os
import datetime

script_path = os.getcwd()
entries_path = os.path.join(script_path, "entries") 

if not os.path.exists(entries_path):
    os.mkdir(entries_path)
    print("entries folder has been created")
