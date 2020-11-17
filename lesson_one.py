from kivy.app import App
from kivy.core.audio import SoundLoader
from kivy.uix.screenmanager import Screen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from database import Login

class Lesson_one(Screen):
    dialog = None
    sound = None
    def __init__(self, *args, **kwargs):
        super(Lesson_one, self).__init__(*args, **kwargs)
        self.ids.ques1.text = '[color=0000ff] Выберите образ, который соответствует числу 7[/color]'
        self.ids.ques2.text = '[color=0000ff] Выберите образ, который соответствует числу 2[/color]'
        self.ids.ques3.text = '[color=0000ff] Выберите образ, который соответствует числу 5[/color]'
        self.ids.propusk1.text = 'Пропустить'
        self.ids.propusk2.text = 'Пропустить'
        self.ids.propusk3.text = 'Пропустить'
        self.ids.zadania.text = 'Задания'
        self.ids.theory.text = 'Теория'
        self.ids.les_one.text = 'Для того чтобы на соробане выставить число 1, большим пальцем правой руки перемещаем одну нижнюю косточку к перекладине\n'\
                                'Для того чтобы на соробане выставить число 2, большим пальцем правой руки перемещаем одновременно две нижние косточки к перекладине\n' \
                                'Для того чтобы на соробане выставить число 3, большим пальцем правой руки перемещаем одновременно три нижние косточки к перекладине\n' \
                                'Для того чтобы на соробане выставить число 4, большим пальцем правой руки перемещаем одновременно четыре нижние косточки к перекладине\n' \
                                'Для того чтобы на соробане выставить число 5, указательным пальцем правой руки перемещаем верхнюю косточку к перекладине\n' \
                                'Для того чтобы на соробане выставить число 6, большим и указательным пальцами правой руки одновременно одну нижнюю и верхнюю косточки к перекладине\n' \
                                'Для того чтобы на соробане выставить число 7, большим и указательным пальцами правой руки одновременно две нижние и верхнюю косточки к перекладине\n' \
                                'Для того чтобы на соробане выставить число 8, большим и указательным пальцами правой руки одновременно три нижние и верхнюю косточки к перекладине\n' \
                                'Для того чтобы на соробане выставить число 9, большим и указательным пальцами правой руки одновременно четыре нижние и верхнюю косточки к перекладине\n'

        self.ids.lb.text = 'Прокручивайте карточки справа. Вы сможете увидеть, как выглядят цифры на соробане'
        self.ids.toolbar.title = 'Урок №1 Однозначные числа прямой счет'
        self.ids.exit.text = "Вернуться на главную страницу"


    def propusk(self):
        if self.ids.screen_1.opacity == 1:
            self.ids.screen_1.opacity = 0
            self.ids.screen_2.opacity = 1
            self.ids.screen_3.opacity = 0
        elif self.ids.screen_2.opacity == 1:
            self.ids.screen_1.opacity = 0
            self.ids.screen_2.opacity = 0
            self.ids.screen_3.opacity = 1
        elif self.ids.screen_3.opacity == 1:
            self.ids.screen_1.opacity = 1
            self.ids.screen_2.opacity = 0
            self.ids.screen_3.opacity = 0
    def answer1_pressed(self):
        sound = SoundLoader.load('sounds/error.wav')
        sound.play()

    def answer2_pressed(self):
        if self.ids.screen_3.opacity == 1:
            sound = SoundLoader.load('sounds/success.WAV')
            self.show_alert_dialog()
            self.ids.screen_1.opacity = 1
            self.ids.screen_2.opacity = 0
            self.ids.screen_3.opacity = 0
            print(Login.urok)
            if Login.urok < 1:
                Login.urok = 1
                self.pars_urok(str(Login.urok))
            print(Login.urok)
        else:
            sound = SoundLoader.load('sounds/error.wav')
        sound.play()

    def pars_urok(self, text):
        self.manager.get_screen('mainscreen').ids.urok_bd.text = 'Вы закончили на Уроке №' + text

    def stop(self):
        if self.sound != None and self.sound.state == 'play':
            self.sound.stop()

    def play_sound(self):
        if self.sound == None or self.sound.state == 'stop':
            self.sound = SoundLoader.load('sounds/urok1.wav')
            self.sound.play()
            self.sound.state = 'play'
            self.ids.button_sound.icon = 'volume-high'
        else:
            self.sound.state = 'stop'
            self.sound.stop()
            self.ids.button_sound.icon = 'volume-off'

    def answer3_pressed(self):
        if self.ids.screen_1.opacity == 1:
            sound = SoundLoader.load('sounds/success.WAV')
            self.ids.screen_1.opacity = 0
            self.ids.screen_2.opacity = 1
            self.ids.screen_3.opacity = 0
        else:
            sound = SoundLoader.load('sounds/error.wav')
        sound.play()

    def answer4_pressed(self):
        if self.ids.screen_2.opacity == 1:
            sound = SoundLoader.load('sounds/success.WAV')
            self.ids.screen_1.opacity = 0
            self.ids.screen_2.opacity = 0
            self.ids.screen_3.opacity = 1
        else:
            sound = SoundLoader.load('sounds/error.wav')
        sound.play()


    def show_alert_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title='Поздравляю',
                text='Вы прошли урок\nМолодец, продолжай в том же духе',
                buttons=[
                    MDFlatButton(
                        text="Продолжить"
                    )
                ],
            )
        self.dialog.open()