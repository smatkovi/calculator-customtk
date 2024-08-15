import customtkinter

# Changing the theme to 'dark'
customtkinter.set_appearance_mode('dark')

# Configuring the window
window = customtkinter.CTk()
window.geometry('361x485+423+159')

def calculate():
    try:
        calculation = output.get('0.0', 'end').strip()
        # Replace ',' with '.' for evaluation
        calculation = calculation.replace(',', '.')
        result = eval(calculation)
        output.delete('0.0', 'end')
        output.insert('0.0', str(result).replace('.', ','))
    except:
        output.delete('0.0', 'end')
        output.insert('0.0', "Error")

def handle_keypress(event):
    key = event.char
    if key in '0123456789+-*/.,':
        output.insert('end', key)
    elif event.keysym == 'Return':  # Enter key for "="
        calculate()
    elif event.keysym == 'BackSpace':  # Backspace key for deleting last character
        current_text = output.get('0.0', 'end').strip()
        if current_text:
            output.delete('0.0', 'end')
            output.insert('0.0', current_text[:-1])
    elif key == 'n':  # 'n' key for inserting '156.68'
        output.insert('end', '156,68')

# Textbox where the user will enter numbers
output = customtkinter.CTkTextbox(window, width=340, height=50, corner_radius=10, border_width=5, border_color='#042940', font=('Arial', 50))
output.grid(row=0, column=0, columnspan=5, padx=5, pady=5, sticky='nsew')

# Configure grid columns and rows to expand
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=1)
window.grid_columnconfigure(3, weight=1)
window.grid_columnconfigure(4, weight=1)
window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=1)
window.grid_rowconfigure(2, weight=1)
window.grid_rowconfigure(3, weight=1)
window.grid_rowconfigure(4, weight=1)
window.grid_rowconfigure(5, weight=1)

# Bind keypress events to the handle_keypress function
window.bind('<Key>', handle_keypress)

# Buttons
btn1 = customtkinter.CTkButton(window, text='1', command=lambda: output.insert('end', '1'), corner_radius=20, width=80, height=55, font=('Arial', 30))
btn1.grid(row=1, column=0, padx=5, pady=5, sticky='nsew')

btn2 = customtkinter.CTkButton(window, text='2', command=lambda: output.insert('end', '2'), corner_radius=20, width=80, height=55, font=('Arial', 30))
btn2.grid(row=1, column=1, padx=5, pady=5, sticky='nsew')

btn3 = customtkinter.CTkButton(window, text='3', command=lambda: output.insert('end', '3'), corner_radius=20, width=80, height=55, font=('Arial', 30))
btn3.grid(row=1, column=2, padx=5, pady=5, sticky='nsew')

btn_add = customtkinter.CTkButton(window, text='+', command=lambda: output.insert('end', '+'), corner_radius=20, width=80, height=55, font=('Arial', 30))
btn_add.grid(row=1, column=3, padx=5, pady=5, sticky='nsew')

btn4 = customtkinter.CTkButton(window, text='4', command=lambda: output.insert('end', '4'), corner_radius=20, width=80, height=55, font=('Arial', 30))
btn4.grid(row=2, column=0, padx=5, pady=5, sticky='nsew')

btn5 = customtkinter.CTkButton(window, text='5', command=lambda: output.insert('end', '5'), corner_radius=20, width=80, height=55, font=('Arial', 30))
btn5.grid(row=2, column=1, padx=5, pady=5, sticky='nsew')

btn6 = customtkinter.CTkButton(window, text='6', command=lambda: output.insert('end', '6'), corner_radius=20, width=80, height=55, font=('Arial', 30))
btn6.grid(row=2, column=2, padx=5, pady=5, sticky='nsew')

btn_subtract = customtkinter.CTkButton(window, text='-', command=lambda: output.insert('end', '-'), corner_radius=20, width=80, height=55, font=('Arial', 30))
btn_subtract.grid(row=2, column=3, padx=5, pady=5, sticky='nsew')

btn7 = customtkinter.CTkButton(window, text='7', command=lambda: output.insert('end', '7'), corner_radius=20, width=80, height=55, font=('Arial', 30))
btn7.grid(row=3, column=0, padx=5, pady=5, sticky='nsew')

btn8 = customtkinter.CTkButton(window, text='8', command=lambda: output.insert('end', '8'), corner_radius=20, width=80, height=55, font=('Arial', 30))
btn8.grid(row=3, column=1, padx=5, pady=5, sticky='nsew')

btn9 = customtkinter.CTkButton(window, text='9', command=lambda: output.insert('end', '9'), corner_radius=20, width=80, height=55, font=('Arial', 30))
btn9.grid(row=3, column=2, padx=5, pady=5, sticky='nsew')

btn_multiply = customtkinter.CTkButton(window, text='x', command=lambda: output.insert('end', '*'), corner_radius=20, width=80, height=55, font=('Arial', 30))
btn_multiply.grid(row=3, column=3, padx=5, pady=5, sticky='nsew')

btn0 = customtkinter.CTkButton(window, text='0', command=lambda: output.insert('end', '0'), corner_radius=20, width=80, height=55, font=('Arial', 30))
btn0.grid(row=4, column=0, padx=5, pady=5, sticky='nsew')

btn_decimal = customtkinter.CTkButton(window, text=',', command=lambda: output.insert('end', ','), corner_radius=20, width=80, height=55, font=('Arial', 30))
btn_decimal.grid(row=4, column=1, padx=5, pady=5, sticky='nsew')

btn_clear = customtkinter.CTkButton(window, text='C', command=lambda: output.delete('0.0', 'end'), corner_radius=20, width=80, height=55, font=('Arial', 30))
btn_clear.grid(row=4, column=2, padx=5, pady=5, sticky='nsew')

btn_calculate = customtkinter.CTkButton(window, text='=', command=calculate, corner_radius=20, width=80, height=55, font=('Arial', 30))
btn_calculate.grid(row=4, column=3, padx=5, pady=5, sticky='nsew')

btn_divide = customtkinter.CTkButton(window, text='/', command=lambda: output.insert('end', '/'), corner_radius=20, width=80, height=55, font=('Arial', 30))
btn_divide.grid(row=5, column=3, padx=5, pady=5, sticky='nsew')

# Button for inserting 156.68
btn_custom = customtkinter.CTkButton(window, text='156.68', command=lambda: output.insert('end', '156,68'), corner_radius=20, width=80, height=55, font=('Arial', 30))
btn_custom.grid(row=5, column=0, padx=5, pady=5, sticky='nsew')

window.mainloop()
