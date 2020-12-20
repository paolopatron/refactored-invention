import os
from tkinter import messagebox

appTitle = "Run Apps v1.1 by Paolo Patron"
selectedapps = []


def runapps():
    for selectedapp in selectedapps:
        os.startfile(selectedapp)

    exit(0)


if os.path.isfile(appTitle):
    with open(appTitle, 'r') as f:
        tempapps = f.read()
        tempapps = tempapps.split(',')
        selectedapps = [x for x in tempapps if x.strip()]

    runapps()
else:
    messagebox.showerror(appTitle, "No saved file found.")