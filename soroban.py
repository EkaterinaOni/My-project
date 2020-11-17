from kivy.uix.screenmanager import Screen
from kivymd.uix.dialog import MDDialog

class Soroban(Screen):
    def __init__(self, *args, **kwargs):
        super(Soroban, self).__init__(*args, **kwargs)
        self.ids.text_lb.text = '       Задайте число и \n ' \
                                'оно установится на соробане'

    def ustanovit(self, n):
        n1 = str(int(n) % 10)
        n2 = str(int(n) // 10)
        self.metka(n1, 1)
        self.metka(n2, 2)
        if n1 < '5':
            self.ids.k5.size_hint = 0.15, 0.1
            self.ids.k6.size_hint = 0, 0
        else:
            self.ids.k5.size_hint = 0, 0
            self.ids.k6.size_hint = 0.15, 0.1

        if (n1 == '0') or (n1 == '5'):
                self.ids.k7.size_hint = 0, 0
                self.ids.k1.size_hint = 0.15, 0.1
                self.ids.k2.size_hint = 0.15, 0.1
                self.ids.k3.size_hint = 0.15, 0.1
                self.ids.k4.size_hint = 0.15, 0.1
        if (n1 == '1') or (n1 == '6'):
                self.ids.k7.size_hint = 0.15, 0.1
                self.ids.k1.size_hint = 0, 0
                self.ids.k2.size_hint = 0.15, 0.1
                self.ids.k3.size_hint = 0.15, 0.1
                self.ids.k4.size_hint = 0.15, 0.1
        if (n1 == '2') or (n1 == '7'):
                self.ids.k7.size_hint = 0.15, 0.1
                self.ids.k1.size_hint = 0.15, 0.1
                self.ids.k2.size_hint = 0, 0
                self.ids.k3.size_hint = 0.15, 0.1
                self.ids.k4.size_hint = 0.15, 0.1
        if (n1 == '3') or (n1 == '8'):
                self.ids.k7.size_hint = 0.15, 0.1
                self.ids.k1.size_hint = 0.15, 0.1
                self.ids.k2.size_hint = 0.15, 0.1
                self.ids.k3.size_hint = 0, 0
                self.ids.k4.size_hint = 0.15, 0.1
        if (n1 == '4') or (n1 == '9'):
                self.ids.k7.size_hint = 0.15, 0.1
                self.ids.k1.size_hint = 0.15, 0.1
                self.ids.k2.size_hint = 0.15, 0.1
                self.ids.k3.size_hint = 0.15, 0.1
                self.ids.k4.size_hint = 0, 0

        if n2 < '5':
            self.ids.k5_1.size_hint = 0.15, 0.1
            self.ids.k6_1.size_hint = 0, 0
        else:
            self.ids.k5_1.size_hint = 0, 0
            self.ids.k6_1.size_hint = 0.15, 0.1

        if (n2 == '0') or (n2 == '5'):
                self.ids.k7_1.size_hint = 0, 0
                self.ids.k1_1.size_hint = 0.15, 0.1
                self.ids.k2_1.size_hint = 0.15, 0.1
                self.ids.k3_1.size_hint = 0.15, 0.1
                self.ids.k4_1.size_hint = 0.15, 0.1
        if (n2 == '1') or (n2 == '6'):
                self.ids.k7_1.size_hint = 0.15, 0.1
                self.ids.k1_1.size_hint = 0, 0
                self.ids.k2_1.size_hint = 0.15, 0.1
                self.ids.k3_1.size_hint = 0.15, 0.1
                self.ids.k4_1.size_hint = 0.15, 0.1
        if (n2 == '2') or (n2 == '7'):
                self.ids.k7_1.size_hint = 0.15, 0.1
                self.ids.k1_1.size_hint = 0.15, 0.1
                self.ids.k2_1.size_hint = 0, 0
                self.ids.k3_1.size_hint = 0.15, 0.1
                self.ids.k4_1.size_hint = 0.15, 0.1
        if (n2 == '3') or (n2 == '8'):
                self.ids.k7_1.size_hint = 0.15, 0.1
                self.ids.k1_1.size_hint = 0.15, 0.1
                self.ids.k2_1.size_hint = 0.15, 0.1
                self.ids.k3_1.size_hint = 0, 0
                self.ids.k4_1.size_hint = 0.15, 0.1
        if (n2 == '4') or (n2 == '9'):
                self.ids.k7_1.size_hint = 0.15, 0.1
                self.ids.k1_1.size_hint = 0.15, 0.1
                self.ids.k2_1.size_hint = 0.15, 0.1
                self.ids.k3_1.size_hint = 0.15, 0.1
                self.ids.k4_1.size_hint = 0, 0

    def number(self):
        self.ustanovit(self.ids.txt.text)

    def metka(self, chislo, k):
        if k == 1:
            self.ids.lb.text = chislo
        else:
            self.ids.lb_1.text = chislo

    def pusto(self):
        self.ids.txt.text = ''

    def fun1(self, i):
        #print(Login.urok)
        self.pusto()
        if i == 1:
            self.ids.k1.size_hint = 0, 0
            if self.ids.k7.size_hint_x == 0:
                self.ids.k7.size_hint = 0.15, 0.1
            else:
                self.ids.k2.size_hint = 0.15, 0.1
                self.ids.k3.size_hint = 0.15, 0.1
                self.ids.k4.size_hint = 0.15, 0.1
            if self.ids.k5.size_hint_x == 0: self.metka('6', 1)
            else: self.metka('1', 1)
        else:
            self.ids.k1_1.size_hint = 0, 0
            if self.ids.k7_1.size_hint_x == 0:
                self.ids.k7_1.size_hint = 0.15, 0.1
            else:
                self.ids.k2_1.size_hint = 0.15, 0.1
                self.ids.k3_1.size_hint = 0.15, 0.1
                self.ids.k4_1.size_hint = 0.15, 0.1
            if self.ids.k5_1.size_hint_x == 0: self.metka('6', 2)
            else: self.metka('1', 2)


    def fun2(self, i):
        self.pusto()
        if i == 1:
            self.ids.k2.size_hint = 0, 0
            if (self.ids.k7.size_hint_x == 0) or (self.ids.k1.size_hint_x == 0):
                self.ids.k7.size_hint = 0.15, 0.1
                self.ids.k1.size_hint = 0.15, 0.1
            else:
                self.ids.k3.size_hint = 0.15, 0.1
                self.ids.k4.size_hint = 0.15, 0.1
            if self.ids.k5.size_hint_x == 0: self.metka('7', 1)
            else: self.metka('2', 1)
        else:
            self.ids.k2_1.size_hint = 0, 0
            if (self.ids.k7_1.size_hint_x == 0) or (self.ids.k1_1.size_hint_x == 0):
                self.ids.k7_1.size_hint = 0.15, 0.1
                self.ids.k1_1.size_hint = 0.15, 0.1
            else:
                self.ids.k3_1.size_hint = 0.15, 0.1
                self.ids.k4_1.size_hint = 0.15, 0.1
            if self.ids.k5_1.size_hint_x == 0:
                self.metka('7', 2)
            else:
                self.metka('2', 2)

    def fun3(self, i):
        self.pusto()
        if i == 1:
            self.ids.k3.size_hint = 0, 0
            if (self.ids.k4.size_hint_x == 0):
                self.ids.k4.size_hint = 0.15, 0.1
            else:
                self.ids.k7.size_hint = 0.15, 0.1
                self.ids.k1.size_hint = 0.15, 0.1
                self.ids.k2.size_hint = 0.15, 0.1
            if self.ids.k5.size_hint_x == 0: self.metka('8', 1)
            else: self.metka('3', 1)
        else:
            self.ids.k3_1.size_hint = 0, 0
            if (self.ids.k4_1.size_hint_x == 0):
                self.ids.k4_1.size_hint = 0.15, 0.1
            else:
                self.ids.k7_1.size_hint = 0.15, 0.1
                self.ids.k1_1.size_hint = 0.15, 0.1
                self.ids.k2_1.size_hint = 0.15, 0.1
            if self.ids.k5_1.size_hint_x == 0: self.metka('8', 2)
            else: self.metka('3', 2)

    def fun4(self, i):
        self.pusto()
        if i == 1:
            self.ids.k4.size_hint = 0, 0
            self.ids.k7.size_hint = 0.15, 0.1
            self.ids.k1.size_hint = 0.15, 0.1
            self.ids.k2.size_hint = 0.15, 0.1
            self.ids.k3.size_hint = 0.15, 0.1
            if self.ids.k5.size_hint_x == 0:
                self.metka('9', 1)
            else:
                self.metka('4', 1)
        else:
            self.ids.k4_1.size_hint = 0, 0
            self.ids.k7_1.size_hint = 0.15, 0.1
            self.ids.k1_1.size_hint = 0.15, 0.1
            self.ids.k2_1.size_hint = 0.15, 0.1
            self.ids.k3_1.size_hint = 0.15, 0.1
            if self.ids.k5_1.size_hint_x == 0:
                self.metka('9', 2)
            else:
                self.metka('4', 2)


    def fun5(self, i):
        self.pusto()
        if i == 1:
            self.ids.k5.size_hint = 0, 0
            self.ids.k6.size_hint = 0.15, 0.1
            if self.ids.k7.size_hint_x == 0: self.metka('5', 1)
            if self.ids.k1.size_hint_x == 0: self.metka('6', 1)
            if self.ids.k2.size_hint_x == 0: self.metka('7', 1)
            if self.ids.k3.size_hint_x == 0: self.metka('8', 1)
            if self.ids.k4.size_hint_x == 0: self.metka('9', 1)
        else:
            self.ids.k5_1.size_hint = 0, 0
            self.ids.k6_1.size_hint = 0.15, 0.1
            if self.ids.k7_1.size_hint_x == 0: self.metka('5', 2)
            if self.ids.k1_1.size_hint_x == 0: self.metka('6', 2)
            if self.ids.k2_1.size_hint_x == 0: self.metka('7', 2)
            if self.ids.k3_1.size_hint_x == 0: self.metka('8', 2)
            if self.ids.k4_1.size_hint_x == 0: self.metka('9', 2)


    def fun6(self,  i):
        self.pusto()
        if i == 1:
            self.ids.k6.size_hint = 0, 0
            self.ids.k5.size_hint = 0.15, 0.1
            if self.ids.k7.size_hint_x == 0: self.metka('0', 1)
            if self.ids.k1.size_hint_x == 0: self.metka('1', 1)
            if self.ids.k2.size_hint_x == 0: self.metka('2', 1)
            if self.ids.k3.size_hint_x == 0: self.metka('3', 1)
            if self.ids.k4.size_hint_x == 0: self.metka('4', 1)
        else:
            self.ids.k6_1.size_hint = 0, 0
            self.ids.k5_1.size_hint = 0.15, 0.1
            if self.ids.k7_1.size_hint_x == 0: self.metka('0', 2)
            if self.ids.k1_1.size_hint_x == 0: self.metka('1', 2)
            if self.ids.k2_1.size_hint_x == 0: self.metka('2', 2)
            if self.ids.k3_1.size_hint_x == 0: self.metka('3', 2)
            if self.ids.k4_1.size_hint_x == 0: self.metka('4', 2)

    def fun7(self, i):
        self.pusto()
        if i == 1:
            self.ids.k7.size_hint = 0, 0
            self.ids.k1.size_hint = 0.15, 0.1
            self.ids.k2.size_hint = 0.15, 0.1
            self.ids.k3.size_hint = 0.15, 0.1
            self.ids.k4.size_hint = 0.15, 0.1
            if self.ids.k5.size_hint_x == 0: self.metka('5', 1)
            else: self.metka('0', 1)
        else:
            self.ids.k7_1.size_hint = 0, 0
            self.ids.k1_1.size_hint = 0.15, 0.1
            self.ids.k2_1.size_hint = 0.15, 0.1
            self.ids.k3_1.size_hint = 0.15, 0.1
            self.ids.k4_1.size_hint = 0.15, 0.1
            if self.ids.k5_1.size_hint_x == 0:
                self.metka('5', 2)
            else:
                self.metka('0', 2)

    def validate(self):
        status = 0 <= int(self.ids.txt.text) <= 99
        if not status:
            print(self.ids.txt.text)
            self.ids.lb.text = '0'
            self.ids.lb_1.text = '0'
            self.ids.txt.text = ''
            dialog = MDDialog(
                title = 'Предупреждение!',
                text='Введите число от 0 до 99',
                size_hint = (None, None),
                size = (300, 200),
            )
            dialog.open()