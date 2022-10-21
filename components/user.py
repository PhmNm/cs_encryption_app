import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry

import os, json
from datetime import datetime

# import hashlib

window_height = 400
window_width = 600
class User:
    def __init__(self, info: dict):
        self.fullname=info['info']['fullname']
        self.email=info['info']['email']
        self.password=info['info']['email']
        self.phone=info['info']['phone']
        self.dob=info['info']['dob']

def user_page(mainframe: tk.Frame, user: User):

    try:
        mainframe.children['loginframe'].forget()
        user_page_frame = tk.Frame(mainframe, name='userpage', width=window_width, height=window_height)

    except:
        user_page_frame = tk.Frame(mainframe, name='userpage', width=window_width, height=window_height)

    user_page_frame.pack(fill='both', expand=1)
    user_page_header_frame = tk.Frame(user_page_frame, padx = 80,
                                    highlightthickness=3, highlightbackground='black')
    
    ulabel = tk.Label(user_page_header_frame, text='THÔNG TIN TÀI KHOẢN',
                    font=('Verdana',18,'bold'))
    u_fullname = tk.Label(user_page_header_frame, text=f'Họ tên: {user.fullname}',
                        font=('Verdana',12))
    u_email = tk.Label(user_page_header_frame, text=f'Email: {user.email}',
                    font=('Verdana',12))
    u_phone = tk.Label(user_page_header_frame, text=f'SĐT: {user.phone}',
                    font=('Verdana',12))
    u_dob = tk.Label(user_page_header_frame, text=f'Ngày sinh: {user.dob}',
                    font=('Verdana',12))

    user_page_header_frame.pack(fill='both')

    ulabel.grid(row=0, column=0, columnspan=3, sticky='w', padx=65)

    u_fullname.grid(row=1, column=0, sticky='w')
    u_email.grid(row=1, column=2, sticky='w', padx=120)
    u_phone.grid(row=2, column=0, sticky='w')
    u_dob.grid(row=2, column=2, sticky='w', padx=120)


    ### Menu panel
    user_page_content_frame_left = tk.Frame(user_page_frame, width=50)
    func_label = tk.Label(user_page_content_frame_left, text='MENU',
                        font=('Verdana',18,'bold'))
    update_button = tk.Button(user_page_content_frame_left, text='Cập nhật thông tin',
                            width=25)
    encrypt_send_button = tk.Button(user_page_content_frame_left, text='Chọn và mã hoá tập tin',
                            width=25)
    decrypt_receive_button = tk.Button(user_page_content_frame_left, text='Giải mã tập tin',
                            width=25)
    sign_file_button = tk.Button(user_page_content_frame_left, text='Ký trên tập tin',
                            width=25)
    confirm_sign_button = tk.Button(user_page_content_frame_left, text='Xác nhận chữ ký',
                            width=25)
    log_out_button = tk.Button(user_page_content_frame_left, text='Đăng xuất',
                            width=25)
    user_page_content_frame_left.pack(fill='both',side = 'left', padx=20, pady=20)
    func_label.grid(row=0, column=0, columnspan=3)
    update_button.grid(row=1, column=0, pady=5)
    encrypt_send_button.grid(row=2, column=0, pady=5)
    decrypt_receive_button.grid(row=3, column=0, pady=5)
    sign_file_button.grid(row=4, column=0, pady=5)
    confirm_sign_button.grid(row=5, column=0, pady=5)
    log_out_button.grid(row=6,column=0, pady=5)
    ### Content panel
    user_page_content_frame_right = tk.Frame(user_page_frame,highlightthickness=2, bg='white',
                                            highlightbackground='black', width=360, height=290)
    user_page_content_frame_right.pack(pady=10, side='left', ipady=40)
    user_page_content_frame_right.grid_propagate(False)

    def logout():
        try:
            for frame in mainframe.children.values():
                frame.forget()
            print(os.getcwd())
            mainframe.children['loginframe'].pack(fill="both", expand=1)

        except:
            mainframe.children['loginframe'].pack(fill="both", expand=1)
            # login_page(mainframe)
    
    def update_user():
        bounded_user = user
        fullname_label_rg = tk.Label(user_page_content_frame_right, text='Họ và tên:', 
                            font=('Verdana',8))
        email_label_rg = tk.Label(user_page_content_frame_right, text='Email:', 
                                    font=('Verdana',8))
        password_label_rg = tk.Label(user_page_content_frame_right, text='Password:', 
                                    font=('Verdana',8))
        confirmpass_label_rg = tk.Label(user_page_content_frame_right, text='Re-Password:', 
                                        font=('Verdana',8))
        phone_label_rg = tk.Label(user_page_content_frame_right, text='SĐT:', 
                                font=('Verdana',8))
        dob_label_rg = tk.Label(user_page_content_frame_right, text='Ngày sinh:', 
                                font=('Verdana',8))

        fullname_entry_rg = tk.Entry(user_page_content_frame_right, width=30,
                                    font=('Verdana',8),
                            )
        email_entry_rg = tk.Label(user_page_content_frame_right,
                                text=user.email, font=('Verdana',8),
                            )
        password_entry_rg = tk.Entry(user_page_content_frame_right, width=30,
                                font=('Verdana',8),show='*'
                            )
        confirmpass_entry_rg = tk.Entry(user_page_content_frame_right, width=30,
                                    font=('Verdana',8),show='*'
                            )
        phone_entry_rg = tk.Entry(user_page_content_frame_right, width=30,
                                font=('Verdana',8)
                        )
        dob = datetime.strptime(user.dob, '%Y-%m-%d')
        dob_entry_rg = DateEntry(user_page_content_frame_right, width = 32,
                            year=dob.year, month=dob.month, day=dob.day
                        )
        confirm_button = tk.Button(user_page_content_frame_right,
                            text='Xác nhận', width=20
                        )
        ### pre-fill in values
        fullname_entry_rg.insert(tk.END, user.fullname)
        password_entry_rg.insert(tk.END, user.password)
        phone_entry_rg.insert(tk.END, user.phone)
        ###
        # empty_space = tk.Label(user_page_content_frame_right, bg='white')
        # empty_space.grid(row=0, column=0)
        fullname_label_rg.grid(row=1, column=0, pady=10, padx=10, sticky='w')
        fullname_entry_rg.grid(row=1, column=1, sticky='w')

        email_label_rg.grid(row=2, column=0, pady=10, padx=10, sticky='w')
        email_entry_rg.grid(row=2, column=1, sticky='w')

        password_label_rg.grid(row=3, column=0, pady=10, padx=10, sticky='w')
        password_entry_rg.grid(row=3, column=1, sticky='w')

        confirmpass_label_rg.grid(row=4, column=0, pady=10, padx=10, sticky='w')
        confirmpass_entry_rg.grid(row=4, column=1, sticky='w')

        phone_label_rg.grid(row=5, column=0, pady=10, padx=10, sticky='w')
        phone_entry_rg.grid(row=5, column=1, sticky='w')

        dob_label_rg.grid(row=6, column=0, pady=10, padx=10, sticky='w')
        dob_entry_rg.grid(row=6, column=1, sticky='w')
        confirm_button.grid(row=7, column=0, columnspan=2, pady=10, padx=100, sticky='w')

        def validateUpdate(): #handle click
            email = bounded_user.email
            password = password_entry_rg.get().strip()
            confirmpass = confirmpass_entry_rg.get().strip()

            with open('data/users_log_data.json', 'r', encoding='utf-8') as input:
                users  = json.load(input)

            if password: # check valid input data
                if confirmpass != password:
                    messagebox.showerror(message='Nhập lại mật khẩu sai')
                else:
                    user_update ={
                        'key': email,
                        'info':{
                            'fullname':fullname_entry_rg.get().strip(),
                            'email': email,
                            'password': password,
                            'phone': phone_entry_rg.get().strip(),
                            'dob': str(dob_entry_rg.get_date()),
                        }
                    }
                    for user in users['data']:
                        if user['key'] == email:
                            user['info'] = user_update['info']
                    with open('data/users_log_data.json','w+',encoding='utf-8') as outputfile:
                        json.dump(users, outputfile,indent=4, ensure_ascii=False)
                    messagebox.showinfo(title='CHÚC MỪNG', message='Chỉnh sửa thông tin thành công')
                    user_page(mainframe, User(user_update))

            else:
                messagebox.showerror(title='LỖI', message='Thiếu password')
        confirm_button['command']=validateUpdate
    log_out_button['command']=logout
    update_button['command']=update_user
