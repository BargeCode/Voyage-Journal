import tkinter as tk
from tkinter import *
from tkinter import ttk
import time

'version 1.1.1. first rework into tkinter'
'GUI works'
'Speed calculator works'
'''to - do'''
#numpad
#save to CSV


def startStopSwitch(buttonName, distance, stamp1, stamp2):
    global start_time_var
    global button_list
    
    if buttonName['text'] == "Start" and stamp1['text'] == "":
        start_time_var = time.time() #save start time
        stamp1['text'] = time.strftime('%H:%M %d-%m-%Y') # show start time
        buttonName['text'] = "Stop"
        disableOtherButtons(buttonName)
        
    elif buttonName['text'] == "Stop" and not stamp1['text'] == "":
        stamp2['text'] = time.strftime('%H:%M %d-%m-%Y') # show stop tome
        speed = calculateSpeed(start_time_var, distance)
        buttonName['text'] = speed + " Km/h" # show speed
        buttonName['state'] = DISABLED
        enableOtherButtons(buttonName)
        
def calculateSpeed(start_time, distance):
    timePassed = time.time() - start_time_var
    timePassed = timePassed / 60 / 60 # turn seconds into hours (i believe, not sure)
    speed = "{:.2f}".format(distance/timePassed) # divide distance by hours and set the format
    return speed

def disableOtherButtons(active_button):
    for i in button_list:
        if i is not active_button:
            i['state'] = DISABLED

def enableOtherButtons(active_button):
    for i in button_list:
        if i is not active_button and i['text'] == "Start":
            i['state'] = ACTIVE
        
### global variables ###
start_time_var = 0
button_list = []

# Main application window
root = Tk()
root.title("Journaal")

# Main Frame
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1, minsize=10)
root.rowconfigure(0, weight=1, minsize=10)
root.minsize(width=800, height=450)


# speed table frame
sector_labelFrame = ttk.Labelframe(mainframe, text='Rivier gedeelten')
sector_labelFrame.grid(column=1, row=5, columnspan=5)

# numpad frame
numpad_labelFrame = ttk.Labelframe(mainframe, text='Toetsen')
numpad_labelFrame.grid(column=6, row=2, rowspan=6)

# Mainframe text
'header'
ttk.Label(mainframe, text="Reisgegevens").grid(column=1, row=0, sticky=(W, E))
'sub header'
ttk.Label(mainframe, text="Reisnummer #").grid(column=1, row=1, sticky=(W, E))
ttk.Label(mainframe, text="Tonnage").grid(column=1, row=2, sticky=(W, E))
ttk.Label(mainframe, text="Diepgang").grid(column=3, row=1, sticky=(W, E))
ttk.Label(mainframe, text="Pegel Kaub").grid(column=3, row=2, sticky=(W, E))

# textboxes
'voyage number'
voyNumber = StringVar()
voyNumber_Entry = ttk.Entry(mainframe, width=10, textvariable=voyNumber)
voyNumber_Entry.grid(column=2, row=1, sticky=(W, E))
'voyage tonnage'
voyTonCou = StringVar()
voyTonCou_Entry = ttk.Entry(mainframe, width=10, textvariable=voyTonCou)
voyTonCou_Entry.grid(column=2, row=2, sticky=(W, E))
'voyage draught'
voyDraugh = StringVar()
voyDraugh_Entry = ttk.Entry(mainframe, width=10, textvariable=voyDraugh)
voyDraugh_Entry.grid(column=4, row=1, sticky=(W, E))
'voyage river level'
voyPegKau = StringVar()
voyPegKau_Entry = ttk.Entry(mainframe, width=10, textvariable=voyPegKau)
voyPegKau_Entry.grid(column=4, row=2, sticky=(W, E))


## sector table ##

# table header
ttk.Label(sector_labelFrame, text="Begin", width=10).grid(column=2, row=0, sticky=(W, E))
ttk.Label(sector_labelFrame, text="Eind", width=10).grid(column=4, row=0, sticky=(W, E))
ttk.Label(sector_labelFrame, text="Meten", width=5).grid(column=5, row=0, sticky=(W, E))

#Sector 1
'fixed'
ttk.Label(sector_labelFrame, text="Kmr 855 (Lobith)").grid(column=1, row=1, sticky=(W, E))
ttk.Label(sector_labelFrame, text="Kmr 777 (Duisburg)").grid(column=3, row=1, sticky=(W, E))
'results'
time_stampS1 = ttk.Label(sector_labelFrame, text="")
time_stampS1.grid(column=2, row=1, sticky=(W, E))
time_stampE1 = ttk.Label(sector_labelFrame, text="")
time_stampE1.grid(column=4, row=1, sticky=(W, E))
'var'
sector1_size = 78
'button'
button_s1 = ttk.Button(sector_labelFrame, text="Start", command=lambda: \
                       startStopSwitch(button_s1, sector1_size, time_stampS1, time_stampE1))
button_s1.grid(column=5, row=1, sticky=(W, E))
button_list.append(button_s1)

#Sector 2
'fixed'
ttk.Label(sector_labelFrame, text="Kmr 777 (Duisburg)").grid(column=1, row=2, sticky=(W, E))
ttk.Label(sector_labelFrame, text="Kmr 742 (Düsseldorf)").grid(column=3, row=2, sticky=(W, E))
'results'
time_stampS2 = ttk.Label(sector_labelFrame, text="")
time_stampS2.grid(column=2, row=2, sticky=(W, E))
time_stampE2 = ttk.Label(sector_labelFrame, text="")
time_stampE2.grid(column=4, row=2, sticky=(W, E))
'var'
sector2_size = 35
'button'
button_s2 = ttk.Button(sector_labelFrame, text="Start", command=lambda: \
                       startStopSwitch(button_s2, sector2_size, time_stampS2, time_stampE2))
button_s2.grid(column=5, row=2, sticky=(W, E))
button_list.append(button_s2)

#Sector 3
'fixed'
ttk.Label(sector_labelFrame, text="Kmr 742 (Düsseldorf)").grid(column=1, row=3, sticky=(W, E))
ttk.Label(sector_labelFrame, text="Kmr 690 (Keulen)").grid(column=3, row=3, sticky=(W, E))
'results'
time_stampS3 = ttk.Label(sector_labelFrame, text="")
time_stampS3.grid(column=2, row=3, sticky=(W, E))
time_stampE3 = ttk.Label(sector_labelFrame, text="")
time_stampE3.grid(column=4, row=3, sticky=(W, E))
'var'
sector3_size = 52
'button'
button_s3 = ttk.Button(sector_labelFrame, text="Start", command=lambda: \
                       startStopSwitch(button_s3, sector3_size, time_stampS3, time_stampE3))
button_s3.grid(column=5, row=3, sticky=(W, E))
button_list.append(button_s3)


#numpad
button_ALS = ttk.Button(numpad_labelFrame, text="ALS").grid(column=1, row=1, sticky=(W, E))
button_RT = ttk.Button(numpad_labelFrame, text="RT").grid(column=2, row=1, sticky=(W, E))
button_T = ttk.Button(numpad_labelFrame, text="T").grid(column=1, row=2, sticky=(W, E))
button_B = ttk.Button(numpad_labelFrame, text="B").grid(column=2, row=2, sticky=(W, E))
button_0 = ttk.Button(numpad_labelFrame, text="0").grid(column=2, row=6, sticky=(W, E))
button_1 = ttk.Button(numpad_labelFrame, text="1").grid(column=1, row=5, sticky=(W, E))
button_2 = ttk.Button(numpad_labelFrame, text="2").grid(column=2, row=5, sticky=(W, E))
button_3 = ttk.Button(numpad_labelFrame, text="3").grid(column=3, row=5, sticky=(W, E))
button_4 = ttk.Button(numpad_labelFrame, text="4").grid(column=1, row=4, sticky=(W, E))
button_5 = ttk.Button(numpad_labelFrame, text="5").grid(column=2, row=4, sticky=(W, E))
button_6 = ttk.Button(numpad_labelFrame, text="6").grid(column=3, row=4, sticky=(W, E))
button_7 = ttk.Button(numpad_labelFrame, text="7").grid(column=1, row=3, sticky=(W, E))
button_8 = ttk.Button(numpad_labelFrame, text="8").grid(column=2, row=3, sticky=(W, E))
button_9 = ttk.Button(numpad_labelFrame, text="9").grid(column=3, row=3, sticky=(W, E))

# padding
for child in mainframe.winfo_children():
    child.grid_configure(padx=3, pady=1)
voyNumber_Entry.focus()

#pressing enter does:
'root.bind("<Return>", selectNext)'


root.mainloop()
