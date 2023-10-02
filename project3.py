#Author name-Ranshiv Kumar

#Importing in-built modules 
import tkinter
from tkinter import *
from timeit import default_timer as timer
import random
window=tkinter.Tk()
#Setting GUI window's geometry
window.geometry("500x500")
#Alotting max-min width and height respectively for tkinter window
window.maxsize(width=800, height=600)
window.minsize(width=800,height=600)
#Title for tkinter window
window.title("Typing speed Test")
#background color -> red
window.configure(bg="green")
# Creating Function
def __design__():
    sentences=['The quick brown fox jumps over a lazy dog','Albus Dumbeldore is a part of fantasy novel Harry Potter written by JK Rowling',
               'Earth is the 5th largest planet in the solar syatem.','Moon''s Largest Crater Name is South pole Aitkin Basin',
               'Parker solar probe is the fastest moving probe till date.']
    sentence=random.choice(sentences)
    begin=timer()
    #Creating label and placing the location of the label
    label1=Label(window,text=sentence,fg="orange",font='times 18')
    label1.grid(row=0,column=2,sticky=W)
    label2=Label(window,text='Start Typing',font="times 20")
    label2.place(x=300,y=40)
    label3=Label(window,text='',font='times 16')
    label3.place(x=320,y=85)
    #Making entry boxes where user can enter the data
    entry = tkinter.Entry(window,bd=7,width=50)
    entry.place(x=220,y=200)
    
    def check():
        if entry.get()==sentence:
            end= timer()
            label3.configure(text=f'Time : {round((end-begin),4)}s')
        else :
            label3.configure(text='You have entered the wrong input')
    button1=tkinter.Button(window,text='Submit',command=check,width = 14,bg='sky blue')
    button1.place(x=280,y=400)
    button2=tkinter.Button(window,text='Reset',command=check,width=14,bg='grey')
    button2.place(x=400,y=400)

__design__()
window.mainloop()

