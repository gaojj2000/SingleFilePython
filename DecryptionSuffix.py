# _*_ coding:utf-8 _*_
# FileName: DecryptionSuffix.py
# IDE: PyCharm

import os
import tkinter
import tkinter.messagebox as msg


def jm():
    if text.get():
        string = text.get()
    else:
        string = '@&'
    for p in os.walk('.'):
        if p[2]:
            for f in p[2]:
                if '.' in f or string not in f:
                    continue
                h = f'{p[0]}\\{f.split(string)[0]}'
                e = f.split(string)[1:]
                os.rename(f'{p[0]}\\{f}', f'{h}.{"".join(e)}')
    msg.showinfo(title='结果', message='解密完毕！')


root = tkinter.Tk(className=' 批量后缀解密')
text = tkinter.StringVar()
tkinter.Label(root, text='解密密文：（请将本程序移动至解密根目录）').pack()
tkinter.Entry(root, textvariable=text).pack()
tkinter.Button(root, text='解密', command=jm).pack()
root.mainloop()
