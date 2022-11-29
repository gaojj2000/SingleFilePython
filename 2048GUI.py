# _*_ coding:utf-8 _*_
# FileName: 2048GUI.py
# IDE: PyCharm

import random
from tkinter import Tk, Label, StringVar, messagebox

# 一般2^11 = 2048
# 最大2^17 = 131072


class GUI2048(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.numbers = [2**n for n in range(1, 18)]
        # self.nums = [[''] * 4] * 4
        self.nums = [
            ['', '', '', ''],
            ['', '', '', ''],
            ['', '', '', ''],
            ['', '', '', '']
        ]
        self.colors = {
            '': '#CCC0B3',
            2: "#EEE4DA",
            4: "#EDE0C8",
            8: "#F2B179",
            16: "#F59563",
            32: "#F67C5F",
            64: "#F65E3B",
            128: "#EDCF72",
            256: "#EDCF72",
            512: "#EDCF72",
            1024: "#EDCF72",
            2048: "#EDCF72",
            4096: "#EDCF72",
            8192: "#EDCF72",
            16384: "#EDCF72",
            32768: "#EDCF72",
            65536: "#EDCF72",
            131072: "#EDCF72"
        }
        self.row = '+' + ('-' * 6 + '+') * 4
        self.level = 0
        self.source = 0
        self.only = True
        self.labels = []
        self.target = 2048  # 目标分数
        self.title('2048')
        self.wm_attributes('-topmost', 1)
        self.configure(background='#c0b0a0')
        self.head = StringVar()
        self.check()
        self.head.set(f'等级：{self.level}\t\t得分：{self.source}')
        self.label = Label(self, textvariable=self.head, background='#ccc0b3')
        self.label.place(x=5, y=10, width=360, height=30)
        self.text = '上w或⬆  下s或⬇  左d或⬅  右d或➡  退出q或esc  重来r或home'
        self.label = Label(self,  text=self.text, background='#ccc0b3')
        self.label.place(x=5, y=410, width=360, height=30)
        for r in range(4):
            for c in range(4):
                text = str(self.nums[r][c])
                label = Label(self, font=('', 30), text=text, background=self.colors[self.nums[r][c]])
                label.place(x=10+c*90, y=50+r*90, width=80, height=80)
                self.labels.append(label)
        self.init()
        self.init()
        self.show()
        self.bind('<Key>', self.judge)

    def restart(self):
        # self.nums = [[''] * 4] * 4
        self.nums = [
            ['', '', '', ''],
            ['', '', '', ''],
            ['', '', '', ''],
            ['', '', '', '']
        ]
        self.only = True
        self.level = 0
        self.source = 0
        self.check()
        self.head.set(f'等级：{self.level}\t\t得分：{self.source}')
        self.init()
        self.init()
        self.show()

    def init(self):
        num = True
        flag = False
        while num:
            for r in self.nums:
                for c in r:
                    if c:
                        flag = True
                        num = False
                    else:
                        flag = False
                        num = True
                        break
                if not flag:
                    r = random.randint(0, 3)
                    c = random.randint(0, 3)
                    if not self.nums[r][c]:
                        num = False
                        self.nums[r][c] = random.choice([2] * 9 + [4])
                    break
            if flag:
                for f in range(4):
                    for s in range(3):
                        if self.nums[f][s] != self.nums[f][s+1] and self.nums[s][f] != self.nums[s+1][f]:
                            flag = True
                        else:
                            flag = False
                            break
                    if not flag:
                        break
            if self.only and flag:
                messagebox.showinfo(title='Game Over !', message=f'游戏结束！您的等级：{self.level}，您的分数：{self.source}')
                break

    def show(self):
        for r in range(4):
            for c in range(4):
                # self.text = str(self.nums[r][c])
                # self.label = Label(self, font=('', 30), text=self.text, background=self.colors[self.nums[r][c]])
                # self.label.place(x=10+c*90, y=50+r*90, width=80, height=80)
                text = str(self.nums[r][c])
                self.labels[r*4+c].configure(text=text, background=self.colors[self.nums[r][c]])
        self.check()

    def judge(self, key):
        key = key.keycode
        # print(key)
        if key in [38, 87, 104]:
            # print('上')
            self.up()
            self.init()
        elif key in [40, 83, 98]:
            # print('下')
            self.down()
            self.init()
        elif key in [37, 65, 100]:
            # print('左')
            self.left()
            self.init()
        elif key in [39, 68, 102]:
            # print('右')
            self.right()
            self.init()
        elif key in [27, 81]:
            # print('退出')
            self.destroy()
            return False
        elif key in [36, 82]:
            # print('重来')
            self.restart()
        self.show()
        if self.target == 2**self.level and self.only:
            messagebox.showinfo(title='恭喜！', message='您已完成了游戏目标！')
            self.only = False

    def check(self):
        for r in self.nums:
            for c in r:
                if isinstance(c, int) and c > 2**self.level:
                    self.level = self.numbers.index(c) + 1
        self.head.set(f'等级：{self.level}\t\t得分：{self.source}')

    def up(self):
        for r in range(4):
            a_list, sco = self.change_list([self.nums[0][r], self.nums[1][r], self.nums[2][r], self.nums[3][r]])
            self.nums[0][r] = a_list[0]
            self.nums[1][r] = a_list[1]
            self.nums[2][r] = a_list[2]
            self.nums[3][r] = a_list[3]
            self.source += sco

    def down(self):
        for r in range(4):
            a_list, sco = self.change_list([self.nums[3][r], self.nums[2][r], self.nums[1][r], self.nums[0][r]])
            self.nums[3][r] = a_list[0]
            self.nums[2][r] = a_list[1]
            self.nums[1][r] = a_list[2]
            self.nums[0][r] = a_list[3]
            self.source += sco

    def left(self):
        for r in range(4):
            a_list, sco = self.change_list(self.nums[r])
            self.nums[r] = a_list
            self.source += sco

    def right(self):
        for r in range(4):
            a_list, sco = self.change_list(self.nums[r][::-1])
            self.nums[r] = a_list[::-1]
            self.source += sco

    def main(self):
        self.geometry('370x450')
        self.resizable(False, False)
        self.mainloop()

    @staticmethod
    def change_list(a_list):
        score = 0
        for w in range(3):
            for l in range(3):
                if not a_list[l] and a_list[l+1]:
                    a_list[l] = a_list[l+1]
                    a_list[l+1] = ''
        for n in range(len(a_list)-1):
            if a_list[n] and a_list[n] == a_list[n+1]:
                a_list[n] *= 2
                score += a_list[n]
                a_list[n+1] = ''
        for w in range(3):
            for l in range(3):
                if not a_list[l] and a_list[l+1]:
                    a_list[l] = a_list[l+1]
                    a_list[l+1] = ''
        return a_list, score


if __name__ == '__main__':
    GUI2048().main()
