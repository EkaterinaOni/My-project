from kivy.uix.screenmanager import Screen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from lesson_one import Lesson_one
from database import Login
import random

class Lesson_three(Screen):
    k = 0
    rez1=0;rez2=0;rez3=0;rez4=0;rez5=0;rez6=0
    dialog = None
    def __init__(self, *args, **kwargs):
        super(Lesson_three, self).__init__(*args, **kwargs)
        self.ids.toolbar.title =  "Урок №3 Сложение и вычитание на всех косточках"
        self.ids.play_video.text = 'Начать урок'
        self.ids.exit.text = "Вернуться на главную страницу"
        self.ids.next_one.text = 'Задания'
        self.ids.prim.text = "Примеры"
        self.ids.prov.text = "Проверка"
        self.ids.next_up_2.text = 'Вернуться'
        self.ids.video.opacity = 0
        self.primer()

    def stop_video(self):
        self.ids.video.state = 'stop'
        self.ids.video.opacity = 0
        self.ids.play_video.text = 'Начать урок'

    def play_video(self):
        if self.ids.video.state == 'stop':
            self.ids.video.state = 'play'
            self.ids.video.opacity = 1
            self.ids.play_video.text = 'Остановить урок'
        else:
            self.ids.video.state = 'stop'
            self.ids.video.opacity = 0
            self.ids.play_video.text = 'Начать урок'

    def clean(self):
        id_o_list = ['o1', 'o2', 'o3', 'o4', 'o5', 'o6']
        id_i_list = ['i1', 'i2', 'i3', 'i4', 'i5', 'i6']
        for i in range(len(id_i_list)):
            self.ids[id_i_list[i]].opacity = 0
        for i in range(len(id_o_list)):
            self.ids[id_o_list[i]].text = ""

    def proverka(self):
        self.flag = True
        self.k = 0
        id_i_list = ['i1', 'i2', 'i3', 'i4', 'i5', 'i6']
        id_o_list = ['o1', 'o2', 'o3', 'o4', 'o5', 'o6']
        for i in range(len(id_o_list)):
            if self.ids[id_o_list[i]].text == '':
                self.show_alert_dialog()
                self.flag = False
        if self.flag == True:
            for i in range(len(id_i_list)):
                self.ids[id_i_list[i]].opacity = 1
            z = int(self.ids.o1.text)
            if self.rez1 == z:
                self.ids.i1.source = "Image/yes.png"
                self.k = self.k + 1
            else:
                self.ids.i1.source = "Image/no.png"
            z = int(self.ids.o2.text)
            if self.rez2 == z:
                self.ids.i2.source = "Image/yes.png"
                self.k = self.k + 1
            else:
                self.ids.i2.source = "Image/no.png"
            z = int(self.ids.o3.text)
            if self.rez3 == z:
                self.ids.i3.source = "Image/yes.png"
                self.k = self.k + 1
            else:
                self.ids.i3.source = "Image/no.png"
            z = int(self.ids.o4.text)
            if self.rez4 == z:
                self.ids.i4.source = "Image/yes.png"
                self.k = self.k + 1
            else:
                self.ids.i4.source = "Image/no.png"
            z = int(self.ids.o5.text)
            if self.rez5 == z:
                self.ids.i5.source = "Image/yes.png"
                self.k = self.k + 1
            else:
                self.ids.i5.source = "Image/no.png"
            z = int(self.ids.o6.text)
            if self.rez6 == z:
                self.ids.i6.source = "Image/yes.png"
                self.k = self.k + 1
            else:
                self.ids.i6.source = "Image/no.png"

        if self.k == 6:
            if Login.urok < 3:
                Login.urok = 3
                self.pars_urok(str(Login.urok))
            print(Login.urok)
            Lesson_one.show_alert_dialog(Lesson_one)

    def pars_urok(self, text):
        self.manager.get_screen('mainscreen').ids.urok_bd.text = 'Вы закончили на Уроке №' + text

    def primer(self):
        # Прямой счет на нижних косточках
        l2 = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 5, 6, 7, 8, -1], [1, 2, 5, 6, 7, -1, -2],
              [1, 5, 6, -1, -2, -3],
              [5, -1, -2, -3, -4], [1, 2, 3, 4, -5], [1, 2, 3, -5, -6], [1, 2, -5, -6, -7],
              [1, -1, -2, -3, -5, -6, -7, -8],
              [-1, -2, -3, -4, -5, -6, -7, -8, -9]]
        id_o_list = ['o1', 'o2', 'o3', 'o4', 'o5', 'o6']
        id_i_list = ['i1', 'i2', 'i3', 'i4', 'i5', 'i6']
        for i in range(len(id_i_list)):
            self.ids[id_i_list[i]].opacity = 0
        for i in range(len(id_o_list)):
            self.ids[id_o_list[i]].text = ""
        for j in range(6):
            s = random.randint(1, 9)
            rezstr = str(s)
            self.str = str(s)
            rez = s
            for i in range(4):
                s = random.choice(l2[rez])
                self.str = str(s)
                rez = rez + s
                if s < 0 :
                    rezstr = rezstr + ' - ' + str((s)*(-1))
                else:
                    rezstr = rezstr + ' + ' + str(s)
            rezstr = rezstr + ' ='
            if j == 0: self.ids.p1.text = rezstr; self.rez1 = rez
            if j == 1: self.ids.p2.text = rezstr; self.rez2 = rez
            if j == 2: self.ids.p3.text = rezstr; self.rez3 = rez
            if j == 3: self.ids.p4.text = rezstr; self.rez4 = rez
            if j == 4: self.ids.p5.text = rezstr; self.rez5 = rez
            if j == 5: self.ids.p6.text = rezstr; self.rez6 = rez

    def show_alert_dialog(self):

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
        self.dialog.open()