# _*_ coding:utf-8 _*_
# FileName: FileSuffix.py
# IDE: PyCharm

import os
import windnd
import tkinter
import filetype


def dragged_files(files):
    for item in items:
        item.destroy()
    for file in [item.decode('gbk') for item in files]:
        if os.path.isfile(file):
            kind = filetype.guess(file)
            if kind is None:
                label = tkinter.Label(tk, text=f'{file}：未知！')
            else:
                label = tkinter.Label(tk, text=f'{file}：{kind.extension}')
            items.append(label)
            label.pack()


items = []
tk = tkinter.Tk(className=' 测试文件后缀名（拖放到窗口内！）')
windnd.hook_dropfiles(tk, func=dragged_files)
tk.attributes('-topmost', 1)
tk.mainloop()
