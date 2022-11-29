# _*_ coding:utf-8 _*_
# FileName: Sort.py
# IDE: PyCharm

import sys
import random
# 设置最大递归深度，默认最大递归 1000 次，设置最大递归深度后有效递归深度跟python版本、cpu性能、操作系统等有关
sys.setrecursionlimit(10000)
array_list = [random.randint(-2000, 2000) for _ in range(5000)]
# array_list = [13, 27, 11, 18, 41, 25, 36, 29, -7, 111, 18, 33, -3]  # TODO：所有的 n 表示局部判断次数、 n_ 表示局部赋值次数，所有的 i 表示全局判断次数、 i_ 表示全局赋值次数。

# 1、冒泡排序（Bubble Sort）


def bubble(array):
    n = 0
    n_ = 0
    for _ in range(1, len(array)):  # TODO：第一层 for 表示循环的遍数
        for __ in range(0, len(array) - _):  # TODO：第二层 for 表示具体比较哪两个元素
            n += 1
            if array[__] > array[__ + 1]:  # TODO：如果前面的大于后面的
                n_ += 1
                array[__], array[__ + 1] = array[__ + 1], array[__]  # TODO：交换这两个元素的位置
    print(f'冒泡排序共判断 {n} 次，执行赋值 {n_} 次。')
    return array


print(bubble(list(array_list)))

# 2、选择排序（Selection Sort）


def selection(array):
    n = 0
    n_ = 0
    for _ in range(len(array) - 1):  # TODO：第一层 for 表示循环的遍数
        n_ += 1
        __ = _  # TODO：将起始元素设为最小元素
        for ___ in range(_ + 1, len(array)):  # TODO：第二层 for 表示最小元素和后面的元素逐个比较
            n += 1
            if array[__] > array[___]:  # TODO：如果当前元素比最小元素小
                n_ += 1
                __ = ___  # TODO：把当前元素角标标记为最小元素角标
        n_ += 1
        array[_], array[__] = array[__], array[_]  # TODO：查找一遍后将最小元素与起始元素互换
    print(f'选择排序共判断 {n} 次，执行赋值 {n_} 次。')
    return array


print(selection(list(array_list)))

# 3、插入排序（Insertion Sort）


def insertion(array):
    n = 0
    n_ = 0
    for _ in range(1, len(array)):  # TODO：第一层 for 表示循环的遍数
        n_ += 1
        __ = array[_]  # TODO：设置当前需要插入的元素
        n += 1
        while _ and array[_ - 1] > __:  # TODO：当比较元素大于当前元素（此时变量 _ 被用于标记与当前元素比较的比较元素）
            n += 1
            n_ += 2
            array[_] = array[_ - 1]  # TODO：把比较元素后移
            _ -= 1  # TODO：往前选择下一个比较元素
        n_ += 1
        array[_] = __  # TODO：当比较元素小于当前元素，则将当前元素插入在其后面
    print(f'插入排序共判断 {n} 次，执行赋值 {n_} 次。')
    return array


print(insertion(list(array_list)))

# 4、希尔排序（Shell Sort）


def shell(array, sep=2):
    n = 0
    n_ = 0
    n_ += 1
    _ = len(array) // sep  # TODO：取整计算增量（间隔）值
    n += 1
    while _:
        for __ in range(_, len(array)):  # TODO：从增量值开始遍历比较
            n_ += 1
            ___ = array[__]  # TODO：设置当前需要插入的元素
            n += 1
            while __ - _ >= 0 and array[__ - _] > ___:  # TODO：当比较元素大于当前元素（此时变量 __ 被用于标记与当前元素比较的比较元素）
                n += 1
                n_ += 2
                array[__] = array[__ - _]  # TODO：把比较元素后移
                __ -= _  # TODO：往前选择下一个比较元素
            n_ += 1
            array[__] = ___  # TODO：当比较元素小于当前元素，则将当前元素插入在其后面
        n_ += 1
        _ //= sep  # TODO：缩小增量（间隔）值
    print(f'希尔排序共判断 {n} 次，执行赋值 {n_} 次。')
    return array


print(shell(list(array_list)))

# 5、归并排序（Merge Sort）

i = 0
i_ = 0

# merge = lambda _: _ if len(_) == 1 else merge_sort(merge(_[:len(_) // 2]), merge(_[len(_) // 2:]))  # TODO：使用递归运算二分法后的数列
# merge = lambda _: len(_) == 1 and _ or merge_sort(merge(_[:len(_) // 2]), merge(_[len(_) // 2:]))  # TODO：使用递归运算二分法后的数列


def merge(array):
    global i, i_
    i += 1
    if len(array) < 2:
        return array
    i_ += 2
    return merge_sort(merge(array[:len(array) // 2]), merge(array[len(array) // 2:]))  # TODO：使用递归运算二分法后的数列


def merge_sort(left, right):
    global i, i_
    i_ += 1
    _ = []  # TODO：排序合并两个数列
    i += 1
    while left and right:  # TODO：两个数列都有值
        i += 2
        i_ += 1
        # _.append((lambda _, __: _[0] <= __[0] and _.pop(0) or __.pop(0))(left, right))  # TODO：左右两个数列第一个最小放前面【 _.append((lambda _, __: _.pop(0) if _[0] <= __[0] else __.pop(0))(left, right)) 】
        if left[0] <= right[0]:  # TODO：左右两个数列第一个最小放前面
            _.append(left.pop(0))
        else:
            _.append(right.pop(0))
    i_ += 1
    _.extend(left and left or right)  # TODO：只要数列中还有值，直接添加【 _ += left if left else right 】
    return _


_ = merge(list(array_list))
print(f'归并排序共判断 {i} 次，执行赋值 {i_} 次。\n{_}')

# 6、快速排序（Quick Sort）

i = 0
i_ = 0


def quick(array):
    global i, i_
    i += 1
    if len(array) < 2:  # TODO：基线条件：为空或只包含一个元素的数组是“有序”的
        return array
    i += 2 * len(array[1:])
    i_ += 2 * len(array[1:])
    return quick([_ for _ in array[1:] if _ <= array[0]]) + [array[0]] + quick([_ for _ in array[1:] if _ > array[0]])  # TODO：由所有小于等于、基准元素、大于基准值的元素（递归条件）组成的子数组重新组合


_ = quick(list(array_list))
print(f'快速排序共判断 {i} 次，执行赋值 {i_} 次。\n{_}')

# 7、堆排序（Heap Sort）

i = 0
i_ = 0


def heap(array):
    global i, i_
    for _ in range(len(array) // 2, -1, -1):
        array = heap_sort(array, _, len(array))  # TODO：从第一个非叶子结点从下至上，从右至左调整结构（构建大顶堆）
    for __ in range(len(array) - 1, 0, -1):
        i_ += 1
        array[0], array[__] = array[__], array[0]  # TODO：将堆顶元素与末尾元素进行交换
        array = heap_sort(array, 0, __)  # TODO：重新对堆进行调整（循环时候排序最后一个元素）
    return array


def heap_sort(array, _, __):  # TODO：堆调整
    global i, i_
    ___ = _
    i += 1
    if 2 * _ + 1 < __ and array[2 * _ + 1] > array[___]:  # TODO：找出较大的一个子节点（当左子结点较大）
        i_ += 1
        ___ = 2 * _ + 1
    i += 1
    if 2 * _ + 2 < __ and array[2 * _ + 2] > array[___]:  # TODO：找出较大的一个子节点（当右子结点较大）
        i_ += 1
        ___ = 2 * _ + 2
    i += 1
    if ___ != _:  # TODO：如果堆项有调整则再次递归
        i_ += 2
        array[_], array[___] = array[___], array[_]  # TODO：将堆顶元素与末尾元素进行交换
        heap_sort(array, ___, __)  # TODO：重新对堆进行调整
    return array


_ = heap(list(array_list))
print(f'堆排序共判断 {i} 次，执行赋值 {i_} 次。\n{_}')

# 8、计数排序（Counting Sort）


def counting(array):
    n = 0
    n_ = 0
    n_ += 1 + 2 * (max(array) - min(array))
    _ = [0] * len(array)  # TODO：存放排序后的数组
    __ = [array.count(_) for _ in range(min(array), max(array) + 1)]  # TODO：通过下标索引，记录数中有哪些数字，相同值的共有几个
    __ = [sum(__[:_]) for _ in range(1, len(__) + 1)]  # TODO：数组中小于某个数的数字个数，用于排序
    for ___ in array[::-1]:
        n_ += 3
        ___ -= min(array)  # TODO：针对负数与下标关系优化，使最小负数下标正好为 0
        _[__[___] - 1] = ___ + min(array)  # TODO：下标值为次序，还原负数与下标关系的优化
        __[___] -= 1  # TODO：每插入一个数，当前下标就减一
    print(f'计数排序共判断 {n} 次，执行赋值 {n_} 次。')
    return _


print(counting(list(array_list)))

# 9、桶排序（Bucket Sort）


def bucket(array):
    n = 0
    n_ = 0
    n_ += max(array) - min(array) + 1
    _ = []  # TODO：存放排序后的数组
    __ = [array.count(_) for _ in range(min(array), max(array) + 1)]  # TODO：通过下标索引，记录数中有哪些数字，相同值的共有几个
    for ___, ____ in enumerate(__):
        for _____ in range(____):  # TODO：执行数字出现次数次操作（对计数排序的优化）
            n_ += 1
            _.append(___ + min(array))  # TODO：下标值为次序，还原负数与下标关系的优化
    print(f'桶排序共判断 {n} 次，执行赋值 {n_} 次。')
    return _


print(bucket(list(array_list)))

# 10、基数排序（Radix Sort）


def radix(array):
    n = 0
    n_ = 0
    n_ += len(array)
    _ = [__ - min(array) for __ in array]  # TODO：针对负数与下标关系优化，使最小负数下标正好为 0，构造没有负数的数组
    for __ in range(len(str(max(_)))):  # TODO：按最大数字长度做多轮操作，从个位到十位到百位...
        n_ += 10
        ____ = [[] for _ in range(10)]  # TODO：因为每一位数字都是 0-9 ，故建立10个桶
        for ___ in _:
            n_ += 1
            ____[int(___ / (10 ** __) % 10)].append(___)  # TODO：按个位、十位、百位...放入桶中
        n_ += 1
        _ = [___ for __ in ____ for ___ in __]  # TODO：按当前桶的顺序重排列表
    print(f'基数排序共判断 {n} 次，执行赋值 {n_} 次。')
    return [__ + min(array) for __ in _]


print(radix(list(array_list)))
