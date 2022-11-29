# _*_ coding:utf-8 _*_
# FileName: DrawPolygon.py
# IDE: PyCharm

import math
import turtle


def draw_polygon_by_point(point, radius, rotate, side, fill=True):
    """
    按起始顶点和边长绘制圆内正多边形。
    :param point: 顶点位置
    :param radius: 边长
    :param rotate: 中心顺时针旋转
    :param side: 边数
    :param fill: 是否填充
    """
    assert side > 2 and isinstance(side, int), ValueError('边数必须是大于2的正整数！')
    turtle.penup()
    turtle.setheading((180 * (side - 2) / side) / 2 - 90)  # 绝对数值对称
    turtle.right(rotate)  # 初始中心旋转
    turtle.goto(point[0], point[1])
    turtle.pendown()
    if fill:
        turtle.begin_fill()
    for angle in range(side):
        turtle.forward(radius)
        turtle.right(180 - (180 * (side - 2) / side))
    if fill:
        turtle.end_fill()
    turtle.penup()
    turtle.setheading(0)  # 恢复到水平向右的方向


def draw_odd_shape(location, radius, rotate, side, fill=True):
    """
    按外接圆圆心和半径绘制圆内正多边形顶点连线图（奇数边数）。
    :param location: 圆心位置
    :param radius: 半径长度
    :param rotate: 中心顺时针旋转
    :param side: 边数
    :param fill: 是否填充
    """
    length = 2 * radius * math.sin(math.radians(180 * (side - 2) / side + (45 if side == 4 else 0)))  # 计算任意两间隔顶点间的距离
    turtle.penup()
    turtle.setheading(90)  # 先将初始顶点设置于正上方
    turtle.right(rotate)  # 初始中心旋转
    turtle.goto(location[0], location[1])
    turtle.forward(radius)  # 此处到达最上方顶点
    turtle.right(90 + 2 * 180 / (side if side != 4 else 8))  # 倾斜方便绘制第一条直线
    turtle.pendown()
    if fill:
        turtle.begin_fill()
    for angle in range(side):
        turtle.forward(length)
        turtle.right(4 * 180 / (side if side != 4 else 8))
    if fill:
        turtle.end_fill()
    turtle.penup()
    turtle.setheading(90)  # 恢复到垂直向上的方向
    turtle.goto(location[0], location[1])


def draw_polygon_by_center(location, radius, rotate, side, fill=True):
    """
    按外接圆圆心和半径绘制圆内正多边形最近间隔顶点连线图。
    :param location: 圆心位置
    :param radius: 半径长度
    :param rotate: 中心顺时针旋转
    :param side: 边数
    :param fill: 是否填充
    """
    assert side > 2 and isinstance(side, int), ValueError('边数必须是大于2的正整数！')
    if side < 5 or side % 2:  # 边数小于5，或者是奇数边数时可以一次性画完
        draw_odd_shape(location, radius, rotate, side, fill)
    else:  # 偶数边数时要分两个小形状变换角度画两次
        '''
            正多边形内间最远隔点连线图：
            draw_polygon_by_center(location, radius, rotate, side // 2, fill)
            draw_polygon_by_center(location, radius, rotate + 360 / side, side // 2, fill)
        '''
        location = (location[0], location[1] + radius)
        draw_polygon_by_point(location, 2 * radius * math.sin(math.radians(180 * (side - 2) / side + (45 if side == 4 else 0))), rotate, side // 2, fill)
        turtle.goto(location[0], location[1] - radius)  # 回到中心
        turtle.setheading(90 - (rotate + 360 / side))  # 向右上角出发
        turtle.forward(radius)  # 前进到右上角顶点
        location = turtle.position()  # 获取右上角顶点坐标
        turtle.back(radius)  # 返回中心
        draw_polygon_by_point(location, 2 * radius * math.sin(math.radians(180 * (side - 2) / side + (45 if side == 4 else 0))), rotate + 360 / side, side // 2, fill)


if __name__ == '__main__':
    turtle.hideturtle()
    turtle.setup(800, 800)
    turtle.color('yellow')
    turtle.speed(10)
    # draw_polygon_by_point((0, 100), 200, 0, 6)
    # draw_polygon_by_center((0, 0), 200, 0, 10, True)
    index = 3
    for row in range(4):
        for col in range(4):
            draw_polygon_by_center((col * 150 - 225, 225 - row * 150), 70, 0, index, False)
            index += 1
    # for i in range(3, 19):
    #     draw_polygon_by_center((0, 0), 200, 0, i, False)
    turtle.done()
