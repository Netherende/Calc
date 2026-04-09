import customtkinter as ctk

def button_pressed(number):
    print(f"{number} pressed")
    current_text = display.get()
    display.delete(0, "end")
    display.insert(0, current_text + str(number))

    if number.strip() == "=":
        try:
            result = eval(current_text)
            display.delete(0, "end")
            display.insert(0, str(result))
        except:
            display.delete(0, "end")
            display.insert(0, "Error")
    elif number.strip() == "C":
        display.delete(0, "end")
    else:
        display.delete(0, "end")
        display.insert(0, current_text + str(number))

app = ctk.CTk()
app.title("Taschenrechner")
app.geometry("400x400")
app.grid_columnconfigure(0, weight=1, uniform="group1")
app.grid_columnconfigure(1, weight=1, uniform="group1")
app.grid_columnconfigure(2, weight=1, uniform="group1")
app.grid_columnconfigure(3, weight=1, uniform="group1")

for i in range(4):
    app.grid_columnconfigure(i, weight=1, uniform="group1")


buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+",
    "C"
]

row_val = 1
col_val = 0

for text in buttons:
    button = ctk.CTkButton(app, text=text, command = lambda b=text: button_pressed(b), width=60, height=60)

    button.grid(row=row_val, column=col_val, padx=5, pady=5, sticky="nsew")

    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1
        

# Das Display ganz oben erstellen
display = ctk.CTkEntry(app, font=("Arial", 24), justify="right")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="ew")
display.bind("<Key>", lambda e: "break")


app.mainloop()