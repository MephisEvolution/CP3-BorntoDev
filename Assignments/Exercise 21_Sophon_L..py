from tkinter import *
import math

def leftClickButton(event):
    weight = float(textboxWeight.get())
    height = float(textboxHeight.get())
    bmi = weight / math.pow(height /100,2)
    print(bmi)
    labelResult2.configure(text=round(bmi,2))
    if bmi >= 30.0:
        category = "อ้วนมาก"
    elif 25.0 <= bmi <= 29.9:
        category = "อ้วน"
    elif 23.0 <= bmi <= 24.9:
        category = "น้ำหนักเกิน"
    elif 18.6 <= bmi <= 22.9:
        category = "น้ำหนักปกติ เหมาะสม"
    else:
        category = "ผอมเกินไป"

    labelResult3.configure(text=category)

Mainwindow = Tk()

labelHeight = Label(Mainwindow, text="ส่วนสูงของคุณ(หน่วยเซ็นติเมตร Cm.)")
textboxHeight = Entry(Mainwindow)
labelWeight = Label(Mainwindow, text="น้ำหนักของคุณ(หน่วยกิโลกรัม Kg.)")
textboxWeight = Entry(Mainwindow)
calculateButton = Button(Mainwindow, text="Calculate")
labelHeight.grid(row=0, column=0)
labelWeight.grid(row=1, column=0)
textboxHeight.grid(row=0, column=1)
textboxWeight.grid(row=1, column=1)
calculateButton.grid(row=2, column=1)
labelResult = Label(Mainwindow, text="ค่า BMI ของคุณคือ: ")
labelResult.grid(row=3, column=0)
labelResult2 = Label(Mainwindow, text=" ", anchor=E)
labelResult2.grid(row=3, column=1)
labelResult3 = Label(Mainwindow, text=" ", anchor=E)
labelResult3.grid(row=4, column=1)

calculateButton.bind('<Button-1>', leftClickButton)
Mainwindow.mainloop()