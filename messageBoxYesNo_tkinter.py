from tkinter import *
from tkinter import ttk
from tools import *
from tkinter import messagebox
form =Tk()
form.geometry("700x500")
tkcenter(form)

def test():
    ans =messagebox.askyesno("","Doyou want test ?")
    print(ans)
Label(form,text ="this is form for test yes or no").pack()
Button(form,text="Test Now",command =test).pack()

    

bg = "navy"
bgall(form,bg)
fg ="lightblue"
fgall(form,fg)
font ="None 30 bold"
fontall(form,font)

form.mainloop()
