from tkinter import *

window = Tk()
window.title("Currency calculator")
window.minsize(width=300, height=500)
window.config(padx=20, pady=20)


def action():
    print("ok")


def radio_used():
    print(radio_state.get())


currency_input = Entry(width=20)
currency_input.grid(column=1, row=0, pady=20)


radio_state = IntVar()
radiobuttonUSD = Radiobutton(text="USD", value=1, variable=radio_state, command=radio_used)
radiobuttonCZK = Radiobutton(text="CZK", value=2, variable=radio_state, command=radio_used)
radiobuttonGBP = Radiobutton(text="GBP", value=3, variable=radio_state, command=radio_used)
radiobuttonPLN = Radiobutton(text="PLN", value=4, variable=radio_state, command=radio_used)
radiobuttonCHF = Radiobutton(text="CHF", value=5, variable=radio_state, command=radio_used)
radiobuttonRUB = Radiobutton(text="RUB", value=6, variable=radio_state, command=radio_used)
radiobuttonUSD.grid(column=0, row=1)
radiobuttonCZK.grid(column=1, row=1)
radiobuttonGBP.grid(column=2, row=1)
radiobuttonPLN.grid(column=0, row=2)
radiobuttonCHF.grid(column=1, row=2)
radiobuttonRUB.grid(column=2, row=2)

# zrobić radiobuttony "to currency"

label_result = Label(text="0", font=("Arial", 28, "bold"))
label_result.grid(column=1, row=3, pady=20)

button = Button(text="Calculate", command=action)
button.grid(column=1, row=4, pady=20)
window.mainloop()