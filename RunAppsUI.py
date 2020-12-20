import tkinter as tk
import os
from tkinter import filedialog, Text, messagebox

appTitle = "Run Apps v1.2 by Paolo Patron"
savedFileName = "defaultapps.txt"
dirtouse = "/"
dirprogram = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs"

root = tk.Tk()
root.title(appTitle)

# This is where we store apps that:
# 1. Were currently selected.
# 2. Previously selected from defaultapps.txt.
selectedapps = []

# This section reads previously selected file names from defaultapps.txt.
if os.path.isfile(savedFileName):
    with open(savedFileName, 'r') as f:
        tempapps = f.read()
        tempapps = tempapps.split(',')
        selectedapps = [x for x in tempapps if x.strip()]


# This method creates labels for every file path in selectedapps
def createlabels():
    for selectedapp in selectedapps:
        label = tk.Label(filePathFrame, text=selectedapp)
        label.pack()


# This method does four things:
# 1. Destroys existing instances of widgets (or labels) in the frame.
# 2. Let's the user choose an app using the file dialog and stores the path of that app.
# 3. Adds the selected path to our selectedapps array for later use.
# 4. Calls createlabels() to displays file paths in our frame.
def addapp():
    if os.path.isfile(dirprogram):
        dirtouse = dirprogram

    filename = filedialog.askopenfilename(initialdir=dirtouse, title="Select File",
                                          filetypes=(("Executable files", "*.exe"), ("All files", "*./")))

    if filename not in selectedapps:
        for widget in filePathFrame.winfo_children():
            widget.destroy()

        selectedapps.append(filename)

        createlabels()
    else:
        messagebox.showerror(appTitle, "The file path already exist.")


# This method runs apps based on the selectedapp array.
def runapps():
    for selectedapp in selectedapps:
        os.startfile(selectedapp)

    # Saves selected apps into a 'defaultapps.txt' for reference later  when we run this Python app again.
    with open('defaultapps.txt', 'w') as f:
        for selectedapp in selectedapps:
            f.write(selectedapp + ',')

    exit(0)


# This method does the things:
# 1. Deletes the defaultapps.txt file.
# 2. Destroys existing instances of widgets (or labels) in the frame.
# 3. Clears the selectedapps array.
# 4. Shows an information message box.
def reset():
    if os.path.isfile(savedFileName):
        os.remove(savedFileName)

        for widget in filePathFrame.winfo_children():
            widget.destroy()

        selectedapps.clear()

        messagebox.showinfo(appTitle, "Reset was successful.")
    else:
        messagebox.showerror(appTitle, "No saved file found.")


# Generates a frame for the file paths.
filePathFrame = tk.Frame(root, bg="white", width=300)
filePathFrame.grid(row=0, column=0, sticky="N")

# Generates a frame for the buttons.
buttonFrame = tk.Frame(root, bg="white")
buttonFrame.grid(row=0, column=1)

# Creates initial labels for each app and displays it in our frame.
# This is done only once when we run this whole Python app.
createlabels()

# Creates a 'Select File Path' button for us to select an app.
selectFilePath = tk.Button(buttonFrame, text="Select File Path", width=15, fg="white", bg="#263D42", command=addapp)
selectFilePath.pack()

# Creates a 'Run All Apps' button so we can run apps that were selected simultaneously.
runAllApps = tk.Button(buttonFrame, text="Run All Apps", width=15, fg="white", bg="#263D42", command=runapps)
runAllApps.pack()

# Creates a 'Reset' button.
resetApps = tk.Button(buttonFrame, text="Reset", width=15, fg="white", bg="#263D42", command=reset)
resetApps.pack()

root.mainloop()