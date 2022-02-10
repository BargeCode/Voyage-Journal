from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import time
import datetime
import statistics
'''
version 1.1.1

additional info:
Some dutch words are translated
Kmr ### are the mile-markers, kilometer-markers along the river Rhine

be kind, keep it simple because ive got no idea for __INIT__ stuff
does.
No clue what that does.

'''


def start_stop_switch(button_name, distance, stamp1, stamp2, sector, entry):
    global start_time_var
    global start_stop_button_ls
    if button_name['text'] == "Start" and stamp1['text'] == "":
        start_time_var = time.time()  # save start time
        stamp1['text'] = time.strftime('%H:%M %d-%m-%Y')  # show start time
        button_name['text'] = "Stop"
        disable_other_buttons(button_name)
    elif button_name['text'] == "Stop" and not stamp1['text'] == "":
        if len(entry.get()) != 0:
            stamp2['text'] = time.strftime('%H:%M %d-%m-%Y')  # show stop tome
            speed = calculate_speed(start_time_var, distance)
            button_name['text'] = speed + " Km/h"  # Show speed
            button_name['state'] = DISABLED
            enable_other_buttons(button_name)
            sector_ls.append(sector)
            sector_rpm_ls.append(entry.get())
            entry['state'] = DISABLED
        else:
            messagebox.showerror("UH-OH", "Geen toeren ingevuld")


def calculate_speed(start_time, distance):
    time_passed = time.time() - start_time_var
    time_passed = time_passed / 60 / 60  # Turn seconds into hours (not sure)
    speed = "{:.2f}".format(distance/time_passed)  # Distance/hrs set format
    average_speed_ls.append(float(speed))
    if len(average_speed_ls) != "":  # Adding avg speed for each sector to ls.
        overal_average = statistics.mean(average_speed_ls)
        average_voyage_speed['text'] = "{:.2f}".format(overal_average)\
            + " Km/h"
    return speed


def disable_other_buttons(active_button):
    for i in start_stop_button_ls:
        if i is not active_button:
            i['state'] = DISABLED


def enable_other_buttons(active_button):
    for i in start_stop_button_ls:
        if i is not active_button and i['text'] == "Start":
            i['state'] = NORMAL


def enable_voy_buttons(event):
    for i in special_character_butt_ls:
        i['state'] = NORMAL


def disable_voy_buttons(event):
    for i in special_character_butt_ls:
        i['state'] = DISABLED


def button_press(button_pressd):
    entry = root.focus_get()  # to see which box was active
    if button_pressd['text'] == "DEL":
        entry.delete(0, END)
    elif button_pressd['text'] == "Reis#":
        current_date = datetime.date.today()
        current_week = current_date.isocalendar()[1]
        current_year = current_date.isocalendar()[0]
        entry.insert("end", str(current_year)[-2:] + str(current_week))
    else:
        entry.insert("end", button_pressd['text'])


def save_voyage(entry_list):
    voyage_save_file = open("voyage logs" + ".csv", "a")
    data_ls = compile_save_file(entry_list)
    for i in data_ls:
        voyage_save_file.write(str(i))
    voyage_save_file.close()


def compile_save_file(entry_list):
    result_list = []
    for i in average_speed_ls:
        for j in entry_list:
            result_list.append(str(j.get()))
            result_list.append(", ")  # entry's
        result_list.append(str(i))  # speed
        result_list.append(", ")
        index = average_speed_ls.index(i)
        result_list.append(sector_rpm_ls[index])
        result_list.append(", ")
        result_list.append(sector_ls[index])
        result_list.append(",\n")  # new line
    return result_list


def key_bind(event):
    global all_entry_ls
    save_voyage(all_entry_ls)


# global variables
start_time_var = 0
sector = 0
start_stop_button_ls = []
special_character_butt_ls = []
all_numpad_character_ls = []
average_speed_ls = []
sector_ls = []
all_entry_ls = []
data_ls = []
sector_rpm_ls = []

# Main application window
root = Tk()
root.title("Journaal")


# Main Frame
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1, minsize=5)
root.rowconfigure(0, weight=1, minsize=5)
root.minsize(width=795, height=410)
root.maxsize(width=795, height=410)


# voyage details frame
voyage_labelFrame = ttk.Labelframe(mainframe, text='Reis gegevens')
'Reis gegevens = Voyage Details'
voyage_labelFrame.grid(column=0, row=0, columnspan=6, rowspan=2, sticky=(N, E))

# speed table frame
sector_labelFrame = ttk.Labelframe(mainframe, text='Rivier gedeelten')
'Rivier gedeelten = River sectors'
sector_labelFrame.grid(column=0, row=7, columnspan=10, sticky=(W))
sector_labelFrame.configure(borderwidth=2, relief=SUNKEN)

# numpad frame
numpad_labelFrame = ttk.Labelframe(mainframe, text='Toetsen')
'Toetsen = Buttons'
numpad_labelFrame.grid(column=6, row=0, rowspan=7, sticky=(N, E))

# Mainframe text
'Reisnummer = Voyage Number'
ttk.Label(voyage_labelFrame, text="Reisnummer #").grid(column=1, row=1,
                                                       sticky=(W, E))

'Tonnage = Net Weight'
ttk.Label(voyage_labelFrame, text="Tonnage").grid(column=1, row=2,
                                                  sticky=(W, E))

'Diepgang = Draught'
ttk.Label(voyage_labelFrame, text="Diepgang").grid(column=3, row=1,
                                                   sticky=(W, E))

'Pegel Kaub = River level at the town called Kaub'
ttk.Label(voyage_labelFrame, text="Pegel Kaub").grid(column=3, row=2,
                                                     sticky=(W, E))

'Gemiddelde snelheid = Average speed'
ttk.Label(voyage_labelFrame, text="Gemiddelde snelheid:").grid(column=5, row=1,
                                                               sticky=(W, E))

average_voyage_speed = ttk.Label(voyage_labelFrame, text="")
average_voyage_speed.grid(column=5, row=2, sticky=(W, E))


# textboxes
'voyage number'
voy_number = StringVar()
voy_number_entry = ttk.Entry(voyage_labelFrame, width=10,
                             textvariable=voy_number)
voy_number_entry.grid(column=2, row=1, sticky=(W, E))
all_entry_ls.append(voy_number_entry)
'voyage tonnage'
voy_ton_cou = StringVar()
voy_ton_cou_entry = ttk.Entry(voyage_labelFrame, width=10,
                              textvariable=voy_ton_cou)
voy_ton_cou_entry.grid(column=2, row=2, sticky=(W, E))
all_entry_ls.append(voy_ton_cou_entry)
'voyage draught'
voy_draugh = StringVar()
voy_draugh_entry = ttk.Entry(voyage_labelFrame, width=10,
                             textvariable=voy_draugh)
voy_draugh_entry.grid(column=4, row=1, sticky=(W, E))
all_entry_ls.append(voy_draugh_entry)
'voyage river level'
voy_peg_kau = StringVar()
voy_peg_kau_entry = ttk.Entry(voyage_labelFrame, width=10,
                              textvariable=voy_peg_kau)
voy_peg_kau_entry.grid(column=4, row=2, sticky=(W, E))
all_entry_ls.append(voy_peg_kau_entry)

# Menu-buttons.
opties = Menu(root)
root.config(menu=opties)
menu1 = Menu(opties)
opties.add_cascade(label="Bestand", menu=menu1)
menu1.add_command(label="Opslaan", command=lambda: save_voyage(all_entry_ls),
                  accelerator="Cmd+S")
menu1.add_command(label="Openen")

menu2 = Menu(opties)
opties.add_cascade(label="Knutselen", menu=menu2)
menu2.add_command(label="Knippen")
menu2.add_command(label="Plakken")

menu3 = Menu(opties)
opties.add_cascade(label="Keuze maken", menu=menu3)
menu3.add_command(label="Gaan")
menu3.add_separator()
menu3.add_command(label="Niet gaan")


# sector table #

# table header
ttk.Label(sector_labelFrame, text="Begin", anchor=(CENTER),
          width=15).grid(column=0, row=0, columnspan=3, sticky=(W, E))
ttk.Label(sector_labelFrame, text="Eind", anchor=(CENTER),
          width=15).grid(column=5, row=0, columnspan=3, sticky=(W, E))
ttk.Label(sector_labelFrame, text="Meten", anchor=(CENTER),
          width=15).grid(column=9, row=0, sticky=(W, E))
'Meten = measuring'
ttk.Label(sector_labelFrame, text="Toeren", anchor=(CENTER),
          width=6).grid(column=8, row=0, sticky=(W, E))
"Toeren = RPM's "


# table header separators.
ttk.Separator(sector_labelFrame,
              orient=VERTICAL).grid(column=1, rowspan=4, row=1,
                                    sticky="N, S")
ttk.Separator(sector_labelFrame,
              orient=VERTICAL).grid(column=6, rowspan=4, row=1,
                                    sticky="N, S")
ttk.Separator(sector_labelFrame,
              orient=VERTICAL).grid(column=4, rowspan=5, row=0,
                                    sticky="N, S")
ttk.Separator(sector_labelFrame,
              orient=HORIZONTAL).grid(column=0, row=1, columnspan=10,
                                      sticky="E, W")


# Sector 1 Lobith - Duisburg
'fixed'
ttk.Label(sector_labelFrame, text="Kmr 855 (Lobith)").grid(column=0, row=2,
                                                           sticky=(W, E))
ttk.Label(sector_labelFrame, text="Kmr 777 (Duisburg)").grid(column=5, row=2,
                                                             sticky=(W, E))
'results'
time_stampS1 = ttk.Label(sector_labelFrame, text="", width=15)
time_stampS1.grid(column=2, row=2, sticky=(W, E))
time_stampE1 = ttk.Label(sector_labelFrame, text="", width=15)
time_stampE1.grid(column=7, row=2, sticky=(W, E))
'var'
sector1_size = 78
'button'
button_s1 = ttk.Button(sector_labelFrame, text="Start", command=lambda:
                       start_stop_switch(button_s1, sector1_size, time_stampS1,
                                         time_stampE1, 1, sector1_rpm_entry))
button_s1.grid(column=9, row=2, sticky=(W, E))
start_stop_button_ls.append(button_s1)
"rpm's"
sector1_rpm = StringVar
sector1_rpm_entry = ttk.Entry(sector_labelFrame, textvariable=sector1_rpm,
                              width=5)
sector1_rpm_entry.grid(column=8, row=2, sticky=(W, E))

# Sector 2 Duisburg - Düsseldorf
'fixed'
ttk.Label(sector_labelFrame, text="Kmr 777 (Duisburg)").grid(column=0, row=3,
                                                             sticky=(W, E))
ttk.Label(sector_labelFrame, text="Kmr 742 (Düsseldorf)").grid(column=5, row=3,
                                                               sticky=(W, E))
'results'
time_stampS2 = ttk.Label(sector_labelFrame, text="")
time_stampS2.grid(column=2, row=3, sticky=(W, E))
time_stampE2 = ttk.Label(sector_labelFrame, text="")
time_stampE2.grid(column=7, row=3, sticky=(W, E))
'var'
sector2_size = 35
'button'
button_s2 = ttk.Button(sector_labelFrame, text="Start", command=lambda:
                       start_stop_switch(button_s2, sector2_size, time_stampS2,
                                         time_stampE2, 2, sector2_rpm_entry))
button_s2.grid(column=9, row=3, sticky=(W, E))
start_stop_button_ls.append(button_s2)
sector2_rpm = StringVar
sector2_rpm_entry = ttk.Entry(sector_labelFrame, textvariable=sector2_rpm,
                              width=5)
sector2_rpm_entry.grid(column=8, row=3, sticky=(W, E))

# Sector 3 Düsseldorf - Cologne
'fixed'
ttk.Label(sector_labelFrame, text="Kmr 742 (Düsseldorf)").grid(column=0, row=4,
                                                               sticky=(W, E))
ttk.Label(sector_labelFrame, text="Kmr 690 (Keulen)").grid(column=5, row=4,
                                                           sticky=(W, E))
'results'
time_stampS3 = ttk.Label(sector_labelFrame, text="")
time_stampS3.grid(column=2, row=4, sticky=(W, E))
time_stampE3 = ttk.Label(sector_labelFrame, text="")
time_stampE3.grid(column=7, row=4, sticky=(W, E))
'var'
sector3_size = 52
'button'
button_s3 = ttk.Button(sector_labelFrame, text="Start", command=lambda:
                       start_stop_switch(button_s3, sector3_size, time_stampS3,
                                         time_stampE3, 3, sector3_rpm_entry))
button_s3.grid(column=9, row=4, sticky=(W, E))
start_stop_button_ls.append(button_s3)
"rpm's"
sector3_rpm = StringVar
sector3_rpm_entry = ttk.Entry(sector_labelFrame, textvariable=sector3_rpm,
                              width=5)
sector3_rpm_entry.grid(column=8, row=4, sticky=(W, E))


# Numpad buttons (voyage number examples: ALS2102T, 1RT2114T, 2RT2114B)

# First 3 characters for a voyage towards or from Antwerp
button_ALS = ttk.Button(numpad_labelFrame, text="ALS", state=DISABLED,
                        takefocus=False,
                        command=lambda: button_press(button_ALS))
button_ALS.grid(column=1, row=1, sticky=(W, E))
special_character_butt_ls.append(button_ALS)

# First 2 characters for a voyage towards or from Rotterdam
button_RT = ttk.Button(numpad_labelFrame, text="RT", state=DISABLED,
                       takefocus=False,
                       command=lambda: button_press(button_RT))
button_RT.grid(column=2, row=1, sticky=(W, E))
special_character_butt_ls.append(button_RT)

# Last character in voyage number for designating a trip towards the ocean
button_T = ttk.Button(numpad_labelFrame, text="T", state=DISABLED,
                      takefocus=False, command=lambda: button_press(button_T))
button_T.grid(column=1, row=2, sticky=(W, E))
special_character_butt_ls.append(button_T)

# Last character in voyage number for designating a trip towards Basel, CH
button_B = ttk.Button(numpad_labelFrame, text="B", state=DISABLED,
                      takefocus=False, command=lambda: button_press(button_B))
button_B.grid(column=2, row=2, sticky=(W, E))
special_character_butt_ls.append(button_B)

# Auto calculate voyage number ( YYWW )
button_YYWW = ttk.Button(numpad_labelFrame, text="Reis#", state=DISABLED,
                         takefocus=False,
                         command=lambda: button_press(button_YYWW))
button_YYWW.grid(column=3, row=1, sticky=(W, E))
special_character_butt_ls.append(button_YYWW)

# To remove mistakes
button_DEL = ttk.Button(numpad_labelFrame, text="DEL",
                        takefocus=False,
                        command=lambda: button_press(button_DEL))
button_DEL.grid(column=3, row=2, sticky=(W, E))


# Numeric buttons
button_0 = ttk.Button(numpad_labelFrame, text="0",
                      takefocus=False, command=lambda: button_press(button_0))
button_0.grid(column=2, row=6, sticky=(W, E))
all_numpad_character_ls.append(button_0)

button_1 = ttk.Button(numpad_labelFrame, text="1",
                      takefocus=False, command=lambda: button_press(button_1))
button_1.grid(column=1, row=5, sticky=(W, E))
all_numpad_character_ls.append(button_1)

button_2 = ttk.Button(numpad_labelFrame, text="2",
                      takefocus=False, command=lambda: button_press(button_2))
button_2.grid(column=2, row=5, sticky=(W, E))
all_numpad_character_ls.append(button_2)

button_3 = ttk.Button(numpad_labelFrame, text="3",
                      takefocus=False, command=lambda: button_press(button_3))
button_3.grid(column=3, row=5, sticky=(W, E))
all_numpad_character_ls.append(button_3)

button_4 = ttk.Button(numpad_labelFrame, text="4",
                      takefocus=False, command=lambda: button_press(button_4))
button_4.grid(column=1, row=4, sticky=(W, E))
all_numpad_character_ls.append(button_4)

button_5 = ttk.Button(numpad_labelFrame, text="5",
                      takefocus=False, command=lambda: button_press(button_5))
button_5.grid(column=2, row=4, sticky=(W, E))
all_numpad_character_ls.append(button_5)

button_6 = ttk.Button(numpad_labelFrame, text="6",
                      takefocus=False, command=lambda: button_press(button_6))
button_6.grid(column=3, row=4, sticky=(W, E))
all_numpad_character_ls.append(button_6)

button_7 = ttk.Button(numpad_labelFrame, text="7",
                      takefocus=False, command=lambda: button_press(button_7))
button_7.grid(column=1, row=3, sticky=(W, E))
all_numpad_character_ls.append(button_7)

button_8 = ttk.Button(numpad_labelFrame, text="8",
                      takefocus=False, command=lambda: button_press(button_8))
button_8.grid(column=2, row=3, sticky=(W, E))
all_numpad_character_ls.append(button_8)

button_9 = ttk.Button(numpad_labelFrame, text="9",
                      takefocus=False, command=lambda: button_press(button_9))
button_9.grid(column=3, row=3, sticky=(W, E))
all_numpad_character_ls.append(button_9)


# padding
for child in mainframe.winfo_children():
    child.grid_configure(padx=3, pady=1)

voy_number_entry.focus()

voy_number_entry.bind("<FocusIn>", enable_voy_buttons)
voy_number_entry.bind("<FocusOut>", disable_voy_buttons)
root.bind("<Command-s>", key_bind)

root.mainloop()
