# _*_ coding:utf-8 _*_
# FileName: NationalFlag.py
# IDE: PyCharm

# 使用turtle库绘制标准的国旗（使用网格线定义坐标绘画）
import math
import turtle

# 窗口属性设置
side = 40  # 网格单位边长为40（可变参数）
width = 30  # 网格的宽为30个单位长度（非可变参数）
height = 20  # 网格的高为20个单位长度（非可变参数）
turtle.speed(10)  # 调整绘图速度 [0-10] 整数
turtle.hideturtle()  # 隐藏海龟图标
turtle.title('五星红旗迎风飘扬~')  # 海龟画图的标题
turtle.setup(width * side, height * side)

# 五角星处网格线绘制
turtle.pencolor('#F00')
# 五角星处网格线绘制（横线）
for row in range(height // 2 + 1):
    turtle.up()
    turtle.goto(-1 * width * side // 2, height * side // 2 - row * side)
    turtle.pendown()
    turtle.forward(width * side // 2)
# 五角星处网格线绘制（竖线）
turtle.right(90)
for col in range(width // 2 + 1):
    turtle.penup()
    turtle.goto(col * side - width * side // 2, height * side // 2)
    turtle.pendown()
    turtle.forward(height * side // 2)

# 绘制五颗黄色的五角星
turtle.speed(5)
turtle.left(180)
turtle.color('#FF0', '#FF0')  # turtle.color(pencolor, fillcolor)
# 五角星外接圆圆心、半径、旋转角数据
stars = {
    (-10, 5): (3, 0),
    (-5, 8): (1, -math.degrees(math.atan(3 / 5)) - 18),
    (-3, 6): (1, -math.degrees(math.atan(1 / 7)) - 18),
    (-3, 3): (1, math.degrees(math.atan(2 / 7)) - 18),
    (-5, 1): (1, math.degrees(math.atan(4 / 5)) - 18),
}


def draw_star(location, radius, rotate):
    """
    按外接圆圆心和半径绘制圆内正五角星。
    :param location: 圆心位置
    :param radius: 半径长度
    :param rotate: 中心顺时针旋转
    """
    length = 2 * radius * side * math.cos(math.pi / 10)  # 计算任意两顶点间的距离
    turtle.penup()
    turtle.right(rotate)  # 初始中心旋转（保证有一角尖指向大星中心点）
    turtle.goto(location[0] * side, location[1] * side)
    turtle.forward(radius * side)  # 此处到达最上方顶点
    turtle.right(180 - 18)  # 倾斜方便绘制第一条直线
    turtle.pendown()
    turtle.begin_fill()
    for angle in range(5):
        turtle.forward(length)
        turtle.right(180 - 36)
    turtle.end_fill()
    turtle.left(18 + rotate)  # 恢复到垂直向上的方向


for star in stars:
    draw_star(star, *stars[star])

# 填充背景颜色红色
turtle.bgcolor('#F00')
# 干扰图片识别 - - - - - - - - - - - - - - - - - - - -
turtle.color('#f6f6f6')
turtle.pensize(60)
turtle.setheading(0)
for t in [1, 0]:
    for i in range(6):
        turtle.up()
        turtle.goto(-600 if t else i * 180 - 460, 460 - i * 180 if t else 400)
        turtle.pendown()
        turtle.forward(1200 if t else 800)
    turtle.right(90)
turtle.up()
# 干扰图片识别结束 - - - - - - - - - - - - - - - - - - -
turtle.done()
