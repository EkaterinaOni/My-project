# -*- coding: utf-8 -*-#
from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.core.audio import SoundLoader
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.dropdown import DropDown
from kivy.core.text import Label as CoreLabel
from kivy.clock import Clock
import time
from database import Login, Registration
from lesson_one import Lesson_one
from soroban import Soroban
from fleshcards import Flashcards

class ImageButton(ButtonBehavior, Image):
	pass

class CustomDropDown(DropDown):
    def __init__(self, *args, **kwargs):
        super(CustomDropDown, self).__init__(*args, **kwargs)
        self.ids.exit.text = 'Выход'

class MainScreen(Screen):
    def __init__(self, *args, **kwargs):
        super(MainScreen, self).__init__(*args, **kwargs)
        self.dropdown = CustomDropDown()
        self.ids.bn.bind(on_release=self.dropdown.open)
        self.ids.uroki.text = '[color=0000ff]Уроки[/color]'
        self.ids.trenajor.text = '[color=0000ff]Тренажеры[/color]'
        self.ids.btvvod.text = 'Вводный урок'
        self.ids.urok1.text = 'Урок №1'
        self.ids.urok2.text = 'Урок №2'
        self.ids.urok3.text = 'Урок №3'
        self.ids.urok4.text = 'Урок №4'
        self.ids.urok5.text = 'Урок №5'
        self.ids.urok6.text = 'Урок №6'
        self.ids.urok7.text = 'Урок №7'
        self.ids.urok8.text = 'Урок №8'
        self.ids.urok9.text = 'Урок №9'
        self.ids.urok10.text = 'Урок №10'
        self.ids.urok11.text = 'Урок №11'
        self.ids.urok12.text = 'Урок №12'
        self.ids.tren_stolb.text = 'Столбцы'
        self.ids.tren_flesh.text = 'Флеш-карты'
        self.ids.tren_audio.text = 'Аудио-диктанты'


class Introductory_lesson(Screen):
    def __init__(self, *args, **kwargs):
        super(Introductory_lesson, self).__init__(*args, **kwargs)
        self.ids.textvvod.font_size = 26
        self.ids.btvvod.text = 'Вводный [ref=l][b][color=0000ff]урок[/color][/b][/ref]'
        self.str = 'Соробан - это японские счеты. В нем 13 (или больше) вертикальных спиц, поделенных поперек.' \
                   'На каждой спице по пять косточек. Снизу - 4, каждая равна единице, сверху - 1, равная пяти.' \
                   'При помощи этих пяти косточек на спице отображают числа от 1 до 9.' \
                   'Считают только костяшки, придвинутые к центру.'
        self.ids.textvvod.typewriter = Clock.create_trigger(self.typeit, 0.1)
        self.ids.textvvod.typewriter()

    def typeit(self, dt):
        self.ids.textvvod.text += self.str[0]
        self.str = self.str[1:]
        if len(self.str) > 0:
            self.ids.textvvod.typewriter()

    def btn_pressed(self):
        flag = True
        if flag:
            sound = SoundLoader.load('sounds/Vvod_urok.wav')
            sound.play()
            flag = False
        else:
            flag = True


class First(Screen):
    pass

def user_name_rew(a):
    global name_user
    name_user = a
    return name_user

class LoginApp(App):
    #username = StringProperty(None)
    #password = StringProperty(None)
    #lesson_one = Lesson_one()

    def build(self):
        self.theme_cls.primary_palette = "Yellow"
        manager = ScreenManager()

        manager.add_widget(First(name='first'))
        manager.add_widget(Login(name='login'))
        manager.add_widget(Registration(name='registration'))
        manager.add_widget(MainScreen(name='mainscreen'))
        manager.add_widget(Introductory_lesson(name='introductory_lesson'))
        manager.add_widget(Lesson_one(name='lesson_one'))
        #manager.add_widget(Lesson_one(name='lesson_one_2'))
        #manager.add_widget(Lesson_one_2(name='lesson_one_2'))
        #manager.add_widget(Lesson_one_3(name='lesson_one_3'))
        #manager.add_widget(Lesson_one_4(name = 'lesson_one_4'))
        manager.add_widget(Soroban(name = 'soroban'))
        manager.add_widget(Flashcards(name = 'flashcards'))
        return manager

if __name__ == '__main__':
    LoginApp().run()