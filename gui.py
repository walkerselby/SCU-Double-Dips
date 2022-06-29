from tkinter import *
import tkinter.messagebox

def validate(): 
    quarter = c.get()  
    if (quarter== "Select academic quarter:"):
        tkinter.messagebox.showinfo("Invalid Message Alert","Field cannot be left empty!")

    else:
        tkinter.messagebox.showinfo("Success Message","Successfully downloaded!")  
        print(quarter)

if __name__ == "__main__":  
    root = Tk()
    root.resizable(0,0)
    root.geometry("500x350")
    root.title("SCU Core Double Dips") 

    label_0 = Label(root, text="SCU Core Double Dips",bg="#FF7C80",fg="white",width=20,font=("bold", 20))
    label_0.place(x=90,y=53) 

    label_1 = Label(root, text="Quarter",width=20,font=("bold", 10))
    label_1.place(x=70,y=180)

    list1 = ["Fall 2022", "Summer 2022", "Spring 2022", "Winter 2022", "Fall 2021"]
    c=StringVar()
    droplist=OptionMenu(root,c, *list1)
    droplist.config(width=22)
    c.set("Select academic quarter:") 
    droplist.place(x=240,y=180) 

    Button(root, text="Download",width=20,bg="#FF7C80",fg="white", command = validate).place(x=180,y=280)

    root.mainloop()