from tkinter import *



def miles_to_km():

    ''' Convert miles to kilometers and show the result '''

    miles = float(entry_box.get())
    km = round(miles * 1.609)
    result_label.config(text=f"{km}")


window = Tk()

window.title("Miles to KM Converter")
window.config(padx = 20, pady = 20)



entry_box = Entry(width=12)
entry_box.grid(column=1 , row=0)



label_1 = Label(text="Miles")
label_1.grid(column=2, row=0)



is_equal_label = Label(text="equal to")
is_equal_label.grid(column=0, row=1)



result_label = Label(text="0")
result_label.grid(column=1, row=1)



km_label = Label(text="KM")
km_label.grid(column=2, row=1)



calculate_button = Button(text="Calculate",command=miles_to_km)
calculate_button.grid(column=1, row=2)
