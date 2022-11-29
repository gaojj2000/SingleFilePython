# _*_ coding:utf-8 _*_
# FileName: ScreenShareServer.py
# IDE: PyCharm

from subprocess import Popen, PIPE
from time import sleep
from os import startfile
from zlib import compress
from threading import Thread
from socket import socket, AF_INET, SOCK_DGRAM, SOL_SOCKET, SO_BROADCAST
from tkinter import Tk, BooleanVar, IntVar, Button, Label, Entry
from _tkinter import TclError
from tkinter.messagebox import showerror
from PIL.ImageGrab import grab

root = Tk()
root.title('屏幕广播发送端')
root.geometry('320x90+500+200')
root.resizable(0, 0)
root.attributes('-topmost', 1)

BUFFER_SIZE = 60 * 1024
sending = BooleanVar(root, value=False)
port = IntVar(root, value=22222)


def get_host_ip():
    s = socket(AF_INET, SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip


def send_image(por):
    sock = socket(AF_INET, SOCK_DGRAM)
    sock.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
    IP = '<broadcast>'

    while sending.get():
        im = grab()
        w, h = im.size
        im_bytes = compress(im.tobytes())
        sock.sendto(b'start', (IP, por))
        for i in range(len(im_bytes)//BUFFER_SIZE+1):
            start = i * BUFFER_SIZE
            end = start + BUFFER_SIZE
            sock.sendto(im_bytes[start: end], (IP, por))
        sock.sendto(b'_over'+str((w, h)).encode(), (IP, por))
        sleep(0.1)

    sock.sendto(b'close', (IP, por))
    sock.close()


def judge():
    try:
        if 5001 <= port.get() <= 65535:
            po = Popen(f'netstat -na | findstr {get_host_ip()}:{port.get()}', shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE).stdout.readlines()
            if po:
                showerror(title='占用错误', message=f'端口号{port.get()}已被占用！')
            else:
                return port.get()
        else:
            showerror(title='范围错误', message='端口号必须在5001-65535之间！')
    except TclError:
        showerror(title='格式错误', message='端口号必须为整数数字！')
    return False


bd = Label(root, text='请点击相应按钮，端口号：', fg='red', cursor='plus')
bd.place(x=40, y=5, width=140, height=20)
p = Entry(root, textvariable=port)
p.place(x=190, y=5, width=90, height=20)
url = 'https://www.baidu.com'
bd.bind("<Button-1>", lambda e: startfile(url))


def btn_start_lick():
    r = judge()
    if r:
        sending.set(True)
        Thread(target=send_image, args=(r,), daemon=True).start()
        btnStart['state'] = 'disabled'
        btnStop['state'] = 'normal'


btnStart = Button(root, text='开始广播', command=btn_start_lick)
btnStart.place(x=30, y=30, width=125, height=20)


def btn_stop_click():
    sending.set(False)
    btnStart['state'] = 'normal'
    btnStop['state'] = 'disabled'


btnStop = Button(root, text='停止广播', command=btn_stop_click)
btnStop.place(x=165, y=30, width=125, height=20)
btnStart['state'] = 'normal'
btnStop['state'] = 'disabled'
ipAddress = Label(text=f'当前IP地址：{get_host_ip()}', font=('', 15))
ipAddress.place(x=20, y=60, width=280, height=20)
root.mainloop()
