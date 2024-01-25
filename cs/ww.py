import tkinter
from tkinter import *
from tkinter import messagebox

import customtkinter
import pymysql

from PIL import ImageTk, Image


class SQL():
    def sql_conn(self):
        try:
            self.conn = pymysql.connect(
                host='localhost',
                port=3306,
                user='root',
                password='11111111',
                database='python'
            )
            # qwer = self.conn.cursor()
            # qwer.execute("SELECT * FROM product")
            # result = qwer.fetchall()
            # print("Начальное подключение")
            # print(result)
        except:
            print("error")

class Super(SQL):
    def okno(self):

        self.sql_conn()

        root = Tk()
        root.title("Ромашка")
        root.geometry("800x600")
        root.resizable(width=False, height=False)
        root.configure(bg="#78DBE2")

        tea1 = ImageTk.PhotoImage(Image.open('flo/1.jpg'))  # or tea1 = CTkImage(Image.open('flo/1.jpg')), но будет маленькое изображение, возможно оно просто подстроило бы под кнопку любой масштаб
        tea2 = ImageTk.PhotoImage(Image.open('flo/2.jpg'))
        tea3 = ImageTk.PhotoImage(Image.open('flo/3.jpg'))
        tea4 = ImageTk.PhotoImage(Image.open('flo/4.jpg'))
        tea5 = ImageTk.PhotoImage(Image.open('flo/5.jpg'))
        tea6 = ImageTk.PhotoImage(Image.open('flo/6.jpg'))

        header = Frame(root, height=80, width=800, bg="#78BCE2")
        header.grid(row=0, column=0)

        title = customtkinter.CTkLabel(header, text_color="white", bg_color="#78BCE2", font=('', 50), text="Ромашка")
        title.place(relx=0.05, rely=0.5, anchor=W)

        # profile_user = customtkinter.CTkButton(header, height=50, width=50, corner_radius=50, text='')
        # profile_user.place(relx=0.9, rely=0.5, anchor=CENTER)

        # user_ = customtkinter.CTkButton(header, height=50, width=50, corner_radius=50, text='')
        # profile_user.place(relx=0.9, rely=0.5, anchor=CENTER)

        self.cards = Frame(root, height=449, width=744, bg="#78DBE2")
        self.cards.place(x=28, y=114, anchor=NW)

        card1 = customtkinter.CTkButton(self.cards, height=200, width=235, text='', fg_color="#B7EDF0",
                                        state='disabled', corner_radius=20)
        card2 = customtkinter.CTkButton(self.cards, height=200, width=235, text='', fg_color="#B7EDF0",
                                        state='disabled', corner_radius=20)
        card3 = customtkinter.CTkButton(self.cards, height=200, width=235, text='', fg_color="#B7EDF0",
                                        state='disabled', corner_radius=20)
        card4 = customtkinter.CTkButton(self.cards, height=200, width=235, text='', fg_color="#B7EDF0",
                                        state='disabled', corner_radius=20)
        card5 = customtkinter.CTkButton(self.cards, height=200, width=235, text='', fg_color="#B7EDF0",
                                        state='disabled', corner_radius=20)
        card6 = customtkinter.CTkButton(self.cards, height=200, width=235, text='', fg_color='#B7EDF0',
                                        state='disabled', corner_radius=20)

        card1.place(relx=0, rely=0.25, anchor=W)
        card2.place(relx=0.5, rely=0.25, anchor=CENTER)
        card3.place(relx=1, rely=0.25, anchor=E)
        card4.place(relx=0, rely=0.75, anchor=W)
        card5.place(relx=0.5, rely=0.75, anchor=CENTER)
        card6.place(relx=1, rely=0.75, anchor=E)

        card_picture1 = customtkinter.CTkButton(self.cards, height=100, width=200, text='', fg_color="white",
                                                bg_color="#B7EDF0", state='disabled', corner_radius=20, image=tea1)
        card_picture2 = customtkinter.CTkButton(self.cards, height=100, width=200, text='', fg_color="white",
                                                bg_color="#B7EDF0", state='disabled', corner_radius=20, image=tea2)
        card_picture3 = customtkinter.CTkButton(self.cards, height=100, width=200, text='', fg_color="white",
                                                bg_color="#B7EDF0", state='disabled', corner_radius=20, image=tea3)
        card_picture4 = customtkinter.CTkButton(self.cards, height=100, width=200, text='', fg_color="white",
                                                bg_color="#B7EDF0", state='disabled', corner_radius=20, image=tea4)
        card_picture5 = customtkinter.CTkButton(self.cards, height=100, width=200, text='', fg_color="white",
                                                bg_color="#B7EDF0", state='disabled', corner_radius=20, image=tea5)
        card_picture6 = customtkinter.CTkButton(self.cards, height=100, width=200, text='', fg_color='white',
                                                bg_color="#B7EDF0", state='disabled', corner_radius=20, image=tea6)

        card_picture1.place(relx=0.024, rely=0.18, anchor=W)
        card_picture2.place(relx=0.5, rely=0.18, anchor=CENTER)
        card_picture3.place(relx=0.976, rely=0.18, anchor=E)
        card_picture4.place(relx=0.024, rely=0.68, anchor=W)
        card_picture5.place(relx=0.5, rely=0.68, anchor=CENTER)
        card_picture6.place(relx=0.976, rely=0.68, anchor=E)

        card_lbl1 = customtkinter.CTkLabel(self.cards, fg_color="#B7EDF0", text_color="#0C547D", font=('', 20),
                                           text="'Ромашки'")
        card_lbl2 = customtkinter.CTkLabel(self.cards, fg_color="#B7EDF0", text_color="#0C547D", font=('', 20),
                                           text="'Greenfield'")
        card_lbl3 = customtkinter.CTkLabel(self.cards, fg_color="#B7EDF0", text_color="#0C547D", font=('', 20),
                                           text="'Житница Здоровья'")
        card_lbl4 = customtkinter.CTkLabel(self.cards, fg_color="#B7EDF0", text_color="#0C547D", font=('', 20),
                                           text="'ФитоЧай' с мятой")
        card_lbl5 = customtkinter.CTkLabel(self.cards, fg_color="#B7EDF0", text_color="#0C547D", font=('', 20),
                                           text="'BioFix' с лимонником")
        card_lbl6 = customtkinter.CTkLabel(self.cards, fg_color="#B7EDF0", text_color="#0C547D", font=('', 20),
                                           text="'Victorian' kamomillatee")

        card_lbl1.place(relx=0.024, rely=0.34, anchor=W)
        card_lbl2.place(relx=0.43, rely=0.34, anchor=CENTER)
        card_lbl3.place(relx=0.95, rely=0.34, anchor=E)
        card_lbl4.place(relx=0.024, rely=0.84, anchor=W)
        card_lbl5.place(relx=0.49, rely=0.84, anchor=CENTER)
        card_lbl6.place(relx=0.98, rely=0.84, anchor=E)

        self.card_btn1 = customtkinter.CTkButton(self.cards, height=30, width=100, fg_color="#78BCE2",
                                                 bg_color="#B7EDF0", corner_radius=10, text="Купить",
                                                 font=('Calibri', 18), command=self.click_card1)
        card_btn2 = customtkinter.CTkButton(self.cards, height=30, width=100, fg_color="#78BCE2", bg_color="#B7EDF0",
                                            corner_radius=10, text="Купить", font=('Calibri', 18), command=self.click_card2)
        card_btn3 = customtkinter.CTkButton(self.cards, height=30, width=100, fg_color="#78BCE2", bg_color="#B7EDF0",
                                            corner_radius=10, text="Купить", font=('Calibri', 18), command=self.click_card3)
        card_btn4 = customtkinter.CTkButton(self.cards, height=30, width=100, fg_color="#78BCE2", bg_color="#B7EDF0",
                                            corner_radius=10, text="Купить", font=('Calibri', 18), command=self.click_card4)
        card_btn5 = customtkinter.CTkButton(self.cards, height=30, width=100, fg_color="#78BCE2", bg_color="#B7EDF0",
                                            corner_radius=10, text="Купить", font=('Calibri', 18), command=self.click_card5)
        card_btn6 = customtkinter.CTkButton(self.cards, height=30, width=100, fg_color="#78BCE2", bg_color="#B7EDF0",
                                            corner_radius=10, text="Купить", font=('Calibri', 18), command=self.click_card6)

        self.card_btn1.place(relx=0.16, rely=0.42, anchor=W)
        card_btn2.place(relx=0.568, rely=0.42, anchor=CENTER)
        card_btn3.place(relx=0.976, rely=0.42, anchor=E)
        card_btn4.place(relx=0.16, rely=0.92, anchor=W)
        card_btn5.place(relx=0.568, rely=0.92, anchor=CENTER)
        card_btn6.place(relx=0.976, rely=0.92, anchor=E)

        root.mainloop()

    def click_card1(self):
        self.sql_conn()

        try:
            qwer = self.conn.cursor()
            qwer.execute("SELECT amount FROM product WHERE id = 1")
            amount_bd = qwer.fetchone()
            print(amount_bd)
            if amount_bd >= (1,):
                print("норм")
                response = messagebox.askokcancel("Подтверждение", "Совершить покупкку?")
                if response is True:
                    messagebox.showinfo("Успешно", "Покупка совершена!")
                    qwer = self.conn.cursor()
                    qwer.execute("UPDATE product SET amount = amount - 1 WHERE id = 1")
                    self.conn.commit()
                    # result = qwer.fetchall()
                    # print(result)
            elif amount_bd == (0,):
                print("закончилось")
                messagebox.showerror("Уведомление", "Товар закончился")
                self.card_btn1 = customtkinter.CTkButton(self.cards, height=30, width=100, fg_color="#78BCE2",
                                                         bg_color="#B7EDF0", state='disabled', corner_radius=10,
                                                         text="Купить", font=('Calibri', 18))
                self.card_btn1.place(relx=0.16, rely=0.42, anchor=W)

        except:
            print("error")

    def click_card2(self):
        self.sql_conn()

        try:
            qwer = self.conn.cursor()
            qwer.execute("SELECT amount FROM product WHERE id = 2")
            amount_bd = qwer.fetchone()
            print(amount_bd)
            if amount_bd >= (1,):
                print("норм")
                response = messagebox.askokcancel("Подтверждение", "Совершить покупкку?")
                if response is True:
                    messagebox.showinfo("Успешно", "Покупка совершена!")
                    qwer = self.conn.cursor()
                    qwer.execute("UPDATE product SET amount = amount - 1 WHERE id = 2")
                    self.conn.commit()
                    # result = qwer.fetchall()
                    # print(result)
            elif amount_bd == (0,):
                print("закончилось")
                messagebox.showerror("Уведомление", "Товар закончился")
                self.card_btn2 = customtkinter.CTkButton(self.cards, height=30, width=100, fg_color="#78BCE2",
                                                         bg_color="#B7EDF0", state='disabled', corner_radius=10,
                                                         text="Купить", font=('Calibri', 18))
                self.card_btn2.place(relx=0.568, rely=0.42, anchor=CENTER)

        except:
            print("error")

    def click_card3(self):
        self.sql_conn()

        try:
            qwer = self.conn.cursor()
            qwer.execute("SELECT amount FROM product WHERE id = 3")
            amount_bd = qwer.fetchone()
            print(amount_bd)
            if amount_bd >= (1,):
                print("норм")
                response = messagebox.askokcancel("Подтверждение", "Совершить покупкку?")
                if response is True:
                    messagebox.showinfo("Успешно", "Покупка совершена!")
                    qwer = self.conn.cursor()
                    qwer.execute("UPDATE product SET amount = amount - 1 WHERE id = 3")
                    self.conn.commit()
                    # result = qwer.fetchall()
                    # print(result)
            elif amount_bd == (0,):
                print("закончилось")
                messagebox.showerror("Уведомление", "Товар закончился")
                self.card_btn3 = customtkinter.CTkButton(self.cards, height=30, width=100, fg_color="#78BCE2",
                                                         bg_color="#B7EDF0", state='disabled', corner_radius=10,
                                                         text="Купить", font=('Calibri', 18))
                self.card_btn3.place(relx=0.976, rely=0.42, anchor=E)

        except:
            print("error")

    def click_card4(self):
        self.sql_conn()

        try:
            qwer = self.conn.cursor()
            qwer.execute("SELECT amount FROM product WHERE id = 4")
            amount_bd = qwer.fetchone()
            print(amount_bd)
            if amount_bd >= (1,):
                print("норм")
                response = messagebox.askokcancel("Подтверждение", "Совершить покупкку?")
                if response is True:
                    messagebox.showinfo("Успешно", "Покупка совершена!")
                    qwer = self.conn.cursor()
                    qwer.execute("UPDATE product SET amount = amount - 1 WHERE id = 4")
                    self.conn.commit()
                    # result = qwer.fetchall()
                    # print(result)
            elif amount_bd == (0,):
                print("закончилось")
                messagebox.showerror("Уведомление", "Товар закончился")
                self.card_btn4 = customtkinter.CTkButton(self.cards, height=30, width=100, fg_color="#78BCE2",
                                                         bg_color="#B7EDF0", state='disabled', corner_radius=10,
                                                         text="Купить", font=('Calibri', 18))
                self.card_btn4.place(relx=0.16, rely=0.92, anchor=W)

        except:
            print("error")

    def click_card5(self):
        self.sql_conn()

        try:
            qwer = self.conn.cursor()
            qwer.execute("SELECT amount FROM product WHERE id = 5")
            amount_bd = qwer.fetchone()
            print(amount_bd)
            if amount_bd >= (1,):
                print("норм")
                response = messagebox.askokcancel("Подтверждение", "Совершить покупкку?")
                if response is True:
                    messagebox.showinfo("Успешно", "Покупка совершена!")
                    qwer = self.conn.cursor()
                    qwer.execute("UPDATE product SET amount = amount - 1 WHERE id = 5")
                    self.conn.commit()
                    # result = qwer.fetchall()
                    # print(result)
            elif amount_bd == (0,):
                print("закончилось")
                messagebox.showerror("Уведомление", "Товар закончился")
                self.card_btn5 = customtkinter.CTkButton(self.cards, height=30, width=100, fg_color="#78BCE2",
                                                         bg_color="#B7EDF0", state='disabled', corner_radius=10,
                                                         text="Купить", font=('Calibri', 18))
                self.card_btn5.place(relx=0.568, rely=0.92, anchor=CENTER)

        except:
            print("error")

    def click_card6(self):
        self.sql_conn()

        try:
            qwer = self.conn.cursor()
            qwer.execute("SELECT amount FROM product WHERE id = 6")
            amount_bd = qwer.fetchone()
            print(amount_bd)
            if amount_bd >= (1,):
                print("норм")
                response = messagebox.askokcancel("Подтверждение", "Совершить покупкку?")
                if response is True:
                    messagebox.showinfo("Успешно", "Покупка совершена!")
                    qwer = self.conn.cursor()
                    qwer.execute("UPDATE product SET amount = amount - 1 WHERE id = 6")
                    self.conn.commit()
                    # result = qwer.fetchall()
                    # print(result)
            elif amount_bd == (0,):
                print("закончилось")
                messagebox.showerror("Уведомление", "Товар закончился")
                self.card_btn6 = customtkinter.CTkButton(self.cards, height=30, width=100, fg_color="#78BCE2",
                                                         bg_color="#B7EDF0", state='disabled', corner_radius=10,
                                                         text="Купить", font=('Calibri', 18))
                self.card_btn6.place(relx=0.976, rely=0.92, anchor=E)

        except:
            print("error")


class User(Super):
    def reg(self):
        self.window = Tk()
        self.window.geometry("600x400")
        self.window.title("Регистрация")

        self.username = StringVar()
        self.password = StringVar()
        self.n_username = StringVar()
        self.n_password = StringVar()
        self.widgets()

        # self.bg_photo = Label(self.window, height=400, width=600, image=self.bg_bg)
        # self.bg_photo.grid(row=0, column=0)

        self.window.mainloop()

    def login(self):
        try:
            self.sql_conn()
            qwer = self.conn.cursor()
            qwer.execute(f"SELECT * FROM users WHERE login = {self.username.get()} and password = {self.password.get()}")
            result = qwer.fetchall()

            if result:
                self.window.destroy()
                self.okno()
            else:
                messagebox.showerror('Уведомление', 'Данный пользователь не найден!')
        except:
            print("неудача")

    def new_user(self):
        try:
            self.sql_conn()
            qwer = self.conn.cursor()
            qwer.execute(f"SELECT login FROM users WHERE login = {self.n_username.get()}")
            result = qwer.fetchall()

            if result:
                messagebox.showerror('Уведомление!', 'Имя пользователя занято, попробуйте другое.')
            else:
                messagebox.showinfo('Успех!', 'Пользователь создан!')
                self.log()

            qwer.execute(f"INSERT INTO users(login, password) VALUES ('{self.n_username.get()}','{self.n_password.get()}');")
            self.conn.commit()
            print("хуй")
        except:
            print("ошибочка")


    def log(self):
        self.username.set('')
        self.password.set('')
        self.crf.place_forget()
        self.head['text'] = 'Авторизация'
        self.logf.place(relx=0.5, rely=0.5, anchor=CENTER)

    def cr(self):
        self.n_username.set('')
        self.n_password.set('')
        self.logf.place_forget()
        self.head['text'] = 'Создать пользователя'
        self.crf.place(relx=0.5, rely=0.5, anchor=CENTER)

    def widgets(self):
        # self.bg_bg = ImageTk.PhotoImage(Image.open('pictures/regbg.jpeg'))

        self.head = Label(self.window, text='Авторизация', font=('', 35), pady=10)
        self.head.place(relx=0.5, rely=0.1, anchor=CENTER)

        self.logf = Frame(self.window, padx=10, pady=10)
        self.logf.place(relx=0.5, rely=0.5, anchor=CENTER)
        # self.bg_photo = Label(self.logf, height=400, width=600, image=self.bg_bg)
        # self.bg_photo.grid(row=0, column=0)

        Label(self.logf, text='Логин: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.logf, textvariable=self.username, bd=5, font=('', 15)).grid(row=0, column=1)
        Label(self.logf, text='Пароль: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.logf, textvariable=self.password, bd=5, font=('', 15), show='*').grid(row=1, column=1)
        Button(self.logf, text=' Войти ', bd=3, font=('', 15), padx=5, pady=5, command=self.login).grid()
        Button(self.logf, text=' Создать пользователя ', bd=3, font=('', 15), padx=5, pady=5, command=self.cr).grid(row=2, column=1)


        self.crf = Frame(self.window, padx=10, pady=10)
        Label(self.crf, text='Логин: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.crf, textvariable=self.n_username, bd=5, font=('', 15)).grid(row=0, column=1)
        Label(self.crf, text='Пароль: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.crf, textvariable=self.n_password, bd=5, font=('', 15), show='*').grid(row=1, column=1)
        Button(self.crf, text='Создать', bd=3, font=('', 15), padx=5, pady=5, command=self.new_user).grid()
        Button(self.crf, text='Назад', bd=3, font=('', 15), padx=5, pady=5, command=self.log).grid(row=2, column=1)


if __name__ == "__main__":
    # app = Super()
    # app.okno()

    aaa = User()
    aaa.reg()
