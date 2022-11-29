# _*_ coding:utf-8 _*_
# FileName: DrawTurtle.py
# IDE: PyCharm

import turtle

# turtle基础教程（常用）
turtle.setup(888, 444, 100, 200)  # 设置画布大小宽 888 高 444，距离左边100，距离上边200
turtle.title('示范绘图')  # 窗口标题
turtle.hideturtle()  # 或 turtle.ht() 隐藏海龟图标
turtle.showturtle()  # 或 turtle.st() 显示海龟图标
turtle.tracer(3)  # 设置False会立刻绘画完成，正整数则每 n 次更新屏幕
turtle.speed(1)  # 调整绘图速度 [0-10] 整数
turtle.goto(100, 100)  # 或 turtle.setpos(100, 100) 或 turtle.setposition(100, 100) 移动当前光标到(100, 100)位置
turtle.penup()  # 或 turtle.up() 或 turtle.pu() 抬笔（之后的操作将不会留下痕迹）
turtle.pendown()  # 或 turtle.down() 或 turtle.pd() 落笔（之后的操作将会留下痕迹）
turtle.forward(100)  # 或 turtle.fd(100) 向当前方向前进 100
turtle.back(100)  # 或 turtle.bk(100) 向当前方向后退 100
turtle.pensize(10)  # 或 turtle.width(10) 设置画笔宽度为 10
turtle.bgcolor('pink')  # 设置背景图颜色为粉色
turtle.pencolor('red')  # 设置画笔颜色为红色
turtle.fillcolor('yellow')  # 设置填充颜色为黄色
turtle.color('green', 'blue')  # 设置画笔颜色为绿色、填充颜色为蓝色
turtle.stamp()  # 印下当前形状（比如说海龟）
turtle.left(30)  # 或 turtle.lt(30) 当前方向逆时针旋转 30 度，负数顺时针旋转（初始方向为正右）
turtle.forward(100)  # 向当前方向前进 100
turtle.right(60)  # 或 turtle.rt(60) 当前方向顺时针旋转 60 度，负数逆时针旋转（初始方向为正右）
turtle.forward(100)  # 向当前方向前进 100
turtle.setheading(90)  # 或 turtle.seth(90) 从初始方向逆时针旋转 90 度，负数顺时针旋转
turtle.forward(100)  # 向当前方向前进 100
print(turtle.pos())  # 或 turtle.position() 获取当前位置坐标
turtle.begin_fill()  # 开始填充
turtle.circle(20, 360)  # 画圆（半径，度数）【非按圆心画圆】（半径正数往当前方向左侧画，当前方向右侧画）
turtle.write("示范文本", font=('Arial', 10, 'bold italic'))  # 在当前位置写字
turtle.end_fill()  # 结束填充（将会填充所有封闭图形区域）
print(turtle.distance(0, 0))  # 获取当前位置到指定位置之间的距离
print(turtle.towards(0, 0))  # 与正右方向旋转多少度才能朝向指定点
print(turtle.heading())  # 获取当前与正右方向的角度
turtle.home()  # 返回原点，相当于 turtle.goto(0, 0)
print(turtle.textinput('示范', '请输入文字：'))  # 输入数据的弹窗【期间会堵塞，直到点击按钮之后】
turtle.dot(max(turtle.pensize() + 4, 2 * turtle.pensize()), 'blue')  # 绘制指定大小颜色的实心圆点

turtle.update()  # 立刻刷新画面（用于处理 turtle.tracer(False) 带来的绘图不全bug）
turtle.exitonclick()  # 在用户点击界面后退出
turtle.done()  # 结束绘图，不自动关闭窗口，和 turtle.mainloop() | input() 功能一致
