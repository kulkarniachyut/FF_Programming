import json
from Tkinter import *

def load_json() :
    with open('ca.json', 'r') as handle:
        parsed = json.load(handle)
    return parsed

class CaliforniaGUI:

    def display(self,event) :
        city_name = self.variable.get()
        city_details = filter(lambda x : x["name"] == city_name,self.parsed )[0]

        self.county_name_text["text"] = city_details["full_county_name"]
        self.latitude_text["text"] = city_details["primary_latitude"]
        self.longitude_text["text"] = city_details["primary_longitude"]

    def __init__(self, master):
        self.parsed = load_json()
        self.master = master
        master.title("California City Information")

        self.city_label = Label(master, text="City")
        self.city_label.grid(row=0)
        self.county_name = Label(master, text="County Name")
        self.county_name.grid(row=1)
        self.latitude = Label(master, text="Latitude")
        self.latitude.grid(row=2)
        self.longitude = Label(master, text="Longitude")
        self.longitude.grid(row=3)

        self.variable = StringVar(master)
        self.variable.set("select") # default value
        self.city_menu = OptionMenu(master, self.variable , *map(lambda x : x["name"] ,self.parsed),command = self.display).grid(row=0,column=1)

        self.county_name_text = Label(master, text="")
        self.county_name_text.grid(row=1,column=1)
        self.latitude_text = Label(master, text="")
        self.latitude_text.grid(row=2,column=1)
        self.longitude_text = Label(master, text="")
        self.longitude_text.grid(row=3,column=1)


def main() :
    root = Tk()
    my_gui = CaliforniaGUI(root)
    root.mainloop()


if __name__ == '__main__':
    main()
