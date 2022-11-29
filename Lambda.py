# _*_ coding:utf-8 _*_
# FileName: Lambda.py
# IDE: PyCharm

# 在lambda递归(循环)表达式中不能出现input，需要先让递归(循环)初始化再赋值input

# 数字累加算法
add = (lambda _: sum(map(int, list(_))))(input('请输入一个正整数：'))
print('数字累加计算结果是：{}'.format(add))

# BMI算法
BMI = (lambda _, __ : (__/_/_ < 18.5 and '偏瘦' or __/_/_ < 25 and '正常' or __/_/_ < 30 and '偏胖' or __/_/_ < 35 and '肥胖' or '重度肥胖', __/_/_))(float(input('身高(m)：')), float(input('体重(kg)：')))
print('体型为：{}，BMI指数为：{:.2f}'.format(*BMI))

# 等差等比之和算法
dcb = (lambda _, __ , ___: (float(round(sum([_ + __ * ____ for ____ in range(___)]), len(str(_).split('.')[1]))), float(round(sum([_ * __ ** ____ for ____ in range(___)]), len(str(_).split('.')[1])))))(float(input('第一个数字：')), float(input('加率/乘率：')), int(input('次数：')))
print('等差之和结果：{}，等比之和结果：{}'.format(*dcb))

# 仅算底数为 2 的最大整数指数函数算法 + 仅算底数为 2 的整数指数函数组成拆分算法（特例）
m2 = (lambda _: (len(_) - 1, int(''.join(map(str, _[::-1])), 2), int(''.join(map(str, _[::-1])), 2), f'\033[4;31m{" + ".join(map(str, [__ * 2 ** ___ for ___, __ in enumerate(_) if __]))}\033[0m'.replace(' + ', '\033[0m + \033[4;31m'), str([__ for __, ___ in enumerate(_) if ___]).replace('[', f'2^\033[4;31m').replace(', ', f'\033[0m + 2^\033[4;31m').replace(']', '\033[0m')))(list(map(int, list(bin(int(input('请输入幂为 2 的指数和：')))[:1:-1]))))
print('底数为 \033[31m{}\033[0m 的最大指数为 \033[31m{}\033[0m 将不超过 \033[31m{}\033[0m\n算式为：\033[31m{}\033[0m = {} = {}'.format(2, *m2))

# 最大整数指数函数算法 + 整数指数函数组成拆分算法
MAX = lambda _, __, ___ = 1: (_ ** ___ <= __) and MAX(_, __, ___ + 1) or (_, ___ - 1, __, ___ - 1)
loop = lambda _, __, ___, ____, _____ = 0, ______ = eval('[]'): __ + 1 and ((_____ + _ ** __ <= ___) and loop(_, __ - 1, ___, ____, _____ + _ ** __, ______ + [__]) or loop(_, __ - 1, ___, ____, _____, ______)) or (_, ____, ___, ___, f'\033[4;31m{" + ".join(map(str, [_ ** __ for __ in ______][::-1]))}\033[0m'.replace(' + ', '\033[0m + \033[4;31m'), str( ______[::-1]).replace('[', f'{_}^\033[4;31m').replace(', ', f'\033[0m + {_}^\033[4;31m').replace(']', '\033[0m'))
loop = loop(*MAX(int(input('请输入指数函数的底数（整数）：')), int(input('请输入指数和（整数）：'))))
print('底数为 \033[31m{}\033[0m 的最大指数为 \033[31m{}\033[0m 将不超过 \033[31m{}\033[0m\n算式为：\033[31m{}\033[0m = {} = {}'.format(*loop))

# 最大整数指数函数算法 + 整数指数函数组成拆分算法（略微优化版）
MAX = lambda _, __, ___ = 1: (_ ** ___ <= __) and MAX(_, __, ___ + 1) or (_, ___ - 1, __)
loop = lambda _, __, ___, ____ = 0, _____ = eval('[]'): __ + 1 and ((____ + _ ** __ <= ___) and loop(_, __ - 1, ___, ____ + _ ** __, _____ + [__]) or loop(_, __ - 1, ___, ____, _____)) or (_, _____[0], ___, ___, f'\033[4;31m{" + ".join(map(str, [_ ** __ for __ in _____][::-1]))}\033[0m'.replace(' + ', '\033[0m + \033[4;31m'), str( _____[::-1]).replace('[', f'{_}^\033[4;31m').replace(', ', f'\033[0m + {_}^\033[4;31m').replace(']', '\033[0m'))
loop = loop(*MAX(int(input('请输入指数函数的底数（整数）：')), int(input('请输入指数和（整数）：'))))
print('底数为 \033[31m{}\033[0m 的最大指数为 \033[31m{}\033[0m 将不超过 \033[31m{}\033[0m\n算式为：\033[31m{}\033[0m = {} = {}'.format(*loop))

# 瓶盖空瓶换啤酒算法（不借瓶盖空瓶，价值不守恒，非找规律）【(2, 2, 4)单位（元/瓶啤酒，空瓶/瓶啤酒，瓶盖/瓶啤酒）】
loop = lambda _, __, ___, ____, _____: (___ or _____ > 3 or ____ > 1) and loop(*((lambda _, __, ___, ____, _____: (_, __ + ___, ___, ____, _____) or (print(_, __, ___, ____, _____) or _, __, ___, ____, _____))(*(lambda _, __, ___, ____, _____: _____ > 3 and (_, __, ___ + int(_____ / _[2]), ____, _____ - _[2] * int(_____ / _[2])) or (_, __, ___, ____, _____))(*(lambda _, __, ___, ____, _____: ____ > 1 and (_, __, ___ + int(____ / _[1]), ____ - _[1] * int(____ / _[1]), _____) or (_, __, ___, ____, _____))(*(lambda _, __, ___, ____, _____: ___ and (_, __, 0, ____ + ___, _____ + ___) or (_, __, ___, ____, _____))(_, __, ___, ____, _____)))))) or (__, ____, _____)
result = loop(*((lambda _, __: (__, int(_ / __[0]), 0, int(_ / __[0]), int(_ / __[0])))(*(lambda _, __ = (2, 2, 4): (_, __))(int(input('请输入总价格：'))))))
print('累计啤酒数 \033[4;31m{}\033[0m ，当前所有的空瓶 \033[4;31m{}\033[0m ，当前所有的瓶盖 \033[4;31m{}\033[0m 。'.format(*result))

# 素数列表算法 + n个数的最大公约数和最小比例组和最小公倍数算法
# 一般素数列表算法（对较大范围计算，算的数据过于庞大）
# ss = (lambda _, __: [_ for _ in range(_, __ + 1) if not (lambda _: [__ for __ in range(2, _) if _ % __ == 0])(_)])(int(input('请输入最小数：')), int(input('请输入最大数：')))
# print('素数列表：{}'.format(ss))
# 理论素数列表算法（只判断到最大数的根号）
ss = lambda _, __: [_ for _ in range(_, __ + 1) if not (lambda _: [___ for ___ in range(2, int(_ ** 0.5) + 1) if _ % ___ == 0])(_)]
# ss = ss(int(input('请输入最小数：')), int(input('请输入最大数：')))
# print('素数列表：{}'.format(ss))
# 分解质因数
zs = lambda _, __, ___: (_ <= ___) and ((___ % _) and zs(_ + 1, __, ___) or zs(_, __ + [_], ___ / _)) or __
# zs = zs(2, [], int(input('请输入要分解质因数的数：')))
# zs = [_ for _ in zs if _ in ss]
# print('质因数分解列表：{}'.format(zs))
# 统计质因数个数
# print('统计质因数个数：{}'.format({_: zs.count(_) for _ in set(zs)}))
# 求最大公约数的质因数个数统计
from functools import reduce
nums = list(map(int, input('\n请输入数字，用单空格隔开：').strip().split(' ')))
decomposes = [{__: zs(2, [], _).count(__) for __ in set(zs(2, [], _))} for _ in nums]
# print('键集合：{}'.format(decomposes))
# 获取键集合
# print('键集合：{}'.format(list(set(reduce(lambda _, __: isinstance(_, dict) and (list(_.keys()) + list(__.keys())) or (_ + list(__.keys())), decomposes)))))
# print('键集合：{}'.format(list(set(reduce(lambda _, __: _ + list(__.keys()), [[]] + decomposes)))))
# 计算最低值
composes = {_: [] for _ in list(set(reduce(lambda _, __: _ + list(__.keys()), [[]] + decomposes)))}
for _ in decomposes:
    for __ in list(set(reduce(lambda _, __: _ + list(__.keys()), [[]] + decomposes))):
        composes[__].append(_.get(__, 0))
composes = {_: min(composes[_]) for _ in composes}
# 最大公约数
MIN = reduce(lambda _, __: (_ ** composes.get(_, 1)) * (__ ** composes.get(__, 1)), composes)
# 最小比例组
MIN_LIST = [int(_ / MIN) for _ in nums]
# 最小公倍数
MAX = reduce(lambda _, __: _ * __, MIN_LIST) * MIN
print('数字 \033[4;31m{}\033[0m 的最小比例组为 \033[4;31m{}\033[0m ，最大公约数为 \033[4;31m{}\033[0m ，最小公倍数为 \033[4;31m{}\033[0m '.format(nums, MIN_LIST, MIN, MAX))

# eval("__import__('os').remove(__file__)")
input('\n键入回车退出程序...\n')
