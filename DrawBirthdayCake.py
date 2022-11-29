# _*_ coding:utf-8 _*_
# FileName: DrawBirthdayCake.py
# IDE: PyCharm

# 画生日蛋糕
import math
import turtle
# 元素函数


def draw_candle(location, width, height):
    """
    画蜡烛。
    :param location: 蜡烛底部中心坐标
    :param width: 蜡烛宽度
    :param height: 蜡烛高度
    """
    color = turtle.color()
    angle = turtle.heading()
    turtle.penup()
    turtle.color('skyblue')
    turtle.setheading(0)
    turtle.goto(*location)
    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(width / 2)
    turtle.setheading(90)
    turtle.forward(height)
    turtle.setheading(180)
    turtle.forward(width)
    turtle.setheading(270)
    turtle.forward(height)
    turtle.setheading(0)
    turtle.forward(width / 2)
    turtle.end_fill()
    turtle.penup()
    turtle.setheading(90)
    turtle.forward(height)
    turtle.setheading(20)
    turtle.color('red')
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(width / 2, 180)
    turtle.setheading(20)
    turtle.circle(-width / 4, 180)
    turtle.setheading(200)
    turtle.circle(width / 4, 180)
    turtle.end_fill()
    turtle.penup()
    turtle.color(*color)
    turtle.goto(*location)
    turtle.setheading(angle)


def draw_oval(location, width, height, fill=True, color='#000000'):
    """
    画椭圆。
    :param location: 椭圆中心坐标
    :param width: 椭圆长轴（横向）
    :param height: 椭圆短轴（纵向）
    :param fill: 是否填充
    :param color: 椭圆颜色
    """
    assert width >= height, ValueError('目前只能长轴是 x 轴，即 width >= height （width == height 时是圆）！')
    a = width / 2
    b = height / 2
    color_old = turtle.color()
    angle = turtle.heading()
    turtle.color(color)
    turtle.penup()
    turtle.goto(*location)
    turtle.setheading(0)
    turtle.forward(width / 2)
    turtle.setheading(90)
    turtle.pendown()
    if fill:
        turtle.begin_fill()
    if width < 180:  # 通过椭圆直角坐标方程计算描点绘画
        #                     ((a ** 2 * b ** 2 - b ** 2 * x ** 2) / a ** 2) ** 0.5
        #                     (((a ** 2 - x ** 2) * b ** 2) / a ** 2) ** 0.5
        #                     (((a + x) * (a - x) * b ** 2) / a ** 2) ** 0.5
        for x in range(width // 2, width // -2, -1):  # 以 y = location[1] 的单位上半部分描点
            y = location[1] + (((a ** 2 - x ** 2) * b ** 2) / a ** 2) ** 0.5
            turtle.goto(x, y)
        for x in range(width // -2, width // 2 + 1):  # 以 y = location[1] 的单位下半部分描点
            y = location[1] - (((a ** 2 - x ** 2) * b ** 2) / a ** 2) ** 0.5
            turtle.goto(x, y)
    else:  # 通过椭圆极坐标方程计算描点绘画
        for ang in range(360):
            turtle.goto(width / 2 * math.cos(math.radians(ang + 1)), location[1] + height / 2 * math.sin(math.radians(ang + 1)))
    if fill:
        turtle.end_fill()
    turtle.penup()
    turtle.color(*color_old)
    turtle.goto(*location)
    turtle.setheading(angle)


def draw_cylinder(location, width, height, altitude, fill=True, color1='#000000', color2='#000000'):
    """
    画椭圆柱。
    :param location: 底部椭圆中心坐标
    :param width: 底部椭圆长轴（横向）
    :param height: 底部椭圆短轴（纵向）
    :param altitude: 椭圆柱高度
    :param fill: 是否填充
    :param color1: 椭圆柱面绘图颜色
    :param color2: 椭圆柱顶绘图颜色
    """
    color_old = turtle.color()
    angle = turtle.heading()
    draw_oval(location, width, height, fill=fill, color=color1)
    turtle.penup()
    turtle.color(color1)
    turtle.goto(*location)
    turtle.setheading(0)
    turtle.forward(width / 2)
    turtle.pendown()
    if fill:
        turtle.begin_fill()
        turtle.setheading(90)
        turtle.forward(altitude)
        turtle.setheading(180)
        turtle.forward(width)
        turtle.setheading(270)
        turtle.forward(altitude)
        turtle.setheading(0)
        turtle.forward(width)
        turtle.end_fill()
    turtle.penup()
    location = (location[0], location[1] + altitude)
    draw_oval(location, width, height, fill=fill, color=color2)
    turtle.penup()
    turtle.color(*color_old)
    turtle.goto(*location)
    turtle.setheading(angle)


def draw_wave(location, width, height, space, pensize=10, color='#000000', towards='right'):
    """
    画波浪线。
    :param location: 波浪线起点（中心点）
    :param width: 波浪线总宽度
    :param height: 波浪线高度
    :param space: 波浪间距
    :param pensize: 波浪粗细
    :param color: 波浪颜色
    :param towards: 破浪线朝向
    """
    assert towards.lower() in ['left', 'right'], '方向只能是 left向左 或 right向右 ！'
    color_old = turtle.color()
    angle = turtle.heading()
    thickness = turtle.pensize()
    turtle.color(color)
    turtle.penup()
    turtle.goto(*location)
    turtle.pensize(pensize)
    turtle.pendown()
    if towards.lower() == 'right':
        turtle.setheading(0)
    else:
        turtle.setheading(180)
    for x in range(width):
        turtle.goto(location[0] + x, location[1] + height / 2 * math.sin(math.radians(x * 180 / space)))
    turtle.penup()
    turtle.color(*color_old)
    turtle.pensize(thickness)
    turtle.goto(*location)
    turtle.setheading(angle)


def draw_love(location, side, color='pink'):
    """
    画爱心。
    :param location: 爱心的上方顶点坐标
    :param side: 爱心边长 或 直径（爱心由一个正方形和两个圆形组成）
    :param color: 爱心颜色
    :return:
    """
    color_old = turtle.color()
    angle = turtle.heading()
    turtle.penup()
    turtle.goto(*location)
    turtle.color(color)
    turtle.pendown()
    turtle.right(45)
    turtle.begin_fill()
    turtle.forward(side)
    turtle.right(90)
    turtle.forward(side)
    turtle.right(90)
    turtle.forward(side)
    turtle.right(90)
    turtle.forward(side)
    turtle.end_fill()
    turtle.left(90)
    turtle.begin_fill()
    turtle.circle(side / 2, 360)
    turtle.end_fill()
    turtle.left(90)
    turtle.begin_fill()
    turtle.circle(side / 2, 360)
    turtle.end_fill()
    turtle.penup()
    turtle.color(*color_old)
    turtle.goto(*location)
    turtle.setheading(angle)


turtle.speed(0)
turtle.tracer(False)
turtle.title('生日快乐~')
turtle.setup(600, 600)
turtle.bgcolor("#D3DAE8")
draw_cylinder((0, -100), 400, 150, 10, True, '#EEEEEE', 'white')  # 绘制最底层白色餐盘
draw_cylinder((0, -90), 320, 120, 80, True, 'skyblue', 'white')  # 绘制第一层蛋糕
draw_wave((-160, -100), 320, 25, 40, 5, 'red')  # 绘制第一层蛋糕侧边曲线1
draw_wave((-160, -95), 320, 25, 40, 5, 'orange')  # 绘制第一层蛋糕侧边曲线2
draw_wave((-160, -90), 320, 30, 40, 5, 'yellow')  # 绘制第一层蛋糕侧边曲线3
draw_cylinder((0, 0), 240, 90, 80, True, 'pink', 'white')  # 绘制第二层蛋糕
draw_wave((-120, -5), 240, 30, 40, 5, 'green')  # 绘制第二层蛋糕侧边曲线1
draw_wave((-120, 0), 240, 30, 40, 5, 'blue')  # 绘制第二层蛋糕侧边曲线2
draw_wave((-120, 5), 240, 30, 40, 5, 'cyan')  # 绘制第二层蛋糕侧边曲线3
draw_wave((-120, 10), 240, 30, 40, 5, 'purple')  # 绘制第二层蛋糕侧边曲线4
# 绘制蜡烛
for x_ in range(-90, 91, 30):
    draw_candle((x_, 100), 10, 80)
for x_ in range(-100, 100, 28):
    draw_candle((x_, 80), 10, 80)
for x_ in range(-90, 91, 30):
    draw_candle((x_, 60), 10, 80)
turtle.penup()
draw_love((-200, 100), 50)
draw_love((200, 100), 50)
turtle.color('#F1ADD1')
turtle.goto(-200, 200)
turtle.write("祝博主生日快乐~", font=('Curlz MT', 40, 'bold italic'))
turtle.goto(-150, -270)
turtle.write("码龄 + 1 ~", font=('Curlz MT', 50, 'bold italic'))
turtle.done()

'''
import math
import turtle


def draw_oval(location, width, height, fill=True, color='#000000'):
    """
    画椭圆。
    :param location: 椭圆中心坐标
    :param width: 椭圆长轴（横向）
    :param height: 椭圆短轴（纵向）
    :param fill: 是否填充
    :param color: 椭圆颜色
    """
    assert width >= height, ValueError('目前只能长轴是 x 轴，即 width >= height （width == height 时是圆）！')
    a = width / 2
    b = height / 2
    color_old = turtle.color()
    angle = turtle.heading()
    turtle.color(color)
    turtle.penup()
    turtle.goto(*location)
    turtle.setheading(0)
    turtle.forward(width / 2)
    turtle.setheading(90)
    turtle.pendown()
    if fill:
        turtle.begin_fill()
    if width < 180:  # 通过椭圆直角坐标方程计算描点绘画
        #                     ((a ** 2 * b ** 2 - b ** 2 * x ** 2) / a ** 2) ** 0.5
        #                     (((a ** 2 - x ** 2) * b ** 2) / a ** 2) ** 0.5
        #                     (((a + x) * (a - x) * b ** 2) / a ** 2) ** 0.5
        for x in range(width // 2, width // -2, -1):  # 以 y = location[1] 的单位上半部分描点
            y = location[1] + (((a ** 2 - x ** 2) * b ** 2) / a ** 2) ** 0.5
            turtle.goto(x, y)
        for x in range(width // -2, width // 2 + 1):  # 以 y = location[1] 的单位下半部分描点
            y = location[1] - (((a ** 2 - x ** 2) * b ** 2) / a ** 2) ** 0.5
            turtle.goto(x, y)
    else:  # 通过椭圆极坐标方程计算描点绘画
        for ang in range(360):
            turtle.goto(width / 2 * math.cos(math.radians(ang + 1)), location[1] + height / 2 * math.sin(math.radians(ang + 1)))
    if fill:
        turtle.end_fill()
    turtle.penup()
    turtle.color(*color_old)
    turtle.goto(*location)
    turtle.setheading(angle)


def draw_cylinder(location, width, height, altitude, fill=True, color1='#000000', color2='#000000'):
    """
    画椭圆柱。
    :param location: 底部椭圆中心坐标
    :param width: 底部椭圆长轴（横向）
    :param height: 底部椭圆短轴（纵向）
    :param altitude: 椭圆柱高度
    :param fill: 是否填充
    :param color1: 椭圆柱面绘图颜色
    :param color2: 椭圆柱顶绘图颜色
    """
    color_old = turtle.color()
    angle = turtle.heading()
    draw_oval(location, width, height, fill=fill, color=color1)
    turtle.penup()
    turtle.color(color1)
    turtle.goto(*location)
    turtle.setheading(0)
    turtle.forward(width / 2)
    turtle.pendown()
    if fill:
        turtle.begin_fill()
        turtle.setheading(90)
        turtle.forward(altitude)
        turtle.setheading(180)
        turtle.forward(width)
        turtle.setheading(270)
        turtle.forward(altitude)
        turtle.setheading(0)
        turtle.forward(width)
        turtle.end_fill()
    turtle.penup()
    location = (location[0], location[1] + altitude)
    draw_oval(location, width, height, fill=fill, color=color2)
    turtle.penup()
    turtle.color(*color_old)
    turtle.goto(*location)
    turtle.setheading(angle)


def draw_wave(location, width, height, space, pensize=10, color='#000000', towards='right'):
    """
    画波浪线。
    :param location: 波浪线起点（中心点）
    :param width: 波浪线总宽度
    :param height: 波浪线高度
    :param space: 波浪间距
    :param pensize: 波浪粗细
    :param color: 波浪颜色
    :param towards: 破浪线朝向
    """
    assert towards.lower() in ['left', 'right'], '方向只能是 left向左 或 right向右 ！'
    color_old = turtle.color()
    angle = turtle.heading()
    thickness = turtle.pensize()
    turtle.color(color)
    turtle.penup()
    turtle.goto(location[0], location[1] + height)
    turtle.pensize(pensize)
    turtle.pendown()
    if towards.lower() == 'right':
        turtle.setheading(0)
    else:
        turtle.setheading(180)
    for x in range(width):
        turtle.goto(location[0] + x, location[1] + height / 2 * math.sin(math.radians(x * 180 / space)) + height * abs(x - width / 2) / width * 2)
    turtle.penup()
    turtle.color(*color_old)
    turtle.pensize(thickness)
    turtle.goto(*location)
    turtle.setheading(angle)


turtle.tracer(False)
turtle.setup(600, 600)
turtle.bgcolor("#D3DAE8")
draw_cylinder((0, -100), 400, 150, 10, True, '#EEEEEE', 'white')  # 绘制最底层白色餐盘
draw_cylinder((0, -90), 320, 120, 80, True, 'skyblue', 'white')  # 绘制第一层蛋糕
draw_wave((-160, -120), 320, 25, 40, 5, 'red')  # 绘制第一层蛋糕侧边曲线1
draw_wave((-160, -115), 320, 25, 40, 5, 'orange')  # 绘制第一层蛋糕侧边曲线2
draw_wave((-160, -110), 320, 30, 40, 5, 'yellow')  # 绘制第一层蛋糕侧边曲线3
turtle.exitonclick()
'''
