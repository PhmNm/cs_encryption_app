import tkinter as tk
from tkinter import messagebox, filedialog
from tkcalendar import DateEntry

import os, json
from datetime import datetime

from components.utils import *

window_height = 400
window_width = 600


def user_page(mainframe: tk.Frame, user: User):

    mainframe.children['loginframe'].forget()
    user_page_frame = tk.Frame(
        mainframe,
        name='userpage',
        width=window_width,
        height=window_height
    )

    user_page_frame.pack(fill='both', expand=1)

    user_page_header_frame = tk.Frame(
        user_page_frame,
        name='header_frame',
        padx = 70,
        highlightthickness=3,
        highlightbackground='black'
    )
    
    ulabel = tk.Label(
        user_page_header_frame,
        text='THÔNG TIN TÀI KHOẢN',
        font=('Verdana',18,'bold')
    )
    u_fullname = tk.Label(
        user_page_header_frame,
        text=f'Họ tên: {user.fullname}',
        font=('Verdana',12)
    )
    u_email = tk.Label(
        user_page_header_frame,
        text=f'Email: {user.email}',
        font=('Verdana',12)
    )
    u_phone = tk.Label(
        user_page_header_frame,
        text=f'SĐT: {user.phone}',
        font=('Verdana',12)
    )
    u_dob = tk.Label(
        user_page_header_frame,
        text=f'Ngày sinh: {user.dob}',
        font=('Verdana',12)
    )

    user_page_header_frame.pack(fill='both')

    ulabel.grid(row=0, column=0, columnspan=3, sticky='w', padx=75)

    u_fullname.grid(row=1, column=0, sticky='w')
    u_email.grid(row=1, column=2, sticky='w', padx=100)
    u_phone.grid(row=2, column=0, sticky='w')
    u_dob.grid(row=2, column=2, sticky='w', padx=100)


    # Menu panel
    user_page_content_frame_left = tk.Frame(
        user_page_frame,
        name='menu_content_frame',
        width=50
    )
    func_label = tk.Label(
        user_page_content_frame_left,
        text='MENU',
        font=('Verdana',18,'bold')
    )
    update_button = tk.Button(
        user_page_content_frame_left,
        text='Cập nhật thông tin',
        width=25
    )
    generate_key_button = tk.Button(
        user_page_content_frame_left,
        text='Sinh khoá KPublic & KPrivate',
        width=25
    )
    encrypt_send_button = tk.Button(
        user_page_content_frame_left,
        text='Chọn và mã hoá tập tin',
        width=25
    )
    decrypt_receive_button = tk.Button(
        user_page_content_frame_left,
        text='Giải mã tập tin',
        width=25
    )
    sign_file_button = tk.Button(
        user_page_content_frame_left,
        text='Ký trên tập tin',
        width=25
    )
    confirm_sign_button = tk.Button(
        user_page_content_frame_left,
        text='Xác nhận chữ ký',
        width=25
    )
    log_out_button = tk.Button(
        user_page_content_frame_left,
        text='Đăng xuất',
        width=25
    )

    user_page_content_frame_left.pack(fill='both',side = 'left', padx=20, pady=10)

    func_label.grid(row=0, column=0, columnspan=3)
    update_button.grid(row=1, column=0, pady=5)
    generate_key_button.grid(row=2, column=0, pady=5)
    encrypt_send_button.grid(row=3, column=0, pady=5)
    decrypt_receive_button.grid(row=4, column=0, pady=5)
    sign_file_button.grid(row=5, column=0, pady=5)
    confirm_sign_button.grid(row=6, column=0, pady=5)
    log_out_button.grid(row=7,column=0, pady=5)

    # Content panel
    user_page_content_frame_right = tk.Frame(
        user_page_frame,
        name='content_frame',
        highlightthickness=2,
        bg='white',
        highlightbackground='black',
        width=360,
        height=290
    )
    user_page_content_frame_right.pack(pady=10, side='left', ipady=40)
    user_page_content_frame_right.grid_propagate(False)
    user_page_content_frame_right.pack_propagate(False)

    def logout():
        forget_old_widgets(mainframe)

        mainframe.children['loginframe'].pack(fill="both", expand=1)
    
    def update_user():
        forget_old_widgets(user_page_content_frame_right)

        bounded_user = user
        fullname_label_rg = tk.Label(
            user_page_content_frame_right,
            text='Họ và tên:', 
            font=('Verdana',8)
        )
        email_label_rg = tk.Label(
            user_page_content_frame_right,
            text='Email:', 
            font=('Verdana',8)
        )
        old_password_label_rg = tk.Label(
            user_page_content_frame_right,
            text='Old-Password:', 
            font=('Verdana',8)
        )                            
        password_label_rg = tk.Label(
            user_page_content_frame_right,
            text='Password:', 
            font=('Verdana',8)
        )
        confirmpass_label_rg = tk.Label(
            user_page_content_frame_right,
            text='Re-Password:', 
            font=('Verdana',8)
        )
        phone_label_rg = tk.Label(
            user_page_content_frame_right,
            text='SĐT:', 
            font=('Verdana',8)
        )
        dob_label_rg = tk.Label(
            user_page_content_frame_right,
            text='Ngày sinh:', 
            font=('Verdana',8)
        )

        fullname_entry_rg = tk.Entry(
            user_page_content_frame_right,
            width=30,
            font=('Verdana',8)
        )
        email_entry_rg = tk.Label(
            user_page_content_frame_right,
            text=user.email,
            font=('Verdana',8)
        )
        old_password_entry_rg = tk.Entry(
            user_page_content_frame_right,
            width=30,
            font=('Verdana',8),
            show='*'
        )
        password_entry_rg = tk.Entry(
            user_page_content_frame_right,
            width=30,
            font=('Verdana',8),
            show='*'
        )
        confirmpass_entry_rg = tk.Entry(
            user_page_content_frame_right,
            width=30,
            font=('Verdana',8),
            show='*'
        )
        phone_entry_rg = tk.Entry(
            user_page_content_frame_right, width=30,
            font=('Verdana',8)
        )
        dob = datetime.strptime(user.dob, '%Y-%m-%d')

        dob_entry_rg = DateEntry(
            user_page_content_frame_right,
            width = 32, 
            ate_pattern='dd/mm/yyyy',
            year=dob.year,
            month=dob.month, 
            ay=dob.day
        )
        confirm_button = tk.Button(
            user_page_content_frame_right,
            text='Xác nhận',
            width=20
        )

        # pre-fill in values
        fullname_entry_rg.insert(tk.END, user.fullname)
        phone_entry_rg.insert(tk.END, user.phone)
        #

        fullname_label_rg.grid(row=1, column=0, pady=8, padx=10, sticky='w')
        fullname_entry_rg.grid(row=1, column=1, sticky='w')

        email_label_rg.grid(row=2, column=0, pady=8, padx=10, sticky='w')
        email_entry_rg.grid(row=2, column=1, sticky='w')

        old_password_label_rg.grid(row=3, column=0, pady=8, padx=10, sticky='w')
        old_password_entry_rg.grid(row=3, column=1, sticky='w')

        password_label_rg.grid(row=4, column=0, pady=8, padx=10, sticky='w')
        password_entry_rg.grid(row=4, column=1, sticky='w')

        confirmpass_label_rg.grid(row=5, column=0, pady=8, padx=10, sticky='w')
        confirmpass_entry_rg.grid(row=5, column=1, sticky='w')

        phone_label_rg.grid(row=6, column=0, pady=8, padx=10, sticky='w')
        phone_entry_rg.grid(row=6, column=1, sticky='w')

        dob_label_rg.grid(row=7, column=0, pady=8, padx=10, sticky='w')
        dob_entry_rg.grid(row=7, column=1, sticky='w')

        confirm_button.grid(row=8, column=0, columnspan=2, pady=6, padx=100, sticky='w')

        def validateUpdate(): #handle click
            email = bounded_user.email
            password = password_entry_rg.get().strip()
            confirmpass = confirmpass_entry_rg.get().strip()
            old_password = old_password_entry_rg.get().strip()
            with open('data/users_log_data.json', 'r', encoding='utf-8') as input:
                users  = json.load(input)

            if password: # check valid input data
                if not validate_password(old_password, bounded_user.password):
                    messagebox.showerror(title='LỖI', message='Nhập sai password cũ')
                elif confirmpass != password:
                    messagebox.showerror(message='Nhập lại mật khẩu sai')
                else:
                    hashed_password = hash_password(password)
                    user_update ={
                        'key': email,
                        'info':{
                            'fullname':fullname_entry_rg.get().strip(),
                            'email': email,
                            'password': hashed_password,
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
    def generate_save_key_pair():
        # generate and show
        user_dir = 'data/' + user.storage
        kpub_dir = user_dir + '/kpublic.pub'
        kpri_dir = user_dir + '/kprivate'
        kpri_enc_dir = user_dir + '/kprivate.enc'

        if os.path.exists(kpub_dir) and os.path.exists(kpri_dir) and os.path.exists(kpri_enc_dir):
            forget_old_widgets(user_page_content_frame_right)
            exist_label = tk.Label(
                user_page_content_frame_right,
                text='ĐÃ TỒN TẠI CẶP KHOÁ\nVUI LÒNG KIỂM TRA\nTRONG THƯ MỤC NGƯỜI DÙNG',
                font=('Verdana',14),
                bg='white'
            )
            exist_label.pack(fill='both',expand=True)
            return

        Kpub, Kpri, Kpri_enc = generate_keypair(user.password)

        normalize_kpub = str(Kpub).replace('\'','').replace('b','').replace(r'\n', '\n')
        normalize_kpri = str(Kpri).replace('\'','').replace('b','').replace(r'\n', '\n')

        scroll_bar_y = tk.Scrollbar(
            user_page_content_frame_right,
            orient='vertical'
        )

        scroll_bar_y.pack(side='right', fill='y')

        text_view = tk.Text(
            user_page_content_frame_right,
            wrap='char',
            yscrollcommand = scroll_bar_y.set,
        )

        text_view.insert(tk.END, '- Kpublic:\n')
        text_view.insert(tk.END, normalize_kpub + '\n')
        text_view.insert(tk.END, '- Kprivate:\n')
        text_view.insert(tk.END, normalize_kpri + '\n')

        text_view.pack(side = 'top', fill = 'both')
        
        scroll_bar_y.config(command=text_view.yview)

        # save to file

        with open(kpub_dir, 'wb+') as output:
            output.write(Kpub)
        with open(kpri_dir, 'wb+') as output:
            output.write(Kpri)
        with open(kpri_enc_dir, 'wb+') as output:
            output.write(Kpri_enc)
        messagebox.showinfo(title='CHÚC MỪNG', message='Tạo cặp khoá thành công')
    
    def encrypt_send_file():

        user_dir = 'data/' + user.storage

        forget_old_widgets(user_page_content_frame_right)

        file_frame = tk.Frame(
            user_page_content_frame_right,
            name='file_pick_frame',
            bg='white',
            width=170,
            height=290
        )

        file_frame.pack(side='left', fill='both')
        file_frame.grid_propagate(False)

        file_choose_label = tk.Label(
            file_frame,
            text='Chọn file cần mã hoá: ',
            font=('Verdana',8),
        )
        file_name_display = tk.Label(
            file_frame,
            wraplength=150,
            bg='white'
        )
        file_name = tk.StringVar(file_frame)
        def get_file():
            get_file_name = filedialog.askopenfilename(
                title='Chọn file',
                initialdir=user_dir
            )
            file_name.set(get_file_name)
            file_name_display['textvariable']=file_name

        file_choose_button = tk.Button(
            file_frame,
            text='Chọn file',
            command=get_file,
            anchor='w'
        )

        file_choose_label.grid(row=0, column=0, pady=5, sticky='w')
        file_choose_button.grid(row=1, column=0, pady=5, sticky='w')
        file_name_display.grid(row=2, column=0, columnspan=1, pady=5, sticky='w')

        user_frame = tk.Frame(
            user_page_content_frame_right,
            name='user_pick_frame',
            bg='white',
            width=190,
            height=290
        )

        user_frame.pack(side='left')
        user_frame.grid_propagate(False)

        user_pick_label = tk.Label(
            user_frame,
            text='Nhập email cần gửi:',
            font=('Verdana',8)
        )
        user_pick_entry = tk.Entry(
            user_frame,
            width=25,
            font=('Verdana',8)
        )

        def submit():
            email = user_pick_entry.get().strip()
            if not get_user(email):
                messagebox.showerror(
                    title='Lỗi',
                    message='Không tồn tại người dùng này!'
                
                )
            else:
                if encrypt_file(file_name.get(), email):
                    messagebox.showinfo(title='CHÚC MỪNG', message='Mã hoá và gửi thành công')
                else: messagebox.showerror(title='LỖI', message='Mã hoá không thành công')
        submit_button = tk.Button(
            user_frame,
            text='Xác nhận',
            width=10,
            command=submit
        )

        user_pick_label.grid(row=0, column=0, pady=5)
        user_pick_entry.grid(row=1, column=0, pady=5, sticky='w')
        submit_button.grid(row=2,column=0, pady=5)

    def decrypt_receive():
        user_dir = 'data/' + user.storage

        forget_old_widgets(user_page_content_frame_right)
        if user_page_content_frame_right.children:
            for i in user_page_content_frame_right.children.values():
                print(i)

        file_choose_label = tk.Label(
            user_page_content_frame_right,
            text='Chọn file cần giải mã: ',
            font=('Verdana',8),
        )
        file_name_display = tk.Label(
            user_page_content_frame_right,
            wraplength=150,
            bg='white'
        )

        file_name = tk.StringVar(user_page_content_frame_right)

        def get_file():
            get_file_name = filedialog.askopenfilename(
                title='Chọn file',
                initialdir=user_dir
            )
            file_name.set(get_file_name)
            file_name_display['textvariable']=file_name

        file_choose_button = tk.Button(
            user_page_content_frame_right,
            text='Chọn file',
            command=get_file,
            anchor='w'
        )
        def submit():
            if decrypt_file(file_name.get(), user.email):
                messagebox.showinfo(title='CHÚC MỪNG', message='Giải mã thành công')
            else: messagebox.showerror(title='LỖI', message='Giải mã không thành công')

        submit_button = tk.Button(
            user_page_content_frame_right,
            text='Xác nhận',
            width=10,
            command=submit
        )

        file_choose_label.grid(row=0, column=0, pady=5, sticky='w')
        file_choose_button.grid(row=1, column=0, pady=5, sticky='w')
        file_name_display.grid(row=2, column=0, columnspan=1, pady=5, sticky='w')
        submit_button.grid(row=3,column=0, pady=5)

    log_out_button['command']=logout
    update_button['command']=update_user
    generate_key_button['command']=generate_save_key_pair
    encrypt_send_button['command']=encrypt_send_file
    decrypt_receive_button['command']=decrypt_receive
