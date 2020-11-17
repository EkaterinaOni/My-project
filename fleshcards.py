from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.behaviors import ToggleButtonBehavior
from kivy.core.audio import SoundLoader
from kivy.clock import Clock
from kivy.uix.image import Image
from database import Login
import random


card = {1: ('Image/1.jpg'),
        2: ('Image/2.jpg'),
        3: ('Image/3.jpg'),
        4: ('Image/4.jpg'),
        5: ('Image/5.jpg'),
        6: ('Image/6.jpg'),
        7: ('Image/7.jpg'),
        8: ('Image/8.jpg'),
        9: ('Image/9.jpg'),
        10: ('Image/10.jpg'),
        11: ('Image/11.jpg'),
        12: ('Image/12.jpg'),
        13: ('Image/13.jpg'),
        14: ('Image/14.jpg'),
        15: ('Image/15.jpg'),
        16: ('Image/16.jpg'),
        17: ('Image/17.jpg'),
        18: ('Image/18.jpg'),
        19: ('Image/19.jpg'),
        20: ('Image/20.jpg'),
        21: ('Image/21.jpg'),
        22: ('Image/22.jpg'),
        23: ('Image/23.jpg'),
        24: ('Image/24.jpg'),
        25: ('Image/25.jpg'),
        26: ('Image/26.jpg'),
        27: ('Image/27.jpg'),
        28: ('Image/28.jpg'),
        29: ('Image/29.jpg'),
        30: ('Image/30.jpg'),
        31: ('Image/31.jpg'),
        32: ('Image/32.jpg'),
        33: ('Image/33.jpg'),
        34: ('Image/34.jpg'),
        35: ('Image/35.jpg'),
        36: ('Image/36.jpg'),
        37: ('Image/37.jpg'),
        38: ('Image/38.jpg'),
        39: ('Image/39.jpg'),
        40: ('Image/40.jpg'),
        41: ('Image/41.jpg'),
        42: ('Image/42.jpg'),
        43: ('Image/43.jpg'),
        44: ('Image/44.jpg'),
        45: ('Image/45.jpg'),
        46: ('Image/46.jpg'),
        47: ('Image/47.jpg'),
        48: ('Image/48.jpg'),
        49: ('Image/49.jpg'),
        50: ('Image/50.jpg'),
        51: ('Image/51.jpg'),
        52: ('Image/52.jpg'),
        53: ('Image/53.jpg'),
        54: ('Image/54.jpg'),
        55: ('Image/55.jpg'),
        56: ('Image/56.jpg'),
        57: ('Image/57.jpg'),
        58: ('Image/58.jpg'),
        59: ('Image/59.jpg'),
        60: ('Image/60.jpg'),
        61: ('Image/61.jpg'),
        62: ('Image/62.jpg'),
        63: ('Image/63.jpg'),
        64: ('Image/64.jpg'),
        65: ('Image/65.jpg'),
        66: ('Image/66.jpg'),
        67: ('Image/67.jpg'),
        68: ('Image/68.jpg'),
        69: ('Image/69.jpg'),
        70: ('Image/70.jpg'),
        71: ('Image/71.jpg'),
        72: ('Image/72.jpg'),
        73: ('Image/73.jpg'),
        74: ('Image/74.jpg'),
        75: ('Image/75.jpg'),
        76: ('Image/76.jpg'),
        77: ('Image/77.jpg'),
        78: ('Image/78.jpg'),
        79: ('Image/79.jpg'),
        80: ('Image/80.jpg'),
        81: ('Image/1.jpg'),
        82: ('Image/82.jpg'),
        83: ('Image/83.jpg'),
        84: ('Ima7e/84.jpg'),
        85: ('Image/85.jpg'),
        86: ('Image/86.jpg'),
        87: ('Image/87.jpg'),
        88: ('Image/88.jpg'),
        89: ('Image/89.jpg'),
        90: ('Image/90.jpg'),
        91: ('Image/91.jpg'),
        92: ('Image/92.jpg'),
        93: ('Image/93.jpg'),
        94: ('Image/94.jpg'),
        95: ('Image/95.jpg'),
        96: ('Image/96.jpg'),
        97: ('Image/97.jpg'),
        98: ('Image/98.jpg'),
        99: ('Image/99.jpg'),
        }


class Prodol(Popup):
    def __init__(self, *args, **kwargs):
        super(Prodol, self).__init__(*args, **kwargs)
        self.title = ''
        self.ids.rez.text = 'Задание выполнено!!!'
        self.ids.bk.text = 'Закончить'
        self.ids.pr.text = 'Продолжить'

    def reshat(self):
        self.dismiss()
    def vih(self):
        self.manager.current = 'mainscreen'


class Flashcards(Screen):
    def __init__(self, *args, **kwargs):
        super(Flashcards, self).__init__(*args, **kwargs)
        self.ids.lb.text = "[b]ФЛЕШ КАРТЫ[/b]"
        self.ids.make.text = "Выполнено 0 из 10"
        self.ids.right.text = "Правильно 0 из 0 "
        self.ids.sk.text = "Скорость"
        self.ids.odnl.text = "Однозначные числа"
        self.ids.dvzl.text = "Двузначные числа"
        self.ids.begin.text = "Начать"
        self.title = "Флеш карты"
        self.ids.bn_back.text = "Вернуться на главную"
        self.ids.list1.text = "Инструкция"
        self.ids.list2.text = "Вернуться к тренажеру"
        self.ids.flash_title.title = "Тренажер Флеш-карты"

    def clean(self):
        self.r = 0
        self.m = 0
        self.ids.my_answer.text = ''
        self.ids.answer.text = ''
        self.ids.vp.opacity = 0
        self.ids.cr.opacity = 0
        self.ids.my_answer.opacity = 0
        self.ids.cr.source = 'None'
        self.ids.make.text = "Выполнено 0 из 10"
        self.ids.right.text = "Правильно 0 из 0 "


    def update(self, dt):
        self.ids.cr.opacity = 0

    def begin_card(self):
        self.r = 0
        self.m = 1
        self.tm = float(self.ids.z.text)
        self.ids.make.text = "Выполнено 0 из 10"
        self.ids.right.text = "Правильно 0 из 0 "
        self.ids.my_answer.focus = True
        self.ids.makeb.value = 0
        self.ids.rightb.value = 0
        if self.ids.odn.state == 'down':
            self.kol1 = 1
            self.kol2 = 9
        else:
            self.kol1 = 10
            self.kol2 = 99

        self.l = random.randint(self.kol1, self.kol2)
        self.ids.cr.source = card[self.l]
        self.ids.cr.opacity = 1
        self.ids.vp.opacity = 1
        self.ids.my_answer.opacity = 1
        Clock.schedule_once(self.update, self.tm)  # отвечает за задержку
        self.ids.my_answer.text = ''
        self.ids.answer.text = ''
        self.prov()
        print('self.r = ', self.r)

    def prov(self):
        if self.ids.vp.opacity == 1:
            if (self.m <= 20) and (self.m % 2 > 0):
                ans = self.ids.my_answer.text
                if ans.isdigit():
                    self.s = str(self.l) + ' '
                    if self.l > 9:
                        self.s = self.s[0:1] + '   ' + self.s[1:2]

                    self.ids.answer.text = self.s
                    self.ids.cr.opacity = 1
                    self.ids.cr.source = card[self.l]
                    if int(ans) == self.l:
                        self.ids.my_answer.text = str(self.l) + ' = ' + ans
                        self.r = self.r + 1
                        Login.progress = Login.progress + 1
                        self.pars_progress(str(Login.progress))
                        print(Login.progress)
                        sound = SoundLoader.load('sounds/success.wav')
                        self.ids.rightb.value += 10
                        sound.play()
                    else:
                        self.ids.my_answer.text = str(self.l) + ' ≠ ' + ans
                        sound = SoundLoader.load('sounds/error.wav')
                        sound.play()
                    self.ids.right.text = 'Правильно ' + str(self.r) + ' из ' + str(self.m // 2 + 1)
                    self.ids.makeb.value += 10
                    self.ids.make.text = 'Выполнено ' + str(self.m // 2 + 1) + ' из 10'
                    self.m = self.m + 1
            else:
                if (self.m < 20) and (self.m % 2 == 0):
                    self.l = random.randint(self.kol1, self.kol2)
                    self.ids.cr.opacity = 1
                    self.ids.cr.source = card[self.l]
                    Clock.schedule_once(self.update, self.tm)
                    self.ids.my_answer.focus = True
                    self.ids.answer.text = ''
                    self.ids.my_answer.text = ''
                    self.m = self.m + 1
                else:
                    self.ids.my_answer.text = ''
                    self.ids.answer.text = ''
                    self.ids.vp.opacity = 0
                    self.ids.cr.opacity = 0
                    self.ids.my_answer.opacity = 0
                    self.ids.cr.source = 'None'
                    Prodol().open()

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