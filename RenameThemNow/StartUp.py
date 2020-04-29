import os, sys

from tkinter.filedialog import askopenfilename
filename = askopenfilename()

directory = os.getcwd() + "\\RenameThemNow\\"
first_name = "first.txt"
first_file = directory + first_name
disired_name = "itworks.txt"
rename_it_to = directory + disired_name


print("start")
#rename_thingy = os.rename(first_file,rename_it_to)
print("end")

