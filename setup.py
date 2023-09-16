# Author : Rouxhero
import tkinter as tk
from tkinter import filedialog
import requests


def ask_path():
    path = filedialog.askdirectory()
    return path


def write(path, content):
    with open(path, "w") as f:
        f.write(content)


def install(install, synch):
    # Download main from github:
    # https://raw.githubusercontent.com/Rouxhero/PySync/master/main.py
    # and put it in the installation directory
    # Create a shortcut to the main.py file in the Desktop
    # Open the synch directory
    # Done
    url = "https://raw.githubusercontent.com/Rouxhero/PySync/master/main.py"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64)",
    }
    r = requests.get(url, headers=headers)
    write(install + "/main.py", r.text.replace("'#path#'", synch))
    write(install + "/PySync.bat", "py " + install + "/main.py")
    write(
        install + "/PySync.lnk",
        "[InternetShortcut]\nURL=file:///" + install + "/PySync.bat",
    )
    print("Done !")


if __name__ == "__main__":
    # Ask for instalation directory with tk
    print("Installation dir :", end="")
    installation_dir = ask_path()
    print(installation_dir)
    # Ask for synch directory with tk
    print("Synch dir :", end="")
    synch_dir = ask_path()
    print(synch_dir)
    install(installation_dir, synch_dir)
