from tkinter import *
from tkinter import filedialog
import tkinter as tk 
from PIL import Image,ImageTk
import os 
from stegano import lsb


root = Tk()

root.title("Steganography--Hide Text in Images")
root.geometry("700x500+150+180")
root.resizable(False,False)
root.configure(bg='#092327')


app_icon = PhotoImage(file='padlock.png')
root.iconphoto(False,app_icon)

logo=PhotoImage(file='logo.png')
Label(root,image=logo,bg='#092327').place(x=10,y=2)

Label(root,text="CyberToolz",bg='#092327',fg='#00A9A5',font='Arial 25 bold').place(x=50,y=0)

first_frame =Frame(root,bd=3,width=340,height=280,relief=GROOVE,bg='#00A9A5')
first_frame.place(x=10,y=40)

first_label = Label(first_frame,bg='black')
first_label.place(x=40,y=10)

second_frame =Frame(root,bd=3,width=340,height=280,relief=GROOVE,bg='#00A9A5')
second_frame.place(x=350,y=40)

first_text = Text(second_frame,font='Robote 20',bg='White',fg='black',relief=GROOVE,wrap=WORD)
first_text.place(x=0,y=0,width=340,height='280')


scrollbar1=Scrollbar(second_frame)
scrollbar1.place(x=325,y=0,height=300)


scrollbar1.configure(command=first_text.yview)
first_text.configure(yscrollcommand=scrollbar1.set)

def open_image():
    global filename
    filename = filedialog.askopenfilename(initialdir=os.getcwd(),
    title='Select Image File',
    filetypes=(('PNG File','*.png'),('Jpeg Files',"*jpg"),('All Files','*txt')))
    img = Image.open(filename)
    img = ImageTk.PhotoImage(image=img)
    first_label.configure(image=img,width=250,height=250)
    first_label.image = img
    
    
def save_image():
    secret.save("Secret.png")
    

    
def hide_data():
    global secret
    message = first_text.get(1.0,END)
    secret = lsb.hide(str(filename),message=message)
    

    
def show_data():
    clear_message = lsb.reveal(filename)
    first_text.delete(1.0,END)
    first_text.insert(END,clear_message)



third_frame = Frame(root,bd=3,relief=GROOVE,width=300,height=100,bg='#092327',)
third_frame.place(x=10,y=370)
Button(third_frame,text="Open Image",width=10,height=2,font='Arial 14 bold',command=open_image).place(x=10,y=30)
Button(third_frame,text="Save Image",width=10,height=2,font='Arial 14 bold',command=save_image).place(x=160,y=30)
Label(third_frame,text='Picture,Image,PhotoFile',bg='#092327',fg='#00A9A5').place(x=70,y=5)



fourth_frame = Frame(root,bd=3,relief=GROOVE,width=300,height=100,bg='#092327',)
fourth_frame.place(x=360,y=370)
Button(fourth_frame,text="Hide Data",width=10,height=2,font='Arial 14 bold',command=hide_data).place(x=10,y=30)
Button(fourth_frame,text="Show Data",width=10,height=2,font='Arial 14 bold',command=show_data).place(x=160,y=30)
Label(fourth_frame,text='Show or Hide Message',bg='#092327',fg='#00A9A5').place(x=70,y=5)




root.mainloop()

