import tkinter as tk

root = tk.Tk()
root.title("Simple Calcuator")

e = tk.Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_click(number):
    current = e.get()
    e.delete(0, tk.END)
    e.insert(0, str(current) + str(number))

def button_click_clear():
    e.delete(0, tk.END)

def button_click_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, tk.END)

def button_click_equal():
    second_number = e.get()
    e.delete(0, tk.END)

    if math == "addition":
        e.insert(0, f_num + int(second_number))
    elif math == "subtraction":
        e.insert(0, f_num - int(second_number))
    elif math == "multiplication":
        e.insert(0, f_num * int(second_number))
    elif math == "division":
        e.insert(0, f_num / int(second_number))

def button_click_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, tk.END)

def button_click_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, tk.END)

def button_click_divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, tk.END)

button_0 = tk.Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0), bg="#99FFFF")
button_1 = tk.Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1), bg="#99FFFF")
button_2 = tk.Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2), bg="#99FFFF")
button_3 = tk.Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3), bg="#99FFFF")
button_4 = tk.Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4), bg="#99FFFF")
button_5 = tk.Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5), bg="#99FFFF")
button_6 = tk.Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6), bg="#99FFFF")
button_7 = tk.Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7), bg="#99FFFF")
button_8 = tk.Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8), bg="#99FFFF")
button_9 = tk.Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9), bg="#99FFFF")
button_add = tk.Button(root, text="+", padx=39, pady=20, command=button_click_add, bg="#FFFF00")
button_equal = tk.Button(root, text="=", padx=39, pady=20, command=lambda: button_click_equal(), bg="#009900")
button_clear = tk.Button(root, text="Clear", padx=125, pady=20, command=lambda: button_click_clear(), bg = "#990000")
button_sub = tk.Button(root, text="-", padx=41, pady=20, command=button_click_subtract, bg="#FFFF00")
button_mul = tk.Button(root, text="*", padx=40, pady=20, command=button_click_multiply, bg="#FFFF00")
button_div = tk.Button(root, text="/", padx=40, pady=20, command=button_click_divide, bg="#FFFF00")

button_0.grid(row=4, column=0)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_add.grid(row=4, column=1)
button_clear.grid(row=6, column=0, columnspan=3)
button_equal.grid(row=5, column=0)
button_sub.grid(row=5, column=1)
button_mul.grid(row=4, column=2)
button_div.grid(row=5, column=2)

root.mainloop()