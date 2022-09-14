# multiclipboard.py
# inspired by Tech With Tim
# https://www.youtube.com/watch?v=Oz3W-LKfafE

import sys, json, pyperclip

SAVED_DATA_FILE = 'clipboard.json'

def save_data(data: dict) -> None:
    global SAVED_DATA_FILE
    try:
        with open(SAVED_DATA_FILE, 'wb') as fh:
            fh.write(json.dumps(data).encode())
    except OSError as e:
        print("Could not saved data")
        print(e)

def load_data() -> dict:
    global SAVED_DATA_FILE
    try:
        with open(SAVED_DATA_FILE, 'rb') as fh:
            return json.loads(fh.read())
    except:
        return {}

def usage() -> None:
    print(f"usage: {sys.argv[0]} <commmand> [key]\n")
    print("available commands:")
    print("  save - save data from clipboard")
    print("  load - load data to clipboard")
    print("  list - list saved clipboard data")
    print("  delete - delete data")


if not len(sys.argv[1:]):
    usage()
else:
    data = load_data()
    command = sys.argv[1]
    if command not in ('save', 'load', 'list', 'delete'):
        usage()
    else:
        if command == 'list':
            for k, v in data.items():
                print(f"{k}: {v}")
            quit()
        if len(sys.argv[2:]):
            key = sys.argv[2]
        else:
            key = input("Enter a key: ")
        if command == 'save':
            data[key] = pyperclip.paste()
            save_data(data)
            print(f"Data saved under a key '{key}' in file '{SAVED_DATA_FILE}'")
        elif command == 'load':
            if key in data:
                pyperclip.copy(data[key])
                print("Data copied to clipboard")
            else:
                print(f"Key '{key}' does not exist in multiclipboard")
        elif command == 'delete':
            if key in data:
                del data[key]
            save_data(data)
            print(f"Data under key '{key}' deleted")
