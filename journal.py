import datetime
import os

script_path = os.getcwd()
entries_path = os.path.join(script_path, "entries") 

def ensure_entries_dir():
    if not os.path.exists(entries_path):
        os.mkdir(entries_path)
        print("entries folder has been created")

def today_filename():
    return str(datetime.date.today()) + ".txt"

def ensure_today_entry():
    today_entry = os.path.join(entries_path, today_filename())
    if not os.path.exists(today_entry):
        flags = os.O_CREAT | os.O_RDWR | os.O_APPEND
        mode = 0o600
        fd = os.open(today_entry, flags, mode)
        os.close(fd)
        print("today's entry has been created")
    return today_entry

def write_to_entry(path):
    while True:
        flags = os.O_RDWR | os.O_APPEND
        fd = os.open(path, flags)
        user_input = input("type to the entry: ")
        if user_input == ":q":
            print("exiting write mode")
            break
        os.write(fd, (user_input + "\n").encode("utf-8"))
        os.close(fd)
    
def read_choice(choice_entry):
    flags = os.O_RDONLY
    fd = os.open(choice_entry, flags)
    content = os.read(fd, 1024).decode()
    print(content)

def prompt_main():
    print("\nWelcome to journal!")
    print(" W - write")
    print(" R - read")
    print(" Q - quit")
    return input("Choice (W/R/Q): ").strip().upper()

def show_entries():
    entries = os.listdir(entries_path)
    print(entries) 

def main():
    ensure_entries_dir()
    today = ensure_today_entry() 
    
    while True:
        choice = prompt_main()

        if choice == "W":
            write_to_entry(today)

        elif choice == "R":
            show_entries() 
            user_choice = input("type in the entry you want to read: \n")
            read_choice(os.path.join(entries_path, user_choice))

        elif choice == "Q":
            break

main()
