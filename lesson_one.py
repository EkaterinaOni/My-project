from kivy.app import App
from kivy.core.audio import SoundLoader
from kivy.uix.screenmanager import Screen

class Lesson_one(Screen):
    def __init__(self, *args, **kwargs):
        super(Lesson_one, self).__init__(*args, **kwargs)
        self.ids.ques1.text = '[color=0000ff] Какое значение [b]ВЕРХНЕЙ[/b] бусины [/color]'
        self.ids.ques3.text = '[color=0000ff] Выберите образ, который соответствует числу 7[/color]'
        self.ids.ques2.text = '[color=0000ff] Какое значение [b]НИЖНЕЙ[/b] бусины [/color]'
        self.ids.propusk1.text = 'Пропустить'
        self.ids.propusk2.text = 'Пропустить'
        self.ids.propusk3.text = 'Пропустить'

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
            self.ids.screen_1.opacity = 1
            self.ids.screen_2.opacity = 0
            self.ids.screen_3.opacity = 0
        else:
            sound = SoundLoader.load('sounds/error.wav')
        sound.play()

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