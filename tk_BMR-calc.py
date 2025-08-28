import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

screen = tk.Tk()
screen.title("BMR Calculator")
screen.minsize(600, 500)


def navigate():
    try:    
        age = int(enter_age.get())
        height = int(enter_height.get())
        weight = int(enter_weight.get())
        gender = gender_combo.get()
        exercise = exercise_combo.get()
    
        if gender == 'female':
            calculate_women(weight, height, age, exercise)
        elif gender == 'male':
            calculate_men(weight, height, age, exercise)
    except ValueError:
        messagebox.showerror("error", "you need to enter an integer")

        enter_age.delete(0, tk.END)
        enter_height.delete(0, tk.END)
        enter_weight.delete(0, tk.END)
        gender_combo.set("select your gender")
        exercise_combo.set("how much do you exercise")


def calculate_women(weight, height, age, exercise):
    BMR = 655 + (weight * 9.6) + (1.8 * height) - (4.7 * age)
    movement(BMR, exercise)

def calculate_men(weight, height, age, exercise):
    BMR = 66 + (weight * 13.7) + (5 * height) - (6.8 * age)
    movement(BMR, exercise)

def movement(BMR, exercise):
    if exercise == 'none':
        messagebox.showinfo("your BMR is:", BMR)
    elif exercise == 'a little bit':
        BMR *= 1.2
        messagebox.showinfo("your BMR is:", BMR)
    elif exercise == 'once every 2 days':
        BMR *= 1.375
        messagebox.showinfo("your BMR is:", BMR)
    elif exercise == 'a very good amount':
        BMR *= 1.55
        messagebox.showinfo("your BMR is:", BMR)
    elif exercise == 'five days a week':
        BMR *= 1.725
        messagebox.showinfo("your BMR is:", BMR)
    elif exercise == 'everyday':
        BMR *= 1.9
        messagebox.showinfo("your BMR is:", BMR)

    enter_age.delete(0, tk.END)
    enter_height.delete(0, tk.END)
    enter_weight.delete(0, tk.END)
    gender_combo.set("select your gender")
    exercise_combo.set("how much do you exercise")


ask_age = tk.Label(text="please enter your age below: ", font=("Arial", 18, "bold")).pack()
enter_age = tk.Entry(background="lightcoral", foreground="white", font=("Arial", 14), width=50, justify="center")
enter_age.pack()

ask_weight = tk.Label(text="please enter your weight in kg below: ", font=("Arial", 18, "bold")).pack()
enter_weight = tk.Entry(background="lightcoral", foreground="white", font=("Arial", 14), width=50, justify="center")
enter_weight.pack()

ask_height = tk.Label(text="please enter your height in cm below: ", font=("Arial", 18, "bold")).pack()
enter_height = tk.Entry(background="lightcoral", foreground="white", font=("Arial", 14), width=50, justify="center")
enter_height.pack()


options_gender = ['male', 'female']
gender_combo = ttk.Combobox(screen, values=options_gender, state="readonly", width=30, font=("Arial", 14))
gender_combo.set("select your gender:")
gender_combo.pack(pady=20)

options_exercise = ['none', 'a little bit', 'once every 2 days', 'a very good amount', 'five days a week', 'everyday']
exercise_combo = ttk.Combobox(screen, values=options_exercise, state="readonly", width=30, font=("Arial", 14))
exercise_combo.set("how much do you exercise:")
exercise_combo.pack(pady=20)

calc_button = tk.Button(text="calculate your BMR", background="dodgerblue", font=("Arial", 18), width=15, command=navigate)
calc_button.pack()





screen.mainloop()