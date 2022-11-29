# _*_ coding:utf-8 _*_
# FileName: EncryptionSuffix.py
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
                if '.' not in f:
                    continue
                h = f'{p[0]}\\{f.split(".")[0]}'.replace(string, string[::-1])
                e = f'{string}'.join(list(f.split('.')[1]))
                os.rename(f'{p[0]}\\{f}', f'{h}{string}{e}')
    msg.showinfo(title='结果', message='加密完毕！')


root = tkinter.Tk(className=' 批量后缀加密')
text = tkinter.StringVar()
tkinter.Label(root, text='加密密文：（请将本程序移动至加密根目录）').pack()
tkinter.Entry(root, textvariable=text).pack()
tkinter.Button(root, text='加密', command=jm).pack()
root.mainloop()
