# _*_ coding:utf-8 _*_
# FileName: SuperClac.py
# IDE: PyCharm

import tkinter
from fractions import Fraction
import tkinter.messagebox as msgbox


class Calc(object):
    def __init__(self):
        self.a1 = self.b1 = self.c1 = ""
        self.a1_s = self.b1_s = self.c1_s = ""
        self.a2 = self.b2 = self.c2 = ""
        self.a2_s = self.b2_s = self.c2_s = ""
        self.result1 = self.result2 = ""

        self.result = ''
        self.show = ''
        self.flag = False
        self.num = False
        self.symbol = False
        self.calc = '0'
        self.ans = 0

        self.title = '超级计算器'
        self.root = tkinter.Tk(className=self.title)
        self.root.wm_attributes('-topmost', 1)

        self.result = tkinter.StringVar()
        self.result.set(0)
        self.show = tkinter.StringVar()
        self.show.set('')

        self.title1 = tkinter.StringVar()
        self.title2 = tkinter.StringVar()
        self.title3 = tkinter.StringVar()
        self.title4 = tkinter.StringVar()
        self.bg1 = tkinter.StringVar()
        self.bg2 = tkinter.StringVar()
        self.title1.set('一元一次方程：')
        self.title2.set('一元二次方程：')
        self.title3.set('二元一次方程组：')
        self.title4.set('方程计算结果是： ')
        self.bg1.set('    x +       = 0                x*x +       x +        = 0    {       x +        y +       = 0')
        self.bg2.set('                                                                            {       x +        y +       = 0')

        self.cs1 = tkinter.StringVar()
        self.cs2 = tkinter.StringVar()
        self.cs3 = tkinter.StringVar()
        self.cs4 = tkinter.StringVar()
        self.cs5 = tkinter.StringVar()
        self.cs6 = tkinter.StringVar()
        self.cs7 = tkinter.StringVar()
        self.cs8 = tkinter.StringVar()
        self.cs9 = tkinter.StringVar()
        self.cs10 = tkinter.StringVar()
        self.cs11 = tkinter.StringVar()
        self.results = tkinter.StringVar()
        self.cs1.set('')
        self.cs2.set('')
        self.cs3.set('')
        self.cs4.set('')
        self.cs5.set('')
        self.cs6.set('')
        self.cs7.set('')
        self.cs8.set('')
        self.cs9.set('')
        self.cs10.set('')
        self.cs11.set('')
        self.results.set('')

        label01 = tkinter.Label(self.root, font=('微软雅黑', 10), bd='9', fg='#4F4F4F', anchor='w', textvariable=self.bg1)
        label01.place(x=10, y=40, width=490, height=25)
        label02 = tkinter.Label(self.root, font=('微软雅黑', 10), bd='9', fg='#4F4F4F', anchor='w', textvariable=self.bg2)
        label02.place(x=10, y=80, width=490, height=25)

        label1 = tkinter.Label(self.root, font=('微软雅黑', 10), bd='9', fg='#4F4F4F', anchor='w', textvariable=self.title1)
        label1.place(x=10, y=10, width=100, height=25)
        label2 = tkinter.Label(self.root, font=('微软雅黑', 10), bd='9', fg='#4F4F4F', anchor='w', textvariable=self.title2)
        label2.place(x=140, y=10, width=100, height=25)
        label3 = tkinter.Label(self.root, font=('微软雅黑', 10), bd='9', fg='#4F4F4F', anchor='w', textvariable=self.title3)
        label3.place(x=330, y=10, width=120, height=25)
        label4 = tkinter.Label(self.root, font=('微软雅黑', 15), bd='9', fg='#4F4F4F', anchor='e', textvariable=self.title4)
        label4.place(x=320, y=360, width=200, height=40)

        label5 = tkinter.Label(self.root, font=('微软雅黑', 15), bg='blue', bd='9', fg='yellow', anchor='w', textvariable=self.results)
        label5.place(x=10, y=400, width=480, height=40)

        entry1 = tkinter.Entry(textvariable=self.cs1, highlightcolor="Fuchsia", highlightthickness=1, width=25)
        entry1.place(x=10, y=40, width=25, height=25)
        entry2 = tkinter.Entry(textvariable=self.cs2, highlightcolor="Fuchsia", highlightthickness=1, width=25)
        entry2.place(x=60, y=40, width=25, height=25)
        entry3 = tkinter.Entry(textvariable=self.cs3, highlightcolor="Fuchsia", highlightthickness=1, width=25)
        entry3.place(x=145, y=40, width=25, height=25)
        entry4 = tkinter.Entry(textvariable=self.cs4, highlightcolor="Fuchsia", highlightthickness=1, width=25)
        entry4.place(x=205, y=40, width=25, height=25)
        entry5 = tkinter.Entry(textvariable=self.cs5, highlightcolor="Fuchsia", highlightthickness=1, width=25)
        entry5.place(x=260, y=40, width=25, height=25)
        entry6 = tkinter.Entry(textvariable=self.cs6, highlightcolor="Fuchsia", highlightthickness=1, width=25)
        entry6.place(x=330, y=40, width=25, height=25)
        entry7 = tkinter.Entry(textvariable=self.cs7, highlightcolor="Fuchsia", highlightthickness=1, width=25)
        entry7.place(x=380, y=40, width=25, height=25)
        entry8 = tkinter.Entry(textvariable=self.cs8, highlightcolor="Fuchsia", highlightthickness=1, width=25)
        entry8.place(x=435, y=40, width=25, height=25)
        entry9 = tkinter.Entry(textvariable=self.cs9, highlightcolor="Fuchsia", highlightthickness=1, width=25)
        entry9.place(x=330, y=80, width=25, height=25)
        entry10 = tkinter.Entry(textvariable=self.cs10, highlightcolor="Fuchsia", highlightthickness=1, width=25)
        entry10.place(x=380, y=80, width=25, height=25)
        entry11 = tkinter.Entry(textvariable=self.cs11, highlightcolor="Fuchsia", highlightthickness=1, width=25)
        entry11.place(x=435, y=80, width=25, height=25)

        btnrun11 = tkinter.Button(self.root, text='计算一元一次方程', font=('微软雅黑', 15), fg='#4F4F4F', bd=0.5, bg='orange', command=lambda: Calc.run11(self))
        btnrun11.place(x=320, y=120, width=180, height=40)
        btnrun12 = tkinter.Button(self.root, text='计算一元二次方程', font=('微软雅黑', 15), fg='#4F4F4F', bd=0.5, bg='orange', command=lambda: Calc.run12(self))
        btnrun12.place(x=320, y=180, width=180, height=40)
        btnrun21 = tkinter.Button(self.root, text='计算二元一次方程', font=('微软雅黑', 15), fg='#4F4F4F', bd=0.5, bg='orange', command=lambda: Calc.run21(self))
        btnrun21.place(x=320, y=240, width=180, height=40)
        btncls = tkinter.Button(self.root, text='清空全部方程数据', font=('微软雅黑', 15), fg='#4F4F4F', bd=0.5, bg='orange', command=lambda: Calc.cls(self))
        btncls.place(x=320, y=300, width=180, height=40)

        label1 = tkinter.Label(self.root, font=('微软雅黑', 15), bg='#EEE9E9', bd='9', fg='#828282', anchor='e', relief='ridge', borderwidth=2, textvariable=self.show)
        label1.place(x=5, y=80, width=300, height=25)
        label2 = tkinter.Label(self.root, font=('微软雅黑', 20), bg='#EEE9E9', bd='9', fg='black', anchor='e', relief='raised', borderwidth=5, textvariable=self.result)
        label2.place(x=5, y=105, width=300, height=35)

        btn0 = tkinter.Button(self.root, text='0', font=('微软雅黑', 20), fg='#4F4F4F', bd=0.5, command=lambda: Calc.num_change(self, '0'))
        btn0.place(x=80, y=340, width=75, height=50)
        btn1 = tkinter.Button(self.root, text='1', font=('微软雅黑', 20), fg='#4F4F4F', bd=0.5, command=lambda: Calc.num_change(self, '1'))
        btn1.place(x=5, y=290, width=75, height=50)
        btn2 = tkinter.Button(self.root, text='2', font=('微软雅黑', 20), fg='#4F4F4F', bd=0.5, command=lambda: Calc.num_change(self, '2'))
        btn2.place(x=80, y=290, width=75, height=50)
        btn3 = tkinter.Button(self.root, text='3', font=('微软雅黑', 20), fg='#4F4F4F', bd=0.5, command=lambda: Calc.num_change(self, '3'))
        btn3.place(x=155, y=290, width=75, height=50)
        btn4 = tkinter.Button(self.root, text='4', font=('微软雅黑', 20), fg='#4F4F4F', bd=0.5, command=lambda: Calc.num_change(self, '4'))
        btn4.place(x=5, y=240, width=75, height=50)
        btn5 = tkinter.Button(self.root, text='5', font=('微软雅黑', 20), fg='#4F4F4F', bd=0.5, command=lambda: Calc.num_change(self, '5'))
        btn5.place(x=80, y=240, width=75, height=50)
        btn6 = tkinter.Button(self.root, text='6', font=('微软雅黑', 20), fg='#4F4F4F', bd=0.5, command=lambda: Calc.num_change(self, '6'))
        btn6.place(x=155, y=240, width=75, height=50)
        btn7 = tkinter.Button(self.root, text='7', font=('微软雅黑', 20), fg='#4F4F4F', bd=0.5, command=lambda: Calc.num_change(self, '7'))
        btn7.place(x=5, y=190, width=75, height=50)
        btn8 = tkinter.Button(self.root, text='8', font=('微软雅黑', 20), fg='#4F4F4F', bd=0.5, command=lambda: Calc.num_change(self, '8'))
        btn8.place(x=80, y=190, width=75, height=50)
        btn9 = tkinter.Button(self.root, text='9', font=('微软雅黑', 20), fg='#4F4F4F', bd=0.5, command=lambda: Calc.num_change(self, '9'))
        btn9.place(x=155, y=190, width=75, height=50)

        btnac = tkinter.Button(self.root, text='AC', bd=0.5, font=('黑体', 20), fg='orange', command=lambda: Calc.ac(self))
        btnac.place(x=5, y=140, width=75, height=50)
        btnback = tkinter.Button(self.root, text='←', font=('微软雅黑', 20), fg='#4F4F4F', bd=0.5, command=lambda: Calc.back(self))
        btnback.place(x=80, y=140, width=75, height=50)
        btndivi = tkinter.Button(self.root, text='÷', font=('微软雅黑', 20), fg='#4F4F4F', bd=0.5, command=lambda: Calc.symbol_change(self, '/'))
        btndivi.place(x=155, y=140, width=75, height=50)
        btnmul = tkinter.Button(self.root, text='×', font=('微软雅黑', 20), fg='#4F4F4F', bd=0.5, command=lambda: Calc.symbol_change(self, '*'))
        btnmul.place(x=230, y=140, width=75, height=50)
        btnsub = tkinter.Button(self.root, text='-', font=('微软雅黑', 20), fg='#4F4F4F', bd=0.5, command=lambda: Calc.symbol_change(self, '-'))
        btnsub.place(x=230, y=190, width=75, height=50)
        btnadd = tkinter.Button(self.root, text='+', font=('微软雅黑', 20), fg='#4F4F4F', bd=0.5, command=lambda: Calc.symbol_change(self, '+'))
        btnadd.place(x=230, y=240, width=75, height=50)
        btnequ = tkinter.Button(self.root, text='=', font=('微软雅黑', 20), fg='#4F4F4F', bd=0.5, bg='orange', command=lambda: Calc.calc(self))
        btnequ.place(x=230, y=290, width=75, height=100)
        btnper = tkinter.Button(self.root, text='%', font=('微软雅黑', 20), fg='#4F4F4F', bd=0.5, command=lambda: Calc.symbol_change(self, '%'))
        btnper.place(x=5, y=340, width=75, height=50)
        btnpoint = tkinter.Button(self.root, text='.', font=('微软雅黑', 20), fg='#4F4F4F', bd=0.5, command=lambda: Calc.symbol_change(self, '.'))
        btnpoint.place(x=155, y=340, width=75, height=50)

    def main(self):
        self.root.geometry('500x450')
        self.root.resizable(False, False)
        self.root.mainloop()

    def num_change(self, num):
        if self.flag:
            self.flag = False
            self.calc = num
        elif self.calc == '0' and num != '0':
            self.calc = num
        elif self.calc == '0' and num == '0':
            self.calc = '0'
        else:
            self.calc += num
        self.result.set(self.calc)

    def calc(self):
        if "=" in self.result.get():
            return
        data = self.result.get().replace('ANS', str(self.ans)).lstrip('+')
        if data[-1] in ['+', '-', '*', '/', '÷', '%']:
            data = data[0:-1]
        self.ans = eval(data.replace('÷', '/'))
        self.flag = True
        self.calc = str(self.ans)
        if int(self.ans) == self.ans:
            self.ans = int(self.ans)
        else:
            self.ans = round(self.ans, 14)
        self.show.set(data)
        self.result.set('= ' + str(self.ans))

    def ac(self):
        self.ans = 0
        self.calc = '0'
        self.flag = False
        self.result.set(0)
        self.show.set('')

    def back(self):
        if self.flag:
            self.flag = False
        if len(self.result.get()) == 1 or self.calc == '' or self.calc == self.ans:
            result = '0'
        else:
            result = str(self.calc)[0:-1]
        self.calc = result
        self.result.set(self.calc)

    def symbol_change(self, symbol):
        if symbol == '/':
            symbol = '÷'
        if self.flag:
            self.calc = 'ANS'
            self.flag = False
        if (self.calc == '0' or self.calc == '-') and symbol != '-' and symbol != '.':
            self.calc = '0'
        elif (self.calc == '0' or self.calc == '-') and symbol == '-':
            self.calc = symbol
        elif self.calc == '0' and symbol == '.':
            self.calc += symbol
        elif self.calc[-1] in ['+', '-', '*', '/', '÷', '%'] and symbol == '.':
            self.calc += '0.'
        elif self.calc[-1] not in ['+', '-', '*', '/', '÷', '%', '.']:
            self.calc = str(self.calc) + symbol
        else:
            self.calc = str(self.calc)[0:-1] + symbol
        self.result.set(self.calc)

    def run11(self):
        self.a1 = self.b1 = ""
        self.a1_s = self.b1_s = ""
        self.result1 = ""
        while not self.a1_s.replace("+", "").replace("-", "").replace("/", "").replace("%", "").replace("*", "").replace(".", "").replace(" ", "").isdigit():
            self.a1_s = self.cs1.get().replace(" ", "")
            if self.a1_s.replace("+", "").replace("-", "").replace("/", "").replace("%", "").replace("*", "") == "0":
                self.a1_s = ""
                self.cs1.set('')
                msgbox.showerror(title="警告", message="一次项系数不能为0！")
                return
            elif self.a1_s == "":
                msgbox.showerror(title="警告", message="一次项系数不能为空！")
                return
            if not self.a1_s.replace("+", "").replace("-", "").replace("/", "").replace("%", "").replace("*", "").replace(".", "").replace(" ", "").isdigit():
                msgbox.showerror(title="警告", message="请输入正确的系数！")
                return
        try:
            self.a1 = Fraction(self.a1_s)
        except ValueError:
            msgbox.showerror(title="警告", message="请勿将算式输入到系数！")
            return
        while not self.b1_s.replace("+", "").replace("-", "").replace("/", "").replace("%", "").replace("*", "").replace(".", "").replace(" ", "").isdigit():
            if self.cs2.get() == "":
                self.cs2.set('0')
            self.b1_s = self.cs2.get().replace(" ", "")
            if not self.b1_s.replace("+", "").replace("-", "").replace("/", "").replace("%", "").replace("*", "").replace(".", "").replace(" ", "").isdigit():
                msgbox.showerror(title="警告", message="请输入正确的系数！")
                return
        try:
            self.b1 = Fraction(self.b1_s)
        except ValueError:
            msgbox.showerror(title="警告", message="请勿将算式输入到系数！")
            return
        self.result1 = (-1) * Fraction(self.b1 / self.a1)
        if self.result1 == int(self.result1):
            self.result1 = int(self.result1)
        self.results.set("x = " + str(self.result1))

    def run12(self):
        self.a1 = self.b1 = self.c1 = ""
        self.a1_s = self.b1_s = self.c1_s = ""
        self.result1 = self.result2 = ""
        while not self.a1_s.replace("+", "").replace("-", "").replace("/", "").replace("%", "").replace("*", "").replace(".", "").replace(" ", "").isdigit():
            self.a1_s = self.cs3.get().replace(" ", "")
            if self.a1_s.replace("+", "").replace("-", "").replace("/", "").replace("%", "").replace("*", "") == "0":
                self.a1_s = ""
                self.cs3.set('')
                msgbox.showerror(title="警告", message="二次项系数不能为0！")
                return
            elif self.a1_s == "":
                msgbox.showerror(title="警告", message="二次项系数不能为空！")
                return
            if not self.a1_s.replace("+", "").replace("-", "").replace("/", "").replace("%", "").replace("*", "").replace(".", "").replace(" ", "").isdigit():
                msgbox.showerror(title="警告", message="请输入正确的系数！")
                return
        try:
            self.a1 = Fraction(self.a1_s)
        except ValueError:
            msgbox.showerror(title="警告", message="请勿将算式输入到系数！")
            return
        while not self.b1_s.replace("+", "").replace("-", "").replace("/", "").replace("%", "").replace("*", "").replace(".", "").replace(" ", "").isdigit():
            if self.cs4.get() == "":
                self.cs4.set('0')
            self.b1_s = self.cs4.get().replace(" ", "")
            if not self.b1_s.replace("+", "").replace("-", "").replace("/", "").replace("%", "").replace("*", "").replace(".", "").replace(" ", "").isdigit():
                msgbox.showerror(title="警告", message="请输入正确的系数！")
                return
        try:
            self.b1 = Fraction(self.b1_s)
        except ValueError:
            msgbox.showerror(title="警告", message="请勿将算式输入到系数！")
            return
        while not self.c1_s.replace("+", "").replace("-", "").replace("/", "").replace("%", "").replace("*", "").replace(".", "").replace(" ", "").isdigit():
            if self.cs5.get() == "":
                self.cs5.set('0')
            self.c1_s = self.cs5.get().replace(" ", "")
            if not self.c1_s.replace("+", "").replace("-", "").replace("/", "").replace("%", "").replace("*", "").replace(".", "").replace(" ", "").isdigit():
                msgbox.showerror(title="警告", message="请输入正确的系数！")
                return
        try:
            self.c1 = Fraction(self.c1_s)
        except ValueError:
            msgbox.showerror(title="警告", message="请勿将算式输入到系数！")
            return
        delta = Fraction(self.b1 * self.b1 - 4 * self.a1 * self.c1)
        if delta < 0:
            self.results.set("该方程无实根")
        else:
            self.result1 = (-1) * (self.b1 - delta ** 0.5) / (2 * self.a1)
            if self.result1 == int(self.result1):
                self.result1 = int(self.result1)
            self.result2 = (-1) * (self.b1 + delta ** 0.5) / (2 * self.a1)
            if self.result2 == int(self.result2):
                self.result2 = int(self.result2)
            self.results.set("x1 = " + str(self.result1) + "，x2 = " + str(self.result2))

    def run21(self):
        self.a1 = self.b1 = self.c1 = ""
        self.a1_s = self.b1_s = self.c1_s = ""
        self.a2 = self.b2 = self.c2 = ""
        self.a2_s = self.b2_s = self.c2_s = ""
        self.result1 = self.result2 = ""
        while True:
            while not self.a1_s.replace("+", "").replace("-", "").replace("/", "").replace("%", "").replace("*", "").replace(".", "").replace(" ", "").isdigit():
                if self.cs6.get() == "":
                    self.cs6.set('0')
                self.a1_s = self.cs6.get().replace(" ", "")
                if not self.a1_s.replace("+", "").replace("-", "").replace("/", "").replace("%", "").replace("*", "").replace(".", "").replace(" ", "").isdigit():
                    msgbox.showerror(title="警告", message="请输入正确的系数！")
                    return
            try:
                self.a1 = Fraction(self.a1_s)
            except ValueError:
                msgbox.showerror(title="警告", message="请勿将算式输入到系数！")
                return
            while not self.b1_s.replace("+", "").replace("-", "").replace("/", "").replace("%", "").replace("*", "").replace(".", "").replace(" ", "").isdigit():
                if self.cs7.get() == "":
                    self.cs7.set('0')
                self.b1_s = self.cs7.get().replace(" ", "")
                if not self.b1_s.replace("+", "").replace("-", "").replace("/", "").replace("%", "").replace("*", "").replace(".", "").replace(" ", "").isdigit():
                    msgbox.showerror(title="警告", message="请输入正确的系数！")
                    return
            try:
                self.b1 = Fraction(self.b1_s)
            except ValueError:
                msgbox.showerror(title="警告", message="请勿将算式输入到系数！")
                return
            if self.a1 == 0 and self.b1 == 0:
                self.cs6.set('')
                self.cs7.set('')
                msgbox.showerror(title="警告", message="第一行方程x、y前系数不能同时为0！")
                return
            elif self.a1_s == "" and self.b1_s == "":
                msgbox.showerror(title="警告", message="第一行方程x、y前系数不能同时为空！")
                return
            else:
                break
        while not self.c1_s.replace("+", "").replace("-", "").replace("/", "").replace("%", "").replace("*", "").replace(".", "").replace(" ", "").isdigit():
            if self.cs8.get() == "":
                self.cs8.set('0')
            self.c1_s = self.cs8.get().replace(" ", "")
            if not self.c1_s.replace("+", "").replace("-", "").replace("/", "").replace("%", "").replace("*", "").replace(".", "").replace(" ", "").isdigit():
                msgbox.showerror(title="警告", message="请输入正确的系数！")
                return
        try:
            self.c1 = Fraction(self.c1_s)
        except ValueError:
            msgbox.showerror(title="警告", message="请勿将算式输入到系数！")
            return
        while True:
            while not self.a2_s.replace("+", "").replace("-", "").replace("/", "").replace("%", "").replace("*", "").replace(".", "").replace(" ", "").isdigit():
                if self.cs9.get() == "":
                    self.cs9.set('0')
                self.a2_s = self.cs9.get().replace(" ", "")
                if not self.a2_s.replace("+", "").replace("-", "").replace("/", "").replace("%", "").replace("*", "").replace(".", "").replace(" ", "").isdigit():
                    msgbox.showerror(title="警告", message="请输入正确的系数！")
                    return
            try:
                self.a2 = Fraction(self.a2_s)
            except ValueError:
                msgbox.showerror(title="警告", message="请勿将算式输入到系数！")
                return
            while not self.b2_s.replace("+", "").replace("-", "").replace("/", "").replace("%", "").replace("*", "").replace(".", "").replace(" ", "").isdigit():
                if self.cs10.get() == "":
                    self.cs10.set('0')
                self.b2_s = self.cs10.get().replace(" ", "")
                if not self.b2_s.replace("+", "").replace("-", "").replace("/", "").replace("%", "").replace("*", "").replace(".", "").replace(" ", "").isdigit():
                    msgbox.showerror(title="警告", message="请输入正确的系数！")
                    return
            try:
                self.b2 = Fraction(self.b2_s)
            except ValueError:
                msgbox.showerror(title="警告", message="请勿将算式输入到系数！")
                return
            if self.a2 == 0 and self.b2 == 0:
                self.cs9.set('')
                self.cs10.set('')
                msgbox.showerror(title="警告", message="第二行方程x、y前系数不能同时为0！")
                return
            elif self.a2_s == "" and self.b2_s == "":
                msgbox.showerror(title="警告", message="第二行方程x、y前系数不能同时为空！")
                return
            else:
                break
        while not self.c2_s.replace("+", "").replace("-", "").replace("/", "").replace("%", "").replace("*", "").replace(".", "").replace(" ", "").isdigit():
            if self.cs11.get() == "":
                self.cs11.set('0')
            self.c2_s = self.cs11.get().replace(" ", "")
            if not self.c2_s.replace("+", "").replace("-", "").replace("/", "").replace("%", "").replace("*", "").replace(".", "").replace(" ", "").isdigit():
                msgbox.showerror(title="警告", message="请输入正确的系数！")
                return
        try:
            self.c2 = Fraction(self.c2_s)
        except ValueError:
            msgbox.showerror(title="警告", message="请勿将算式输入到系数！")
            return
        delta = Fraction(self.a1 * self.b2 - self.a2 * self.b1)
        if delta == 0:
            self.results.set("该二元一次方程组无解")
        else:
            x = self.c2 * self.b1 - self.c1 * self.b2
            y = self.a2 * self.c1 - self.a1 * self.c2
            self.result1 = Fraction(x / delta)
            self.result2 = Fraction(y / delta)
            self.results.set("x = " + str(self.result1) + "，y = " + str(self.result2))

    def cls(self):
        self.cs1.set('')
        self.cs2.set('')
        self.cs3.set('')
        self.cs4.set('')
        self.cs5.set('')
        self.cs6.set('')
        self.cs7.set('')
        self.cs8.set('')
        self.cs9.set('')
        self.cs10.set('')
        self.cs11.set('')
        self.results.set('')


if __name__ == '__main__':
    calc = Calc()
    calc.main()
