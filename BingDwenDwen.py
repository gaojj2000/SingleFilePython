# _*_ coding:utf-8 _*_
# FileName: BingDwenDwen.py
# IDE: PyCharm

"""
冰墩墩
——压缩代码版本
学习C站博客：https://blog.csdn.net/weixin_46318141/article/details/122841674
跳转源代码地址：https://0xtlu.me/article/f87e7fbe.html
"""

import turtle
turtle.speed(10)  # 画笔移动速度
turtle.hideturtle()  # 隐藏光标
turtle.tracer(False)  # 设置False会立刻绘画完成，正整数则每 n 次更新屏幕
turtle.setup(600, 600)  # 设置画布大小
turtle.title('可爱的冰墩墩~')  # 设置窗口标题
step_list = [  # 记录轮廓的步骤（正向旋转度数，画弧次数）
    (20, 1),  # 画脑门
    (50, 1),  # 右耳
    (-50, 2),  # 右侧脸与右侧肚子
    (0, 5),  # 右脚
    (0, 3),  # 裤裆
    (0, 4),  # 左脚
    (0, 2),  # 左侧肚子
    (-120, 3),  # 左手
    (86, 1),  # 左侧脸
    (122, 1)  # 左耳
]
circle_list = iter([  # 记录每段弧线（半径，弧角度数）【按顺序往后堆叠】
    #   脑门   |    右耳    |    右侧脸与右侧肚子     |                         右   脚
    (-250, 35), (-42, 180), (-190, 30), (-320, 45), (120, 30), (200, 12), (-18, 85), (-180, 23), (-20, 110),
    #            裤   裆            |                           左   脚
    (15, 115), (100, 12), (15, 120), (-15, 110), (-150, 30), (-15, 70), (-150, 10), (200, 35), (-150, 20),
    #            左   手             |   左侧脸   |    左耳    |         右手
    (50, 30), (-35, 200), (-300, 23), (-300, 26), (-53, 160), (-45, 200), (-300, 23),
    #                 画脸上的彩虹圈                  |                         ②
    (-165, 150), (-130, 78), (-250, 30), (-138, 105), (-160, 144), (-120, 78), (-242, 30), (-135, 105),
    #                      ③                        |                        ④
    (-155, 136), (-116, 86), (-220, 30), (-134, 103), (-150, 136), (-104, 86), (-220, 30), (-126, 102),
    #                      ⑤
    (-145, 136), (-90, 83), (-220, 30), (-120, 100),
    #                   左黑眼圈                   |                     右黑眼圈
    (-35, 152), (-100, 50), (-35, 130), (-100, 50), (-32, 152), (-100, 55), (-25, 120), (-120, 45),
    #        右耳黑       |         左耳黑        |                   左手黑
    (-30, 170), (150, 23), (-28, 160), (150, 20), (50, 30), (-27, 200), (-300, 20), (300, 14),
    #                                    左脚黑
    (15, 100), (-10, 110), (-100, 30), (-15, 65), (-100, 10), (200, 15), (-200, 27),
    #                                   右脚黑
    (110, 15), (200, 10), (-18, 80), (-180, 13), (-20, 90), (15, 60), (-200, 29),
    #            右手内部              |                  左眼珠子
    (-37, 160), (-20, 50), (-200, 30), (25, 360), (19, 360), (10, 360), (5, 360),
    #                 右眼珠子                 |             大黑鼻子
    (24, 360), (19, 360), (10, 360), (5, 360), (-8, 130), (-22, 100), (-8, 130),
    #      小嘴儿        |                   右手爱心
    (60, 70), (-45, 100), (-8, 180), (-60, 24), (-60, 24), (-8, 180)
])


def draw_eye(goto, setheading):  # 画眼睛
    turtle.color('black')
    turtle.penup()
    turtle.goto(*goto)
    turtle.pendown()
    turtle.begin_fill()
    turtle.setheading(setheading)
    [turtle.circle(*next(circle_list)) for _ in range(4)]
    turtle.end_fill()


def draw_eyeball(goto1, goto2, goto3, goto4):  # 画眼球
    for goto, color_ in zip([goto1, goto2, goto3, goto4], ['white', 'darkslategray', 'black', 'white']):
        turtle.penup()
        turtle.goto(*goto)
        turtle.pendown()
        turtle.begin_fill()
        turtle.setheading(0)
        turtle.color(color_)
        turtle.circle(*next(circle_list))
        turtle.end_fill()


def draw_ear(goto, setheading1, setheading2):  # 画耳朵
    turtle.color('black')
    turtle.penup()
    turtle.goto(*goto)
    turtle.pendown()
    turtle.begin_fill()
    turtle.setheading(setheading1)
    turtle.circle(*next(circle_list))
    turtle.setheading(setheading2)
    turtle.circle(*next(circle_list))
    turtle.end_fill()


def draw_foot(goto, setheading1, setheading2):  # 画脚
    turtle.color('black')
    turtle.penup()
    turtle.goto(*goto)
    turtle.pendown()
    turtle.begin_fill()
    turtle.setheading(setheading1)
    [turtle.circle(*next(circle_list)) for _ in range(6)]
    turtle.setheading(setheading2)
    turtle.circle(*next(circle_list))
    turtle.end_fill()


# 轮廓
turtle.penup()  # 抬起画笔，不绘图
turtle.pensize(3)  # 画笔粗细
turtle.goto(-73, 230)  # 定位到指定坐标
turtle.color('lightgray', 'white')  # turtle.color(pencolor, fillcolor) # 画笔颜色、填充颜色
turtle.pendown()  # 画笔落下，开始绘图
turtle.setheading(20)
for step in step_list:
    step[0] and turtle.setheading(step[0])  # 每次都从正右开始旋转，turtle.left(step[0])则是从当前角度开始旋转
    [turtle.circle(*next(circle_list)) for _ in range(step[1])]  # 画圆
# 补上右手
turtle.penup()
turtle.goto(177, 112)
turtle.pendown()
turtle.setheading(80)
turtle.begin_fill()  # 从此处落笔开始，准备填充封闭图形
[turtle.circle(*next(circle_list)) for _ in range(2)]
turtle.end_fill()  # 填充封闭图形，若图形不封闭，则起点终点连线封闭
# 画脸上的彩虹圈
turtle.pensize(5)
for site, color in zip([(-135, 120), (-131, 116), (-127, 112), (-123, 108), (-120, 104)], ['cyan', 'slateblue', 'orangered', 'gold', 'greenyellow']):
    turtle.penup()
    turtle.goto(*site)
    turtle.pendown()
    turtle.setheading(60)
    turtle.pencolor(color)
    [turtle.circle(*next(circle_list)) for _ in range(4)]
# 填充黑色部分
turtle.pensize(1)
# 填充左右眼睛
draw_eye((-64, 120), 40)
draw_eye((51, 82), 120)
# 填充右左耳
draw_ear((90, 230), 40, 125)
draw_ear((-130, 180), 120, 210)
# 填充左手
turtle.penup()
turtle.goto(-180, -55)
turtle.pendown()
turtle.begin_fill()
turtle.setheading(-120)
[turtle.circle(*next(circle_list)) for _ in range(3)]
turtle.setheading(-90)
turtle.circle(*next(circle_list))
turtle.end_fill()
# 填充左脚
draw_foot((-38, -210), -155, -14)
# 填充右脚
draw_foot((108, -168), -115, 42)
# 填充右手
turtle.penup()
turtle.goto(182, 95)
turtle.pendown()
turtle.begin_fill()
turtle.setheading(95)
[turtle.circle(*next(circle_list)) for _ in range(3)]
turtle.end_fill()
# 填充左右眼球
draw_eyeball((-47, 55), (-45, 62), (-45, 68), (-47, 86))
draw_eyeball((79, 60), (79, 64), (79, 70), (79, 88))
# 大黑鼻子
turtle.penup()
turtle.goto(37, 80)
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor("black")
[turtle.circle(*next(circle_list)) for _ in range(3)]
turtle.end_fill()
# 小嘴儿
turtle.penup()
turtle.goto(-15, 48)
turtle.pendown()
turtle.begin_fill()
turtle.setheading(-36)
turtle.circle(*next(circle_list))
turtle.setheading(-132)
turtle.circle(*next(circle_list))
turtle.end_fill()
# 右手爱心
turtle.penup()
turtle.goto(220, 115)
turtle.pendown()
turtle.begin_fill()
turtle.color("brown")
turtle.setheading(36)
[turtle.circle(*next(circle_list)) for _ in range(2)]
turtle.setheading(110)
[turtle.circle(*next(circle_list)) for _ in range(2)]
turtle.end_fill()
turtle.penup()
# 奥运时间地点
turtle.pencolor("black")
turtle.goto(-24, -160)
turtle.write("BEIJING 2022", font=('Arial', 10, 'bold italic'))
# 奥运五环
for site, color in zip([(-5, -170), (10, -170), (25, -170), (2, -175), (16, -175)], ['blue', 'black', 'brown', 'lightgoldenrod', 'green']):
    turtle.penup()
    turtle.goto(*site)
    turtle.pendown()
    turtle.pencolor(color)
    turtle.circle(6)
    turtle.penup()
# 干扰图片识别 - - - - - - - - - - - - - - - - - - - -
turtle.color('#000')
turtle.pensize(30)
turtle.setheading(0)
for t in [1, 0]:
    for i in range(6):
        turtle.up()
        turtle.goto(-300 if t else i * 90 - 230, 230 - i * 90 if t else 300)
        turtle.pendown()
        turtle.forward(600)
    turtle.right(90)
turtle.up()
# 干扰图片识别结束 - - - - - - - - - - - - - - - - - - -
turtle.done()
