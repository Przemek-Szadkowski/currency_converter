from tkinter import *
import pandas

currency_data = pandas.read_csv("rates.csv")

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

row = 0
column = 0

radio_state = IntVar()

for number in range(0, len(currency_data.country)):
    row += 1
    radiobutton = Radiobutton(text=f"{currency_data.country[number]}",
                              value=currency_data.cost[number], variable=radio_state, command=radio_used)
    radiobutton.grid(column=0, row=row)

# for country in currency_data_dict["country"].values():
#     row += 1
#     radiobutton = Radiobutton(text=f"{country}")
#     radiobutton.grid(column=0, row=row)
#     print(country)

# radio_state = IntVar()
# radiobuttonUSD = Radiobutton(text="USD", value=1, variable=radio_state, command=radio_used)
# radiobuttonCZK = Radiobutton(text="CZK", value=2, variable=radio_state, command=radio_used)
# radiobuttonGBP = Radiobutton(text="GBP", value=3, variable=radio_state, command=radio_used)
# radiobuttonPLN = Radiobutton(text="PLN", value=4, variable=radio_state, command=radio_used)
# radiobuttonCHF = Radiobutton(text="CHF", value=5, variable=radio_state, command=radio_used)
# radiobuttonRUB = Radiobutton(text="RUB", value=6, variable=radio_state, command=radio_used)
# radiobuttonUSD.grid(column=0, row=1)
# radiobuttonCZK.grid(column=1, row=1)
# radiobuttonGBP.grid(column=2, row=1)
# radiobuttonPLN.grid(column=0, row=2)
# radiobuttonCHF.grid(column=1, row=2)
# radiobuttonRUB.grid(column=2, row=2)

label_to = Label(text="to", font=("Arial", 22, "normal"))
label_to.grid(column=1, row=7, pady=20)

# radio_state_to = IntVar()
# radiobuttonUSD_to = Radiobutton(text="USD", value=1, variable=radio_state_to, command=radio_used)
# radiobuttonCZK_to = Radiobutton(text="CZK", value=2, variable=radio_state_to, command=radio_used)
# radiobuttonGBP_to = Radiobutton(text="GBP", value=3, variable=radio_state_to, command=radio_used)
# radiobuttonPLN_to = Radiobutton(text="PLN", value=4, variable=radio_state_to, command=radio_used)
# radiobuttonCHF_to = Radiobutton(text="CHF", value=5, variable=radio_state_to, command=radio_used)
# radiobuttonRUB_to = Radiobutton(text="RUB", value=6, variable=radio_state_to, command=radio_used)
# radiobuttonUSD_to.grid(column=0, row=4)
# radiobuttonCZK_to.grid(column=1, row=4)
# radiobuttonGBP_to.grid(column=2, row=4)
# radiobuttonPLN_to.grid(column=0, row=5)
# radiobuttonCHF_to.grid(column=1, row=5)
# radiobuttonRUB_to.grid(column=2, row=5)

label_result = Label(text="0", font=("Arial", 28, "bold"))
label_result.grid(column=1, row=8, pady=20)

button = Button(text="Calculate", command=action)
button.grid(column=1, row=9, pady=10)
window.mainloop()