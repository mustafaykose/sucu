import tkinter as tk
from datetime import datetime

# Set up the GUI
root = tk.Tk()
root.title("Sucu bitki takipçisi")

plants = {
    "ananas": None,
    "orkide": None,
    "kaktüs": None,
    "sinekkapan": None
}

data_file = "sucudata.txt"

def save_data():
    with open(data_file, "w") as file:
        for plant, last_watered in plants.items():
            if last_watered:
                line = plant + "," + last_watered + "\n"
                file.write(line)

def load_data():
    try:
        with open(data_file, "r") as file:
            for line in file:
                plant, last_watered = line.strip().split(",")
                plants[plant] = last_watered
    except FileNotFoundError:
        pass

load_data()

plant_labels = []
plant_entries = []
for i, plant in enumerate(plants.keys()):
    label = tk.Label(root, text=plant + ":")
    label.grid(row=i, column=0)
    entry = tk.Entry(root, width=30)
    entry.grid(row=i, column=1, padx=10, pady=10)
    plant_labels.append(label)
    plant_entries.append(entry)
    if plants[plant]:
        plant_entries[i].insert(0, plants[plant])
    else:
        plant_entries[i].insert(0, "Last watered date (MM/DD/YYYY)")

def update_last_watered(plant):
    now = datetime.now()
    plants[plant] = now.strftime("%m/%d/%Y %I:%M %p")
    index = list(plants.keys()).index(plant)
    plant_entries[index].delete(0, tk.END)
    plant_entries[index].insert(0, plants[plant])
    save_data()

update_buttons = []
for i, plant in enumerate(plants.keys()):
    button = tk.Button(root, text= plant + " Sulandı", command=lambda plant=plant: update_last_watered(plant))
    button.grid(row=i, column=2, pady=10)
    update_buttons.append(button)

root.mainloop()
