# Author : Rouxhero
import tkinter as tk
from tkinter import filedialog
import requests

def ask_path():
    path = filedialog.askdirectory()
    return path

def install(install,synch):
    # Download main from github:
    # https://raw.githubusercontent.com/Rouxhero/PySync/master/main.py
    # and put it in the installation directory
    # Create a shortcut to the main.py file in the Desktop
    # Open the synch directory
    # Done
    url = "https://raw.githubusercontent.com/Rouxhero/PySync/master/main.py"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)',
    }
    r = requests.get(url,headers=headers)
    with open(install+"/main.py","w") as f:
        f.write(r.text.replace("'#path#'",synch))
    # Create a shortcut to the main.py file in the Desktop
    with open(install+"/PySync.lnk","w") as f:
        f.write("[InternetShortcut]\nURL=file:///"+install+"/main.py")
    # Done
    print("Done !")








if __name__ == '__main__' :
    # Ask for instalation directory with tk
    print("Installation dir :",end="")
    installation_dir = ask_path()
    print(installation_dir)
    # Ask for synch directory with tk
    print("Synch dir :",end="")
    synch_dir = ask_path()
    print(synch_dir)
    install(installation_dir,synch_dir)







