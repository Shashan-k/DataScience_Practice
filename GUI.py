# Import tkinter - already comes with python tkinter
# will create a login window
# Creating a simple window through tkinter

from tkinter import *

#for 6.(Have to install the library from(pip install pillow))
from PIL import ImageTk,Image

from tkinter import messagebox # For 15th
#For 15th
# Need to fetch data from both the field then display 1 window else display another window
def handle_login():
    #print("Login clicked")
    email = email_input.get()
    password = password_input.get()
    #print(email,password)
    # write the check
    if email =='shashank@gmail.com' and password == '1234':     # Import (from tkinter import messagebox)
        messagebox.showinfo('Yay','Login Successful')
    else:
        messagebox.showerror("Error",'Login Failed')



# 1. After below code , call mainloop()
root = Tk() # object of Tk class, can access every methods inside a Tk class

root.title('Login Form') # 1. changing the title of the window
# 2.TO change the icon on the top left.
root.iconbitmap('youtube.ico')

# 3.Controlling the size of the window- to restrict it from a particular size
# root.minsize(400,400)
# root.maxsize(600,600)

# 4. To give a particular geometry size
root.geometry('350x500') # For a login window, keeping the width small and the height more

# 5. Background color
root.configure(background='blue')

# 6. for adding an image in the window
#img = ImageTk.PhotoImage(Image.open('download_flipkart.png'))

# 7. Resizing the image
img = Image.open(('download_flipkart.png'))
resize_img = img.resize((70,70))
img = ImageTk.PhotoImage(resize_img)

#Need to be placed on our window. So we need to use a label for it(label can be used to print img as well as text)
img_label = Label(root,image=img)
# You have to explicitly place over the GUI (using geometry manager(GM)- this GM will decide where to place the items in a screen)
#img_label.pack() # Might have to resize the image move to 7.
img_label.pack(pady=(10,10)) # After 7.

# 8. Write text below the image -  we will use label again Label(root,text='Flipkart')()
text_label = Label(root,text='Flipkart', fg='white', bg = 'blue')  # 9.No Params 1st-> color of text should be white and text bg shouldn't white and increase text size
text_label.pack()
text_label.config(font=('verdana',24)) # 10. To change font type and size -> you can also do bold italics.(Do it yourself!)

# 11. To make a login form - we need a text box for email -> for password -> Login button
email_label = Label(root,text='Enter Email', fg = 'white', bg='blue')
email_label.pack(pady=(20,5))
email_label.config(font=('Verdana',12))

# 12. need a entry box for entering the email
email_input = Entry(root,width = 50) # take only root 1st -> increase width of the box
email_input.pack(ipady=6,pady=(1,15)) # ipady for increasing height and pady for increasing space below

#13. Copy entire thing for password textbox
password_label = Label(root,text='Enter Password', fg = 'white', bg='blue')
password_label.pack(pady=(20,5))
password_label.config(font=('Verdana',12))
password_input = Entry(root,width = 50) # take only root 1st -> increase width of the box
password_input.pack(ipady=6,pady=(1,15))

# 14. Adding login button
login_btn = Button(root,text='Login Now',bg='white',fg = 'black',width=20,height=2,command = handle_login) # Add command attribute for 15.
login_btn.pack(pady=(10,20))
login_btn.config(font=('verdana',12))

# 15. Adding a functionality to check if email is "shashank@gmail" and password is 1234 the Open another window and display "Login Successful"
# Need to add command attribute inside button and go at the top to define the function


root.mainloop() # 1. will keep the GUI consistently on the screen
# you will see the first GUI window
# Use this window as per your choice


## Download a .ico
## Downlaod a png (flipkart)
