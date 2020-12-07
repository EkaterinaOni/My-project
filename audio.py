from kivy.core.audio import SoundLoader
from kivy.uix.screenmanager import Screen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from fleshcards import Prodol
from database import Login

tema = {1: 'Прямой счет на нижних косточках',
        2: 'Прямой счет на всех косточках',
        3: 'Младшие товарищи +',
        4: 'Младшие товарищи -',
        5: 'Младшие товарищи + -',
        6: 'Старшие товарищи +',
        7: 'Старшие товарищи -',
        8: 'Старшие товарищи + -'}

temaobr = {'Прямой счет на нижних косточках': 1,
           'Прямой счет на всех косточках': 2,
           'Младшие товарищи +': 3,
           'Младшие товарищи -': 4,
           'Младшие товарищи + -': 5,
           'Старшие товарищи +': 6,
           'Старшие товарищи -': 7,
           'Старшие товарищи + -': 8}
dictant = {1: 'sounds/dic1.wav',
           2: 'sounds/dic2.wav',
           3: 'sounds/dic3.wav',
           4: 'sounds/dic4.wav',
           5: 'sounds/dic5.wav',
           6: 'sounds/dic6.wav',
           7: 'sounds/dic7.wav',
           8: 'sounds/dic8.wav'}

otvet = {1: [4, 4, 3, 0, 1, 1, 2, 1, 2, 2],
         2: [7, 0, 1, 6, 1, 9, 8, 4, 5, 1],
         3: [8, 7, 7, 1, 5, 0, 9, 2, 5, 6],
         4: [3, 6, 4, 0, 3, 1, 4, 9, 5, 2],
         5: [3, 4, 1, 2, 5, 8, 6, 0, 4, 9],
         6: [20, 23, 30, 29, 22, 25, 32, 21, 23, 31],
         7: [3, 4, 8, 1, 12, 8, 4, 7, 8, 8],
         8: [21, 19, 9, 24, 18, 30, 20, 8, 15, 13]}



class Audio_tren(Screen):
    d = 0
    sound = None
    dialog = None
    def __init__(self, *args, **kwargs):
        super(Audio_tren, self).__init__(*args, **kwargs)
        self.ids.list.text = "Выберите аудио диктант"
        self.ids.list.values = (tema[1], tema[2],tema[3],tema[4],tema[5], tema[6], tema[7], tema[8])
        self.ids.lb.text = "Слушайте диктант и записывайте ответы"
        self.ids.exit_main.text = "Вернуться на главную страницу"
        self.ids.beg.text = "Начать"
        self.ids.prov.text = "Проверить"
        self.ids.cl.text = "Очистить"
        self.ids.help_prav.text = "Инструкция"



    def vibor_dic(self, value):
        if value == "Выберите аудио диктант":
            self.show_alert_dialog(1)
        else:
            self.ids.beg.disabled = True
            self.d = temaobr[value]
            self.sound = SoundLoader.load(dictant[self.d])
            self.sound.play()
            self.clean()
            self.ids.prov.disabled = False


    def clean(self):
        id_im_list = ['im1', 'im2', 'im3', 'im4', 'im5', 'im6', 'im7', 'im8', 'im9', 'im10']
        id_r_list = ['r1', 'r2', 'r3', 'r4', 'r5', 'r6', 'r7', 'r8', 'r9', 'r10']
        for i in range(len(id_im_list)):
            self.ids[id_im_list[i]].opacity = 0
        for i in range(len(id_r_list)):
            self.ids[id_r_list[i]].text = ""


    def stop_audio(self):
        if self.sound != None:
            self.sound.stop()
            self.ids.prov.disabled = True
            self.ids.beg.disabled = False

    def proverka(self):
        otv = otvet[self.d]
        self.flag = True
        self.ids.beg.disabled = False
        id_im_list = ['im1','im2','im3','im4','im5','im6','im7','im8','im9','im10']
        id_r_list = ['r1', 'r2', 'r3', 'r4', 'r5', 'r6', 'r7', 'r8', 'r9', 'r10']

        for i in range(len(id_r_list)):
            if self.ids[id_r_list[i]].text == '':
                self.show_alert_dialog(2)
                self.sound.stop()
                self.ids.beg.disabled = False
                self.flag = False
        self.k = 0
        if self.flag:
            for i in range(len(id_im_list)):
                self.ids[id_im_list[i]].opacity = 1
            for i in range(len(id_r_list)):
                z = int(self.ids[id_r_list[i]].text)
                if z == otv[i]:
                    self.k = self.k + 1
                    self.ids[id_im_list[i]].source = "Image/yes.png"
                else:
                    self.ids[id_im_list[i]].source = "Image/no.png"
            Login.progress = Login.progress + self.k
            self.pars_progress(str(Login.progress))
            print(Login.progress)
        print(self.k)

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

    def show_alert_dialog(self, n):
        if not self.dialog:
            self.dialog = MDDialog(
                title='Осторожно',
                text='Выберите аудио диктант!'
            )
        if n == 2:
            self.dialog.text='Какие-то поля для ответов остались пустыми\n' \
                             'Введите все ответы'

        self.dialog.open()
