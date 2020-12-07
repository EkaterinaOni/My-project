# -*- coding: utf-8 -*-#
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.config import Config
Window.size = (1366, 768)
Window.fullscreen = True
import sqlite3
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.audio import SoundLoader
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.popup import Popup
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.uix.behaviors import ButtonBehavior
from database import Login, Registration
from soroban import Soroban
from fleshcards import Flashcards
from stolb import Stolb
from help import Help
from audio import Audio_tren
from lesson_one import Lesson_one
from lesson_two import Lesson_two
from lesson_three import Lesson_three
from lesson_four import Lesson_four
from lesson_five import Lesson_five
from lesson_six import Lesson_six
from lesson_seven import Lesson_seven
from lesson_eight import Lesson_eight
from lesson_nine import Lesson_nine

class ImageButton(ButtonBehavior, Image):
	pass


class MainScreen(Screen):
    dialog = None
    def __init__(self, *args, **kwargs):
        super(MainScreen, self).__init__(*args, **kwargs)
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
        self.ids.soroban.text = 'Соробан'
        self.ids.bn.text = 'Выход'
        self.ids.bn_clear.text = 'Сбросить прогресс'
        self.ids.tren_stolb.text = 'Столбцы'
        self.ids.tren_flesh.text = 'Флеш-карты'
        self.ids.tren_audio.text = 'Аудио-диктанты'

    def exit_func(self):
        print(Login.urok)
        conn = sqlite3.connect("Pupil.db")
        cur = conn.cursor()
        cur.execute(" UPDATE users SET count_lesson = ?, progress = ? WHERE id_users = ?", (Login.urok, Login.progress, Login.id))
        conn.commit()
        conn.close()
        print(Login.progress)

    def show_alert_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Предупреждение!",
                type="custom",
                text="Вы уверены, что хотите сбросить прогресс?",
                buttons=[
                    MDFlatButton(
                        text="Сбросить", on_release=self.clearprogress
                    ),
                    MDFlatButton(
                        text="Отмена", on_release=self.closeDialog
                    ),
                ],
            )
        self.dialog.set_normal_height()
        self.dialog.open()

    def clearprogress(self, inst):
        print("Сброс")
        Login.urok = 0
        Login.progress = 0
        conn = sqlite3.connect("Pupil.db")
        cur = conn.cursor()
        cur.execute(" UPDATE users SET count_lesson = ?, progress = ? WHERE id_users = ?",
                    (Login.urok, Login.progress, Login.id))
        conn.commit()
        conn.close()
        self.manager.get_screen('mainscreen').ids.urok_bd.text = 'Начните с Вводного урока'
        self.manager.get_screen('mainscreen').ids.progress_bd.text = 'Вы правильно выполнили 0 заданий'
        self.dialog.dismiss()

    def closeDialog(self, inst):
        self.dialog.dismiss()

class Introductory_lesson(Screen):
    dialog = None
    sound = None
    def __init__(self, *args, **kwargs):
        super(Introductory_lesson, self).__init__(*args, **kwargs)
        self.ids.textvvod.font_size = 26
        self.ids.answer1.text = "Большой"
        self.ids.answer2.text = "Указательный"
        self.ids.answer3.text = "Мизинец"
        self.ids.answer4.text = "Средний"
        self.ids.answer1_1.text = "Большой"
        self.ids.answer2_1.text = "Указательный"
        self.ids.answer3_1.text = "Мизинец"
        self.ids.answer4_1.text = "Средний"
        self.ids.exit.text = "Вернуться на главную страницу"
        self.ids.zadania.text = 'Задания'
        self.ids.theory.text = 'Теория'
        self.ids.propusk1.text = 'Пропустить'
        self.ids.propusk2.text = 'Пропустить'
        self.ids.propusk3.text = 'Пропустить'
        self.ids.propusk4.text = 'Пропустить'
        self.ids.ques1.text = '[color=0000ff] Какое значение [b]ВЕРХНЕЙ[/b] бусины [/color]'
        self.ids.ques2.text = '[color=0000ff] Какое значение [b]НИЖНЕЙ[/b] бусины [/color]'
        self.ids.ques3.text = '[color=0000ff] Каким пальцем передвигаются [b]ВЕРХНИЕ[/b] бусины [/color]'
        self.ids.ques4.text = '[color=0000ff] Каким пальцем передвигаются [b]НИЖНИЕ[/b] бусины [/color]'
        self.ids.toolbar.title = 'Вводный урок'
        self.ids.textvvod.text = 'Соробан - это японские счеты. В нем 13 (или больше) вертикальных спиц, поделенных поперек.\n' \
                   'На каждой спице по пять косточек. Снизу - 4, каждая равна единице, сверху - 1, равная пяти.\n' \
                   'При помощи этих пяти косточек на спице отображают числа от 1 до 9.\n' \
                   'Считают только костяшки, придвинутые к центру.\n'\
                    'При счете на соробане используются только большой и указательный пальцы\n'\
                    'Передвигая нижние косточки, используем БОЛЬШОЙ палец\n' \
                    'Передвигая верхние косточки, используем УКАЗАТЕЛЬНЫЙ палец'

    def propusk(self):
        if self.ids.screen_1.opacity == 1:
            self.ids.screen_1.opacity = 0
            self.ids.screen_2.opacity = 1
            self.ids.screen_3.opacity = 0
            self.ids.screen_4.opacity = 0
        elif self.ids.screen_2.opacity == 1:
            self.ids.screen_1.opacity = 0
            self.ids.screen_2.opacity = 0
            self.ids.screen_3.opacity = 1
            self.ids.screen_4.opacity = 0
        elif self.ids.screen_3.opacity == 1:
            self.ids.screen_1.opacity = 0
            self.ids.screen_2.opacity = 0
            self.ids.screen_3.opacity = 0
            self.ids.screen_4.opacity = 1
        elif self.ids.screen_1.opacity == 1:
            self.ids.screen_1.opacity = 1
            self.ids.screen_2.opacity = 0
            self.ids.screen_3.opacity = 0
            self.ids.screen_4.opacity = 0

    def answer1_pressed(self):
        if self.ids.screen_4.opacity == 1:
            sound = SoundLoader.load('sounds/success.WAV')
            self.ids.screen_1.opacity = 1
            self.ids.screen_2.opacity = 0
            self.ids.screen_3.opacity = 0
            self.ids.screen_4.opacity = 0
            print(Login.urok)
            if Login.urok < 1:
                Login.urok = 1
                self.pars_urok()
            Lesson_one.show_alert_dialog(Lesson_one)
            print(Login.urok)
        else:
            sound = SoundLoader.load('sounds/error.wav')
        sound.play()

    def pars_urok(self):
        self.manager.get_screen('mainscreen').ids.urok_bd.text = 'Вы закончили на Вводном Уроке'


    def answer2_pressed(self):
        if self.ids.screen_3.opacity == 1:
            sound = SoundLoader.load('sounds/success.WAV')
            self.ids.screen_1.opacity = 0
            self.ids.screen_2.opacity = 0
            self.ids.screen_3.opacity = 0
            self.ids.screen_4.opacity = 1
        else:
            sound = SoundLoader.load('sounds/error.wav')
        sound.play()

    def answer3_pressed(self):
        if self.ids.screen_1.opacity == 1:
            sound = SoundLoader.load('sounds/success.WAV')
            self.ids.screen_1.opacity = 0
            self.ids.screen_2.opacity = 1
            self.ids.screen_3.opacity = 0
            self.ids.screen_4.opacity = 0
        else:
            sound = SoundLoader.load('sounds/error.wav')
        sound.play()

    def answer4_pressed(self):
        if self.ids.screen_2.opacity == 1:
            sound = SoundLoader.load('sounds/success.WAV')
            self.ids.screen_1.opacity = 0
            self.ids.screen_2.opacity = 0
            self.ids.screen_3.opacity = 1
            self.ids.screen_4.opacity = 0
        else:
            sound = SoundLoader.load('sounds/error.wav')
        sound.play()

    def stop(self):
        if self.sound != None and self.sound.state == 'play':
            self.sound.stop()

    def play_sound(self):
        if self.sound == None or self.sound.state == 'stop':
            self.sound = SoundLoader.load('sounds/Vvod_urok.wav')
            self.sound.play()
            self.sound.state = 'play'
            self.ids.button_sound.icon = 'volume-high'
        else:
            self.sound.state = 'stop'
            self.sound.stop()
            self.ids.button_sound.icon = 'volume-off'


class First(Screen):
    def __init__(self, *args, **kwargs):
        super(First, self).__init__(*args, **kwargs)
        self.ids.button_input.text = 'Вход'
        self.ids.Register.text = 'Регистрация'


class LoginApp(MDApp):

    def build(self):
        self.icon = 'Image/icon.png'
        self.title = 'Mental_math'
        self.theme_cls.primary_palette = "Yellow"
        manager = ScreenManager()
        manager.add_widget(First(name='first'))
        manager.add_widget(Login(name='login'))
        manager.add_widget(Registration(name='registration'))
        manager.add_widget(MainScreen(name='mainscreen'))
        manager.add_widget(Introductory_lesson(name='introductory_lesson'))
        manager.add_widget(Lesson_one(name='lesson_one'))
        manager.add_widget(Lesson_two(name='lesson_two'))
        manager.add_widget(Lesson_three(name='lesson_three'))
        manager.add_widget(Lesson_four(name = 'lesson_four'))
        manager.add_widget(Lesson_five(name='lesson_five'))
        manager.add_widget(Lesson_six(name='lesson_six'))
        manager.add_widget(Lesson_seven(name='lesson_seven'))
        manager.add_widget(Lesson_eight(name='lesson_eight'))
        manager.add_widget(Lesson_nine(name='lesson_nine'))
        manager.add_widget(Soroban(name = 'soroban'))
        manager.add_widget(Flashcards(name = 'flashcards'))
        manager.add_widget(Stolb(name='stolb'))
        manager.add_widget(Help(name='help'))
        manager.add_widget(Audio_tren(name='audio_tren'))
        return manager

if __name__ == '__main__':
    Config.set('graphics', 'fullscreen', 'auto')
    Config.set('graphics', 'window_state', 'maximized')
    Config.write()
    LoginApp().run()