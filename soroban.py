from kivy.uix.screenmanager import Screen

class Soroban(Screen):
    def __init__(self, *args, **kwargs):
        super(Soroban, self).__init__(*args, **kwargs)

    def ustanovit(self, n):
        self.metka(n)
        if n < '5':
            self.ids.k5.size_hint = 0.15, 0.1
            self.ids.k6.size_hint = 0, 0
        else:
            self.ids.k5.size_hint = 0, 0
            self.ids.k6.size_hint = 0.15, 0.1

        if (n == '0') or (n == '5'):
                self.ids.k7.size_hint = 0, 0
                self.ids.k1.size_hint = 0.15, 0.1
                self.ids.k2.size_hint = 0.15, 0.1
                self.ids.k3.size_hint = 0.15, 0.1
                self.ids.k4.size_hint = 0.15, 0.1
        if (n == '1') or (n == '6'):
                self.ids.k7.size_hint = 0.15, 0.1
                self.ids.k1.size_hint = 0, 0
                self.ids.k2.size_hint = 0.15, 0.1
                self.ids.k3.size_hint = 0.15, 0.1
                self.ids.k4.size_hint = 0.15, 0.1
        if (n == '2') or (n == '7'):
                self.ids.k7.size_hint = 0.15, 0.1
                self.ids.k1.size_hint = 0.15, 0.1
                self.ids.k2.size_hint = 0, 0
                self.ids.k3.size_hint = 0.15, 0.1
                self.ids.k4.size_hint = 0.15, 0.1
        if (n == '3') or (n == '8'):
                self.ids.k7.size_hint = 0.15, 0.1
                self.ids.k1.size_hint = 0.15, 0.1
                self.ids.k2.size_hint = 0.15, 0.1
                self.ids.k3.size_hint = 0, 0
                self.ids.k4.size_hint = 0.15, 0.1
        if (n == '4') or (n == '9'):
                self.ids.k7.size_hint = 0.15, 0.1
                self.ids.k1.size_hint = 0.15, 0.1
                self.ids.k2.size_hint = 0.15, 0.1
                self.ids.k3.size_hint = 0.15, 0.1
                self.ids.k4.size_hint = 0, 0

    def number(self):
        self.ustanovit(self.ids.txt.text)

    def metka(self, chislo):
        self.ids.lb.text = chislo

    def pusto(self):
        self.ids.txt.text = ''

    def fun1(self):
        #print(Login.urok)
        self.pusto()
        self.ids.k1.size_hint = 0, 0
        if self.ids.k7.size_hint_x == 0:
            self.ids.k7.size_hint = 0.15, 0.1
        else:
            self.ids.k2.size_hint = 0.15, 0.1
            self.ids.k3.size_hint = 0.15, 0.1
            self.ids.k4.size_hint = 0.15, 0.1
        if self.ids.k5.size_hint_x == 0: self.metka('6')
        else: self.metka('1')

    def fun2(self):
        self.pusto()
        self.ids.k2.size_hint = 0, 0
        if (self.ids.k7.size_hint_x == 0) or (self.ids.k1.size_hint_x == 0):
            self.ids.k7.size_hint = 0.15, 0.1
            self.ids.k1.size_hint = 0.15, 0.1
        else:
            self.ids.k3.size_hint = 0.15, 0.1
            self.ids.k4.size_hint = 0.15, 0.1
        if self.ids.k5.size_hint_x == 0: self.metka('7')
        else: self.metka('2')

    def fun3(self):
        self.pusto()
        self.ids.k3.size_hint = 0, 0
        if (self.ids.k4.size_hint_x == 0):
            self.ids.k4.size_hint = 0.15, 0.1
        else:
            self.ids.k7.size_hint = 0.15, 0.1
            self.ids.k1.size_hint = 0.15, 0.1
            self.ids.k2.size_hint = 0.15, 0.1
        if self.ids.k5.size_hint_x == 0: self.metka('8')
        else: self.metka('3')

    def fun4(self):
        self.pusto()
        self.ids.k4.size_hint = 0, 0
        self.ids.k7.size_hint = 0.15, 0.1
        self.ids.k1.size_hint = 0.15, 0.1
        self.ids.k2.size_hint = 0.15, 0.1
        self.ids.k3.size_hint = 0.15, 0.1
        if self.ids.k5.size_hint_x == 0:
            self.metka('9')
        else:
            self.metka('4')

    def fun5(self):
        self.pusto()
        self.ids.k5.size_hint = 0, 0
        self.ids.k6.size_hint = 0.15, 0.1
        if self.ids.k7.size_hint_x == 0: self.metka('5')
        if self.ids.k1.size_hint_x == 0: self.metka('6')
        if self.ids.k2.size_hint_x == 0: self.metka('7')
        if self.ids.k3.size_hint_x == 0: self.metka('8')
        if self.ids.k4.size_hint_x == 0: self.metka('9')

    def fun6(self):
        self.pusto()
        self.ids.k6.size_hint = 0, 0
        self.ids.k5.size_hint = 0.15, 0.1
        if self.ids.k7.size_hint_x == 0: self.metka('0')
        if self.ids.k1.size_hint_x == 0: self.metka('1')
        if self.ids.k2.size_hint_x == 0: self.metka('2')
        if self.ids.k3.size_hint_x == 0: self.metka('3')
        if self.ids.k4.size_hint_x == 0: self.metka('4')

    def fun7(self):
        self.pusto()
        self.ids.k7.size_hint = 0, 0
        self.ids.k1.size_hint = 0.15, 0.1
        self.ids.k2.size_hint = 0.15, 0.1
        self.ids.k3.size_hint = 0.15, 0.1
        self.ids.k4.size_hint = 0.15, 0.1
        if self.ids.k5.size_hint_x == 0: self.metka('5')
        else: self.metka('0')