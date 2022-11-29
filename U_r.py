# _*_ coding:utf-8 _*_
# FileName: U_r.py
# IDE: PyCharm

# U盘加密程序！

import os
import sys
import tkinter
import win32api
import win32con

Attributes = """
FILE_ATTRIBUTE_READONLY = 1 (0x1)  # 属性-隐藏
FILE_ATTRIBUTE_HIDDEN = 2 (0x2)  # 属性-隐藏
FILE_ATTRIBUTE_SYSTEM = 4 (0x4)  # 属性-系统文件
FILE_ATTRIBUTE_DIRECTORY = 16 (0x10)
FILE_ATTRIBUTE_ARCHIVE = 32 (0x20)
FILE_ATTRIBUTE_NORMAL = 128 (0x80)  # 属性-正常
FILE_ATTRIBUTE_TEMPORARY = 256 (0x100)
FILE_ATTRIBUTE_SPARSE_FILE = 512 (0x200)
FILE_ATTRIBUTE_REPARSE_POINT = 1024 (0x400)
FILE_ATTRIBUTE_COMPRESSED = 2048 (0x800)
FILE_ATTRIBUTE_OFFLINE = 4096 (0x1000)
FILE_ATTRIBUTE_NOT_CONTENT_INDEXED = 8192 (0x2000)
FILE_ATTRIBUTE_ENCRYPTED = 16384 (0x4000)
"""

"""
我的电脑 {20D04FE0-3AEA-1069-A2D8-08002B30309D}
我的文档 {450D8FBA-AD25-11D0-98A8-0800361B1103}
拨号网络 {992CFFA0-F557-101A-88EC-00DD010CCC48}
控制面板 {21EC2020-3AEA-1069-A2DD-08002B30309D}
计划任务 {D6277990-4C6A-11CF-8D87-00AA0060F5BF}
打印机 {2227A280-3AEA-1069-A2DE-08002B30309D}
记事本 {1FBA04EE-3024-11D2-8F1F-0000F87ABD16}
网络邻居 {208D2C60-3AEA-1069-A2D7-08002B30309D}
回收站 {645FF040-5081-101B-9F08-00AA002F954E}
公文包 {85BBD920-42A0-1069-A2E4-08002B30309D}
字体 {BD84B380-8CA2-1069-AB1D-08000948F534}
Web 文件夹 {BDEADF00-C265-11d0-BCED-00A0C90AB50F
“上帝模式”{ED7BA470-8E54-465E-825C-99712043E01C}
"""


class EXE(tkinter.Tk):
    def __init__(self):
        super().__init__(className=' U盘解密程序')
        self.flag = 0
        self.inp = tkinter.StringVar()
        self.label = tkinter.Label(self, font=('', 12))
        self.label.place(x=0, y=10, width=400, height=20)
        self.entry = tkinter.Entry(self, show='*', textvariable=self.inp)
        self.entry.place(x=150, y=35, width=100, height=25)
        self.button = tkinter.Button(self, text='解密', command=self.judge)
        self.button.place(x=160, y=65, width=80, height=30)
        self.check()
        self.attributes('-topmost', 1)
        self.geometry(f'400x100')
        self.bind('<Return>', self.judge)
        self.protocol("WM_DELETE_WINDOW", self.close)
        self.mainloop()

    def check(self):
        if os.path.isdir('3.{21EC2020-3AEA-1069-A2DD-08002B30309D}'):
            text = '当前处于解密状态，还剩 3 次解密机会。'
            self.flag = 3
        elif os.path.isdir('2.{21EC2020-3AEA-1069-A2DD-08002B30309D}'):
            text = '当前处于解密状态，还剩 2 次解密机会。'
            self.flag = 2
        elif os.path.isdir('1.{21EC2020-3AEA-1069-A2DD-08002B30309D}'):
            text = '当前处于解密状态，还剩 1 次解密机会。'
            self.flag = 1
        elif os.path.isdir('0.{21EC2020-3AEA-1069-A2DD-08002B30309D}'):
            text = '当前解密次数已用完，请联系管理员恢复！'
            self.flag = 0
            self.entry.configure(state=tkinter.DISABLED)
            self.button.configure(state=tkinter.DISABLED)
        else:
            if not os.path.isdir('加密文件夹（请勿改名）'):
                os.mkdir('加密文件夹（请勿改名）')
            else:
                win32api.SetFileAttributes('加密文件夹（请勿改名）', win32con.FILE_ATTRIBUTE_DIRECTORY)
            text = '当前处于待加密状态，关闭程序时会自动加密。'
            self.entry.configure(state=tkinter.DISABLED)
            self.button.configure(state=tkinter.DISABLED)
        self.label.configure(text=text)

    @staticmethod
    def close():
        if os.path.isdir('加密文件夹（请勿改名）'):
            os.rename('加密文件夹（请勿改名）', '3.{21EC2020-3AEA-1069-A2DD-08002B30309D}')
            win32api.SetFileAttributes('3.{21EC2020-3AEA-1069-A2DD-08002B30309D}', win32con.FILE_ATTRIBUTE_HIDDEN | win32con.FILE_ATTRIBUTE_SYSTEM | win32con.FILE_ATTRIBUTE_DIRECTORY)
        sys.exit()

    def judge(self, e=True):
        if e and self.inp.get().strip():
            if self.entry.get().strip() == 'XXXXXX':
                os.rename(str(self.flag)+'.{21EC2020-3AEA-1069-A2DD-08002B30309D}', '加密文件夹（请勿改名）')
                win32api.SetFileAttributes('加密文件夹（请勿改名）', win32con.FILE_ATTRIBUTE_DIRECTORY)
            else:
                self.flag -= 1
                self.inp.set('')
                os.rename(str(self.flag+1)+'.{21EC2020-3AEA-1069-A2DD-08002B30309D}', str(self.flag)+'.{21EC2020-3AEA-1069-A2DD-08002B30309D}')
                win32api.SetFileAttributes(str(self.flag)+'.{21EC2020-3AEA-1069-A2DD-08002B30309D}', win32con.FILE_ATTRIBUTE_HIDDEN | win32con.FILE_ATTRIBUTE_SYSTEM | win32con.FILE_ATTRIBUTE_DIRECTORY)
            self.check()


if __name__ == '__main__':
    EXE()
