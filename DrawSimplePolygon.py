# _*_ coding:utf-8 _*_
# FileName: DrawSimplePolygon.py
# IDE: PyCharm

# 基础图形绘图
# import math
# import turtle
# import timeit

# 绘画正三角形、四边形、五边形、六边形、七边形、八边形、九边形...
# turtle.setup(800, 200)
# for i in range(3, 10):
#     turtle.penup()
#     turtle.goto(x=i * 110 - 660, y=-50)
#     turtle.pendown()
#     print(f'执行语句：turtle.circle(radius=50, extent=360, steps={i})')
#     turtle.circle(radius=50, extent=360, steps=i)

# 正五角星
# turtle.setup(200, 200)
# turtle.right(72)
# for i in range(5):
#     turtle.forward(80)
#     turtle.right(144)

# 正七边形内邻点连线图形
# turtle.setup(200, 200)
# turtle.right(360 / 7)
# for i in range(7):
#     turtle.forward(60)
#     turtle.right(720 / 7)

# 绘画正多边形内邻点连线图形
# turtle.setup(680, 200)
# for s in range(5, 12, 2):
#     turtle.penup()
#     turtle.goto(x=s * 80 - 660, y=60)
#     turtle.pendown()
#     turtle.setheading(-2 * 180 / s)
#     for i in range(s):
#         turtle.forward(70)
#         turtle.right(4 * 180 / s)


# 绘画奇数正多边形内邻点连线图形的函数
# def draw_odd_polygon(location, radius, side):
#     turtle.penup()
#     turtle.goto(*location)
#     turtle.pendown()
#     turtle.setheading(-2 * 180 / side)
#     for i in range(side):
#         turtle.forward(radius)
#         turtle.right(4 * 180 / side)
#
#
# turtle.setup(680, 200)
# for s in range(5, 12, 2):
#     draw_odd_polygon((s * 80 - 660, 60), 70, s)


# 绘画偶数正多边形内邻点连线图形的函数
# def draw_polygon(location, radius, side):
#     if radius % 2:
#         draw_odd_polygon(location, radius, side)
#     else:
#         turtle.penup()
#         turtle.goto(*location)
#         turtle.pendown()
#         turtle.circle(radius=-radius, extent=360, steps=side // 2)
#         turtle.penup()
#         turtle.setheading(-90)
#         turtle.forward(radius)
#         turtle.setheading(90 - 360 / side)
#         turtle.forward(radius)
#         turtle.setheading(-360 / side)
#         turtle.pendown()
#         turtle.circle(radius=-radius, extent=360, steps=side // 2)
#
#
# turtle.setup(400, 400)
# draw_polygon((0, 100), 100, 10)

# 不用函数绘画圆形的三种方法
# turtle.setup(300, 300)
# turtle.penup()
# turtle.goto(0, 100)
# turtle.pendown()
# # turtle.circle(-100)
# for i in range(60):
#     turtle.forward(10)
#     turtle.right(6)
# turtle.penup()

# turtle.setup(300, 300)
# turtle.penup()
# turtle.goto(50, 0)
# turtle.pendown()
# # x^2 + y^2 = 50^2 => y = (50^2 - x^2) ^ 0.5
# for x in range(50, -50, -1):
#     turtle.goto(x, (50 ** 2 - x ** 2) ** 0.5)
# for x in range(-50, 50 + 1):
#     turtle.goto(x, -(50 ** 2 - x ** 2) ** 0.5)
# turtle.penup()

# turtle.setup(300, 300)
# turtle.penup()
# turtle.goto(50, 0)
# turtle.pendown()
# # x = r * cos(α); y = r * sin(α)
# for a in range(360):
#     turtle.goto(50 * math.cos(math.radians(a + 1)), 50 * math.sin(math.radians(a + 1)))
# turtle.penup()

# 绘画椭圆形——数量足够大的多边形
# turtle.setup(300, 200)
# turtle.penup()
# turtle.setheading(90)
# turtle.goto(-100, 0)
# turtle.pendown()
# fd = 1  # 前进的距离
# for _ in range(2):
#     for i in range(60):
#         if i < 30:
#             fd += 0.2
#         else:
#             fd -= 0.2
#         turtle.forward(fd)
#         turtle.right(3)
# turtle.penup()

# 绘画椭圆形——椭圆直角坐标方程
# turtle.setup(300, 200)
# turtle.penup()
# turtle.forward(100)
# turtle.setheading(90)
# turtle.pendown()
# # x^2 / a^2 + y^2 / b^2 = 1 (焦点在X轴上) => y = (((a^2 - x^2) * b^2) / a^2) ^ 0.5
# for x in range(100, -100, -1):
#     turtle.goto(x, (((100 ** 2 - x ** 2) * 60 ** 2) / 100 ** 2) ** 0.5)
# for x in range(-100, 100 + 1):
#     turtle.goto(x, -1 * (((100 ** 2 - x ** 2) * 60 ** 2) / 100 ** 2) ** 0.5)
# turtle.penup()

# 绘画椭圆形——椭圆参数方程
# turtle.setup(300, 200)
# turtle.penup()
# turtle.goto(100, 0)
# turtle.pendown()
# # x = a * cos(β); y = b * sin(β)
# for a in range(360):
#     turtle.goto(100 * math.cos(math.radians(a + 1)), 60 * math.sin(math.radians(a + 1)))
# turtle.penup()

# 合理计算绘画椭圆形最短时间的方法
# a, b = 90, 54
# zj = f"""import math, turtle
# turtle.setup({a * 3}, {b * 4})
# turtle.penup()
# turtle.forward({a})
# turtle.setheading(90)
# turtle.pendown()
# for x in range({a}, -{a}, -1):
#     turtle.goto(x, ((({a} ** 2 - x ** 2) * {b} ** 2) / {a} ** 2) ** 0.5)
# for x in range(-{a}, {a} + 1):
#     turtle.goto(x, -1 * ((({a} ** 2 - x ** 2) * {b} ** 2) / {a} ** 2) ** 0.5)
# turtle.penup()"""
# cs = f"""import math, turtle
# turtle.setup({a * 3}, {b * 4})
# turtle.penup()
# turtle.goto({a}, 0)
# turtle.pendown()
# for a in range(360):
#     turtle.goto({a} * math.cos(math.radians(a + 1)), {b} * math.sin(math.radians(a + 1)))
# turtle.penup()"""
# print(timeit.timeit(stmt=zj, number=1))  # 直角坐标系画椭圆
# print(timeit.timeit(stmt=cs, number=1))  # 参数方程画椭圆

# 绘画圆柱体
# turtle.setup(300, 400)
# turtle.penup()
# turtle.goto(100, -40)
# turtle.color('pink')
# turtle.pendown()
# turtle.begin_fill()
# for a in range(360):
#     turtle.goto(100 * math.cos(math.radians(a + 1)), -40 + 60 * math.sin(math.radians(a + 1)))
# turtle.setheading(90)
# turtle.forward(80)
# turtle.setheading(180)
# turtle.forward(200)
# turtle.setheading(270)
# turtle.forward(80)
# turtle.setheading(0)
# turtle.forward(200)
# turtle.end_fill()
# turtle.penup()
# turtle.color('skyblue')
# turtle.goto(100, 40)
# turtle.pendown()
# turtle.begin_fill()
# for a in range(360):
#     turtle.goto(100 * math.cos(math.radians(a + 1)), 40 + 60 * math.sin(math.radians(a + 1)))
# turtle.end_fill()
# turtle.penup()

# 画太极
# turtle.setup(300, 300)
# turtle.penup()
# turtle.goto(0, -100)
# turtle.color('red')
# turtle.pendown()
# turtle.begin_fill()
# turtle.circle(100, 180)
# turtle.setheading(0)
# turtle.circle(-50, 180)
# turtle.setheading(180)
# turtle.circle(50, 180)
# turtle.end_fill()
# turtle.penup()
# turtle.color('blue')
# turtle.pendown()
# turtle.begin_fill()
# turtle.setheading(180)
# turtle.circle(-100, 180)
# turtle.setheading(0)
# turtle.circle(-50, 180)
# turtle.setheading(180)
# turtle.circle(50, 180)
# turtle.end_fill()
# turtle.penup()

# turtle.exitonclick()
