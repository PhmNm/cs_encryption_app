import tkinter as tk
from tkinter import messagebox

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


def userPage(mainframe: tk.Frame, user: User):

    try:
        mainframe.children['loginframe'].forget()
        user_page_frame = tk.Frame(mainframe, name='userpage', width=window_width, height=window_height)

    except:
        user_page_frame = tk.Frame(mainframe, name='userpage', width=window_width, height=window_height)

    user_page_frame.pack(fill='both', expand=1)
    user_page_header_frame = tk.Frame(user_page_frame,width=100, padx = 150,
                                    highlightthickness=3, highlightbackground='black')
    
    ulabel = tk.Label(user_page_header_frame, text='THÔNG TIN TÀI KHOẢN',
                    font=('Verdana',18,'bold'))
    u_fullname = tk.Label(user_page_header_frame, text=f'Họ tên: {user.fullname}',
                        font=('Verdana',12))
    u_email = tk.Label(user_page_header_frame, text=f'Password: {user.email}',
                    font=('Verdana',12))
    u_phone = tk.Label(user_page_header_frame, text=f'SĐT: {user.phone}',
                    font=('Verdana',12))
    u_dob = tk.Label(user_page_header_frame, text=f'Ngày sinh: {user.dob}',
                    font=('Verdana',12))

    user_page_header_frame.pack(fill='both')

    ulabel.grid(row=0, column=0, columnspan=7)

    u_fullname.grid(row=1, column=0)
    u_email.grid(row=1, column=1)
    u_phone.grid(row=2, column=0)
    u_dob.grid(row=2, column=1)

    user_page_content_frame = tk.Frame(user_page_frame, padx=200)
    func_label = tk.Label(user_page_content_frame, text='MENU',
                        font=('Verdana',18,'bold'))
    update_button = tk.Button(user_page_content_frame, text='Cập nhật thông tin',
                            width=25)
    encrypt_send_button = tk.Button(user_page_content_frame, text='Chọn và mã hoá tập tin',
                            width=25)
    decrypt_receive_button = tk.Button(user_page_content_frame, text='Giải mã tập tin',
                            width=25)
    sign_file_button = tk.Button(user_page_content_frame, text='Ký trên tập tin',
                            width=25)
    confirm_sign_button = tk.Button(user_page_content_frame, text='Xác nhận chữ ký',
                            width=25)
    user_page_content_frame.pack(fill='both')
    func_label.grid(row=0, column=0, columnspan=3)
    update_button.grid(row=1, column=0, pady=5)
    encrypt_send_button.grid(row=2, column=0, pady=5)
    decrypt_receive_button.grid(row=3, column=0, pady=5)
    sign_file_button.grid(row=4, column=0, pady=5)
    confirm_sign_button.grid(row=5, column=0, pady=5)
