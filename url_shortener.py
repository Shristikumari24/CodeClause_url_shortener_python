import pyshorteners
from tkinter import *
win = Tk()
win.geometry("900x770")
win.configure(bg="grey")
#Button function
def short():
    url = entry.get()
    s = pyshorteners.Shortener().tinyurl.short(url)

    entry1.insert(END,s)
Label(win,text=" URL SHORTENER",font="impack 25 bold",bg="black",fg="white").pack(fill="x")
#Label for entering user url
Label(win,text="Enter Your URL Link",font="impack 17 bold",bg="grey",fg="black",pady=15).pack(fill="x")
#Entry box
entry = Entry(win,font="10",bd=3,width=60)
entry.pack(pady=20)
#Button
Button(win,text="Click Me",font="impack 12 bold",bg="black",fg="white",width="15",command=short).pack()
#Entry
entry1 = Entry(win,font="impack 16 bold",bg="grey",width=44,)
entry1.pack(pady=30)
mainloop()