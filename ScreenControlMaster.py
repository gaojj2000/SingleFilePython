# _*_ coding:utf-8 _*_
# FileName: ScreenControlMaster.py
# IDE: PyCharm

# 控制端

from time import sleep
from zlib import decompress
from threading import Thread
from tkinter import Tk, BOTH, YES, Label, Button, Entry, IntVar
from tkinter.messagebox import showerror
from _tkinter import TclError
from socket import socket, AF_INET, SOCK_DGRAM, SOCK_STREAM
from PIL.Image import frombytes
from PIL.ImageTk import PhotoImage
from win32api import GetAsyncKeyState
from pynput.keyboard import Listener
from queue import Queue

# 连接方IP
ip = ''
queue = Queue(64)
# 按下的功能键
ctrl_key = None
# 鼠标状态
mouse = 0  # 0为释放，1为左键，2为中键，3为右键，4为滚轮上，5为滚轮下
control_key = [r'\x0' + str(x) for x in range(1, 9)] + [r'\t', r'\n', r'\x0b', r'\x0c', r'\r', r'\x0e', r'\x0f'] + [r'\x' + str(int(x)) for x in range(10, 20)] + [r'\x1a']

root = Tk()
root.title('屏幕广播接收端')
root.geometry('800x600+0+0')
root.resizable(1, 1)
root.attributes('-topmost', 0)
lbImage = Label(root)
lbImage.pack(fill=BOTH, expand=YES)

BUFFER_SIZE = 60 * 1024
data = []


def get_host_ip():
    s = socket(AF_INET, SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip


def close():
    top.deiconify()
    top.overrideredirect(1)
    top.geometry('0x0')
    root.wm_attributes("-topmost", 1)
    Thread(target=key, daemon=True).start()


def cover():
    top.geometry('200x160+0+0')
    top.deiconify()
    root.wm_attributes("-topmost", 0)


def full_screen():
    root.attributes('-fullscreen', 1)
    button2['text'] = '取消全屏'
    button2['command'] = normal_screen
    button2.place(x=50, y=30, width=100, height=20)


def normal_screen():
    root.attributes('-fullscreen', 0)
    button2['text'] = '全屏'
    button2['command'] = full_screen
    button2.place(x=75, y=30, width=50, height=20)


def judge():
    try:
        if 5001 <= port.get() <= 65535:
            return True
        else:
            showerror(title='范围错误', message='端口号必须在5001-65535之间！')
    except TclError:
        showerror(title='格式错误', message='端口号必须为整数数字！')
    return False


def set_port():
    global PORT, receiving, thread_sender
    r = judge()
    if r:
        PORT = port.get()
        # button3['state'] = 'disabled'
        receiving = False
        sleep(0.3)
        receiving = True
        thread_sender = Thread(target=recv_image, daemon=True)
        thread_sender.start()


def q():
    top.destroy()
    top.quit()
    root.destroy()
    root.quit()


def top_window():
    # 置顶功能区
    global top, port, button2, button3
    top = Tk()
    top.title('工具箱（F7）')
    top.wm_attributes("-topmost", 1)
    top.overrideredirect(1)
    top.geometry('200x160+0+0')
    root.wm_attributes("-topmost", 0)
    port = IntVar(top, value=22222)
    button1 = Button(top, text='关闭功能区（F7召唤回来）', command=close)
    button1.place(x=25, y=5, width=150, height=20)
    button2 = Button(top, text='全屏', command=full_screen)
    button2.place(x=75, y=30, width=50, height=20)
    label = Label(top, text='请输入端口号：')
    label.place(x=25, y=55, width=150, height=20)
    entry = Entry(top, textvariable=port)
    entry.place(x=75, y=80, width=50, height=20)
    button3 = Button(top, text='修改端口', command=set_port)
    button3.place(x=50, y=105, width=100, height=20)
    button4 = Button(top, text='退出', command=q)
    button4.place(x=75, y=130, width=50, height=20)
    top.mainloop()


def key():
    while 1:
        if GetAsyncKeyState(118):
            cover()
            break
        sleep(1)


def show_image(image_bytes, image_size):
    screen_width = root.winfo_width()
    screen_height = root.winfo_height()
    global im
    try:
        im = frombytes('RGB', image_size, image_bytes)
    except Exception as e:
        print(e)
        return
    im = im.resize((screen_width, screen_height))
    im = PhotoImage(im)
    lbImage['image'] = im
    lbImage.image = im


def recv_image():
    global receiving, im, ip
    sock = socket(AF_INET, SOCK_DGRAM)
    try:
        sock.bind(('', PORT))
    except OSError:
        return

    while receiving:
        while receiving:
            chunk, _ = sock.recvfrom(BUFFER_SIZE)
            ip = _[0]
            if chunk == b'start':
                break
            elif chunk == b'close':
                sleep(0.1)
        else:
            break
        while receiving:
            chunk, _ = sock.recvfrom(BUFFER_SIZE)
            if chunk.startswith(b'_over'):
                image_data = ''
                image_size = eval(chunk[5:])
                try:
                    image_data = decompress(b''.join(data))
                except Exception as e:
                    print(e)
                    pass
                global thread_show
                if image_data:
                    thread_show = Thread(target=show_image, args=(image_data, image_size), daemon=True)
                    thread_show.start()
                data.clear()
                break
            elif chunk == b'close':
                sleep(0.1)
            data.append(chunk)


receiving = True
PORT = 22222
thread_sender = Thread(target=recv_image, daemon=True)
thread_sender.start()
Thread(target=top_window, daemon=True).start()


def close_window():
    global receiving
    receiving = False
    sleep(0.3)
    root.destroy()


def check(k):
    global ctrl_key
    k = str(k)
    # 获取最终按键字符串
    if 'Key.' in k:
        k = k[4:]
    elif "'" in k:
        if not k.count("'") % 2:
            k = k.replace("'", '')
    elif '<' in k and '>' in k:
        k = k.replace('<', '').replace('>', '')
    # 小数字键盘按键代号转换
    if k.isdigit() and int(k) in list(range(96, 106)):
        k = str(int(k) - 96)
    # 过滤掉^[a-z]，防止下面分离混乱
    if k in ['^' + chr(x) for x in range(97, 123)]:
        k = ' '.join(list(k))
    # 功能键字母转换
    if k in control_key:
        k = '^' + chr(control_key.index(k) + 97)
    if k in ['shift', 'ctrl_l', 'alt_l', 'shift_r', 'ctrl_r', 'alt_r']:
        k = k.split('_')[0]
    if k == 'cmd':
        k = 'meta'
    if ctrl_key and k[0] == '^':
        k = k[1:]
    return k


def check_down(k):
    global ctrl_key
    k = check(k)
    if k in ['shift', 'ctrl', 'alt', 'meta']:
        ctrl_key = k
    if k is not None:
        if ctrl_key and k not in ['shift', 'ctrl', 'alt', 'meta']:
            queue.put((ctrl_key+'+', k))
        else:
            queue.put((k, ))


def check_up(k):
    global ctrl_key
    k = check(k)
    if k in ['shift', 'ctrl', 'alt', 'meta']:
        ctrl_key = None


def send():
    global ctrl_key
    s = socket(family=AF_INET, type=SOCK_STREAM)
    while 1:
        if ip:
            s.connect((ip, PORT+1))
            while 1:
                while queue.qsize():
                    a = queue.get()
                    try:
                        s.send(str(a).encode())
                    except ConnectionResetError:
                        exit(-1)
                sleep(1)
        sleep(1)


def click(e):
    x, y = e.x / root.winfo_width(), e.y / root.winfo_height()
    queue.put((x, y, mouse))


def click1(e):
    global mouse
    mouse = 1
    x, y = e.x / root.winfo_width(), e.y / root.winfo_height()
    queue.put((x, y, mouse))


def click2(e):
    global mouse
    mouse = 2
    x, y = e.x / root.winfo_width(), e.y / root.winfo_height()
    queue.put((x, y, mouse))


def click3(e):
    global mouse
    mouse = 3
    x, y = e.x / root.winfo_width(), e.y / root.winfo_height()
    queue.put((x, y, mouse))


def click4(e):
    global mouse
    mouse = 4
    x, y = e.x / root.winfo_width(), e.y / root.winfo_height()
    queue.put((x, y, mouse))


def click5(e):
    global mouse
    mouse = 5
    x, y = e.x / root.winfo_width(), e.y / root.winfo_height()
    queue.put((x, y, mouse))


def release(e):
    global mouse
    mouse = 0
    x, y = e.x / root.winfo_width(), e.y / root.winfo_height()
    queue.put((x, y, mouse))


Listener(on_press=check_down).start()
Listener(on_release=check_up).start()
Thread(target=send, daemon=True).start()

# root.bind('<Motion>', click)  # 避免频繁发送数据
root.bind('<Button-1>', click1)  # 鼠标左键
root.bind('<Button-2>', click2)  # 鼠标中键
root.bind('<Button-3>', click3)  # 鼠标右键
# root.bind('<Button-4>', click4)  # Linux生效
# root.bind('<Button-5>', click5)  # Linux生效
root.bind('<ButtonRelease>', release)  # 释放鼠标
root.protocol('VM_DELETE_WINDOW', close_window)
root.mainloop()
