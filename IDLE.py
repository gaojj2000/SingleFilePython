# _*_ coding:utf-8 _*_
# FileName: IDLE.py
# IDE: PyCharm

import os
import sys
import tkinter


class IDLE(object):
    def __init__(self):
        self.insert = '3.4'
        self.code = ""
        self.tabs = ""
        self.flag = False
        self.tab = False
        self.root = tkinter.Tk()
        self.wz = tkinter.StringVar()
        self.root.title(' Python ' + sys.version[0:5] + ' Shell')
        self.connect = 'Python ' + sys.version + ' on win64\nType "copyright", "credits" or "license()" for more information.\n>>> '
        self.wz.set("Ln:3  Col:4")

        self.file = tkinter.Button(self.root, text='File', font=('黑体', 10), fg='black', activebackground='#e5f3ff', command=lambda: self.ls)
        self.file.place(x=1, y=0, width=50, height=21)
        self.edit = tkinter.Button(self.root, text='Edit', font=('黑体', 10), fg='black', activebackground='#e5f3ff', command=lambda: self.ls)
        self.edit.place(x=51, y=0, width=50, height=21)
        self.shell = tkinter.Button(self.root, text='Shell', font=('黑体', 10), fg='black', activebackground='#e5f3ff', command=lambda: self.ls)
        self.shell.place(x=101, y=0, width=50, height=21)
        self.debug = tkinter.Button(self.root, text='Debug', font=('黑体', 10), fg='black', activebackground='#e5f3ff', command=lambda: self.ls)
        self.debug.place(x=151, y=0, width=50, height=21)
        self.options = tkinter.Button(self.root, text='Options', font=('黑体', 10), fg='black', activebackground='#e5f3ff', command=lambda: self.ls)
        self.options.place(x=201, y=0, width=50, height=21)
        self.window = tkinter.Button(self.root, text='Window', font=('黑体', 10), fg='black', activebackground='#e5f3ff', command=lambda: self.ls)
        self.window.place(x=251, y=0, width=50, height=21)
        self.help = tkinter.Button(self.root, text='Help', font=('黑体', 10), fg='black', activebackground='#e5f3ff', command=lambda: self.ls)
        self.help.place(x=301, y=0, width=50, height=21)

        self.scrollbar = tkinter.Scrollbar(self.root)
        self.scrollbar.place(x=577, y=21, width=16, height=524)
        self.text = tkinter.Text(self.root, font=('微软雅黑', 10), bd=0, fg='black', yscrollcommand=self.scrollbar.set, relief='flat', wrap='none')  # wrap 设置不自动换行
        self.text.place(x=1, y=21, width=576, height=524)
        self.scrollbar.config(command=self.text.yview)
        self.text.insert('insert', self.connect)
        self.text.bind('<Return>', self.get_connect)
        self.text.bind('<Key>', self.change_wz_jp)
        self.text.update()

        self.label = tkinter.Label(self.root, font=('微软雅黑', 10), bd='9', fg='#4F4F4F', anchor='e', textvariable=self.wz)
        self.label.place(x=1, y=545, width=593, height=20)

    def main(self):
        self.root.geometry('595x565')
        self.root.resizable(False, False)
        self.root.mainloop()

    def ls(self):
        pass

    def get_connect(self, event):
        key_words1 = ['if', 'elif', 'else', 'while', 'for', 'class', 'def']
        key_words2 = ['print', 'return', 'input']
        if event:
            back = ""
            connect = self.text.get(self.insert, tkinter.END)
            if ':' in connect:
                for item in key_words1:
                    if item in connect:
                        self.tabs += "    "
                        break
            old = self.code
            self.code += connect
            path = r'C:\Windows\Temp\temp.py'
            with open(path, 'w', encoding='utf-8') as f:
                f.write(self.code)
            for item in key_words2:
                if item in connect:
                    self.flag = True
                    break
            if self.flag:
                self.flag = False
                cmd = 'python ' + path
                flag = os.system(cmd)
                back = os.popen(cmd).read()
            else:
                flag = 0
            if flag == 0:
                if back == "":
                    self.text.insert('insert', "\n>>> " + self.tabs)
                else:
                    self.text.insert('insert', "\n" + back + ">>> ")
                    if 'print' in connect:
                        self.code = self.code.replace(connect, "")
            else:
                self.code = old
                self.text.insert('insert', "\n" + "命令输入错误！\n" + ">>> ")
            self.insert = str(int(float(self.text.index('insert')))) + ".4"

    def change_wz_jp(self, event):
        if event.keycode != 229:
            if event.keycode in [8, 37]:
                if len(self.text.get(self.insert, tkinter.END).replace(" ", "")) == 1:
                    self.tabs = int((len(self.text.get(self.insert, tkinter.END)) - 2) / 4) * 4 * " "
                self.wz.set("Ln:{}  Col:{}".format(self.text.index('insert').split('.')[0], int(self.text.index('insert').split('.')[1]) - 1))
            elif event.keycode in [38]:
                self.wz.set("Ln:{}  Col:{}".format(int(self.text.index('insert').split('.')[0]) - 1, self.text.index('insert').split('.')[1]))
            elif event.keycode in [40]:
                self.wz.set("Ln:{}  Col:{}".format(int(self.text.index('insert').split('.')[0]) + 1, self.text.index('insert').split('.')[1]))
            else:
                self.wz.set("Ln:{}  Col:{}".format(self.text.index('insert').split('.')[0], int(self.text.index('insert').split('.')[1]) + 1))


if __name__ == '__main__':
    i = IDLE()
    i.main()
