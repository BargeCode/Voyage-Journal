from tkinter import *
from tkinter import ttk
from class_dir import Voyage, Sector

root = Tk()
root.title("Journaal")
root.minsize(width=795, height=410)
root.maxsize(width=795, height=410)

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

sector_labelFrame = ttk.Labelframe(mainframe, text='Rivier gedeelten')
'Rivier gedeelten = River sectors'
sector_labelFrame.grid(column=0, row=7, columnspan=10, sticky=(W))
sector_labelFrame.configure(borderwidth=2, relief=SUNKEN)

# voyage details
voyage_labelFrame = ttk.Labelframe(mainframe, text="Reis gegevens")
voyage_labelFrame.grid(column=0, row=0, columnspan=6, rowspan=2, sticky=(N, E))

ttk.Label(voyage_labelFrame, text="Reisnummer #").grid(column=1, row=1,
                                                       sticky=(W, E))
ttk.Label(voyage_labelFrame, text="Tonnage").grid(column=1, row=2,
                                                  sticky=(W, E))
ttk.Label(voyage_labelFrame, text="Diepgang").grid(column=3, row=1,
                                                   sticky=(W, E))
ttk.Label(voyage_labelFrame, text="Pegel Kaub").grid(column=3, row=2,
                                                     sticky=(W, E))

all_entry_ls = []


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
button_s1 = ttk.Button(sector_labelFrame, text="Start",
                       command=lambda: sector1.sectorLength())
button_s1.grid(column=9, row=2, sticky=(W, E))

"rpm's"
sector1_rpm = StringVar
sector1_rpm_entry = ttk.Entry(sector_labelFrame, textvariable=sector1_rpm,
                              width=5)
sector1_rpm_entry.grid(column=8, row=2, sticky=(W, E))

voyage_number = Voyage(voy_number, voy_ton_cou, voy_draugh, voy_peg_kau)
sector1 = Sector(1, 855, "lobith", 777, "Duisburg")

root.mainloop()
