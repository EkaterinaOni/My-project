from kivy.core.audio import SoundLoader
from kivy.uix.screenmanager import Screen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from lesson_one import Lesson_one
from database import Login
import random

class Lesson_seven(Screen):
    dialog = None
    k = 0
    sound = None
    rez1 = 0;rez2 = 0;rez3 = 0;rez4 = 0;rez5 = 0;rez6 = 0
    flag = True
    def __init__(self, *args, **kwargs):
        super(Lesson_seven, self).__init__(*args, **kwargs)
        self.ids['toolbar'].title = 'Урок №7 Сложение и вычитание двузначных чисел'
        self.ids.next_one.text = 'Далее'
        self.ids.next_up.text = 'Вернуться'
        self.ids.next_one_1.text = 'Далее'
        self.ids.next_up_1.text = 'Вернуться'
        self.ids.next_up_2.text = 'Вернуться'
        self.ids.exit.text = "Вернуться на главную страницу"
        self.ids.first_text.text = 'Считать на соробане достаточно просто. Для понимания возьмем пример 26+34'
        self.ids.second_text.text = 'Устанавливаем первое число 26 :'
        self.ids.third_text.text = 'Раскладываем все числа на простые цифры, не забывая, к какой спице они относятся: 2 и 3 к десяткам, а 6 и 4 к единицам. ' \
                                   'Производим сложение простых чисел. 6+4 и 2+3.'
        self.ids.fourth_text.text = 'Теперь сдвигаем единицы на первой спице 6+4 =10, то есть на 1 спице надо показать 0, ' \
                                    'и развести все костяшки по местам, а к двум костяшкам на второй спице добавить еще одну, получим 30:'
        self.ids.fifth_text.text = 'Но мы добавляли не 4, а 34, поэтому на второй спице надо добавить еще 3 костяшки и показать цифру 6, ' \
                                   'для этого опускаются снизу 2 костяшки и «5». Итого мы получаем 60.'
        self.ids.sixth_text.text = "Сложение всегда начинается с меньшего числа с переходом к большему. Если костяшек на спице получается больше чем 9, " \
                                   "тогда на соседней спице добавится еще одна."
        self.ids.seventh_text.text = "Также рассмотрим пример сложения 13 + 23"
        self.ids.seventh_text_1.text = "1) Отложите на спицах первое число – 13. " \
                                     "Для этого в ряду десятков поднимите 1 бусину на нижнем ряду; на спице, отвечающей за единицы, отложите 3 костяшки. "
        self.ids.seventh_text_2.text = "2) Прибавляем 23. " \
                                     "Для этого в ряду единиц добавляете 3 бусины, в ряду десятков – 2. "
        self.ids.seventh_text_3.text = "3) Получаем 36."
        self.ids.eight_text.text = 'В случае с вычитанием система та же, начинаем с меньшего, только если вычитается от меньшей цифры большая,' \
                                   ' тогда они меняются местами, а с соседней спицы убирается костяшка.'
        self.ids.nine_text_1.text = 'Например, 15-13:'
        self.ids.nine_text_2.text = ' - ставим 15;'
        self.ids.ten_text.text =  '- раскладываем число на простые цифры 1 и 5 и 1 и 3, от 1 отнимаем 1, от 5 отнимаем 3 и получаем 2:'
        self.ids.next_one_2.text = 'Перейти к заданиям'
        self.ids.prim.text = "Примеры"
        self.ids.prov.text = "Проверка"
        self.primer()

    def proverka(self):
        self.flag = True
        self.k = 0
        id_i_list = ['i1', 'i2', 'i3', 'i4', 'i5', 'i6']
        id_o_list = ['o1', 'o2', 'o3', 'o4', 'o5', 'o6']
        for i in range(len(id_o_list)):
            if self.ids[id_o_list[i]].text == '':
                self.show_alert_dialog()
                self.flag = False
        if self.flag:
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
            if Login.urok < 7:
                Login.urok = 7
                self.pars_urok(str(Login.urok))
            Lesson_one.show_alert_dialog(Lesson_one)

    def pars_urok(self, text):
        self.manager.get_screen('mainscreen').ids.urok_bd.text = 'Вы закончили на Уроке №' + text

    def stop(self):
        if self.sound != None and self.sound.state == 'play':
            self.sound.stop()

    def play_sound(self):
        if self.sound == None or self.sound.state == 'stop':
            self.sound = SoundLoader.load('sounds/urok7.wav')
            self.sound.play()
            self.sound.state = 'play'
            self.ids.button_sound.icon = 'volume-high'
        else:
            self.sound.state = 'stop'
            self.sound.stop()
            self.ids.button_sound.icon = 'volume-off'

    def clean(self):
        id_o_list = ['o1', 'o2', 'o3', 'o4', 'o5', 'o6']
        id_i_list = ['i1', 'i2', 'i3', 'i4', 'i5', 'i6']
        for i in range(len(id_i_list)):
            self.ids[id_i_list[i]].opacity = 0
        for i in range(len(id_o_list)):
            self.ids[id_o_list[i]].text = ""

    def primer(self):
        l3 = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 5, 6, 7, 8, -1], [0, 1, 2, 5, 6, 7, -1, -2],
              [0, 1, 5, 6, -1, -2, -3],
              [0, 5, -1, -2, -3, -4], [0, 1, 2, 3, 4, -5], [0, 1, 2, 3, -5, -6], [0, 1, 2, -5, -6, -7],
              [0, 1, -1, -2, -3, -5, -6, -7, -8],
              [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]]
        id_o_list = ['o1', 'o2', 'o3', 'o4', 'o5', 'o6']
        id_i_list = ['i1', 'i2', 'i3', 'i4', 'i5', 'i6']
        for i in range(len(id_i_list)):
            self.ids[id_i_list[i]].opacity = 0
        for i in range(len(id_o_list)):
            self.ids[id_o_list[i]].text = ""

        for j in range(6):
            s2 = random.randint(1, 9)
            s1 = random.randint(1, 9)
            rezstr = str(s2) + str(s1)
            rez = 10 * s2 + s1
            for i in range(4):
                s2 = rez // 10
                s1 = rez % 10
                s = s1
                s2 = random.choice(l3[s2])
                s1 = random.choice(l3[s])
                print(s)
                while s1 * s2 < 0:
                    s1 = random.choice(l3[s])
                if s2 < 0 or s1 < 0 :
                    rezstr = rezstr + ' - ' + str((10 * s2 + s1)*(-1))
                else:
                    rezstr = rezstr + ' + ' + str(10 * s2 + s1)
                rez = rez + 10 * s2 + s1
                print('rez', rez)
            rezstr = rezstr + ' = '
            if j == 0: self.ids.p1.text = rezstr; self.rez1 = rez
            if j == 1: self.ids.p2.text = rezstr; self.rez2 = rez
            if j == 2: self.ids.p3.text = rezstr; self.rez3 = rez
            if j == 3: self.ids.p4.text = rezstr; self.rez4 = rez
            if j == 4: self.ids.p5.text = rezstr; self.rez5 = rez
            if j == 5: self.ids.p6.text = rezstr; self.rez6 = rez

    def show_alert_dialog(self):

        if not self.dialog:
            self.dialog = MDDialog(
                text='Некоторые поля остались пустыми'
            )
            self.dialog.open()