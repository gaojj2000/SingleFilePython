# _*_ coding:utf-8 _*_
# FileName: countdown.py
# IDE: PyCharm

from threading import Thread
from time import time, sleep, localtime
from tkinter import Tk, messagebox, Button, Label, StringVar, IntVar, Entry, Checkbutton


class Countdown(Tk):
    def __init__(self):
        super().__init__()
        self.title("计时&倒计时小工具")
        self.wm_attributes('-topmost', 1)
        self.geometry('400x300')
        self.resizable(False, False)
        self.new = ''
        self.hour = ''
        self.min = ''
        self.sec = ''
        self.time = None

        self.choice = IntVar()
        self.choice.set(1)

        self.text1 = StringVar()
        self.text2 = StringVar()
        self.text1.set('         小时     分钟     秒后提醒')
        self.text2.set('  在     小时     分钟     秒时提醒')

        self.text = StringVar()
        self.text.set('请在此键入需要定时提醒的消息内容...')

        self.bg = StringVar()
        self.bg.set('      :     :      ')

        self.h = IntVar()
        self.m = IntVar()
        self.s = IntVar()
        self.h.set(0)
        self.m.set(0)
        self.s.set(0)

        self.h_s = StringVar()
        self.m_s = StringVar()
        self.s_s = StringVar()
        self.h_s.set('00')
        self.m_s.set('00')
        self.s_s.set('00')

        self.start = StringVar()
        self.start.set('开始倒计时')
        self.create = StringVar()
        self.create.set('创建定时')
        self.begin = StringVar()
        self.begin.set('开始计时')
        self.end = StringVar()
        self.end.set('清空全部内容')

        self.statue = IntVar()
        self.statue.set(0)

        self.check = Checkbutton(self, text='窗口置顶', font=('黑体', 12), onvalue=1, offvalue=0, variable=self.choice, command=lambda: self.change_window())
        self.check.place(x=5, y=5, width=80, height=20)

        self.bg = Label(self, textvariable=self.bg, bg='#b4b5b2', relief='ridge', font=('黑体', 30))
        self.bg.place(x=20, y=130, width=360, height=100)

        self.msg = Entry(self, textvariable=self.text, font=('黑体', 10))
        self.msg.place(x=100, y=6, width=280, height=20)

        self.la1 = Label(self, textvariable=self.text1, font=('黑体', 12))
        self.la1.place(x=10, y=35, width=280, height=30)
        self.la2 = Label(self, textvariable=self.text2, font=('黑体', 12))
        self.la2.place(x=10, y=85, width=280, height=30)

        self.la3 = Label(self, textvariable=self.h_s, bg='#b4b5b2', font=('黑体', 50))
        self.la3.place(x=50, y=145, width=70, height=70)
        self.la4 = Label(self, textvariable=self.m_s, bg='#b4b5b2', font=('黑体', 50))
        self.la4.place(x=170, y=145, width=70, height=70)
        self.la5 = Label(self, textvariable=self.s_s, bg='#b4b5b2', font=('黑体', 50))
        self.la5.place(x=290, y=145, width=70, height=70)

        self.entry1 = Entry(self, textvariable=self.h, font=('黑体', 15))
        self.entry1.place(x=50, y=55, width=30, height=40)
        self.entry2 = Entry(self, textvariable=self.m, font=('黑体', 15))
        self.entry2.place(x=120, y=55, width=30, height=40)
        self.entry3 = Entry(self, textvariable=self.s, font=('黑体', 15))
        self.entry3.place(x=190, y=55, width=30, height=40)

        self.bot1 = Button(self, textvariable=self.start, font=('黑体', 12), command=lambda: self.f_start())
        self.bot1.place(x=300, y=35, width=90, height=30)
        self.bot2 = Button(self, textvariable=self.create, font=('黑体', 12), command=lambda: self.f_create())
        self.bot2.place(x=300, y=85, width=90, height=30)
        self.bot3 = Button(self, textvariable=self.begin, font=('黑体', 15), command=lambda: self.f_begin())
        self.bot3.place(x=50, y=245, width=130, height=40)
        self.bot4 = Button(self, textvariable=self.end, font=('黑体', 15), command=lambda: self.f_end())
        self.bot4.place(x=220, y=245, width=130, height=40)

    def change_window(self):
        if self.choice.get() == 0:
            self.wm_attributes('-topmost', 0)
        elif self.choice.get() == 1:
            self.wm_attributes('-topmost', 1)

    def js(self):
        while True:
            sleep(1)
            if self.statue.get():
                if self.s_s.get() == '59':
                    if self.m_s.get() == '59':
                        if self.h_s.get() == '99':
                            messagebox.showerror(title="Time Error", message="计时时间已达上限！")
                            self.begin.set('开始计时')
                            return
                        else:
                            self.s_s.set('00')
                            self.m_s.set('00')
                            self.la3.update()
                            self.h_s.set('%02d' % (int(self.h_s.get()) + 1))
                    else:
                        self.s_s.set('00')
                        self.la4.update()
                        self.m_s.set('%02d' % (int(self.m_s.get()) + 1))
                else:
                    self.s_s.set('%02d' % (int(self.s_s.get()) + 1))
                    self.la5.update()
            else:
                return

    def djs(self):
        while True:
            sleep(1)
            if self.statue.get():
                if self.s_s.get() == '00':
                    if self.m_s.get() == '00':
                        if self.h_s.get() == '00':
                            if self.text.get() == '请在此键入需要定时提醒的消息内容...':
                                messagebox.showinfo(title="时间到！", message='主人主人时间到啦~')
                            else:
                                messagebox.showinfo(title="时间到！", message=self.text.get())
                            self.start.set('开始倒计时')
                            self.h.set(0)
                            self.m.set(0)
                            self.s.set(0)
                            self.statue.set(0)
                            return
                        else:
                            self.s_s.set('59')
                            self.m_s.set('59')
                            self.h_s.set('%02d' % (int(self.h_s.get()) - 1))
                            self.la3.update()
                    else:
                        self.s_s.set('59')
                        self.m_s.set('%02d' % (int(self.m_s.get()) - 1))
                        self.la4.update()
                else:
                    self.s_s.set('%02d' % (int(self.s_s.get()) - 1))
                    self.la5.update()
            else:
                return

    def f_start(self):
        try:
            if 0 <= self.h.get() < 100 and 0 <= self.m.get() < 60 and 0 <= self.s.get() < 60 and not (self.h.get() == self.m.get() == self.s.get() == 0):
                if self.start.get() == '开始倒计时':
                    self.h_s.set("%02d" % self.h.get())
                    self.m_s.set("%02d" % self.m.get())
                    self.s_s.set("%02d" % self.s.get())
                    self.start.set('暂停倒计时')
                    self.statue.set(0)
                    sleep(0.1)
                    self.statue.set(1)
                    sleep(0.1)
                    self.threads(self.djs)
                elif self.start.get() == '继续倒计时':
                    self.start.set('暂停倒计时')
                    self.statue.set(0)
                    sleep(0.1)
                    self.statue.set(1)
                    sleep(0.1)
                    self.threads(self.djs)
                elif self.start.get() == '暂停倒计时':
                    self.start.set('继续倒计时')
                    self.statue.set(0)
            else:
                messagebox.showerror(title="Value Error", message='0<=hour<100；0<=minute<60；0<=second<60')
                return
        except:
            messagebox.showerror(title="Bug Error", message='请删除数字前多余的0或将空白处填为0再尝试开始倒计时！')

    def f_create(self):
        self.time = localtime(time())
        self.hour = self.time.tm_hour
        self.min = self.time.tm_min
        self.sec = self.time.tm_sec
        if self.sec > self.s.get():
            self.s_s.set("%02d" % (self.s.get() - self.sec + 60))
            self.min += 1
        else:
            self.s_s.set("%02d" % (self.s.get() - self.sec))
        if self.min > self.m.get():
            self.m_s.set("%02d" % (self.m.get() - self.min + 60))
            self.hour += 1
        else:
            self.m_s.set("%02d" % (self.m.get() - self.min))
        if self.hour > self.h.get():
            self.h_s.set("%02d" % (self.h.get() - self.hour + 24))
        else:
            self.h_s.set("%02d" % (self.h.get() - self.hour))
        self.statue.set(0)
        sleep(0.1)
        self.statue.set(1)
        sleep(0.1)
        self.threads(self.djs)

    def f_begin(self):
        if self.begin.get() == '开始计时' or self.begin.get() == '继续计时':
            self.begin.set('暂停计时')
            self.statue.set(0)
            sleep(0.1)
            self.statue.set(1)
            sleep(0.1)
            self.threads(self.js)
        elif self.begin.get() == '暂停计时':
            self.begin.set('继续计时')
            self.statue.set(0)

    def f_end(self):
        self.begin.set('开始计时')
        self.statue.set(0)
        self.h.set(0)
        self.m.set(0)
        self.s.set(0)
        self.h_s.set('00')
        self.m_s.set('00')
        self.s_s.set('00')
        self.start.set('开始倒计时')
        self.begin.set('开始计时')
        self.text.set('请在此键入需要定时提醒的消息内容...')

    # 打包进线程（耗时的操作）
    @staticmethod
    def threads(func, *args):
        t = Thread(target=func, args=args)
        t.setDaemon(True)  # 守护--就算主界面关闭，线程也会留守后台运行（不对！）
        t.start()  # 启动
        # t.join()  # 阻塞--会卡死界面！


if __name__ == '__main__':
    Countdown().mainloop()
