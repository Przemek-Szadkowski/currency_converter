from tkinter import *

window = Tk()
window.title("Currency calculator")
window.minsize(width=300, height=500)
window.config(padx=20, pady=20)


def convert():
    user_input = float(currency_input.get())
    user_currency = float(radio_state.get())
    result_currency = float(radio_state_to.get())
    result = round((user_input / user_currency) * result_currency, 2)
    label_result.config(text=result)


currency_input = Entry(width=20)
currency_input.grid(column=1, row=0, pady=20)


radio_state = StringVar()
radiobuttonUSD = Radiobutton(text="USD", value="1.216", tristatevalue="1.216", variable=radio_state)
radiobuttonCZK = Radiobutton(text="CZK", value="26.173", tristatevalue="26.173", variable=radio_state)
radiobuttonGBP = Radiobutton(text="GBP", value="0.889", tristatevalue="0.889", variable=radio_state)
radiobuttonPLN = Radiobutton(text="PLN", value="4.52", tristatevalue="4.52", variable=radio_state)
radiobuttonCHF = Radiobutton(text="CHF", value="1.081", tristatevalue="1.081", variable=radio_state)
radiobuttonRUB = Radiobutton(text="RUB", value="89.785", tristatevalue="89.785", variable=radio_state)
radiobuttonUSD.grid(column=0, row=1)
radiobuttonCZK.grid(column=1, row=1)
radiobuttonGBP.grid(column=2, row=1)
radiobuttonPLN.grid(column=0, row=2)
radiobuttonCHF.grid(column=1, row=2)
radiobuttonRUB.grid(column=2, row=2)

label_to = Label(text="to", font=("Arial", 22, "normal"))
label_to.grid(column=1, row=3, pady=20)

radio_state_to = StringVar()
radiobuttonUSD_to = Radiobutton(text="USD", value="1.216", tristatevalue="1.216", variable=radio_state_to)
radiobuttonCZK_to = Radiobutton(text="CZK", value="26.173", tristatevalue="26.173", variable=radio_state_to)
radiobuttonGBP_to = Radiobutton(text="GBP", value="0.889", tristatevalue="0.889", variable=radio_state_to)
radiobuttonPLN_to = Radiobutton(text="PLN", value="4.52", tristatevalue="4.52", variable=radio_state_to)
radiobuttonCHF_to = Radiobutton(text="CHF", value="1.081", tristatevalue="1.081", variable=radio_state_to)
radiobuttonRUB_to = Radiobutton(text="RUB", value="89.785", tristatevalue="89.785", variable=radio_state_to)
radiobuttonUSD_to.grid(column=0, row=4)
radiobuttonCZK_to.grid(column=1, row=4)
radiobuttonGBP_to.grid(column=2, row=4)
radiobuttonPLN_to.grid(column=0, row=5)
radiobuttonCHF_to.grid(column=1, row=5)
radiobuttonRUB_to.grid(column=2, row=5)

label_result = Label(text="0", font=("Arial", 28, "bold"))
label_result.grid(column=1, row=6, pady=20)

button = Button(text="Calculate", command=convert)
button.grid(column=1, row=7, pady=10)

window.mainloop()