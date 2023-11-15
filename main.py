from tkinter import *

window = Tk()
window.title("BMI Calculator")
window.config(padx=20, pady=20)
height = 250
width = 250
window.minsize(width, height)
user_bmi = 0
bmi_category = ""
FONT = ("Arial", 10, "normal")

def bmi_calculator():
    global user_bmi
    h = int(body_height_entry.get())/100
    w = int(body_weight_entry.get())
    user_bmi = float(f'{w / h ** 2:.2f}')

def check_bmi_category():
    global bmi_category
    if user_bmi <= 18.5:
        bmi_category = "Zayıf"
    elif user_bmi > 18.5 and user_bmi <= 24.9:
        bmi_category = "Normal ağırlıkta"
    elif user_bmi > 24.9 and user_bmi <= 29.9:
        bmi_category = "Kilolu"
    elif user_bmi > 29.9 and user_bmi <= 34.9:
        bmi_category = "1. derece obezite"
    elif user_bmi > 34.9 and user_bmi <= 39.9:
        bmi_category = "2. derece obezite"
    elif user_bmi > 39.9:
        bmi_category = "3. derece obezite"
def entry_validation():
    if len(body_height_entry.get()) == 0 or len(body_weight_entry.get()) == 0:
        enter_height_label.config(text="Boy ve kilo alanları zorunlu", fg="red")
        enter_weight_label.config(text="Boy ve kilo alanları zorunlu", fg="red")
    elif body_height_entry.get().isdecimal() == False or body_weight_entry.get().isdecimal() == False:
        enter_height_label.config(text="Sayı değeri giriniz", fg="red")
        enter_weight_label.config(text="Sayı değeri giriniz", fg="red")
    else:
        enter_height_label.config(text="Boyunuzu giriniz(cm): ", fg="#000000")
        enter_weight_label.config(text="Kilonuzu giriniz: ", fg="#000000")
        bmi_calculator()
        check_bmi_category()
        result_label.config(text=f"BMI Değeriniz: {user_bmi} \n \n {bmi_category}")

#---------Height Label------------
enter_height_label = Label(text="Boyunuzu giriniz(cm): ", fg="#000000", font=FONT)
enter_height_label.config()
enter_height_label.grid(row=1, column=1, padx=50, pady=5)

#---------Height Entry------------
body_height_entry = Entry(width=20)
body_height_entry.grid(row=2, column=1, padx=50, pady=5)
user_body_height = body_height_entry.get()

#---------Weight Label------------
enter_weight_label = Label(text="Kilonuzu giriniz: ", fg="#000000", font=FONT)
enter_weight_label.config()
enter_weight_label.grid(row=3, column=1, padx=50, pady=5)

#---------Weight Entry------------
body_weight_entry = Entry(width=20)
body_weight_entry.grid(row=4, column=1, padx=50, pady=5)

#-------------Button---------------
button = Button(text="Hesapla", width=17, command=entry_validation)
button.config(pady=5)
button.grid(row=5, column=1, padx=50, pady=5)

#---------Result Label------------
result_label = Label(font=("Verdana", 12, "normal"))
result_label.grid(row=6, column=1, padx=20, pady=20)


window.mainloop()
