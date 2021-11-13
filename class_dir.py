import time
from tkinter import ttk


class Voyage:
    def __init__(self, voyage_number=None, voyage_ton=None,
                 voyage_draught=None,
                 voyage_riverlevel=None):
        self.voyage_number = voyage_number
        self.voyage_ton = voyage_ton
        self.voyage_draught = voyage_draught
        self.voyage_riverlevel = voyage_riverlevel

    def setup_voyage_UI(object):
        label1 = ttk.Label(object, text="test")
        label1.grid(column=0, row=0)

    def get_voyage_number(self):
        return self.voyage_number


class Sector(Voyage):
    marker = "kmr"

    def __init__(self, s_number, s_start, s_start_city, s_end, s_end_city,
                 s_rpm=None, start_time=None, end_time=None, total_time=None):
        self.s_number = s_number
        self.s_start = s_start
        self.s_end = s_end
        self.s_start_city = s_start_city
        self.s_end_city = s_end_city
        self.s_rpm = s_rpm
        self.start_time = start_time
        self.end_time = end_time
        self.total_time = total_time

    def sectorLength(self) -> str:
        return self.s_start - self.s_end

    def set_start_time(self):
        self.start_time = time.time()

    def set_end_time(self):
        self.end_time = time.time()

    def get_total_time(self):
        self.total_time = self.end_time - self.start_time
