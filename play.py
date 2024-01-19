import tkinter as tk

# Function to print the entered value
def printgenerating():
    uname_sto = uname_strvar.get()
    print("Entered value:", uname_sto)

# Window details
window = tk.Tk()
width = window.winfo_screenwidth() 
height = window.winfo_screenheight()
window.geometry("%dx%d" % (width, height))
window.title('Login')

# Labels
headlabel = tk.Label(window, text="Enter the details", font=("Helvetica", 35))
headlabel.place(x=470, y=36)

uname = tk.Label(window, text="Registered phone number or Email", font=("Helvetica", 24))
uname.place(x=200, y=196)

# StringVar for entry
uname_strvar = tk.StringVar()

# Entry
uname_entry = tk.Entry(window, font=("Helvetica", 24), textvariable=uname_strvar)
uname_entry.place(x=200, y=246)

# Button to trigger the function
submit_button = tk.Button(window, text="Submit", command=printgenerating)
submit_button.place(x=200, y=296)

window.mainloop()
