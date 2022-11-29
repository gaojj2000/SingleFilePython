# _*_ coding:utf-8 _*_
# FileName: U_rw.py
# IDE: PyCharm

# U盘加密程序可设置密码版！

import os
import sys
import tkinter
import win32api
import win32con
from tkinter import messagebox as msg


class EXE(tkinter.Tk):
    def __init__(self):
        super().__init__(className=' U盘加密解密程序——GJJ定制版')
        self.flag = 0
        self.password = ''
        self.inp = tkinter.StringVar()
        self.click = tkinter.Label(self, text='显示', font=('', 10), foreground='red')
        self.click.place(x=230, y=35, width=100, height=25)
        self.label = tkinter.Label(self, font=('', 12))
        self.label.place(x=0, y=10, width=420, height=20)
        self.entry = tkinter.Entry(self, show='*', textvariable=self.inp)
        self.entry.place(x=160, y=35, width=100, height=25)
        self.button = tkinter.Button(self, text='解密', command=self.judge)
        self.button.place(x=170, y=65, width=80, height=30)
        self.get()
        self.check()
        self.attributes('-topmost', 1)
        self.geometry(f'420x100')
        self.click.bind('<Button-1>', self.psd_config)
        self.protocol("WM_DELETE_WINDOW", self.close)
        self.mainloop()

    def check(self):
        if os.path.isdir('0.' + self.password + '.{21EC2020-3AEA-1069-A2DD-08002B30309D}'):
            text = '当前解密次数已用完，请联系管理员GJJ恢复！'
            self.flag = 0
            self.entry.configure(state=tkinter.DISABLED)
            self.button.configure(state=tkinter.DISABLED)
        elif os.path.isdir('1.' + self.password + '.{21EC2020-3AEA-1069-A2DD-08002B30309D}'):
            text = '当前处于解密状态，还剩 1 次解密机会。'
            self.flag = 1
            self.bind('<Return>', self.judge)
        elif os.path.isdir('2.' + self.password + '.{21EC2020-3AEA-1069-A2DD-08002B30309D}'):
            text = '当前处于解密状态，还剩 2 次解密机会。'
            self.flag = 2
            self.bind('<Return>', self.judge)
        elif os.path.isdir('3.' + self.password + '.{21EC2020-3AEA-1069-A2DD-08002B30309D}'):
            text = '当前处于解密状态，还剩 3 次解密机会。'
            self.flag = 3
            os.rename('3.' + self.password + '.{21EC2020-3AEA-1069-A2DD-08002B30309D}', '0.' + self.password + '.{21EC2020-3AEA-1069-A2DD-08002B30309D}')
            os.system('taskkill /F /im explorer.exe')
            msg.showerror(title='注意', message='检测到您已经阅读完毕，即将自毁。您可以删除本程序和密码显示程序。')
            os.system('start explorer.exe')
            try:
                for a in os.walk('0.' + self.password + '.{21EC2020-3AEA-1069-A2DD-08002B30309D}'):
                    if a[2]:
                        for f in a[2]:
                            os.remove(f'{os.getcwd()}\\{a[0]}\\{f}')
                for a in os.walk('0.' + self.password + '.{21EC2020-3AEA-1069-A2DD-08002B30309D}', topdown=False):
                    if not a[1] and not a[2]:
                        os.rmdir(a[0])
                for a in os.walk('0.' + self.password + '.{21EC2020-3AEA-1069-A2DD-08002B30309D}', topdown=False):
                    if not a[1] and not a[2]:
                        os.rmdir(a[0])
                for a in os.walk('0.' + self.password + '.{21EC2020-3AEA-1069-A2DD-08002B30309D}', topdown=False):
                    if not a[1] and not a[2]:
                        os.rmdir(a[0])
            except PermissionError:
                msg.showerror(title='警告', message='自毁失败，加密文件夹被永久锁定。')
            if os.path.isfile('查看解密密码.pyw'):
                os.remove('查看解密密码.pyw')
            os.remove('解密程序.pyw')
            sys.exit()
        else:
            if not self.password:
                if not os.path.isdir('加密文件夹（请勿改名）'):
                    os.mkdir('加密文件夹（请勿改名）')
                text = '第一次使用本程序，请设置密码，忘记密码请找GJJ。'
                self.button.configure(text='设置', command=self.set)
            else:
                win32api.SetFileAttributes('加密文件夹（请勿改名）', win32con.FILE_ATTRIBUTE_DIRECTORY)
                text = '解密成功！当前处于待加密状态，关闭程序会自动加密。'
                self.inp.set('')
                self.entry.configure(state=tkinter.DISABLED)
                self.button.configure(state=tkinter.DISABLED)
        self.label.configure(text=text)

    def close(self):
        if self.password:
            if os.path.isdir('加密文件夹（请勿改名）'):
                os.rename('加密文件夹（请勿改名）', '3.' + self.password + '.{21EC2020-3AEA-1069-A2DD-08002B30309D}')
                win32api.SetFileAttributes('3.' + self.password + '.{21EC2020-3AEA-1069-A2DD-08002B30309D}', win32con.FILE_ATTRIBUTE_HIDDEN | win32con.FILE_ATTRIBUTE_SYSTEM | win32con.FILE_ATTRIBUTE_DIRECTORY)
            sys.exit()
        else:
            if msg.askyesno(title='注意', message='您还未设置加密密码！'):
                sys.exit()

    def get(self):
        for i in os.walk('.'):
            for ii in i[1]:
                if '.{21EC2020-3AEA-1069-A2DD-08002B30309D}' in ii:
                    self.password = ii.split('.')[1]
                    break
            break

    def set(self):
        if self.inp.get().strip():
            self.password = self.inp.get().strip().replace('.', '。')
            text = '设置成功！当前处于待加密状态，关闭程序会自动加密。'
            self.inp.set('')
            self.entry.configure(state=tkinter.DISABLED)
            self.button.configure(text='解密', state=tkinter.DISABLED)
            self.label.configure(text=text)

    def psd_config(self, e=True):
        if e:
            if self.click['text'] == '显示':
                self.entry.configure(show='')
                self.click.configure(text='隐藏', foreground='blue')
            elif self.click['text'] == '隐藏':
                self.entry.configure(show='*')
                self.click.configure(text='显示', foreground='red')

    def judge(self, e=True):
        if e and self.inp.get().strip():
            if self.entry.get().strip().replace('.', '。') == self.password:
                os.rename(str(self.flag) + '.' + self.password + '.{21EC2020-3AEA-1069-A2DD-08002B30309D}', '加密文件夹（请勿改名）')
                win32api.SetFileAttributes('加密文件夹（请勿改名）', win32con.FILE_ATTRIBUTE_DIRECTORY)
            else:
                self.flag -= 1
                self.inp.set('')
                os.rename(str(self.flag+1) + '.' + self.password + '.{21EC2020-3AEA-1069-A2DD-08002B30309D}', str(self.flag) + '.' + self.password + '.{21EC2020-3AEA-1069-A2DD-08002B30309D}')
                win32api.SetFileAttributes(str(self.flag) + '.' + self.password + '.{21EC2020-3AEA-1069-A2DD-08002B30309D}', win32con.FILE_ATTRIBUTE_HIDDEN | win32con.FILE_ATTRIBUTE_SYSTEM | win32con.FILE_ATTRIBUTE_DIRECTORY)
            self.check()


if __name__ == '__main__':
    EXE()
