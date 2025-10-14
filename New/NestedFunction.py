#Pass a function inside another funcion that prnts something
import tkinter as tk

def OuterFunction():
    print('Outer Function')

    def InnerFunction():
        print('Inner Function')
        
    InnerFunction()

w=tk.Tk()
w.title('Start?')
w.geometry('110x20')

yes=tk.Button(w,text='Run Nested Functions',command=OuterFunction)
yes.pack()
w.mainloop()