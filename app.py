#!!!JUST A TEST!!!
from tkinter import *

#Create window
app = Tk()

#User
user_text = StringVar()
user_label = Label(app, text='Username', font=('bold',8), pady=20)
user_label.grid(row=0, column=0, sticky=W)
user_entry = Entry(app, textvariable=user_text)
user_entry.grid(row=0, column=1)

#Message
msg_text = StringVar()
msg_label = Label(app, text='Message', font=('bold',8))
msg_label.grid(row=1, column=0, sticky=W)
msg_entry = Entry(app, textvariable=msg_text)
msg_entry.grid(row=1, column=1)

app.title("Chat client")
app.geometry("700x350")

#Start program
app.mainloop()