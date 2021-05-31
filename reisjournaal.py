import tkinter as tk
from tkinter import *
from tkinter import ttk
import time

'''
version 1.1.1

additional info:
Some dutch words are translated
Kmr ### are the mile-markers, kilometer-markers along the river Rhine

be kind, keep it simple because im not ready for __INIT__ stuff.
No clue what that does.

'''

def startStopSwitch(buttonName, distance, stamp1, stamp2):
    global start_time_var
    global start_stop_button_list
    
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
    for i in start_stop_button_list:
        if i is not active_button:
            i['state'] = DISABLED

def enableOtherButtons(active_button):
    for i in start_stop_button_list:
        if i is not active_button and i['text'] == "Start":
            i['state'] = NORMAL

def enableVoyButtons(event):
    for i in special_character_butt_ls:
        i['state'] = NORMAL

def disableVoyButtons(event):
    for i in special_character_butt_ls:
        i['state'] = DISABLED

def buttonPress(button_pressd):
    print(button_pressd['text'])
        
### global variables ###
start_time_var = 0
start_stop_button_list = []
special_character_butt_ls = []
allNumpad_character_ls = []


# Main application window
root = Tk()
root.title("Journaal")

# Main Frame
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1, minsize=5)
root.rowconfigure(0, weight=1, minsize=5)
root.minsize(width=800, height=450)

# voyage details frame
voyage_labelFrame = ttk.Labelframe(mainframe, text='Reis gegevens') #Reis gegevens = Voyage Details
voyage_labelFrame.grid(column=0, row=0, columnspan=1, rowspan=4)

# speed table frame
sector_labelFrame = ttk.Labelframe(mainframe, text='Rivier gedeelten') #Rivier gedeelten = River sectors
sector_labelFrame.grid(column=0, row=8, columnspan=5)

# numpad frame
numpad_labelFrame = ttk.Labelframe(mainframe, text='Toetsen') # Toetsen = Buttons
numpad_labelFrame.grid(column=6, row=0, rowspan=6)

# Mainframe text
ttk.Label(voyage_labelFrame, text="Reisnummer #").grid(column=1, row=1, sticky=(W, E))
                                    # Reisnummer = Voyage Number
ttk.Label(voyage_labelFrame, text="Tonnage").grid(column=1, row=2, sticky=(W, E))
                                    # Tonnage = Net Weight
ttk.Label(voyage_labelFrame, text="Diepgang").grid(column=3, row=1, sticky=(W, E))
                                    # Diepgang = Draught
ttk.Label(voyage_labelFrame, text="Pegel Kaub").grid(column=3, row=2, sticky=(W, E))
                                    # Pegel Kaub = River level at the town called Kaub
ttk.Label(voyage_labelFrame, text="Gemiddelde snelheid:").grid(column=5, row=1, sticky=(W, E))
                                    # Gemiddelde snelheid = Average speed
average_voyage_speed = ttk.Label(voyage_labelFrame, text="speed")
average_voyage_speed.grid(column=6, row=1, sticky=(W, E))

# textboxes
'voyage number'
voyNumber = StringVar()
voyNumber_Entry = ttk.Entry(voyage_labelFrame, width=10, textvariable=voyNumber)
voyNumber_Entry.grid(column=2, row=1, sticky=(W, E))
'voyage tonnage'
voyTonCou = StringVar()
voyTonCou_Entry = ttk.Entry(voyage_labelFrame, width=10, textvariable=voyTonCou)
voyTonCou_Entry.grid(column=2, row=2, sticky=(W, E))
'voyage draught'
voyDraugh = StringVar()
voyDraugh_Entry = ttk.Entry(voyage_labelFrame, width=10, textvariable=voyDraugh)
voyDraugh_Entry.grid(column=4, row=1, sticky=(W, E))
'voyage river level'
voyPegKau = StringVar()
voyPegKau_Entry = ttk.Entry(voyage_labelFrame, width=10, textvariable=voyPegKau)
voyPegKau_Entry.grid(column=4, row=2, sticky=(W, E))


## sector table ##

# table header
ttk.Label(sector_labelFrame, text="Begin", width=10).grid(column=2, row=0, sticky=(W, E)) 
ttk.Label(sector_labelFrame, text="Eind", width=10).grid(column=4, row=0, sticky=(W, E)) # Eind = end
ttk.Label(sector_labelFrame, text="Meten", width=5).grid(column=5, row=0, sticky=(W, E)) # Meten = measures

#Sector 1 Lobith - Duisburg
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
start_stop_button_list.append(button_s1)

#Sector 2 Duisburg - Düsseldorf
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
start_stop_button_list.append(button_s2)

#Sector 3 Düsseldorf - Cologne
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
start_stop_button_list.append(button_s3)

### numpad buttons (voyage number examples: ALS2102T, 1RT2114T, 2RT2114B, ALS2103B) ###

#first 3 characters for a voyage towards or from Antwerp
button_ALS = ttk.Button(numpad_labelFrame, text="ALS", state=DISABLED \
                        , command=lambda: buttonPress(button_ALS))
button_ALS.grid(column=1, row=1, sticky=(W, E))
special_character_butt_ls.append(button_ALS)
#first 2 characters for a voyage towards or from Rotterdam
button_RT = ttk.Button(numpad_labelFrame, text="RT", state=DISABLED \
                       , command=lambda: buttonPress(button_RT))
button_RT.grid(column=2, row=1, sticky=(W, E))
special_character_butt_ls.append(button_RT)
#Last character in voyage number for designating a trip towards the ocean
button_T = ttk.Button(numpad_labelFrame, text="T", state=DISABLED \
                      , command=lambda: buttonPress(button_T))
button_T.grid(column=1, row=2, sticky=(W, E))
special_character_butt_ls.append(button_T)
#Last character in voyage number for designating a trip towards Basel, CH
button_B = ttk.Button(numpad_labelFrame, text="B", state=DISABLED \
                      , command=lambda: buttonPress(button_B))
button_B.grid(column=2, row=2, sticky=(W, E))
special_character_butt_ls.append(button_B)
#auto calculate voyage number ( YYWW )
button_YYWW = ttk.Button(numpad_labelFrame, text="Reis#", state=DISABLED)
button_YYWW.grid(column=3, row=1, sticky=(W, E))
special_character_butt_ls.append(button_YYWW)

#To remove mistakes
button_DEL = ttk.Button(numpad_labelFrame, text="DEL")
button_DEL.grid(column=3, row=2, sticky=(W, E))

button_0 = ttk.Button(numpad_labelFrame, text="0", \
                      command=lambda: buttonPress(button_0))
button_0.grid(column=2, row=6, sticky=(W, E))
allNumpad_character_ls.append(button_0)
button_1 = ttk.Button(numpad_labelFrame, text="1", \
                      command=lambda: buttonPress(button_1))
button_1.grid(column=1, row=5, sticky=(W, E))
allNumpad_character_ls.append(button_1)
button_2 = ttk.Button(numpad_labelFrame, text="2", \
                      command=lambda: buttonPress(button_2))
button_2.grid(column=2, row=5, sticky=(W, E))
allNumpad_character_ls.append(button_2)
button_3 = ttk.Button(numpad_labelFrame, text="3", \
                      command=lambda: buttonPress(button_3))
button_3.grid(column=3, row=5, sticky=(W, E))
allNumpad_character_ls.append(button_3)
button_4 = ttk.Button(numpad_labelFrame, text="4", \
                      command=lambda: buttonPress(button_4))
button_4.grid(column=1, row=4, sticky=(W, E))
allNumpad_character_ls.append(button_4)
button_5 = ttk.Button(numpad_labelFrame, text="5", \
                      command=lambda: buttonPress(button_5))
button_5.grid(column=2, row=4, sticky=(W, E))
allNumpad_character_ls.append(button_5)
button_6 = ttk.Button(numpad_labelFrame, text="6", \
                      command=lambda: buttonPress(button_6))
button_6.grid(column=3, row=4, sticky=(W, E))
allNumpad_character_ls.append(button_6)
button_7 = ttk.Button(numpad_labelFrame, text="7", \
                      command=lambda: buttonPress(button_7))
button_7.grid(column=1, row=3, sticky=(W, E))
allNumpad_character_ls.append(button_7)
button_8 = ttk.Button(numpad_labelFrame, text="8", \
                      command=lambda: buttonPress(button_8))
button_8.grid(column=2, row=3, sticky=(W, E))
allNumpad_character_ls.append(button_8)
button_9 = ttk.Button(numpad_labelFrame, text="9", \
                      command=lambda: buttonPress(button_9))
button_9.grid(column=3, row=3, sticky=(W, E))
allNumpad_character_ls.append(button_9)


# padding
for child in mainframe.winfo_children():
    child.grid_configure(padx=3, pady=1)
voyNumber_Entry.focus()

voyNumber_Entry.bind("<FocusIn>", enableVoyButtons)
voyNumber_Entry.bind("<FocusOut>", disableVoyButtons)

root.mainloop()
