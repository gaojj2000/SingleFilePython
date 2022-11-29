# _*_ coding:utf-8 _*_
# FileName: auto_tips.py
# IDE: PyCharm

import os
import time
import tkinter
import pyperclip
import tkinter.messagebox as msgbox


class Tips(object):
    def __init__(self):
        self.root = tkinter.Tk(className=' Tips')
        self.root.wm_attributes('-topmost', 1)
        self.info = tkinter.StringVar()
        self.time = tkinter.IntVar()
        self.time.set(2)
        self.choice = tkinter.IntVar()
        self.choice.set(0)
        self.connect = []
        self.line = self.lines = 0
        self.show = tkinter.StringVar()
        self.show.set(f'当前是第 {self.line} 条内容')
        self.check = tkinter.Checkbutton(self.root, text='定时        秒自动复制粘贴文字', font=('黑体', 12), onvalue=1, offvalue=0, variable=self.choice, command=lambda: Tips.auto_copy(self))
        self.check.place(x=20, y=5, width=260, height=30)
        self.qq_info = tkinter.Entry(self.root, textvariable=self.time, highlightcolor="Fuchsia", highlightthickness=1, width=25)
        self.qq_info.place(x=80, y=5, width=50, height=30)
        self.qq_info = tkinter.Entry(self.root, textvariable=self.info, highlightcolor="Fuchsia", highlightthickness=1, width=25)
        self.qq_info.place(x=10, y=40, width=210, height=30)
        self.botten1 = tkinter.Button(self.root, text='重置', font=('微软雅黑', 12), fg='#4F4F4F', bd=0.5, bg='orange', command=lambda: Tips.clean(self))
        self.botten1.place(x=230, y=40, width=50, height=30)
        self.btn_addition = tkinter.Button(self.root, text='+', font=('微软雅黑', 12), fg='#4F4F4F', bd=0.5, bg='orange', command=lambda: Tips.addition(self))
        self.btn_addition.place(x=70, y=80, width=30, height=30)
        self.btn_minus = tkinter.Button(self.root, text='-', font=('微软雅黑', 12), fg='#4F4F4F', bd=0.5, bg='orange', command=lambda: Tips.minus(self))
        self.btn_minus.place(x=20, y=80, width=30, height=30)
        self.botten1 = tkinter.Button(self.root, text='上一条', font=('微软雅黑', 12), fg='#4F4F4F', bd=0.5, bg='orange', command=lambda: Tips.last(self))
        self.botten1.place(x=120, y=80, width=75, height=30)
        self.botten2 = tkinter.Button(self.root, text='下一条', font=('微软雅黑', 12), fg='#4F4F4F', bd=0.5, bg='orange', command=lambda: Tips.next(self))
        self.botten2.place(x=210, y=80, width=75, height=30)
        self.label = tkinter.Label(self.root, font=('微软雅黑', 12), bd='9', fg='#4F4F4F', anchor='w', textvariable=self.show)
        self.label.place(x=10, y=290, width=180, height=30)
        self.scrollbar = tkinter.Scrollbar(self.root)
        self.scrollbar.place(x=260, y=120, width=18, height=180)
        self.text = tkinter.Text(self.root, font=('微软雅黑', 10), bd=0, fg='black', yscrollcommand=self.scrollbar.set, relief='flat')
        self.text.place(x=10, y=120, width=250, height=170)
        self.scrollbar.config(command=self.text.yview)
        self.root.bind('<Key>', self.judge)

    def addition(self):
        self.text.delete('0.0', tkinter.END)
        self.text.insert(tkinter.END, self.info.get())
        pyperclip.copy(self.info.get())
        if self.info.get():
            self.connect.append(self.info.get())
            self.lines += 1
            self.line = self.lines
            self.info.set('')
        else:
            if os.path.isfile('tips.txt'):
                if msgbox.askyesno(title='询问', message='是否要导入现有的“tips.txt”文件？'):
                    with open('tips.txt', 'r', encoding='utf-8') as r:
                        self.connect = []
                        self.connect = r.read().split('\n')
                        self.connect.remove('')
                        self.lines = len(self.connect)
            else:
                msgbox.showerror(title='警告', message='请输入内容！')
        Tips.change(self)

    def minus(self):
        self.connect.remove(pyperclip.paste())
        self.lines -= 1
        self.text.delete('0.0', tkinter.END)
        Tips.last(self)
        Tips.change(self)

    def last(self):
        if self.lines > 0:
            if 2 <= self.line <= self.lines + 1:
                self.line -= 1
            else:
                self.line = self.lines
            self.text.delete('0.0', tkinter.END)
            self.text.insert(tkinter.END, self.connect[self.line - 1])
            pyperclip.copy(self.connect[self.line - 1])
        Tips.change(self)

    def next(self):
        if self.lines > 0:
            if 0 <= self.line <= self.lines - 1:
                self.line += 1
            else:
                self.line = 1
            self.text.delete('0.0', tkinter.END)
            self.text.insert(tkinter.END, self.connect[self.line - 1])
            pyperclip.copy(self.connect[self.line - 1])
        Tips.change(self)

    def clean(self):
        if self.connect:
            if msgbox.askyesno(title='警告', message='是否要保存当前内容到文件？（将覆盖当前文件【如果存在】）'):
                with open('tips.txt', 'w') as w:
                    w.write('')
                    w.close()
                with open('tips.txt', 'a') as w:
                    for i in self.connect:
                        w.write(i+'\n')
                    w.close()
                msgbox.showinfo(title='提示', message='文件已保存至同目录下的“tips.txt”文件内')
        try:
            self.info.set('')
            self.line = self.lines = 0
            self.connect = []
            self.text.delete('0.0', tkinter.END)
        except:
            pass
        Tips.change(self)

    def judge(self, event):
        if event.keycode in [27]:
            if self.choice.get() == 0:
                Tips.clean(self)
                quit()
            elif self.choice.get() == 1:
                self.choice.set(0)
        elif event.keycode in [37]:
            Tips.last(self)
        elif event.keycode in [38]:
            Tips.addition(self)
        elif event.keycode in [39]:
            Tips.next(self)
        elif event.keycode in [40]:
            Tips.minus(self)
        Tips.change(self)

    def change(self):
        self.show.set(f'当前是第 {self.line} 条内容')
        self.label = tkinter.Label(self.root, font=('微软雅黑', 12), bd='9', fg='#4F4F4F', anchor='w', textvariable=self.show)
        self.label.place(x=10, y=290, width=180, height=30)

    def auto_copy(self):
        if not self.connect:
            if self.time.get() > 0:
                time.sleep(self.time.get())
                temp = ''
                while self.choice.get() == 1:
                    time.sleep(self.time.get())
                    self.info.set(pyperclip.paste())
                    Tips.addition(self)
                    if pyperclip.paste() == temp:
                        Tips.minus(self)
                    temp = pyperclip.paste()
                    self.root.update()
        if self.time.get() > 0:
            time.sleep(self.time.get())
            while self.choice.get() == 1:
                time.sleep(self.time.get())
                Tips.next(self)
                self.root.update()
                if self.line == self.lines:
                    msgbox.showinfo(title='提示', message='已自动复制到结尾')
                    self.choice.set(0)
                    return

    def main(self):
        self.root.geometry('300x330')
        self.root.resizable(False, False)
        self.root.mainloop()
        try:
            self.root.protocol("WM_DELETE_WINDOW", Tips.clean(self))
        except:
            pass


if __name__ == '__main__':
    Tips().main()
