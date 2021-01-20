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


def convert():
    """Main function. Converting amount from one currency to another"""
    user_input = float(currency_input.get())
    user_currency = float(radio_state.get())
    result_currency = float(radio_state_to.get())
    result = round((user_input / user_currency) * result_currency, 2)
    currency_label = currency_data[currency_data.cost == result_currency]["currency"].item()
    label_result.config(text=f"{result}\n{currency_label}")


def display_countries(state_variable):
    """Displaying radiobuttons with currency names and rendering it from csv file"""
    global column, row
    for nr in range(0, len(currency_data.country)):
        column += 1
        if column == 3:
            column = 0
            row += 1
        radiobtn = Radiobutton(text=f"{currency_data.country[nr]}", value=currency_data.cost[nr],
                               tristatevalue=currency_data.cost[nr], variable=state_variable)
        radiobtn.grid(column=column, row=row)


currency_input = Entry(width=30)
currency_input.grid(column=1, row=0, pady=20)

# first row of radiobuttons

radio_state = StringVar()
display_countries(radio_state)

row = row + 1

label_to = Label(text="to", font=("Arial", 22, "normal"))
label_to.grid(column=1, row=row + 1, pady=20)

row = row + 1

# second row of radiobuttons

column += 1
radio_state_to = StringVar()
display_countries(radio_state_to)


label_result = Label(text="0", font=("Arial", 18, "bold"))
label_result.grid(column=1, row=row + 2, pady=30)

button = Button(text="Calculate", command=convert)
button.grid(column=1, row=row + 3, pady=10)

window.mainloop()