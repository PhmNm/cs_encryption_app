import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry

import json, os
import uuid
import datetime

from components.user import User, user_page
from components.utils import *

window_height = 400
window_width = 600


def login_page(mainframe: tk.Frame):
    loginframe = tk.Frame(
        mainframe,
        name='loginframe',
        width=window_width,
        height=window_height
    )
    try:
        for frame in mainframe.children.values():
            frame.forget()
    except:
        mainframe.children['loginframe'].pack(fill="both", expand=1)

    loginframe = mainframe.children['loginframe']
    login_contentframe = tk.Frame(loginframe, padx=130, pady=10)

    login_label = tk.Label(
        login_contentframe,
        text='USER LOGIN',
        font=('', 24, 'bold'),
        padx=5,
        pady=20,
        width=10
    )

    email_label = tk.Label(
        login_contentframe,
        text='Email:', 
        font=('Verdana',14)
    )
    password_label = tk.Label(
        login_contentframe,
        text='Password:', 
        font=('Verdana',14)
    )

    email_entry = tk.Entry(login_contentframe, font=('Verdana',14))
    password_entry = tk.Entry(login_contentframe, font=('Verdana',14), show='*')

    login_button = tk.Button(
        login_contentframe,
        text="Login",
        font=('Verdana',10),
        bg='#2980b9',
        fg='#fff',
        padx=10,
        pady=10,
        width=8
    )

    go_register_label = tk.Label(
        login_contentframe, 
        text="Don't have an account? Create one", 
        font=('Verdana',10),
        fg='red'
    )

    mainframe.pack(fill='both', expand=1)
    loginframe.pack(fill='both', expand=1)
    login_contentframe.pack(fill='both', expand=1)

    login_label.grid(row=0, column=0, columnspan=3)

    email_label.grid(row=1, column=0, pady=10)
    email_entry.grid(row=1, column=1)

    password_label.grid(row=2, column=0, pady=10)
    password_entry.grid(row=2, column=1)

    def validate_login(): #handle click
        users = dict()
        success = False
        if os.path.exists('data/users_log_data.json'):
            with open('data/users_log_data.json', 'r', encoding='utf-8') as input:
                users  = json.load(input)
        if users:
            email = email_entry.get().strip()
            password = password_entry.get().strip()

            for i in users['data']:
                if i['key'] == email:
                    from_dir = i['info']['password']
                    if validate_password(password, from_dir):
                        user = User(i)
                        user_page(mainframe, user)
                        success = True
                        break

            print("Email entered: ", email)
            print("Password entered: ", password)
        if success == False:
            messagebox.showerror(title='LỖI', message='Sai Email hoặc Mật khẩu!\nVui lòng nhập lại!')
            login_page(mainframe)
        
    login_button.grid(row=3, column=0, columnspan=2, pady=30)
    login_button.bind("<Return>", (lambda e: validate_login))
    login_button['command'] = validate_login
    
    go_register_label.grid(row=4, column=0, columnspan=3, pady=20)

    go_register_label.bind("<Button-1>", lambda page: signup_page(mainframe))

def signup_page(mainframe: tk.Frame):
    registerframe = tk.Frame(
        mainframe,
        name='registerframe',
        width=window_width,
        height=window_height
    )

    try:
        for frame in mainframe.children.values():
            frame.forget()
    except:
        mainframe.children['registerframe'].pack(fill="both", expand=1)
    # mainframe.children['loginframe'].forget()
    mainframe.children['registerframe'].pack(fill="both", expand=1)

    registerframe = mainframe.children['registerframe']
    register_contentframe = tk.Frame(registerframe, padx=130, pady=15)

    signup_label = tk.Label(
        register_contentframe,
        text='USER SIGN UP',
        font=('', 24, 'bold'),
        padx=20,
        pady=5,
        width=15
    )
    fullname_label_rg = tk.Label(
        register_contentframe,
        text='Họ và tên:', 
        font=('Verdana',12)
    )
    email_label_rg = tk.Label(
        register_contentframe,
        text='Email:', 
        font=('Verdana',12)
    )
    password_label_rg = tk.Label(
        register_contentframe,
        text='Password:', 
        font=('Verdana',12)
    )
    confirmpass_label_rg = tk.Label(
        register_contentframe,
        text='Re-Password:', 
        font=('Verdana',12)
    )
    phone_label_rg = tk.Label(
        register_contentframe,
        text='SĐT:', 
        font=('Verdana',12)
    )
    dob_label_rg = tk.Label(
        register_contentframe,
        text='Ngày sinh:', 
        font=('Verdana',12)
    )


    fullname_entry_rg = tk.Entry(
        register_contentframe,
        font=('Verdana',12),
        width=22
    )
    email_entry_rg = tk.Entry(
        register_contentframe,
        font=('Verdana',12),
        width=22
    )
    password_entry_rg = tk.Entry(
        register_contentframe,
        font=('Verdana',12),
        width=22, 
        show='*'
    )
    confirmpass_entry_rg = tk.Entry(
        register_contentframe,
        font=('Verdana',12),
        width=22, 
        show='*'
    )
    phone_entry_rg = tk.Entry(
        register_contentframe,
        font=('Verdana',12),
        width=22
    )
    now = datetime.datetime.now()
    dob_entry_rg = DateEntry(
        register_contentframe,
        width=34,
        date_pattern='dd/mm/yyyy',
        year=now.year,
        month=now.month,
        day=now.day
    )

    register_button = tk.Button(
        register_contentframe,
        text="Register",
        font=('Verdana',14),
        bg='#2980b9',
        fg='#fff',
        padx=25,
        pady=10,
        width=25
    )

    go_login_label = tk.Label(
        register_contentframe, 
        text="Already have an account? Sign in" , 
        font=('Verdana',10),fg='red'
    )

    register_contentframe.pack(fill='both', expand=1)
    
    signup_label.grid(row=0, column=0, columnspan=3)

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
    
    def validate_signup(): #handle click
        email, password = '',''
        email = email_entry_rg.get().strip()
        password = password_entry_rg.get().strip()
        confirmpass = confirmpass_entry_rg.get().strip()

        print("Fullname entered: ", fullname_entry_rg.get().strip())
        print("Email entered: ", email_entry_rg.get().strip())
        print("Password entered: ", password_entry_rg.get().strip())
        print("Pass confirmed entered: ", confirmpass_entry_rg.get().strip())
        print("Phone entered: ", phone_entry_rg.get().strip())
        print("Date of birth enterd: ", dob_entry_rg.get_date())

        users = dict()
        if not os.path.exists('data/'):
            os.mkdir('data/')
        if os.path.exists('data/users_log_data.json'):
            with open('data/users_log_data.json', 'r', encoding='utf-8') as input:
                users  = json.load(input)
        if not users:
            users['data'] = []
        if email and password: # check valid input data
            if email in [i['key'] for i in users['data']]:
                messagebox.showerror(message='Email đã tồn tại')
            elif confirmpass != password:
                messagebox.showerror(message='Nhập lại mật khẩu sai')
            else:
                storage_name = str(uuid.uuid4())
                while os.path.exists('data/'+ storage_name):
                    storage_name = str(uuid.uuid4())
                os.mkdir('data/' + storage_name)
                # generate salt
                hashed_password = hash_password(password)
                user ={
                    'key': email,
                    'info':{
                        'fullname':fullname_entry_rg.get().strip(),
                        'email': email,
                        'password': hashed_password,
                        'phone': phone_entry_rg.get().strip(),
                        'dob': str(dob_entry_rg.get_date()),
                        'storage': storage_name
                    }
                }
                users['data'].append(user)
                with open('data/users_log_data.json','w+',encoding='utf-8') as outputfile:
                    json.dump(users, outputfile,indent=4, ensure_ascii=False)
                messagebox.showinfo(title='CHÚC MỪNG', message='Đăng kí thành công')
        else:
            messagebox.showerror(title='LỖI', message='Thiếu email hoặc password')
        login_page(mainframe)


    register_button.grid(row=7, column=0, columnspan=2, pady=10)
    register_button['command'] = validate_signup

    go_login_label.grid(row=8, column=0, columnspan=3)

    go_login_label.bind("<Button-1>", lambda page: login_page(mainframe))
