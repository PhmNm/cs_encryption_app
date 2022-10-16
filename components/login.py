import tkinter as tk
from tkinter import messagebox
from tkcalendar import Calendar, DateEntry

import json, os
import uuid
import datetime

from user import *

window_height = 400
window_width = 600


def login_page(mainframe: tk.Frame):
    loginframe = tk.Frame(mainframe, name='loginframe', width=window_width, height=window_height)
    try:
        mainframe.children['registerframe'].forget()
    except:
        mainframe.children['loginframe'].pack(fill="both", expand=1)

    loginframe = mainframe.children['loginframe']
    login_contentframe = tk.Frame(loginframe, padx=110, pady=10)

    login_label = tk.Label(login_contentframe, text='USER LOGIN',
                        font=('', 24, 'bold'), padx=5, pady=20, width=10)

    email_label = tk.Label(login_contentframe, text='Email:', 
                            font=('Verdana',14))
    password_label = tk.Label(login_contentframe, text='Password:', 
                            font=('Verdana',14))

    email_entry = tk.Entry(login_contentframe, font=('Verdana',14))
    password_entry = tk.Entry(login_contentframe, font=('Verdana',14), show='*')

    login_button = tk.Button(login_contentframe,text="Login", font=('Verdana',10),
                            bg='#2980b9',fg='#fff', padx=10, pady=10, width=8)

    go_register_label = tk.Label(login_contentframe, 
                        text="Don't have an account? Create one" , 
                        font=('Verdana',10), fg='red')

    mainframe.pack(fill='both', expand=1)
    loginframe.pack(fill='both', expand=1)
    login_contentframe.pack(fill='both', expand=1)

    login_label.grid(row=0, column=0, columnspan=2)

    email_label.grid(row=1, column=0, pady=10)
    email_entry.grid(row=1, column=1)

    password_label.grid(row=2, column=0, pady=10)
    password_entry.grid(row=2, column=1)

    def validateLogin(): #handle click
        email = email_entry.get().strip()
        password = password_entry.get().strip()
        print("Email entered: ", email)
        print("Password entered: ", password)

        
        # mainformwindow = tk.Toplevel(root)
        # app = mainform(mainformwindow)
        # root.withdraw() # hide the root
        # mainformwindow.protocol("WM_DELETE_WINDOW", close_win)
        userPage(mainframe, email, password)
        
    login_button.grid(row=3, column=0, columnspan=2, pady=30)
    login_button['command'] = validateLogin
    
    go_register_label.grid(row=4, column=0, columnspan=2, pady=20)

    go_register_label.bind("<Button-1>", lambda page: signup_page(mainframe))
def signup_page(mainframe: tk.Frame):
    registerframe = tk.Frame(mainframe, name='registerframe', width=window_width, height=window_height)

    mainframe.children['loginframe'].forget()
    mainframe.children['registerframe'].pack(fill="both", expand=1)

    registerframe = mainframe.children['registerframe']
    register_contentframe = tk.Frame(registerframe, padx=110, pady=15)

    signup_label = tk.Label(register_contentframe, text='USER SIGN UP',
                    font=('', 24, 'bold'), padx=20, pady=5, width=15)
    fullname_label_rg = tk.Label(register_contentframe, text='Họ và tên:', 
                                font=('Verdana',12))
    email_label_rg = tk.Label(register_contentframe, text='Email:', 
                                font=('Verdana',12))
    password_label_rg = tk.Label(register_contentframe, text='Password:', 
                                font=('Verdana',12))
    confirmpass_label_rg = tk.Label(register_contentframe, text='Re-Password:', 
                                    font=('Verdana',12))
    phone_label_rg = tk.Label(register_contentframe, text='Phone:', 
                            font=('Verdana',12))
    dob_label_rg = tk.Label(register_contentframe, text='Ngày sinh:', 
                            font=('Verdana',12))


    fullname_entry_rg = tk.Entry(register_contentframe, font=('Verdana',12), width=22)
    email_entry_rg = tk.Entry(register_contentframe, font=('Verdana',12), width=22)
    password_entry_rg = tk.Entry(register_contentframe, font=('Verdana',12), width=22, 
                                show='*')
    confirmpass_entry_rg = tk.Entry(register_contentframe, font=('Verdana',12), width=22, 
                                    show='*')
    phone_entry_rg = tk.Entry(register_contentframe, font=('Verdana',12), width=22)
    now = datetime.datetime.now()
    dob_entry_rg = DateEntry(register_contentframe, width=34,
                            year=now.year, month=now.month, day=now.day)

    register_button = tk.Button(register_contentframe,text="Register", font=('Verdana',14)
                                , bg='#2980b9',fg='#fff', padx=25, pady=10, width=25)

    go_login_label = tk.Label(register_contentframe, 
                            text="Already have an account? Sign in" , 
                            font=('Verdana',10), fg='red')

    register_contentframe.pack(fill='both', expand=1)
    
    signup_label.grid(row=0, column=0, columnspan=2)

    fullname_label_rg.grid(row=1, column=0, pady=5, sticky='e')
    fullname_entry_rg.grid(row=1, column=1)

    email_label_rg.grid(row=2, column=0, pady=5, sticky='e')
    email_entry_rg.grid(row=2, column=1)

    password_label_rg.grid(row=3, column=0, pady=5, sticky='e')
    password_entry_rg.grid(row=3, column=1)

    confirmpass_label_rg.grid(row=4, column=0, pady=5, sticky='e')
    confirmpass_entry_rg.grid(row=4, column=1)

    phone_label_rg.grid(row=5, column=0, pady=5, sticky='e')
    phone_entry_rg.grid(row=5, column=1)

    dob_label_rg.grid(row=6, column=0, pady=5, sticky='e')
    dob_entry_rg.grid(row=6, column=1)
    
    def validateSignup(): #handle click
        email, password = '',''
        email = email_entry_rg.get().strip()
        password = password_entry_rg.get().strip()
        print("Fullname entered: ", fullname_entry_rg.get().strip())
        print("Email entered: ", email_entry_rg.get().strip())
        print("Password entered: ", password_entry_rg.get().strip())
        print("Pass confirmed entered: ", confirmpass_entry_rg.get().strip())
        print("Phone entered: ", phone_entry_rg.get().strip())
        print("Date of birth enterd: ", dob_entry_rg.get_date())
        users = dict()
        if os.path.exists('users_log_data.json'):
            with open('users_log_data.json', 'r', encoding='utf-8') as input:
                users  = json.load(input)
        if not users:
            users['data'] = []
        # for i in users['data']:
        #     print(i['key'])
        if email and password: # check valid input data
            if email in [i['key'] for i in users['data']]:
                messagebox.showerror(message='Email đã tồn tại')
            else:
                user ={
                    'key': email,
                    'infos':{
                        'fullname':fullname_entry_rg.get().strip(),
                        'email': email,
                        'password': password,
                        'phone': phone_entry_rg.get().strip(),
                        'dob': str(dob_entry_rg.get_date())
                    }
                }
                users['data'].append(user)
                with open('users_log_data.json','w+',encoding='utf-8') as outputfile:
                    json.dump(users, outputfile,indent=4, ensure_ascii=False)
                messagebox.showinfo(message='Đăng kí thành công')
        else:
            messagebox.showerror(message='Thiếu email hoặc password')
        login_page(mainframe)


    register_button.grid(row=7, column=0, columnspan=2, pady=10)
    register_button['command'] = validateSignup

    go_login_label.grid(row=8, column=0, columnspan=2)

    go_login_label.bind("<Button-1>", lambda page: login_page(mainframe))
