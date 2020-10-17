import sqlite3

from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.popup import Popup


class Login(Screen):
    def __init__(self, *args, **kwargs):
        super(Login, self).__init__(*args, **kwargs)
        self.ids.welcome.text = 'Добро пожаловать'
        self.ids.login_name.text = 'Имя'
        self.ids.login_password.text = 'Пароль'
        self.ids.connection.text = 'Вход'
    urok = 0

    def resetForm(self):
        self.ids['login'].text = ""
        self.ids['password'].text = ""

    def pars(self, text):
        self.manager.get_screen('mainscreen').ids.user_name.text = 'Привет, ' + text

    def do_login(self, loginText, passwordText):
        if loginText == "":
            popup = Popup(title='Test popup',
                          content=Label(text='The login field is empty'), size_hint=(None, None), size=(400, 400))
            popup.open()
            return
        elif passwordText == "":
            popup = Popup(title='Test popup',
                          content=Label(text='The password field is empty'), size_hint=(None, None), size=(400, 400))
            popup.open()
            return
        else:
            print(loginText, passwordText)
            conn = sqlite3.connect("Pupil.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM users WHERE login=? and password=?", (loginText,passwordText,))
            one_result = cur.fetchone()  # результат поиска из базы данных
            Login.urok = one_result[3]
            print(Login.urok)
            if one_result:
                self.pars(one_result[1])
                self.manager.current = 'mainscreen'
                print(one_result)
                conn.commit()
                conn.close()

#class Proverka(Popup):
 #   def proverklav_open(self):
  #      Proverka().open()

class Registration(Screen):
    def __init__(self, *args, **kwargs):
        super(Registration, self).__init__(*args, **kwargs)
        self.ids.registration.text = 'Регистрация'
        self.ids.login_label.text = 'Имя'
        self.ids.password_label.text = 'Пароль'
        self.ids.password_repeat.text = 'Подтвердите пароль'
        self.ids.registration_button.text = 'Регистрация'



    def insert_user(self, l, p, p_rep):
        self.ids['login'].text = ""
        self.ids['password'].text = ""
        self.ids['password_rep'].text = ""
        conn = sqlite3.connect("Pupil.db")
        cur = conn.cursor()
        print(l, p, p_rep)
        if p != p_rep:
            popup = Popup(title='Test popup',
                          content=Label(text='Password repeated incorrectly'), size_hint=(None, None), size=(400, 400))
            popup.open()
            return
        if l != '' and p != '' and p == p_rep:
            print('+')
            #cur.execute("INSERT INTO students (login, password, count_lesson, PROGRESS) VALUES (l, p, 1, 0)")
            params = (l, p, 1, 0)
            cur.execute("INSERT INTO users VALUES (NULL, ?, ?, ?, ?)", params)
            conn.commit()
        conn.close()

        self.manager.current = 'first'
