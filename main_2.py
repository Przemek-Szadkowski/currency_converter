from tkinter import *
import pandas

window = Tk()
window.title("Currency calculator")
window.minsize(width=500, height=500)
window.config(padx=100, pady=20)

currency_data = pandas.read_csv("rates.csv")
row = 1
column = -1
print(currency_data)

# main calculate function


def convert():
    user_input = float(currency_input.get())
    user_currency = float(radio_state.get())
    result_currency = float(radio_state_to.get())
    result = round((user_input / user_currency) * result_currency, 2)
    currency_label = currency_data[currency_data.cost == result_currency]["currency"].item()
    label_result.config(text=f"{result}\n{currency_label}")


currency_input = Entry(width=30)
currency_input.grid(column=1, row=0, pady=20)

# first row of radiobuttons

radio_state = StringVar()
for number in range(0, len(currency_data.country)):
    column += 1
    if column == 3:
        column = 0
        row += 1
    radiobutton = Radiobutton(text=f"{currency_data.country[number]}",
                              value=currency_data.cost[number],
                              tristatevalue=currency_data.cost[number], variable=radio_state)
    radiobutton.grid(column=column, row=row)

row = row + 1

label_to = Label(text="to", font=("Arial", 22, "normal"))
label_to.grid(column=1, row=row + 1, pady=20)

row = row + 1

# second row of radiobuttons

radio_state_to = StringVar()
column = -1
for number in range(0, len(currency_data.country)):
    column += 1
    if column == 3:
        column = 0
        row += 1
    radiobutton = Radiobutton(text=f"{currency_data.country[number]}",
                              value=currency_data.cost[number],
                              tristatevalue=currency_data.cost[number], variable=radio_state_to)
    radiobutton.grid(column=column, row=row + 1)


label_result = Label(text="0", font=("Arial", 18, "bold"))
label_result.grid(column=1, row=row + 2, pady=30)

button = Button(text="Calculate", command=convert)
button.grid(column=1, row=row + 3, pady=10)

window.mainloop()