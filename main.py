import tkinter as tk


calculation = ""


def add_to_cal(sym):
    global calculation
    sym = str(sym)
    if sym in "+-*/":
        if calculation.endswith(("+", "-", "*", "/")):
            calculation = calculation[:-1]
    calculation += sym
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)


def back_cal():
    global calculation
    calculation = calculation[:-1]
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)


def evaluate_cal():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "Error")


def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")


root = tk.Tk()
root.geometry("472x364")
root.title("Omega-Calculator")
root.configure(background="#1f1f1f")

text_result = tk.Text(root, height=4, width=23, font=("Arial", 27), background="#1f1f1f", fg="white")
text_result.grid(columnspan=5)

btn_1 = tk.Button(root, text="1", command=lambda: add_to_cal(1), width=11, font=("Arial", 14), bg="#3b3b3b", fg="white", activebackground="white")
btn_1.grid(row=3, column=1)
btn_2 = tk.Button(root, text="2", command=lambda: add_to_cal(2), width=11, font=("Arial", 14), bg="#3b3b3b", fg="white", activebackground="white")
btn_2.grid(row=3, column=2)
btn_3 = tk.Button(root, text="3", command=lambda: add_to_cal(3), width=11, font=("Arial", 14), bg="#3b3b3b", fg="white", activebackground="white")
btn_3.grid(row=3, column=3)
btn_4 = tk.Button(root, text="4", command=lambda: add_to_cal(4), width=11, font=("Arial", 14), bg="#3b3b3b", fg="white", activebackground="white")
btn_4.grid(row=4, column=1)
btn_5 = tk.Button(root, text="5", command=lambda: add_to_cal(5), width=11, font=("Arial", 14), bg="#3b3b3b", fg="white", activebackground="white")
btn_5.grid(row=4, column=2)
btn_6 = tk.Button(root, text="6", command=lambda: add_to_cal(6), width=11, font=("Arial", 14), bg="#3b3b3b", fg="white", activebackground="white")
btn_6.grid(row=4, column=3)
btn_7 = tk.Button(root, text="7", command=lambda: add_to_cal(7), width=11, font=("Arial", 14), bg="#3b3b3b", fg="white", activebackground="white")
btn_7.grid(row=5, column=1)
btn_8 = tk.Button(root, text="8", command=lambda: add_to_cal(8), width=11, font=("Arial", 14), bg="#3b3b3b", fg="white", activebackground="white")
btn_8.grid(row=5, column=2)
btn_9 = tk.Button(root, text="9", command=lambda: add_to_cal(9), width=11, font=("Arial", 14), bg="#3b3b3b", fg="white", activebackground="white")
btn_9.grid(row=5, column=3)
btn_0 = tk.Button(root, text="0", command=lambda: add_to_cal(0), width=11, font=("Arial", 14), bg="#3b3b3b", fg="white", activebackground="white")
btn_0.grid(row=6, column=2)

btn_open = tk.Button(root, text="(", command=lambda: add_to_cal("("), width=11, font=("Arial", 14), bg="#3b3b3b", fg="white", activebackground="white")
btn_open.grid(row=6, column=1)
btn_close = tk.Button(root, text=")", command=lambda: add_to_cal(")"), width=11, font=("Arial", 14), bg="#3b3b3b", fg="white", activebackground="white")
btn_close.grid(row=6, column=3)

btn_plus = tk.Button(root, text="+", command=lambda: add_to_cal("+"), width=6, font=("Arial", 14), bg="#3b3b3b", fg="white", activebackground="white")
btn_plus.grid(row=3, column=4)
btn_minus = tk.Button(root, text="-", command=lambda: add_to_cal("-"), width=6, font=("Arial", 14), bg="#3b3b3b", fg="white", activebackground="white")
btn_minus.grid(row=4, column=4)
btn_mul = tk.Button(root, text="×", command=lambda: add_to_cal("*"), width=6, font=("Arial", 14), bg="#3b3b3b", fg="white", activebackground="white")
btn_mul.grid(row=5, column=4)
btn_div = tk.Button(root, text="÷", command=lambda: add_to_cal("/"), width=6, font=("Arial", 14), bg="#3b3b3b", fg="white", activebackground="white")
btn_div.grid(row=6, column=4)

btn_clear = tk.Button(root, text="CLEAR", command=clear_field, width=11, font=("Arial", 14), bg="#641e1e", fg="white", activebackground="white")
btn_clear.grid(row=2, column=1)
btn_equals = tk.Button(root, text="=", command=evaluate_cal, width=11, font=("Arial", 14), bg="#255318", fg="white", activebackground="white")
btn_equals.grid(row=2, column=2)

btn_back = tk.Button(root, text="⌫", command=back_cal, width=18, font=("Arial", 14), bg="#3b3b3b", fg="white", activebackground="white")
btn_back.grid(row=2, column=3, columnspan=2)

root.mainloop()
