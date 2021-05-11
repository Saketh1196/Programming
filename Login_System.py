import os
import tkinter as tk

sys = tk.Tk()

def register_user():

    username_info = username.get()
    password_info = password.get()

    file = open(username_info+".txt", 'w')  # The details are stored in text file when registered.
    file.write(username_info+"\n")
    file.write(password_info)
    file.close()

    a.delete(0)
    b.delete(0)

    tk.Label(reg, text='Registration Successful', fg='green', font=('times new roman',15)).pack()

def register_file():
    global reg
    reg = tk.Toplevel(sys)
    reg1 = tk.Canvas(reg, height=30, width=80)
    reg1.pack()

    global username
    global password
    global a
    global b
    username = tk.StringVar()
    password = tk.StringVar()

    tk.Label(reg, text='Please Enter your details below', font=('times new roman',15)).pack()

    tk.Label(reg,text='Username', font=('times new roman',15)).pack()
    a = tk.Entry(reg,textvariable= username)
    a.pack()
    tk.Entry(reg, text=" ")

    tk.Label(reg,text='Password',font=('times new roman',15)).pack()
    b = tk.Entry(reg,textvariable=password)
    b.pack()
    tk.Entry(reg, text=" ")

    tk.Button(reg, text='Register', width=15, height=1, command=lambda: register_user()).pack()


def login_file():
    global login
    login = tk.Toplevel(sys)
    login1 = tk.Canvas(login, height=30, width=80)
    login1.pack()

    tk.Label(login, text='Please Enter your Login details below', font=('times new roman', 15)).pack()

    global username_verify
    global password_verify
    global user_entry_login
    global pass_entry_login
    username_verify = tk.StringVar()
    password_verify = tk.StringVar()

    tk.Label(login, text='Username', font=('times new roman', 15)).pack()
    user_entry_login = tk.Entry(login, textvariable=username_verify)
    user_entry_login.pack()
    tk.Entry(reg, text=" ")

    tk.Label(login, text='Password', font=('times new roman', 15)).pack()
    pass_entry_login = tk.Entry(login, textvariable=password_verify)
    pass_entry_login.pack()
    tk.Entry(login, text=" ")

    tk.Button(login, text='Register', width=15, height=1, command=lambda: verify_login()).pack()

def verify_login():
    username1 = username_verify.get()
    password1 = password_verify.get()
    user_entry_login.delete(0)
    pass_entry_login.delete(0)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1= open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_success()
        else:
            login_failed()
    else:
        no_user()

def login_success():
    global success
    success = tk.Toplevel(sys)
    sucess1 = tk.Canvas(success, height=30, width=80)
    sucess1.pack()
    tk.Label(success, text = "Login Successful", font=('times new roman',15)).pack()
    tk.Button(success, text="ok",command=lambda:delete1()).pack()

def delete1():
    success.destroy()

def login_failed():
    global failed
    failed = tk.TOP(sys)
    failed1 = tk.Canvas(failed, height=30,width=80)
    failed1.pack()
    tk.Label(failed, text='Incorrect Password', font=('times new roman',15)).pack()
    tk.Button(failed, text="ok", command=lambda: delete2()).pack()

def delete2():
    failed.destroy()

def no_user():
    global user
    user = tk.Toplevel(sys)
    user1 = tk.Canvas(user, height=30,width=80)
    user1.pack()
    tk.Label(user, text='No user found', font=('times new roman',15)).pack()
    tk.Button(user, text="ok", command=lambda: delete3()).pack()

def delete3():
    user.destroy()

# height and width of the interface
h = 500
w = 600

# size of interface
canvas = tk.Canvas(sys, height=h, width=w, bg='red')
canvas.pack()

img = tk.PhotoImage(file="img.png")
bg_img = tk.Label(sys, image=img)
bg_img.place(relwidth=1, relheight=1)

# Creating a label for 'Login Credentials'
label = tk.Label(sys, text='Login Credentials', bg='dark green', fg='black', font=('Times new Roman', 20))
label.place(relwidth=1, relheight=0.1)

# Frame for 'Username'
frame = tk.Frame(sys, bg="white")
frame.place(relx=0.2, rely=0.35, relwidth=0.6, relheight=0.1)

# Creating a label for 'Username'
user_label = tk.Label(frame, text='Username: ', bg='white', fg='black', font=('Times new Roman', 15), bd=2)
user_label.place(relwidth=0.5, relheight=1)

# Entry for the 'Username'
user_entry = tk.Entry(frame, font=30, bd=5)
user_entry.place(relx=0.5, relwidth=0.9, relheight=1)

# Frame for 'Password'
frame1 = tk.Frame(sys, bg="white")
frame1.place(relx=0.2, rely=0.5, relwidth=0.6, relheight=0.1)

# Creating a label for 'Password'
pass_label = tk.Label(frame1, text='Password: ', bg='white', fg='black', font=('Times new Roman', 15), bd=2)
pass_label.place(relwidth=0.5, relheight=1)

# Entry for the 'Password'
pass_entry = tk.Entry(frame1, font=30, bd=5)
pass_entry.place(relx=0.5, relwidth=0.9, relheight=1)

# Button for 'Login'
button = tk.Button(sys, text='Login', font=('Times new Roman', 12), activebackground='blue',
                   command=lambda: login_file())
button.place(relx=0.3, rely=0.65, relwidth=0.15, relheight=0.09)

# Button for 'Register'
button1 = tk.Button(sys, text='Register', font=('Times new Roman', 12), activebackground='blue',
                    command=lambda: register_file())
button1.place(relx=0.57, rely=0.65, relwidth=0.15, relheight=0.09)

sys.mainloop()
