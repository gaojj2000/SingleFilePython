# _*_ coding:utf-8 _*_
# FileName: Mouse_Log_And_Repeat.py
# IDE: PyCharm

import re
import time
import tkinter
import win32api
from autopy import mouse
from threading import Thread


def get_location(e):
    global times, start, split, go
    if e:
        listbox.insert(tkinter.END, str(mouse.location()))
        listbox.see(tkinter.END)
        if start:
            split = round(round(time.time(), 3) - start, 3)
            times.append(split)
        start = round(time.time(), 3)


def check_mouse():
    while move:
        if label:
            label.configure(text=f'当前移动位置：{mouse.location()}\n当前时间戳：{round(time.time(), 3)}\n上次点击间隔：{split}s')
        time.sleep(1)
    label.configure(text='已结束鼠标点击记录，\n正在进行鼠标循环点击\n按W停止循环')


def go_mouse():
    global start, move, go
    move = 0
    go = 1
    nums = 0
    button.configure(state=tkinter.DISABLED)
    if str(entry.get()).replace(' ', '').isdigit():
        nums = int(entry.get())
    if not nums:
        nums = 999999999
    Thread(target=stop_mouse, daemon=True).start()
    for _ in range(nums):
        if not go:
            break
        start = 0
        for i in listbox.get(0, tkinter.END):
            if not go:
                break
            mouse.move(*tuple(map(float, re.findall(r'\((.*?),.(.*?)\)', i)[0])))
            mouse.click()
            if start < len(times):
                time.sleep(times[start])
                start += 1
            else:
                time.sleep(1)
    root.destroy()
    root.quit()


def stop_mouse():
    global go
    while 1:
        if win32api.GetAsyncKeyState(87):
            go = 0
            break
        time.sleep(1)


go = 0
move = 1
start = 0
split = 0
times = []
root = tkinter.Tk()
root.title('鼠标点击记录&执行程序')

label = tkinter.Label(root, text=f'当前点击位置：{mouse.location()}')
label.place(x=10, y=10, height=60, width=180)
listbox = tkinter.Listbox(root)
listbox.place(x=200, y=10, height=180, width=180)
entry = tkinter.Entry(root)
entry.place(x=60, y=100, height=20, width=80)
button = tkinter.Button(root, text='开始执行', command=lambda: Thread(target=go_mouse, daemon=True).start())
button.place(x=60, y=150, height=20, width=80)

root.bind('<Lock-KeyPress-Q>', get_location)
Thread(target=check_mouse, daemon=True).start()
root.wm_attributes('-topmost', 1)
root.geometry('400x200')
root.resizable(0, 0)
root.mainloop()
