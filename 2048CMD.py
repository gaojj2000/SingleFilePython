# _*_ coding:utf-8 _*_
# FileName: 2048CMD.py
# IDE: PyCharm

import os
import random
from pynput.keyboard import Listener

# 一般2^11 = 2048
# 最大2^17 = 131072


class CMD2048(object):
    def __init__(self):
        self.numbers = [2**n for n in range(1, 18)]
        # self.nums = [[''] * 4] * 4
        self.nums = [
            ['', '', '', ''],
            ['', '', '', ''],
            ['', '', '', ''],
            ['', '', '', '']
        ]
        self.row = '+' + ('-' * 6 + '+') * 4
        self.rows = ['|'] * 4
        self.target = 2048  # 目标分数
        self.source = 0
        self.level = 0
        self.only = True
        self.init()
        self.init()
        self.show()

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
                input(f'游戏结束！您的等级：{self.level}，您的分数：{self.source}')
                self.only = False
                break

    def prepare(self):
        self.rows = ['|'] * 4
        for r in range(4):
            for c in range(4):
                self.rows[r] += '{: ^6}|'.format(self.nums[r][c])

    def show(self):
        self.prepare()
        os.system('cls')
        print(f'等级：{self.level}\t得分：{self.source}')
        for n in range(4):
            print(self.row)
            print(self.rows[n])
        print(self.row)
        print('{: ^22}'.format('上w或⬆  下s或⬇  左a或⬅  右d或➡'))
        print('{: ^22}'.format('退出q或esc  重来r或home'))
        self.check()

    def judge(self, key):
        key = str(key)
        if 'Key.' in key:
            key = key[4:]
        elif "'" in key:
            key = key.replace("'", '')
        elif '<' in key and '>' in key:
            key = key.replace('<', '').replace('>', '')
        # print(key)
        if key in ['up', 'w', '104']:
            # print('上')
            self.up()
            self.init()
        elif key in ['down', 's', '98']:
            # print('下')
            self.down()
            self.init()
        elif key in ['left', 'a', '100']:
            # print('左')
            self.left()
            self.init()
        elif key in ['right', 'd', '102']:
            # print('右')
            self.right()
            self.init()
        elif key in ['esc', 'q']:
            # print('退出')
            return False
        elif key in ['home', 'r']:
            # print('重来')
            self.restart()
        self.show()
        if self.target == 2**self.level and self.only:
            input('{: ^20}'.format('你赢了！（回车以继续游戏）'))
            self.only = False

    def check(self):
        for r in self.nums:
            for c in r:
                if isinstance(c, int) and c > 2**self.level:
                    self.level = self.numbers.index(c) + 1

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
        with Listener(on_press=self.judge) as listener:
            listener.join()

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
    CMD2048().main()
