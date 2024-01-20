import tkinter as tk
from tkinter import messagebox
import random
import boto3

from sendmail import send_otp
from sendmail import send_report

##window detailed
window = tk.Tk()
width= window.winfo_screenwidth() 
height= window.winfo_screenheight()
window.geometry("%dx%d" % (width, height))
window.title('Login')

#vars
uname_strvar = tk.StringVar()
otp_var = tk.IntVar()

#arrs
reg_nums = ['9502092440']
#functioning

def create_otp_win():

    otp_win = tk.Toplevel(window)
    otp_win.title("enter otp")

    otp_label = tk.Label(otp_win, text="Enter OTP:", font=("Helvetica", 12))
    otp_label.pack(pady=5)

    otp_entry = tk.Entry(otp_win, font=("Helvetica", 12), textvariable=otp_var)
    otp_entry.pack(pady=10)

    verify_otp_button = tk.Button(otp_win, text="Verify OTP", font=("Helvetica", 12))
    verify_otp_button.pack(pady=10)

def printgenerating():
    checkvar = uname_strvar.get()
    if checkvar in reg_nums:
        send_otp()
        create_otp_win()
    
        
    else:
        send_report(checkvar)
        messagebox.showerror(title="Error",message="Number is not registered")
        messagebox.showwarning(title="reported",message="Reported to the root user")








##labels
headlabel = tk.Label(window,text= "Enter the details" , font =("Helvetica",35))
headlabel.place(x=470,y=36)

uname = tk.Label(window,text="Registered phone number or Email",font =("Helvetica",24))
uname.place(x= 200, y= 196)

#entries
uname_entry = tk.Entry(window,font=("Helvetica",24),textvariable=uname_strvar)
uname_entry.place(x = 710,y=196)


#buttons
get_otp_but = tk.Button(window,font=("Helvetica",24),command=printgenerating,text="get otp")
get_otp_but.place(x = 710, y = 300)









window.mainloop()

