from tkinter import *
from tkinter import ttk


def new_root():
    root2 = Tk()
    root2.title("Calculator")
    root2.geometry("300x300")
    
    number_entry = ttk.Entry(root2, width=20)
    number_entry.grid(row=0, columnspan=1)
    
    # command=lambda: 뒤에 명령 작성.
    button1 = ttk.Button(root2, text="1", command=new_root)
    button1.grid(row=1, column=0)
    
    root2.mainloop()

new_root()