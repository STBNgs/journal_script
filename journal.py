import os
import datetime

script_path = os.getcwd()
entries_path = os.path.join(script_path, "entries") 

if not os.path.exists(entries_path):
    os.mkdir(entries_path)
    print("entries folder has been created")

today = str(datetime.date.today())
today_entry = os.path.join(entries_path, today + ".txt")

if not os.path.exists(today_entry):
    flags = os.O_CREAT | os.O_RDWR | os.O_APPEND
    mode = 0o600
    fd = os.open(today_entry, flags, mode)
    os.close(fd)
    print("today's entry has been created")


def write_to_entry():
    flags = os.O_RDWR | os.O_APPEND
    fd = os.open(today_entry, flags)
    user_input = input("type to the entry: ")
    os.write(fd, (user_input + "\n").encode("utf-8"))
    os.close(fd)

def read_entry():
    flags = os.O_RDONLY
    fd = os.open(today_entry, flags)
    content = os.read(fd, 1024).decode()
    print(content)

read_entry()
