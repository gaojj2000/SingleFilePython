# _*_ coding:utf-8 _*_
# FileName: JavaScript.py
# IDE: PyCharm

import execjs
import tkinter


def call():
    try:
        f = fun.get().strip().replace('（', '(').replace('）', ')')
        args = eval(f[f.find('('): f.find(')') + 1])
        res.delete(tkinter.START, tkinter.END)
        res.insert(tkinter.END, execjs.compile(text.get(tkinter.START, tkinter.END)).call(f[:f.find('(')], *args))
    except Exception as e:
        print(e)
        res.insert(tkinter.END, str(e))


root = tkinter.Tk()
text = tkinter.Text(root)
text.insert(tkinter.END, '请在此粘贴JavaScript代码。')
text.pack(fill=tkinter.BOTH)
fun = tkinter.Entry(root)
fun.insert('0', '请输入执行函数名和参数【fun("a", 1, "b")】')
fun.pack(fill=tkinter.BOTH)
tkinter.Button(root, text='执行', command=call).pack(fill=tkinter.BOTH, after=fun, side=tkinter.LEFT)
res = tkinter.Text(root)
res.insert(tkinter.END, '执行结果显示处。')
res.pack(fill=tkinter.BOTH)
root.title('JavaScript执行器')
root.attributes('-topmost', 1)
root.geometry('500x380')
root.resizable(1, 1)
root.mainloop()
