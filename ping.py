# _*_ coding:utf-8 _*_
# FileName: ping.py
# IDE: PyCharm

import os
import re
import sys
import time
import tkinter
import getpass
import datetime
import threading
from tkinter import filedialog
import tkinter.messagebox
from subprocess import run


class Ping(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title(' Ping通测试器')
        self.wm_attributes('-topmost', 1)
        self.file_path = ''
        self.thread = ''
        self.pings = []
        self.paths = {}
        self.logs = {}
        self.pp = {}
        self.flag = False
        self.false = False
        self.choose = 0
        self.time = 30
        self.dir = 'C:/Users/' + getpass.getuser() + '/Desktop'
        self.setting = f'# ping时间间隔（单位为秒）\nping_seq=30\n# 日志报告文件存放路径：（保持最后空一行！）\npath1={self.dir}/success.log\nlog1={self.dir}/failed.log\n'
        self.settings = []
        self.button = tkinter.Button(self, text='选择配置文件', font=('微软雅黑', 12), fg='#4F4F4F', bd=0.5, bg='orange', command=lambda: self.threads(self.choice))
        self.button.place(x=10, y=10, width=130, height=30)
        self.button = tkinter.Button(self, text='开始PING测试', font=('微软雅黑', 12), fg='#4F4F4F', bd=0.5, bg='orange', command=lambda: self.threads(self.go))
        self.button.place(x=160, y=10, width=130, height=30)
        self.scrollbar = tkinter.Scrollbar(self)
        self.scrollbar.place(x=272, y=50, width=18, height=230)
        self.text = tkinter.Text(self, font=('微软雅黑', 10), bd=0, fg='black', yscrollcommand=self.scrollbar.set, relief='flat')
        self.text.place(x=10, y=50, width=262, height=230)
        self.scrollbar.config(command=self.text.yview)
        self.text.insert('insert', '请选择配置文件！\n')
        self.text.config(state='disabled')
        if not os.path.isfile('settings.ini'):
            with open('settings.ini', 'w', encoding='utf-8') as f:
                f.write(self.setting)
                f.close()

    def choice(self):
        self.file_path = filedialog.askopenfilename(filetypes=[('ini配置文件', '*.ini')], initialdir=self.dir, initialfile='暂未选择配置文件', parent=self, title='请选择配置文件(*.ini)')
        if self.file_path:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                self.pings = f.read().split('\n')
            self.text.config(state='normal')
            self.text.delete('0.0', tkinter.END)
            self.text.insert('insert', 'IP配置文件一览：\n')
            for ip in self.pings:
                if re.findall(r'((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})(\.((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})){3}', ip):
                    self.text.insert('insert', f'{ip}\n')
                else:
                    self.false = True
                    pass
            if self.false:
                self.text.insert('insert', '注意：\n')
                self.false = False
            for ip in self.pings:
                if re.findall(r'((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})(\.((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})){3}', ip):
                    pass
                else:
                    self.text.insert('insert', f'\n{ip} 不是IPv4地址')
                    # self.pings.remove(ip)  # 删除非IPv4地址
            self.text.config(state='disabled')

    def less(self, path):
        with open(path, 'r', encoding='utf-8') as f:
            lines = len(f.readlines())
            f.close()
        if lines > 500:
            if os.path.exists(path + '.old'):
                with open(path + '.old', 'r', encoding='utf-8') as f:
                    connect = f.read()
                    f.close()
                with open(path + '.old', 'a', encoding='utf-8') as f:
                    f.write(f'\n{connect}')
                    f.close()
            else:
                os.rename(path, path + '.old')
            with open(path, 'w', encoding='utf-8') as f:
                f.write('')
                f.close()

    def ping(self):
        self.button = tkinter.Button(self, text='暂停PING测试', font=('微软雅黑', 12), fg='#4F4F4F', bd=0.5, bg='orange', command=lambda: self.threads(self.paste))
        self.button.place(x=160, y=10, width=130, height=30)
        self.text.config(state='normal')
        self.text.delete('0.0', tkinter.END)
        self.text.config(state='disabled')
        self.text.update()
        while self.flag:
            if float(self.text.index(tkinter.END)) > 100:
                self.text.config(state='normal')
                self.text.delete('0.0', tkinter.END)
                self.text.config(state='disabled')
            for ip in range(len(self.pings)):
                time.sleep(1)
                # a = os.system(f'ping -n 1 {self.pings[ip]}')
                a = run(f'ping -n 1 {self.pings[ip]}', shell=True).returncode
                offset = datetime.datetime.fromtimestamp(time.time()) - datetime.datetime.utcfromtimestamp(time.time())
                local_st = datetime.datetime.utcnow() + offset
                self.text.config(state='normal')
                self.text.insert('insert', f'\n时间：{local_st}\n')
                self.text.config(state='disabled')
                if not a:
                    self.text.config(state='normal')
                    self.text.insert('insert', f'ping {self.pings[ip]} 成功！')
                    self.text.config(state='disabled')
                    if self.choose == 1:
                        try:
                            dirc = self.paths[min(list(self.paths.keys()))]
                            self.less(dirc)
                            with open(dirc, 'a', encoding='utf-8') as f:
                                f.write(f'在 {local_st} ping {self.pings[ip]} 成功！\n')
                                f.close()
                        except:
                            tkinter.messagebox.showerror(title='注意！', message='您的配置文件有误，请检查！')
                            self.button = tkinter.Button(self, text='继续PING测试', font=('微软雅黑', 12), fg='#4F4F4F', bd=0.5, bg='orange', command=lambda: self.threads(self.go))
                            self.button.place(x=160, y=10, width=130, height=30)
                            sys.exit()
                    elif self.choose == 2:
                        try:
                            dirc = self.paths[self.pp[self.pings[ip]]]
                            self.less(dirc)
                            with open(dirc, 'a', encoding='utf-8') as f:
                                f.write(f'在 {local_st} ping {self.pings[ip]} 成功！\n')
                                f.close()
                        except:
                            tkinter.messagebox.showerror(title='注意！', message='您的配置文件有误，请检查！')
                            self.button = tkinter.Button(self, text='继续PING测试', font=('微软雅黑', 12), fg='#4F4F4F', bd=0.5, bg='orange', command=lambda: self.threads(self.go))
                            self.button.place(x=160, y=10, width=130, height=30)
                            sys.exit()
                else:
                    self.text.config(state='normal')
                    self.text.insert('insert', f'ping {self.pings[ip]} 失败！\n')
                    self.text.config(state='disabled')
                    if self.choose == 1:
                        try:
                            dirc = self.logs[min(list(self.paths.keys()))]
                            self.less(dirc)
                            with open(dirc, 'a', encoding='utf-8') as f:
                                f.write(f'在 {local_st} ping {self.pings[ip]} 失败！\n')
                                f.close()
                        except:
                            tkinter.messagebox.showerror(title='注意！', message='您的配置文件有误，请检查！')
                            self.button = tkinter.Button(self, text='继续PING测试', font=('微软雅黑', 12), fg='#4F4F4F', bd=0.5, bg='orange', command=lambda: self.threads(self.go))
                            self.button.place(x=160, y=10, width=130, height=30)
                            sys.exit()
                    elif self.choose == 2:
                        try:
                            dirc = self.logs[self.pp[self.pings[ip]]]
                            self.less(dirc)
                            with open(dirc, 'a', encoding='utf-8') as f:
                                f.write(f'在 {local_st} ping {self.pings[ip]} 失败！\n')
                                f.close()
                        except:
                            tkinter.messagebox.showerror(title='注意！', message='您的配置文件有误，请检查！')
                            self.button = tkinter.Button(self, text='继续PING测试', font=('微软雅黑', 12), fg='#4F4F4F', bd=0.5, bg='orange', command=lambda: self.threads(self.go))
                            self.button.place(x=160, y=10, width=130, height=30)
                            sys.exit()
                self.update()
            self.update()
            time.sleep(self.time)
        self.text.update()

    def go(self):
        if not os.path.isfile('settings.ini'):
            with open('settings.ini', 'w', encoding='utf-8') as f:
                f.write(self.setting)
                f.close()
        with open('settings.ini', 'r', encoding='utf-8') as f:
            temp = f.read()
            f.close()
            self.time = float(re.findall('([0-9]*[0-9])', re.findall('\n([^#]*)\n', temp)[0])[0])
            self.settings = re.findall('\n([^#]*)\n', temp)[1].split('\n')
        for s in self.settings:
            if re.findall('path([0-9]{1,})', s):
                self.paths[re.findall('path([0-9]{1,})', s)[0]] = s.replace(re.findall('path[0-9]{1,}=', s)[0], '')
            elif re.findall('log([0-9]{1,})', s):
                self.logs[re.findall('log([0-9]{1,})', s)[0]] = s.replace(re.findall('log[0-9]{1,}=', s)[0], '')
        if self.paths.keys() != self.logs.keys():
            self.text.config(state='normal')
            self.text.delete('0.0', tkinter.END)
            self.text.config(state='disabled')
            tkinter.messagebox.showerror(title='注意！', message='您的配置文件有误，请检查！')
            self.button = tkinter.Button(self, text='继续PING测试', font=('微软雅黑', 12), fg='#4F4F4F', bd=0.5, bg='orange', command=lambda: self.threads(self.go))
            self.button.place(x=160, y=10, width=130, height=30)
            sys.exit()
        elif len(self.paths) < len(self.pings):
            self.choose = 1
        elif len(self.paths) >= len(self.pings):
            self.choose = 2
            keys = list(self.paths.keys())
            keys.sort()
            for k in range(len(self.pings)):
                self.pp[self.pings[k]] = keys[k]
        for c in list(self.paths.values()):
            if not os.path.isfile(c):
                with open(c, 'w', encoding='utf-8') as f:
                    f.write('')
        for c in list(self.logs.values()):
            if not os.path.isfile(c):
                with open(c, 'w', encoding='utf-8') as f:
                    f.write('')
        if self.pings:
            self.flag = True
            self.ping()
        else:
            self.text.config(state='normal')
            self.text.delete('0.0', tkinter.END)
            self.text.insert('insert', '还未选择配置文件！\n')
            self.text.config(state='disabled')
        self.text.update()

    def paste(self):
        self.button = tkinter.Button(self, text='继续PING测试', font=('微软雅黑', 12), fg='#4F4F4F', bd=0.5, bg='orange', command=lambda: self.threads(self.go))
        self.button.place(x=160, y=10, width=130, height=30)
        self.flag = False
        self.text.update()

    # 打包进线程（耗时的操作）
    @staticmethod
    def threads(func, *args):
        t = threading.Thread(target=func, args=args)
        t.setDaemon(True)  # 守护--就算主界面关闭，线程也会留守后台运行（不对！）
        t.start()  # 启动
        # t.join()  # 阻塞--会卡死界面！

    def main(self):
        self.geometry('300x300')
        self.resizable(False, False)
        self.mainloop()


if __name__ == '__main__':
    Ping().main()
