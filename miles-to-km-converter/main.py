from tkinter import *

def miles_to_km():
    miles = float(Miles_input.get())
    km = miles*1.609
    kilometer_result_label.config(text=f"{km}")

window = Tk()
window.title("Miles To Kilometer Converter")
window.config(padx=20,pady=20)


Miles_input = Entry(width=7)
Miles_input.grid(column=1,row=0)

Miles_label = Label(text="Miles")
Miles_label.grid(column=2,row=0)

equal_label = Label(text="is equal to")
equal_label.grid(column=0,row=1)

kilometer_result_label = Label(text="")
kilometer_result_label.grid(column=1,row=1)

kilometer_label = Label(text="Km")
kilometer_label.grid(column=2,row=1)

calculate_button = Button(text="calculcate",command=miles_to_km)
calculate_button.grid(column=1,row=2)



window.mainloop()
