# _*_ coding:utf-8 _*_
# FileName: ScreenControlClient.py
# IDE: PyCharm

# 受制端

from subprocess import Popen, PIPE
from time import sleep
from os import startfile
from zlib import compress
from threading import Thread
from socket import socket, AF_INET, SOCK_DGRAM, SOL_SOCKET, SO_BROADCAST, SOCK_STREAM
from tkinter import Tk, BooleanVar, IntVar, Button, Label, Entry
from _tkinter import TclError
from tkinter.messagebox import showerror
from PIL.ImageGrab import grab
from autopy import mouse, key
from ast import literal_eval

buttons = {
    'alt': key.Code.ALT,
    'shift': key.Code.SHIFT,
    'ctrl': key.Code.CONTROL,
    'meta': key.Code.META,
    'backspace': key.Code.BACKSPACE,
    'delete': key.Code.DELETE,
    'caps_lock': key.Code.ALT,
    'esc': key.Code.ESCAPE,
    'space': key.Code.SPACE,
    'enter': key.Code.RETURN,
    'tab': key.Code.TAB,
    'home': key.Code.HOME,
    'end': key.Code.END,
    'page_down': key.Code.PAGE_DOWN,
    'page_up': key.Code.PAGE_UP,
    'up': key.Code.UP_ARROW,
    'down': key.Code.DOWN_ARROW,
    'right': key.Code.RIGHT_ARROW,
    'left': key.Code.LEFT_ARROW,
    'alt+': key.Modifier.ALT,
    'shift+': key.Modifier.SHIFT,
    'ctrl+': key.Modifier.CONTROL,
    'meta+': key.Modifier.META,
    0: None,
    1: mouse.Button.LEFT,
    2: mouse.Button.MIDDLE,
    3: mouse.Button.RIGHT
}

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


def receive(por):
    global sss
    sss = socket(family=AF_INET, type=SOCK_STREAM)
    sss.bind((get_host_ip(), por))
    sss.listen(1)
    i, _ = sss.accept()

    while sending.get():
        r = i.recv(60 * 1024).decode()
        try:
            try:
                rs = [literal_eval(r)]
            except ValueError:
                rs = [literal_eval('(' + b + ')') for b in r.lstrip('(').rstrip(')').split(')(')]
            for r in rs:
                if len(r) == 1:
                    if r[0] in buttons:
                        key.tap(buttons[r[0]])
                    else:
                        key.tap(r[0])
                elif len(r) == 2:
                    if r[1] in buttons:
                        key.tap(buttons[r[1]], [buttons[r[0]]])
                    else:
                        key.tap(r[1], [buttons[r[0]]])
                elif len(r) == 3:
                    mouse.move(r[0] * root.winfo_screenwidth(), r[1] * root.winfo_screenheight())
                    mouse.toggle(buttons[r[2]], True if r[2] else False)
                    # if r[2] == 4:
                    #     win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 0, 0, 1000)
                    # elif r[2] == 5:
                    #     win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 0, 0, -1000)
        except SyntaxError:
            exit(-1)


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
        Thread(target=receive, args=(r+1,), daemon=True).start()
        btnStart['state'] = 'disabled'
        btnStop['state'] = 'normal'


btnStart = Button(root, text='开始广播', command=btn_start_lick)
btnStart.place(x=30, y=30, width=125, height=20)


def btn_stop_click():
    global sss
    sending.set(False)
    btnStart['state'] = 'normal'
    btnStop['state'] = 'disabled'
    sss.close()


btnStop = Button(root, text='停止广播', command=btn_stop_click)
btnStop.place(x=165, y=30, width=125, height=20)
btnStart['state'] = 'normal'
btnStop['state'] = 'disabled'
ipAddress = Label(text=f'当前IP地址：{get_host_ip()}', font=('', 15))
ipAddress.place(x=20, y=60, width=280, height=20)
root.mainloop()
