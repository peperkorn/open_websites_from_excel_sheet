#!/usr/bin/python3

import webbrowser
import time
import pandas as pd

import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()


filename_path = filedialog.askopenfilename()

tablename = ["Tabelle1", "Tabelle2", "Tabelle3"]

moretable = input("Searching for the following tablenames in excel sheet by default: " + str(tablename) +". Add additional tablename and hit 'enter' (otherwise just hit 'enter' to continue): ")
tablename.append(moretable)

columnname = ["Domain", "Website"]
morecolumn = input("Searching for the following coumnnames in excel sheet by default: " + str(columnname) +". Add additional columnname and hit 'enter' (otherwise just hit 'enter' to continue): ")
columnname.append(morecolumn)

for t in tablename:
	try:
		df = pd.read_excel (filename_path, t) 
	except:
		continue
	break	

browser = webbrowser.get("safari")

for c in columnname:
	try:
		url = df[c].tolist() 
	except:
		continue
	break


print(str(len(url)) + " URLs will be opened. :-D")

y = 10 

url2 = [url[i:i + y] for i in range(0, len(url), y)]

if len(url)%y == 0: 
	print(str(len(url2)) + " batches of " + str(y) + " in total.")
else:
	print(str(len(url2) - 1 ) + " batches of " + str(y) + " and one final batch of "   + str(len(url) - ((len(url2)-1)*y) )  +  " in total.")

for x in range(len(url2)):
	print(url2[x])
	print("Websites opening in webbrowser")
	for i in url2[x]:
		browser.open_new_tab(i)
		time.sleep(0.5)
	if len(url2) - (x+1) == 0:
		break
	else:
		print("still " + str(len(url2) - (x+1)) + " batches to go.")
	input("press 'enter' for next batch!")
print ("Ende!")
