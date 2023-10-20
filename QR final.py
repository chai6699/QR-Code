import qrcode
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import pyqrcode

app = Tk()
app.title('QR Code Generator')
app.geometry('1050x1050')
app.config(bg='#c183de')

headingFrame = Frame(app,bg="#c291d9",bd=5)
headingFrame.place(relx=0.10,rely=0.05,relwidth=0.7,relheight=0.1)
headingLabel = Label(headingFrame, text="Generate QR Code", fg='black', bg='#c183de', font=('Times',20,'bold'))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

canvas1 = Canvas(app, relief=RIDGE, bd=2,bg='#c291d9')
canvas1.place(relx=0.65,rely=0.20,  relwidth=0.2, relheight=0.2)
def generate():
    if text.get() != '' and name.get() != '':
        qr = pyqrcode.create(text.get())
        img = qr.png(name.get() + ".png", scale=5)
        info = Label( text="Generated QR code", font=('ariel 15 bold'),fg='black', bg='#c183de')
        info.place(x=700, y=410)
        img = Image.open(name.get() + ".png")
        img = ImageTk.PhotoImage(img)
        canvas1.create_image(105,87,anchor=CENTER,image=img)
        canvas1.image = img

    else:
        info = Label( text="Please enter the data for QR code", font=('ariel 15 bold'),fg='black', bg='#c183de')
        info.place(x=700, y=410)

Frame1 = Frame(app,bg="#c183de")
Frame1.place(relx=0.1,rely=0.15,relwidth=0.5,relheight=0.2)

label1 = Label(Frame1,text="Enter the text/URL: ",fg='black', bg='#c183de',font=('Courier',13,'bold'))
label1.place(relx=0.05,rely=0.1, relheight=0.08)

text = Entry(Frame1,font=('Century 12'))
text.place(relx=0.05,rely=0.4, relwidth=1, relheight=0.2)

Frame3 = Frame(app,bg="#c183de")
Frame3.place(relx=0.1,rely=0.35,relwidth=0.5,relheight=0.2)

label3 = Label(Frame3,text="Enter the name of the QR Code: ",fg='black', bg='#c183de',font=('Courier',13,'bold'))
label3.place(relx=0.05,rely=0.2, relheight=0.08)

name = Entry(Frame3,font=('Century 12'))
name.place(relx=0.05,rely=0.4, relwidth=1, relheight=0.2)

button = Button(app, text='Generate Code',font=('Courier',15,'normal'),command=generate)
button.place(relx=0.69,rely=0.43, relwidth=0.15, relheight=0.05)

app.mainloop()
