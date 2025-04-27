from customtkinter import *
from PIL import Image
from tkinter import messagebox

def login():
    if usernameEntry.get() == '' or passwordEntry.get() == '':
        messagebox.showerror('Error', "All fields are required")
    elif usernameEntry.get() == 'dan' and passwordEntry.get() == '123':
        messagebox.showinfo('Success', 'Login is successful')
        root.destroy()
        import ems
    else:
        messagebox.showerror('Error', 'Wrong credentials')

def exit_program():
    root.quit()  # Exits the program

root = CTk()

# Set window size
root.geometry('736x736')

# Get screen width and height to center the window
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate position to center the window
x = (screen_width // 2) - (736 // 2)
y = (screen_height // 2) - (736 // 2)

# Position the window at the calculated position
root.geometry(f'736x736+{x}+{y}')

root.resizable(0, 0)
root.title('Login Module')

# Background image
image = CTkImage(Image.open(r"C:\Users\Dandy\Downloads\penthouse.jpg"), size=(736, 736))
imageLabel = CTkLabel(root, image=image, text='')
imageLabel.place(x=210, y=0)

# Heading
headinglabel = CTkLabel(root, text='Employee Management System')
headinglabel.place(x=20, y=100)

# Username Entry
usernameEntry = CTkEntry(root, placeholder_text='Enter your Username')
usernameEntry.place(x=50, y=150)

# Password Entry
passwordEntry = CTkEntry(root, placeholder_text='Enter your Password', show='*')
passwordEntry.place(x=50, y=200)

# Login Button
loginButton = CTkButton(root, text='Login', cursor='hand2', command=login)
loginButton.place(x=50, y=250)

# Exit Button (colored)
exitButton = CTkButton(root, text='Exit', cursor='hand2', command=exit_program, fg_color="red", hover_color="darkred")
exitButton.place(x=50, y=300)

root.mainloop()
