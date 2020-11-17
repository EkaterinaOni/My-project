import sqlite3

from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.popup import Popup
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton


class Login(Screen):
    dialog = None
    def __init__(self, *args, **kwargs):
        super(Login, self).__init__(*args, **kwargs)
        self.ids.welcome.text = 'Добро пожаловать'
        self.ids.login_name.text = 'Имя'
        self.ids.login_password.text = 'Пароль'
        self.ids.connection.text = 'Вход'
        self.ids.login.hint_text = 'Введите логин'
        self.ids.password_text.hint_text = 'Введите пароль'
    urok = 0
    progress = 0

    def resetForm(self):
        self.ids['login'].text = ""
        self.ids['password_text'].text = ""

    def show_alert_dialog(self):

        if not self.dialog:
            self.dialog = MDDialog(
                title='Ошибка',
                text='Неверно введен Логин или Пароль',
                buttons=[
                    MDFlatButton(
                        text="Закрыть"
                    )
                ],
            )
        self.dialog.open()

    def pars(self, text):
        self.manager.get_screen('mainscreen').ids.user_name.text = 'Привет, ' + text

    def pars_urok(self, text):
        if text == '0':
            self.manager.get_screen('mainscreen').ids.urok_bd.text = 'Начните с Вводного урока'
        else:
            self.manager.get_screen('mainscreen').ids.urok_bd.text = 'Вы закончили на Уроке №' + text

    def pars_progress(self, text):
        a1 = [0,5,6,7,8,9]
        a2 = [1]
        a3 = [2,3,4]
        if int(text) % 10 in a1:
            self.manager.get_screen('mainscreen').ids.progress_bd.text = 'Вы правильно выполнили ' + text + " заданий"
        elif int(text) % 10 in a2:
            self.manager.get_screen('mainscreen').ids.progress_bd.text = 'Вы правильно выполнили ' + text + " задание"
        elif int(text) % 10 in a3:
            self.manager.get_screen('mainscreen').ids.progress_bd.text = 'Вы правильно выполнили ' + text + " задания"

    def do_login(self, loginText, passwordText):
        self.resetForm()
        if loginText == "":
            popup = Popup(title='Ошибка',
                          content=Label(text='Поле логина пустое'), size_hint=(None, None), size=(400, 400))
            popup.open()
            return
        elif passwordText == "":
            popup = Popup(title='Ошибка',
                          content=Label(text='Поле пароля пустое'), size_hint=(None, None), size=(400, 400))
            popup.open()
            return
        else:
            print(loginText, passwordText)
            conn = sqlite3.connect("Pupil.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM users WHERE login=? and password=?", (loginText,passwordText,))
            one_result = cur.fetchone()  # результат поиска из базы данных
            if one_result:
                Login.id = one_result[0]
                Login.urok = one_result[3]
                Login.progress = one_result[4]
                print(Login.urok)
                self.pars(one_result[1])
                self.pars_urok(str(one_result[3]))
                self.pars_progress(str(one_result[4]))
                self.manager.current = 'mainscreen'
                print(one_result)
                conn.commit()
                conn.close()
            else:
                self.show_alert_dialog()


class Registration(Screen):
    dialog = None
    def __init__(self, *args, **kwargs):
        super(Registration, self).__init__(*args, **kwargs)
        self.ids.registration.text = 'Регистрация'
        self.ids.login_label.text = 'Логин'
        self.ids.password_label.text = 'Пароль'
        self.ids.password_repeat.text = 'Подтвердите пароль'
        self.ids.registration_button.text = 'Регистрация'
        self.ids.login.hint_text = 'Введите логин'
        self.ids.password_one.hint_text = 'Введите пароль'
        self.ids.password_rep.hint_text = 'Подтвердите пароль'

    def resetForm(self):
        self.ids['login'].text = ""
        self.ids['password_label'].text = ""
        self.ids['password_repeat'].text = ""

    def insert_user(self, l, p, p_rep):

        if l == '' or p == '' or p_rep == '':
            self.show_alert_dialog(1);
        elif p != p_rep:
            self.show_alert_dialog(2);
            self.ids['password_one'].text = ""
            self.ids['password_rep'].text = ""
            return
        else:
            self.ids['login'].text = ""
            conn = sqlite3.connect("Pupil.db")
            cur = conn.cursor()
            print(l, p, p_rep)
            if l != '' and p != '' and p == p_rep:
                print('+')
                params = (l, p, 0, 0)
                cur.execute("INSERT INTO users VALUES (NULL, ?, ?, ?, ?)", params)
                conn.commit()
            conn.close()
            self.manager.current = 'first'

    def show_alert_dialog(self, n):

        if not self.dialog:
            self.dialog = MDDialog(
                title='Ошибка',
                text='Некоторые поля остались пустыми',
                buttons=[
                    MDFlatButton(
                        text="CANCEL"
                    )
                ],
            )
        if n == 2:
            self.dialog.text='Пароли не совпадают, попробуйте ввести еще раз'
        self.dialog.open()
