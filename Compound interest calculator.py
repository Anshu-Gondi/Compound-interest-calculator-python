from tkinter import *
from PIL import Image, ImageTk
import locale

# Set locale to Indian format for currency
locale.setlocale(locale.LC_ALL, 'en_IN.UTF-8')

# Function for clearing the contents of all entry boxes
def clear_all():
    principal_field.delete(0, END)
    rate_field.delete(0, END)
    time_field.delete(0, END)
    compound_field.delete(0, END)

    # set focus on principal_field entry box
    principal_field.focus_set()

# Function to calculate compound interest and display in INR format
def calculate_ci():
    # get content from entry boxes
    principal = int(principal_field.get())
    rate = float(rate_field.get())
    time = int(time_field.get())

    # Calculate compound interest
    CI = principal * (pow((1 + rate / 100), time))

    # Format CI in Indian currency format (INR)
    formatted_CI = locale.currency(CI, grouping=True)

    # Insert the value in the text entry box
    compound_field.delete(0, END)  # Clear previous result
    compound_field.insert(10, formatted_CI)

# Driver code
if __name__ == "__main__":
    # Create a GUI window
    root = Tk()

    # set the name of tkinter GUI window
    root.title("Compound Interest Calculator")
    root.geometry('1200x1200')

    # Background Image 
    bg = PhotoImage(file='CI.png')
    label007 = Label(root, image=bg)
    label007.place(x=0, y=0)

    # Labels
    label1 = Label(root, text="Principal Amount (Rs) : ", fg='white', bg='blue')
    label2 = Label(root, text="Rate (%) : ", fg='white', bg='blue')
    label3 = Label(root, text="Time (years) : ", fg='white', bg='blue')
    label4 = Label(root, text="Compound Interest : ", fg='white', bg='blue')

    # Packing labels
    label1.grid(row=1, column=0, padx=10, pady=10)
    label2.grid(row=2, column=0, padx=10, pady=10)
    label3.grid(row=3, column=0, padx=10, pady=10)
    label4.grid(row=5, column=0, padx=10, pady=10)

    # Create entry boxes for user input
    principal_field = Entry(root)
    rate_field = Entry(root)
    time_field = Entry(root)
    compound_field = Entry(root)

    # Packing entry boxes
    principal_field.grid(row=1, column=1, padx=10, pady=10)
    rate_field.grid(row=2, column=1, padx=10, pady=10)
    time_field.grid(row=3, column=1, padx=10, pady=10)
    compound_field.grid(row=5, column=1, padx=10, pady=10)

    # Buttons
    button1 = Button(root, text='Submit', fg='white', bg='green', command=calculate_ci)
    button1.grid(row=4, column=1, pady=10)

    button2 = Button(root, text="Clear", bg='red', fg='white', command=clear_all)
    button2.grid(row=6, column=1, pady=10)

    # Start the GUI
    root.mainloop()
