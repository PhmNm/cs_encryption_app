import tkinter as tk
from tkinter import messagebox

import hashlib

window_height = 400
window_width = 600
class User:
    def __init__(self, info: dict):
        self.id = info['id']
        self.fullname=info['info']['fullname']
        self.email=info['info']['email']
        self.password=info['info']['email']
        self.phone=info['info']['phone']
        self.dob=info['info']['dob']


def userPage(mainframe: tk.Frame, email, password):

    try:
        mainframe.children['loginframe'].forget()
        user_page_frame = tk.Frame(mainframe, name='userpage', width=window_width, height=window_height)

    except:
        user_page_frame = tk.Frame(mainframe, name='userpage', width=window_width, height=window_height)

    user_page_frame.pack(fill='both', expand=1)
    user_page_header_frame = tk.Frame(user_page_frame,width=100)
    
    ulabel = tk.Label(user_page_header_frame, text='USER INFORMATION',
                    font=('Verdana',18,'bold'))
    u_email = tk.Label(user_page_header_frame, text=f'Email: {email}')
    u_password = tk.Label(user_page_header_frame, text=f'Password: {password}')

    user_page_header_frame.pack(fill='both')

    ulabel.grid(row=0, column=0)
    u_email.grid(row=1, column=0)

    u_password.grid(row=1, column=1)

    user_page_content_frame = tk.Frame(user_page_frame)
    func_label = tk.Label(user_page_content_frame, text='MENU',
                        font=('Verdana',18,'bold'))

    user_page_content_frame.pack(fill='both')
    func_label.grid(row=0, column=0)

