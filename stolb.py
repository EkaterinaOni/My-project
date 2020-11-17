from kivy.uix.screenmanager import Screen
from kivy.core.audio import SoundLoader
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from fleshcards import Prodol
from help import Help
from database import Login

import random
# Прямой счет на нижних косточках
l1=[[0,1,2,3,4],[0,1,2,3,-1],[0,1,2,-1,-2],[0,1,-1,-2,-3],[0,-1,-2,-3,-4]]
# Прямой счет на всех косточках
l2=[[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,5,6,7,8,-1],[0,1,2,5,6,7,-1,-2],[0,1,5,6,-1,-2,-3],
    [0,5,-1,-2,-3,-4],[0,1,2,3,4,-5],[0,1,2,3,-5,-6],[0,1,2,-5,-6,-7],[0,1,-1,-2,-3,-5,-6,-7,-8],
    [0,-1,-2,-3,-4,-5,-6,-7,-8,-9]]
# Младшие товарищи +
l3=[[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,-1],[0,1,2,3,4,5,6,7,-1,-2],[0,1,2,3,4,5,6,-1,-2,-3],
    [0,5,1,-1,-2,-3,-4],[0,1,2,3,4,-5],[0,1,2,3,-5,-6,-1],[0,1,2,-5,-6,-7,-1,-2],
    [0,1,-1,-2,-3,-5,-6,-7,-8],[0,-1,-2,-3,-4,-5,-6,-7,-8,-9]]

# Младшие товарищи -
l4=[[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,-1],[0,1,2,3,4,5,6,7,-1,-2],[0,1,2,3,4,5,6,-1,-2,-3],
    [0,5,1,-1,-2,-3,-4],[0,1,2,3,4,-1,-2,-3,-4,-5],[0,1,2,3,-1,-2,-3,-4,-5,-6],
    [0,1,2,-1,-2,-3,-4,-5,-6,-7],[0,1,-1,-2,-3,-4,-5,-6,-7,-8],[0,-1,-2,-3,-4,-5,-6,-7,-8,-9]]



# Старшие товарищи

class Stolb(Screen):
    dialog = None
    def __init__(self, *args, **kwargs):
        super(Stolb, self).__init__(*args, **kwargs)
        self.ids.title_stolb.title = 'Тренажер Столбцы'
        self.ids.begin.text = 'Начать'
        self.ids.odnozn.text = 'Однозначные числа'
        self.ids.dvuznach.text = 'Двузначные числа'
        self.m = 0
        self.ids.my_answer.hint_text = 'Введите ответ'
        self.ids.my_answer.helper_text= "Ошибка"
        self.ids.prov.text = "Проверка"
        self.ids.help.text = "Посмотреть ответ"
        self.ids.exit.text = "Вернуться на главную страницу"
        self.ids.help_prav.text = "Инструкция"
        self.ids.straight_lower.text = "Прямой счет на нижних косточках"
        self.ids.straight_all.text = "Прямой счет на всех косточках"
        self.ids.young_plus.text = "Младшие товарищи на +"
        self.ids.young_minus.text = "Младшие товарищи на -"
        self.ids.make.text = "Правильно 0 из 10"
        self.ids.success.text = "Поздравляю!"
        self.ids.fail.text = "Неправильно("
    rez_stolb = 0
    flag = True

    def resetForm(self):
        num_list = ['num0', 'num1', 'num2', 'num3', 'num4']
        for i in range(len(num_list)):
            self.ids[num_list[i]].text = ""
        self.ids.success.opacity = 0
        self.ids.fail.opacity = 0
        self.ids.my_answer.text = ""
        self.ids.make.text = "Правильно 0 из 10"
        self.m = 0

    def prov(self):
        if self.ids.prov.opacity == 1:
            if self.ids.my_answer.text != '' and Stolb.flag:
                Stolb.flag = False
                ans = self.ids.my_answer.text
                print(ans)
                print('m == ', self.m)
                if self.m < 9:
                    if int(ans) == Stolb.rez_stolb:
                        sound = SoundLoader.load('sounds/success.wav')
                        self.ids.success.opacity = 1
                        self.ids.fail.opacity = 0
                        self.m = self.m + 1
                        Login.progress = Login.progress + 1
                        self.pars_progress(str(Login.progress))
                        print(Login.progress)
                        print('m == ', self.m)
                        self.ids.make.text = 'Правильно ' + str(self.m) + ' из 10'
                        sound.play()
                    else:
                        Stolb.flag = True
                        sound = SoundLoader.load('sounds/error.wav')
                        self.ids.fail.opacity = 1
                        self.ids.success.opacity = 0
                        sound.play()
                else:
                    self.resetForm()
                    Prodol().open()
            else:
                self.begin_stolb()

                Stolb.flag = True

    # def set_error_message(self, instance_textfield):
    #     self.screen.ids.text_field_error.error = True


    def begin_stolb(self):
        self.ids.prov.opacity = 1
        self.ids.success.opacity = 0
        self.ids.fail.opacity = 0
        self.ids.my_answer.text = ''
        if self.ids.odn.state == "down":
            if self.ids.straight_lower_tog.state == "down":
                s = random.randint(1, 4)
                rezstr = str(s)
                self.str = str(s)
                self.ids.num0.text = self.str
                rez = s
                for i in range(4):
                    s = random.choice(l1[rez])
                    self.str = str(s)
                    self.input_card(i, self.str)
                    rez = rez + s
                    rezstr = rezstr + ' + ' + str(s)
            elif self.ids.straight_all_tog.state == "down":
                s = random.randint(0, 9)
                rezstr = str(s)
                self.str = str(s)
                self.ids.num0.text = self.str
                rez = s
                for i in range(4):
                    s = random.choice(l2[rez])
                    self.str = str(s)
                    self.input_card(i, self.str)
                    rez = rez + s
                    rezstr = rezstr + ' + ' + str(s)
            elif self.ids.young_plus_tog.state == "down":
                s = random.randint(0, 9)
                rezstr = str(s)
                self.str = str(s)
                self.ids.num0.text = self.str
                rez = s
                for i in range(4):
                    s = random.choice(l3[rez])
                    self.str = str(s)
                    self.input_card(i, self.str)
                    rez = rez + s
                    rezstr = rezstr + ' + ' + str(s)
            elif self.ids.young_minus_tog.state == "down":
                s = random.randint(0, 9)
                rezstr = str(s)
                self.str = str(s)
                self.ids.num0.text = self.str
                rez = s
                for i in range(4):
                    s = random.choice(l4[rez])
                    self.str = str(s)
                    self.input_card(i, self.str)
                    rez = rez + s
                    rezstr = rezstr + ' + ' + str(s)
        elif self.ids.dvuz.state == "down":
            if self.ids.straight_lower_tog.state == "down":
                s2 = random.randint(0, 4)
                s1 = random.randint(0, 4)
                self.ids.num0.text = str(10 * s2 + s1)
                rezstr = str(s2) + str(s1)
                rez = 10 * s2 + s1
                for i in range(4):
                    s2 = rez // 10
                    s1 = rez % 10
                    s = s1
                    s2 = random.choice(l1[s2])
                    s1 = random.choice(l1[s])
                    print(s)
                    while s1 * s2 < 0:
                       s1 = random.choice(l1[s])
                    self.input_card(i, str(10*s2+s1))
                    rezstr = rezstr + ' + ' + str(10*s2+s1)
                    rez = rez + 10 * s2 + s1

            elif self.ids.straight_all_tog.state == "down":
                s2 = random.randint(0, 9)
                s1 = random.randint(0, 9)
                self.ids.num0.text = str(10 * s2 + s1)
                rezstr = str(s2) + str(s1)
                rez = 10 * s2 + s1
                for i in range(4):
                    s2 = rez // 10
                    s1 = rez % 10
                    s = s1
                    s2 = random.choice(l2[s2])
                    s1 = random.choice(l2[s])
                    print(s)
                    while s1 * s2 < 0:
                        s1 = random.choice(l2[s])
                    self.input_card(i, str(10 * s2 + s1))
                    rezstr = rezstr + ' + ' + str(10 * s2 + s1)
                    rez = rez + 10 * s2 + s1
            elif self.ids.young_plus_tog.state == "down":
                s2 = random.randint(0, 9)
                s1 = random.randint(0, 9)
                self.ids.num0.text = str(10 * s2 + s1)
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
                    self.input_card(i, str(10 * s2 + s1))
                    rezstr = rezstr + ' + ' + str(10 * s2 + s1)
                    rez = rez + 10 * s2 + s1
            elif self.ids.young_minus_tog.state == "down":
                s2 = random.randint(0, 9)
                s1 = random.randint(0, 9)
                self.ids.num0.text = str(10 * s2 + s1)
                rezstr = str(s2) + str(s1)
                rez = 10 * s2 + s1
                for i in range(4):
                    s2 = rez // 10
                    s1 = rez % 10
                    s = s1
                    s2 = random.choice(l4[s2])
                    s1 = random.choice(l4[s])
                    print(s)
                    while s1 * s2 < 0:
                        s1 = random.choice(l4[s])
                    self.input_card(i, str(10 * s2 + s1))
                    rezstr = rezstr + ' + ' + str(10 * s2 + s1)
                    rez = rez + 10 * s2 + s1
        Stolb.rez_stolb = rez
        print(rez)
        print(rezstr)

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


    def input_card(self, i, str):
        if i == 0:
            if str[0] == '-':
                self.ids.num1.text = str
            else:
                self.ids.num1.text = '+' + str
        elif i == 1:
            if str[0] == '-':
                self.ids.num2.text = str
            else:
                self.ids.num2.text = '+' + str
        elif i == 2:
            if str[0] == '-':
                self.ids.num3.text = str
            else:
                self.ids.num3.text = '+' + str
        elif i == 3:
            if str[0] == '-':
                self.ids.num4.text = str
            else:
                self.ids.num4.text = '+' + str

    def help(self):
        self.ids.my_answer.text = ''
        Stolb.flag = True
        print(Stolb.rez_stolb)
        if not self.dialog:
            self.dialog = MDDialog(
                title='Ответ',
                text = str(Stolb.rez_stolb),
                buttons=[
                    MDFlatButton(
                        text="CANCEL"
                    )
                ],
            )
        self.dialog.open()

