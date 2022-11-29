# _*_ coding:utf-8 _*_
# FileName: ToolsWindow.py

"""
总体功能描述：【tabControl控制tab标签】
    三种翻译方式（百度、有道、腾讯）translate
    置顶文本编辑器（锁定、解锁、临时保存）note_tip
    算式计算器（通过eval计算，确定算式提示错误；执行cmd）calculator
    显示剪贴板或文件的图片（创建、销毁、保存、读取，比例缩放图片）picture
    计时器（开始计时、暂停计时、时间标记、结束计时、清除标记、独特数显）timer
    文本查找工具（批量查找可直接打开文本文件，剪贴板，看文本在哪些文件内）find
    设置（置顶、透明度、文件保存路径、保存当前状态、载入状态、变量设置）setting
"""

import os
import re
import json
import time
import ctypes
import requests
import pywintypes
import win32clipboard
from io import BytesIO
from win32con import CF_UNICODETEXT
from win32api import GetAsyncKeyState
from threading import Thread
from PIL import Image, ImageGrab, ImageTk, UnidentifiedImageError
from tkinter import Tk, StringVar, IntVar, Text, scrolledtext, messagebox, Canvas, filedialog, Scale, DoubleVar, Listbox, Button
from tkinter.ttk import Notebook, Frame, Entry, Treeview, LabelFrame, Label, Radiobutton, Checkbutton


# 函数功能区
def zoom(e):
    # 鼠标滚轮控制界面大小，基础 delta = 120
    w = int(root.winfo_width() * (1 + e.delta / 2400))
    h = int(root.winfo_height() * (1 + e.delta / 2400))
    if w >= width and h >= height:
        root.geometry(f'{w}x{h}')


def try_tran():
    if translate_text.get().strip():
        Thread(target=tran, daemon=True).start()


def tran():
    # 中英互译
    text = translate_text.get().strip()
    result.configure(state='normal')
    result.delete('0.0', 'end')
    if not text:
        result.insert('end', '请正确输入想查询的内容！')
        return False
    lan = ['zh', 'en']
    url_bd_lan = 'https://fanyi.baidu.com/langdetect'  # 确定中英文
    if requests.post(url_bd_lan, data={"query": text}).json()["lan"] not in lan:
        result.insert('end', '目前只支持英汉互译哦~')
        return False
    result.insert('end', f'正在查询：{text} ......')
    result.update()
    result.configure(state='disabled')

    def get_bin(num: int) -> str:
        num = bin(num).split('b')[-1]
        string = '{:0>' + str(32) + '}'
        return string.format(num)  # 填充 0 到高一级长度

    def sign_bin_right(num: int, offset: int) -> int:
        return ctypes.c_int32(num >> offset).value

    def get_sign(te: str) -> str:
        te = len(te) > 30 and te[0:10] + te[int(len(te) / 2) - 5: int(len(te) / 2) + 5] + te[-10:] or te
        m = 320305
        pass_go = False
        s = []
        for v in range(len(te)):
            if pass_go:
                pass_go = False
                continue
            a = ord(te[v])
            if a < 128:
                s.append(a)
            else:
                if a < 2048:
                    s.append(sign_bin_right(a, 6) | 192)
                else:
                    if 64512 & a is 55296 and v + 1 < len(te) and 64512 & ord(te[v + 1]) is 56320:
                        v += 1
                        pass_go = True
                        a = 65536 + ((1023 & a) << 10) + (1023 & ord(te[v]))
                        s.append(sign_bin_right(a, 18) | 240)
                        s.append(sign_bin_right(a, 12) & 63 | 128)
                    else:
                        s.append(sign_bin_right(a, 12) | 224)
                        s.append(sign_bin_right(a, 6) & 63 | 128)
                    s.append(63 & a | 128)
        p = m
        for b in range(len(s)):
            p += s[b]
            p = ctypes.c_int32(p + ctypes.c_int32(p << 10).value).value
            p ^= int(get_bin(ctypes.c_int32(ctypes.c_uint32(p).value >> 6).value)[6:], 2)
        p = ctypes.c_int32(p + ctypes.c_int32(p << 3).value).value
        p ^= int(get_bin(ctypes.c_int32(ctypes.c_uint32(p).value >> 11).value)[11:], 2)
        p = ctypes.c_int32(p + ctypes.c_int32(p << 15).value).value
        p ^= 131321201
        p = p < 0 and (2147483647 & p) + 2147483648 or p
        p %= 1e6
        return f'{int(p)}.{int(p) ^ m}'

    # 百度翻译url
    url_bd = f'https://fanyi.baidu.com/v2transapi?from={lan.pop(lan.index(requests.post(url_bd_lan, data={"query": text}).json()["lan"]))}&to={lan[0]}'
    # 百度请求头（ab_sr[1.0.0_+128位0-9+a-z+A-Z]一天一刷新，暂时还未获取获得方法）
    headers_bd = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
    }
    headers_bd['Cookie'] = requests.get('https://www.baidu.com', headers=headers_bd).headers['Set-Cookie'].split(';')[0] + ';ab_sr=1.0.0_'
    # 百度翻译数据
    data_bd = {
        'query': text,
        'sign': get_sign(text),
        'token': re.findall("token: '(.*?)'", requests.get('https://fanyi.baidu.com/translate', headers=headers_bd).text)[0]
    }
    # 有道翻译url
    url_yd = 'http://fanyi.youdao.com/translate'
    # 有道翻译数据
    data_yd = {
        'i': text,
        'doctype': 'json'
    }
    # 腾讯翻译url
    url_qq = 'https://fanyi.qq.com/api/translate'
    # 腾讯请求头
    headers_qq = {
        'Referer': 'https://fanyi.qq.com/'
    }
    # 腾讯翻译数据
    data_qq = {
        'sourceText': text
    }

    result.configure(state='normal')
    result.delete('0.0', 'end')
    if translate_choice.get() == 0:
        # data_bd['query'] = text
        # data_bd['sign'] = get_sign(text)
        # text = '\n'.join([te['dst'] for te in requests.post(url=url_bd, headers=headers_bd, data=data_bd).json()['trans_result']['data']])
        # # 在一号方案未研究出来之前，统一用二号方案不变
        data = {
            'kw': text
        }
        text = requests.post(url='https://fanyi.baidu.com/sug', json=data).json()['data'][0]['v']
    elif translate_choice.get() == 1:
        data_qq['sourceText'] = text
        data_qq.update(requests.post(url='https://fanyi.qq.com/api/reauth1232f').json())
        text = ''.join([te['targetText'] for te in requests.post(url=url_qq, headers=headers_qq, data=data_qq).json()['translate']['records']])
    elif translate_choice.get() == 2:
        data_yd['i'] = text
        text = '\n'.join([''.join(sentence['tgt'] for sentence in te) for te in requests.post(url=url_yd, data=data_yd).json()['translateResult']])
    if not text:
        result.insert('end', '未有翻译返回结果，请更换翻译源！')
    result.insert('end', text)
    result.update()
    copy_text()
    result.configure(state='disabled')


def copy_text(e=True):
    if e and copy.get():
        result.tag_add('sel', "0.0", 'end')
        result.event_generate("<<Copy>>")


def freeze():
    global ins
    ins = False
    button.configure(text='取消冻结', command=unfreeze)
    scrolled_text.configure(state='disabled')


def unfreeze():
    global ins
    ins = True
    button.configure(text='冻结输入', command=freeze)
    scrolled_text.configure(state='normal')


def insert():
    n = 1
    while f'存档{n}' in notes:
        n += 1
    notes[f'存档{n}'] = scrolled_text.get('0.0', 'end').strip()
    tree.insert('', index='end', iid=f'存档{n}', tag=f'存档{n}', text=scrolled_text.get('0.0', 'end').strip().replace('\n', '')[:15])
    if not ins:
        scrolled_text.configure(state='normal')
    scrolled_text.delete('0.0', 'end')
    if not ins:
        scrolled_text.configure(state='disabled')


def format_json():
    try:
        fj = json.dumps(json.loads(scrolled_text.get('0.0', 'end').strip(), encoding='utf-8'), indent=4, ensure_ascii=False)
        if not ins:
            scrolled_text.configure(state='normal')
        scrolled_text.delete('0.0', 'end')
        scrolled_text.insert('end', fj)
        if not ins:
            scrolled_text.configure(state='disabled')
    except json.decoder.JSONDecodeError:
        messagebox.showerror(title='严重错误', message='json格式不正确！')


def replace_text():
    text = scrolled_text.get('0.0', 'end').strip()
    if not ins:
        scrolled_text.configure(state='normal')
    scrolled_text.delete('0.0', 'end')
    scrolled_text.insert('end', text.replace(replace_before.get(), replace_after.get()))
    if not ins:
        scrolled_text.configure(state='disabled')


def click(e):
    if e and tree.item(tree.focus())['tags']:
        if not ins:
            scrolled_text.configure(state='normal')
        scrolled_text.delete('0.0', 'end')
        scrolled_text.insert('end', notes[tree.item(tree.focus())['tags'][0]])
        if not ins:
            scrolled_text.configure(state='disabled')


def delete(e):
    tree.focus(tree.identify_row(e.y))
    tree.selection_set(tree.identify_row(e.y))
    if tree.item(tree.focus())['tags'] and messagebox.askyesno(title='删除确认', message=f"确认删除{tree.item(tree.focus())['tags'][0]}？"):
        del notes[tree.item(tree.focus())['tags'][0]]
        tree.delete(tree.item(tree.focus())['tags'][0])


def calc_formula(e=True):
    if e and formula.get().replace(' ', ''):
        f = formula.get().replace(' ', '').replace('（', '(').replace('）', ')').replace('。', '.').replace('^', '**')
        if re.findall(r'[0-9.+\-*/()]*', f)[0] == f:
            try:
                res_c = eval(f)
                if int(str(res_c).split('.')[0]) == res_c:
                    res_c = int(res_c)
                calc.configure(text=f'计算结果：{res_c}')
            except SyntaxError:
                messagebox.showerror(title='严重错误', message='运算符输入不合法！')
        else:
            messagebox.showerror(title='严重错误', message='算式输入不合法！')
        formula.set('')
    else:
        calc.configure(text='计算结果：')


def cmd(e=True):
    global ask
    if e and command.get().strip():
        if (ask and not ctypes.windll.shell32.IsUserAnAdmin()) and not messagebox.askyesno(title='重要的询问', message='当前不是管理员状态，是否继续？'):
            close()
        ask = False
        cmd_result.configure(state='normal')
        res_c = os.popen(command.get().strip()).read()
        cmd_result.delete('0.0', 'end')
        if res_c.strip('\n'):
            cmd_result.insert('end', res_c)
        else:
            cmd_result.insert('end', f'cmd命令 {command.get().strip()} 无返回结果或命令不正确！')
        cmd_result.configure(state='disabled')


def copy_pic():
    global img
    if isinstance(img, Image.Image):
        out = BytesIO()
        img.save(out, 'BMP')  # 将图片写入到流
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(win32clipboard.CF_DIB, out.getvalue()[14:])
        win32clipboard.CloseClipboard()
    else:
        messagebox.showerror(title='严重错误', message='程序内存中的图片格式不正确，无法复制到剪贴板！')


def paste_pic():
    global img, img_tk, action, temp
    img = ImageGrab.grabclipboard()
    temp = img
    if isinstance(img, Image.Image):
        img_tk = ImageTk.PhotoImage(img)
        pic.configure(scrollregion=(0, 0, *img.size))
        action and pic.delete(action)
        action = pic.create_image(img.size[0] / 2, img.size[1] / 2, image=img_tk)
    else:
        win32clipboard.OpenClipboard()
        text = win32clipboard.GetClipboardData(13)
        win32clipboard.CloseClipboard()
        if os.path.isfile(text):
            try:
                img = Image.open(text)
                temp = img
                img_tk = ImageTk.PhotoImage(img)
                pic.configure(scrollregion=(0, 0, *img.size))
                action and pic.delete(action)
                action = pic.create_image(img.size[0] / 2, img.size[1] / 2, image=img_tk)
            except UnidentifiedImageError:
                messagebox.showerror(title='严重错误', message=f'文件 {text} 不是标准的图片格式！')
        else:
            messagebox.showerror(title='严重错误', message='剪贴板内无图片！')


def save_pic():
    global img
    if isinstance(img, Image.Image):
        file_name = filedialog.asksaveasfilename() or 'save'
        if '.' not in file_name:
            img.save(f'{file_name}.png', 'png')
        else:
            img.save(file_name, file_name.split('.')[-1])
    else:
        messagebox.showerror(title='严重错误', message='程序内存中的图片格式不正确，无法保存！')


def read_pic():
    global img, img_tk, action, temp
    file_name = filedialog.askopenfilename()
    if file_name:
        try:
            img = Image.open(file_name)
            temp = img
            img_tk = ImageTk.PhotoImage(img)
            pic.configure(scrollregion=(0, 0, *img.size))
            action and pic.delete(action)
            action = pic.create_image(img.size[0] / 2, img.size[1] / 2, image=img_tk)
        except UnidentifiedImageError:
            messagebox.showerror(title='严重错误', message=f'文件 {file_name} 不是标准的图片格式！')


def pic_size(e):
    global img, img_tk, action, temp
    # 鼠标滚轮控制图片大小，基础 delta = 120
    if not temp:
        return False
    w = int(temp.size[0] * (1 + e.delta / 2400))
    h = int(temp.size[1] * (1 + e.delta / 2400))
    if w > 0 and h > 0 and isinstance(img, Image.Image):
        temp = img.resize((w, h), Image.ANTIALIAS)
        img_tk = ImageTk.PhotoImage(temp)
        pic.configure(scrollregion=(0, 0, *temp.size))
        action and pic.delete(action)
        action = pic.create_image(temp.size[0] / 2, temp.size[1] / 2, image=img_tk)


def pic_on_tap(event):
    global abs_x, abs_y, root_x, root_y  # , r_x, r_y
    abs_x, abs_y = x.get(), y.get()  # 滚动条原始位置
    root_x, root_y = event.x_root, event.y_root  # 鼠标点击绝对位置
    # r_x, r_y = event.x_root, event.y_root


def pic_on_move(event):
    global r_x, r_y
    if not temp:
        return False
    x_ = - (event.x_root - root_x) / temp.size[0]
    y_ = - (event.y_root - root_y) / temp.size[1]
    if abs_x[0] + x_ < 0:
        x_ = - abs_x[0]
    if abs_y[0] + y_ < 0:
        y_ = - abs_y[0]
    if abs_x[1] + x_ > 1:
        x_ = 1 - abs_x[1]
    if abs_y[1] + y_ > 1:
        y_ = 1 - abs_y[1]
    x.set(*(abs_x[0] + x_, abs_x[1] + x_))
    y.set(*(abs_y[0] + y_, abs_y[1] + y_))
    pic.xview('moveto', str(abs_x[0] + x_))
    pic.yview('moveto', str(abs_y[0] + y_))
    # pic.move(action, event.x_root - r_x, event.y_root - r_y)
    # r_x, r_y = event.x_root, event.y_root  # 鼠标点击绝对位置（动态刷新）


def on_tap(event):
    global abs_x, abs_y, root_x, root_y
    abs_x, abs_y = root.winfo_x(), root.winfo_y()  # 界面左上角绝对位置
    root_x, root_y = event.x_root, event.y_root  # 鼠标点击绝对位置


def on_move(event):
    root.geometry(f'+{abs_x + event.x_root - root_x}+{abs_y + event.y_root - root_y}')


def change_time(h: int, m: int, s: int):
    global t_t
    t_t = f"{len(str(h)) == 1 and '0' or ''}{str(h)}：{len(str(m)) == 1 and '0' or ''}{str(m)}：{len(str(s)) == 1 and '0' or ''}{str(s)}"
    t = t_t.replace('：', '')
    for i in range(6):
        change_num(6 - i, int(t[i]))


def change_num(place: int, num: int = 0):
    for c in zip(labels[6 - place], nums[num]):
        c[0].configure(background=colors[c[1]])


def start():
    global js, pas, now
    h = 0
    m = 0
    s = 0
    js = True
    pas = False
    now = time.time()
    las = int(now)
    start_button.configure(text='暂停计时', command=suspend)
    tag_button.configure(state='normal')
    stop_button.configure(state='normal')
    while js:
        while pas:
            las = int(time.time()) - s
            time.sleep(0.1)
        s = int(time.time() - las)
        if s == 60:
            m += 1
            s = 0
            if m == 60:
                h += 1
                m = 0
                if h == 24:
                    h = 0
            las = int(time.time())
        change_time(h, m, s)
        time.sleep(0.2)
    tag_button.configure(state='disable')
    stop_button.configure(state='disable')
    start_button.configure(text='开始计时', command=lambda: Thread(target=start, daemon=True).start())
    change_time(0, 0, 0)


def suspend():
    global pas
    pas = True
    start_button.configure(text='继续计时', command=cont)


def cont():
    global pas
    pas = False
    start_button.configure(text='暂停计时', command=suspend)


def tag():
    listbox.insert('end', t_t)
    timers.append(t_t)


def stop():
    global js, pas
    js = False
    pas = False


def delete_all():
    if messagebox.askyesno(title='询问', message='是否要删除全部标记？'):
        listbox.delete('0', 'end')


def restore():
    while 1:
        if GetAsyncKeyState(119):
            root.overrideredirect(0)
        time.sleep(1)


def add_file():
    file = filedialog.askopenfiles()
    if file:
        for _ in file:
            listbox_d.insert('end', _.name)
            ranges.append(_.name)


def delete_l():
    if listbox_d.curselection():
        ranges.remove(ranges[listbox_d.curselection()[0]])
        listbox_d.delete(listbox_d.curselection()[0])


def mkdir():
    if text_get.get():
        for n in ['\\', ':', '*', '?', '"', '<', '>', '|']:
            if n in text_get.get():
                messagebox.showerror(title='警告', message='文件夹不能含有以下任何字符：\\/:?"<>|仅保留/做分隔符')
                return False
        directory = filedialog.askdirectory()
        if directory:
            for d in text_get.get().split('/'):
                if not os.path.isdir(f'{directory}/{d}'):
                    os.mkdir(f'{directory}/{d}')
            messagebox.showinfo(title='完成', message='文件夹（组）创建完成！')


def clipboard():
    global cli
    cli = True
    clip.configure(text='\n'.join(list('停止剪贴板')), command=stop_clip)
    while cli:
        try:
            win32clipboard.OpenClipboard()
            try:
                text = win32clipboard.GetClipboardData(CF_UNICODETEXT)
                if text and text_get.get() and text_get.get() in text:
                    res.configure(foreground='green', text='\n'.join(list('检测结果：存在文本')))
                else:
                    res.configure(foreground='red', text='\n'.join(list('检测结果：文本不存在')))
            except TypeError:
                pass
            win32clipboard.CloseClipboard()
        except pywintypes:
            pass
        time.sleep(1)


def stop_clip():
    global cli
    cli = False
    clip.configure(text='\n'.join(list('剪贴板检测')), command=lambda: Thread(target=clipboard, daemon=True).start())
    res.configure(foreground='black', text='\n'.join(list('检测结果：')))


def search():
    for r in ranges:
        try:
            if text_get.get() and text_get.get() in open(r, 'r', encoding='utf-8').read():
                listbox_r.insert('end', r)
                search_r.append(r)
        except UnicodeDecodeError:
            if text_get.get() and text_get.get() in open(r, 'r', encoding='ansi').read():
                listbox_r.insert('end', r)
                search_r.append(r)
        except Exception:
            print(r)
            pass


def save_action():
    save_dict = {
        'NormalVar': {
            'ask': 'true' if ask else '',
            'ins': 'true' if ins else '',
            'text_get': text_get.get(),
            'notes': notes,
            'timers': timers,
            'ranges': ranges,
            'search_r': search_r
        },
        'TkVar': {
            'command': command.get(),
            'formula': formula.get(),
            'replace_before': replace_before.get(),
            'replace_after': replace_after.get(),
            'translate_text': translate_text.get(),
            'top': top.get(),
            'copy': copy.get(),
            'tou': tou.get(),
            'translate_choice': translate_choice.get()
        }
    }
    open(save.get(), 'w', encoding='utf-8').write(json.dumps(save_dict, ensure_ascii=False))


def empty_action():
    global img, img_tk, action, temp, ask, ins, notes, command, formula, replace_before, replace_after, translate_text, top, copy, tou, translate_choice, save, js, pas
    if messagebox.askyesno(title='清空确认', message='将删除现有所有状态 ，是否继续？'):
        result.configure(state='normal')
        result.delete('0.0', 'end')
        result.configure(state='disabled')
        scrolled_text.configure(state='normal')
        scrolled_text.delete('0.0', 'end')
        unfreeze()
        for i in notes:
            tree.delete(i)
        js = False
        pas = False
        stop()
        stop_clip()
        change_time(0, 0, 0)
        listbox.delete('0', 'end')
        text_get.delete('0', 'end')
        listbox_d.delete('0', 'end')
        listbox_r.delete('0', 'end')
        calc.configure(text='计算结果：')
        cmd_result.configure(state='normal')
        cmd_result.delete('0.0', 'end')
        cmd_result.configure(state='disabled')
        pic.configure(scrollregion=(0, 0, 1, 1))
        action and pic.delete(action)
        img = None  # 图片变量<class 'Image.Image'>
        img_tk = None  # 图片变量<class 'ImageTk.PhotoImage'>
        action = None  # 图片操作动作
        temp = None  # 临时图片（缩放后的）
        ask = True  # 询问是否在非管理员状态运行cmd命令
        ins = True  # notetip的文本框是否允许输入
        notes = {}  # notetip的文本目录内容映射
        command.set('')  # 用户输入的cmd命令
        formula.set('')  # 用户输入的算式
        replace_before.set('')  # 替换文本前
        replace_after.set('')  # 替换文本后
        translate_text.set('')  # 翻译的内容
        top.set(1)  # 是否窗口置顶
        copy.set(1)  # 翻译是否自动复制
        tou.set(1.0)  # 透明度设置
        translate_choice.set(0)  # 翻译的选择
        save.set(f'{__file__.split(".")[0]}.json')  # 文件保存位置


def load_file():
    if os.path.isfile(save.get()) and messagebox.askyesno(title='载入确认', message='载入将覆盖现有的所有数据，是否继续？'):
        try:
            load_dict = json.load(open(save.get(), 'r', encoding='utf-8'))
            globals()['ask'] = bool(load_dict['NormalVar']['ask'])
            globals()['ins'] = bool(load_dict['NormalVar']['ins'])
            text_get.delete('0', 'end')
            text_get.insert('end', load_dict['NormalVar']['text_get'])
            for i in notes:
                tree.delete(i)
            globals()['notes'] = load_dict['NormalVar']['notes']
            globals()['timers'] = load_dict['NormalVar']['timers']
            globals()['ranges'] = load_dict['NormalVar']['ranges']
            globals()['search_r'] = load_dict['NormalVar']['search_r']
            for k in load_dict['TkVar']:
                globals()[k].set(load_dict['TkVar'][k])
            for i in notes:
                tree.insert('', index='end', iid=i, tag=i, text=notes[i].replace('\n', '')[:15])
            for i in timers:
                listbox.insert('end', i)
            for i in ranges:
                listbox_d.insert('end', i)
            for i in search_r:
                listbox_r.insert('end', i)
        except json.decoder.JSONDecodeError:
            messagebox.showerror(title='严重错误', message='json文件格式错误！')


def empty_file():
    if os.path.isfile(save.get()) and messagebox.askyesno(title='清空确认', message=f'将删除现有保存的状态文件 {save.get()} ，是否继续？'):
        os.remove(save.get())


def close():
    if messagebox.askyesno(title='退出确认', message='请您确认是否已经保存当前状态，点否取消退出~'):
        # 安全退出
        root.quit()
        root.destroy()


# 根窗口、Tab标签和Frame空间区
root = Tk()
tabControl = Notebook(root)
translate = Frame(tabControl, borderwidth=2)
tabControl.add(translate, text='翻译')
note_tip = Frame(tabControl)
tabControl.add(note_tip, text='文本')
calculator = Frame(tabControl)
tabControl.add(calculator, text='计算')
picture = Frame(tabControl)
tabControl.add(picture, text='图片')
timer = Frame(tabControl)
tabControl.add(timer, text='计时')
find = Frame(tabControl)
tabControl.add(find, text='查找')
setting = Frame(tabControl)
tabControl.add(setting, text='设置【在我这行滚轮可以缩放界面哦~】')
tabControl.grid(column=0, row=0, sticky='WENS')  # 左、右、下 占据 2 上 占据 26
tabControl.select(6)  # 默认 tab 页设置，6 为设置页面


# 变量区
img = None  # 图片变量<class 'Image.Image'>
img_tk = None  # 图片变量<class 'ImageTk.PhotoImage'>
action = None  # 图片操作动作
temp = None  # 临时图片（缩放后的）
width = 576  # 程序窗口基础宽
height = 408  # 程序窗口基础高
ask = True  # 询问是否在非管理员状态运行cmd命令
ins = True  # notetip的文本框是否允许输入
notes = {}  # notetip的文本目录内容映射
timers = []  # timer的计时数据
command = StringVar()  # 用户输入的cmd命令
formula = StringVar()  # 用户输入的算式
replace_before = StringVar()  # 替换文本前
replace_after = StringVar()  # 替换文本后
translate_text = StringVar()  # 翻译的内容
top = IntVar(value=1)  # 是否窗口置顶
copy = IntVar(value=1)  # 翻译是否自动复制
tou = DoubleVar(value=1.0)  # 透明度设置
translate_choice = IntVar(value=0)  # 翻译的选择
translates = ['百度翻译', '腾讯翻译', '有道翻译']
r_x = 0  # 图片移动x临时变量
r_y = 0  # 图片移动y临时变量
js = False  # timer的结束状态
pas = False  # timer的暂停状态
t_t = ''  # timer的计时表示文本
labels = []  # timer的计时数字存储
now = time.time()  # 当前的时间戳
helps = ['双击隐藏程序标题栏', 'F8恢复程序标题栏']  # timer所有帮助
m = max(len(h) for h in helps)  # timer所有帮助中最长字符
helps = [h + (m - len(h)) * ' ' for h in helps]             # 0-9                   A-Z                   a-z
helps = '\n'.join([' '.join(z) for z in zip(*[[ord(l) in list(range(48, 58)) + list(range(65, 91)) + list(range(97, 123)) and l+' ' or l.replace(' ', '  ') for l in list(l)] for l in helps])])  # 获取竖排帮助
colors = {0: '#f0f0f0', 1: 'red'}  # timer计时器显示颜色
num0 = [1, 0, 1, 1, 1, 1, 1]
num1 = [0, 0, 0, 0, 1, 0, 1]
num2 = [1, 1, 1, 0, 1, 1, 0]
num3 = [1, 1, 1, 0, 1, 0, 1]
num4 = [0, 1, 0, 1, 1, 0, 1]
num5 = [1, 1, 1, 1, 0, 0, 1]
num6 = [1, 1, 1, 1, 0, 1, 1]
num7 = [1, 0, 0, 0, 1, 0, 1]
num8 = [1, 1, 1, 1, 1, 1, 1]
num9 = [1, 1, 1, 1, 1, 0, 1]
nums = [num0, num1, num2, num3, num4, num5, num6, num7, num8, num9]
frame_coordinates = [(45, 50), (105, 50), (195, 50), (255, 50), (345, 50), (405, 50)]  # timer中组件布局数据
label_coordinates = [(5, 0, 40, 5), (5, 45, 40, 5), (5, 90, 40, 5), (0, 5, 5, 40), (45, 5, 5, 40), (0, 50, 5, 40), (45, 50, 5, 40)]  # timer中计时区布局数据
frame_coordinates = [{'x': c[0], 'y': c[1]} for c in frame_coordinates]  # timer中组件布局
label_coordinates = [{'x': c[0], 'y': c[1], 'width': c[2], 'height': c[3]} for c in label_coordinates]  # timer中计时区布局
ranges = []  # 文本查找保存
search_r = []  # 查找结果保存
cli = False  # 剪贴板激活状态
save = StringVar(value=f'{__file__.split(".")[0]}.json')  # 文件保存位置


# 翻译区 translate
translate_input = Entry(translate, textvariable=translate_text)
translate_input.grid(column=0, row=0, sticky='WE', columnspan=3)
Button(translate, width=10, text='中英互译', command=tran).grid(column=3, row=0, sticky='NS', rowspan=2)
for t in range(len(translates)):
    Radiobutton(translate, text=translates[t], variable=translate_choice, value=t, command=try_tran).grid(column=t, row=1, sticky='WENS')
translate_result = LabelFrame(translate, text='翻译结果【自动全部复制 / 双击全部复制】')
translate_result.grid(column=0, row=2, sticky='WENS', columnspan=4)
result = Text(translate_result, wrap='word')
result.configure(state='disabled')
result.grid(column=0, row=0, sticky='WENS')
# 一次性控制各控件之间的距离
for child in translate.winfo_children():
    child.grid_configure(padx=2, pady=1)
result.configure(padx=10, pady=10)


# 文本区 note_tip
scrolled_text = scrolledtext.ScrolledText(note_tip)
scrolled_text.grid(column=0, row=0, sticky='WENS', rowspan=4)
button = Button(note_tip, text='冻结输入', command=freeze)
button.grid(column=1, row=0, sticky='W', padx=10, pady=10)
Button(note_tip, text='临时存储', command=insert).grid(column=1, row=1, sticky='W', padx=10, pady=10)
Button(note_tip, text='json格式化', command=format_json).grid(column=1, row=2, sticky='W', padx=10, pady=10)
replace = LabelFrame(note_tip, text='替换文本')
replace.grid(column=2, row=0, sticky='WENS', rowspan=3)
Entry(replace, textvariable=replace_before).grid(column=2, row=0, sticky='WENS', padx=10, pady=10)
Button(replace, text='替换文本', command=replace_text).grid(column=2, row=2)
Entry(replace, textvariable=replace_after).grid(column=2, row=4, sticky='WENS', padx=10, pady=10)
label_t = LabelFrame(note_tip, text='左键选择，右键删除')
label_t.grid(column=1, row=3, sticky='WENS', columnspan=2)
tree = Treeview(label_t, show='tree')
tree.grid(column=0, row=0, sticky='WENS')


# 计算区 calculator
calc = LabelFrame(calculator, text='计算结果：')
calc.grid(column=0, row=0, sticky='WE', columnspan=2)
inp_for = Entry(calc, textvariable=formula)
inp_for.grid(column=0, row=0, sticky='WE', padx=10)
Button(calc, text='计算', command=calc_formula).grid(column=1, row=0, padx=10)
com = LabelFrame(calculator, text='执行cmd命令')
com.grid(column=0, row=1, sticky='WENS')
inp_com = Entry(com, textvariable=command)
inp_com.grid(column=0, row=0, sticky='WE', padx=10)
Button(com, text='执行', command=lambda: Thread(target=cmd, daemon=True).start()).grid(column=1, row=0, padx=10)
cmd_result = scrolledtext.ScrolledText(com)
cmd_result.grid(column=0, row=1, sticky='WENS', padx=10, pady=10, columnspan=2)
cmd_result.configure(state='disabled')


# 图片区 picture
pic = Canvas(picture)
pic.grid(column=0, row=0, sticky='WENS', columnspan=4)
x = scrolledtext.Scrollbar(picture, orient='horizontal', command=pic.xview)
x.grid(column=0, row=1, sticky='WE', columnspan=4)
y = scrolledtext.Scrollbar(picture, orient='vertical', command=pic.yview)
y.grid(column=4, row=0, sticky='NS')
pic.configure(xscrollcommand=x.set, yscrollcommand=y.set)
Button(picture, text='复制图片', command=copy_pic).grid(column=0, row=2)
Button(picture, text='粘贴图片', command=paste_pic).grid(column=1, row=2)
Button(picture, text='保存图片', command=save_pic).grid(column=2, row=2)
Button(picture, text='读取图片', command=read_pic).grid(column=3, row=2)


# 计时区 timer
Label(timer, font=('黑体', 20), text='小时       分钟      秒钟').place(x=70, y=0, width=360, height=50)
for f in frame_coordinates:
    num_frame = Frame(timer)
    num_frame.place(**f, width=50, height=95)
    label_temp = []
    for l in label_coordinates:
        label = Label(num_frame)
        label.place(**l)
        label_temp.append(label)
    labels.append(label_temp)
change_time(0, 0, 0)
listbox = Listbox(timer, font=('黑体', 24))
listbox.place(x=40, y=165, width=180, height=200)
start_button = Button(timer, text='开始计时', font=('黑体', 12), command=lambda: Thread(target=start, daemon=True).start())
start_button.place(x=240, y=175, width=80, height=30)
tag_button = Button(timer, text='时间标记', font=('黑体', 12), command=tag, state='disable')
tag_button.place(x=240, y=225, width=80, height=30)
stop_button = Button(timer, text='结束计时', font=('黑体', 12), command=stop, state='disable')
stop_button.place(x=240, y=275, width=80, height=30)
Button(timer, text='清除标记', font=('黑体', 12), command=delete_all).place(x=240, y=325, width=80, height=30)
tip = LabelFrame(timer, text='程序说明')
tip.place(x=340, y=165, width=120, height=200)
Label(tip, font=('黑体', 14), text=helps).pack()


# 查找区 find
Label(find, text='请输入要查找的单词：').grid(column=0, row=0, padx=10, pady=5, columnspan=2)
text_get = Entry(find)
text_get.grid(column=2, row=0, sticky='WE', columnspan=2)
Button(find, text='添加文件', command=add_file).grid(column=0, row=1, padx=5, pady=5)
Button(find, text='搜索文本', command=lambda: Thread(target=search, daemon=True).start()).grid(column=1, row=1, padx=5, pady=5)
Button(find, text='删除选定选项', command=delete_l).grid(column=0, row=2, padx=5, pady=5, columnspan=2)
Button(find, text='用/分割文本以创建文件夹组', command=mkdir).grid(column=0, row=3, padx=5, pady=5, columnspan=2)
listbox_d = Listbox(find, font=('黑体', 12))
listbox_d.grid(column=0, row=4, sticky='WENS', padx=10, pady=5, columnspan=2)
Label(find, text='查询结果：（剪贴板单独结果）').grid(column=2, row=1, padx=10, pady=5)
listbox_r = Listbox(find, font=('黑体', 12))
listbox_r.grid(column=2, row=2, sticky='WENS', padx=10, pady=5, rowspan=3)
clip = Button(find, text='\n'.join(list('剪贴板检测')), command=lambda: Thread(target=clipboard, daemon=True).start())
clip.grid(column=3, row=1, padx=10, pady=5, rowspan=3)
res = Label(find, text='\n'.join(list('检测结果：')))
res.grid(column=3, row=3, padx=10, pady=5, rowspan=2)


# 设置区 setting
Checkbutton(setting, text='窗口置顶', offvalue=0, onvalue=1, variable=top, command=lambda: root.attributes('-topmost', top.get())).grid(column=0, row=0)
Checkbutton(setting, text='翻译自动复制', offvalue=0, onvalue=1, variable=copy).grid(column=0, row=1)
tmd = LabelFrame(setting, text='透明度设置')
tmd.grid(column=1, row=0, sticky='WE', rowspan=3, columnspan=3)
t_m_d = Scale(tmd, from_=0.30, to=1.00, orient='horizontal', length=200, variable=tou, showvalue=1, tickinterval=0.1, resolution=0.01, command=lambda _: root.attributes('-alpha', tou.get()))
t_m_d.grid(column=0, row=0, sticky='WE')
t_m_d.set(1.00)
Button(setting, text='文件保存设置', command=lambda: save.set(filedialog.asksaveasfilename(filetypes=[('*.json', 'json')]))).grid(column=0, row=2)
path = LabelFrame(setting, text='文件路径')
path.grid(column=0, row=3, sticky='WE', columnspan=4, pady=10)
Label(path, textvariable=save, anchor='center', foreground='#f00').grid(column=0, row=0, sticky='WE')
Button(setting, text='保存当前状态', command=save_action).grid(column=0, row=4)
Button(setting, text='清空当前状态', command=empty_action).grid(column=1, row=4)
Button(setting, text='载入已保存的状态', command=load_file).grid(column=2, row=4)
Button(setting, text='清空已保存的状态', command=empty_file).grid(column=3, row=4)
explain = LabelFrame(setting, text='软件说明')
explain.grid(column=0, row=5, sticky='WENS', columnspan=4)
Label(explain, text="""总体功能描述：\n
    三种翻译方式（百度、有道、腾讯）\n
    置顶文本编辑器（锁定、解锁、临时保存）\n
    算式计算器（通过eval计算，确定算式提示错误；执行cmd）\n
    显示剪贴板或文件的图片（创建、销毁、保存、读取，比例缩放图片）\n
    计时器（开始计时、暂停计时、时间标记、结束计时、清除标记、独特数显）\n
    文本查找工具（批量查找可直接打开文本文件，剪贴板，看文本在哪些文件内）\n
""", anchor='center', font=('黑体', 10, 'bold', 'italic')).grid(column=0, row=0, sticky='WENS')


# 绑定区
tabControl.bind("<MouseWheel>", zoom)
tree.bind('<ButtonRelease-1>', click)
tree.bind('<ButtonRelease-3>', delete)
root.protocol("WM_DELETE_WINDOW", close)
result.bind('<Double-1>', copy_text)
inp_for.bind('<KeyPress-Return>', calc_formula)
inp_com.bind('<KeyPress-Return>', lambda _: Thread(target=cmd, daemon=True).start())
translate_input.bind('<KeyPress-Return>', lambda _: Thread(target=tran, daemon=True).start())
result.bind('<KeyPress-Return>', lambda _: Thread(target=tran, daemon=True).start())
pic.bind("<MouseWheel>", pic_size)
pic.bind("<Button-1>", pic_on_tap)
pic.bind('<B1-Motion>', pic_on_move)
timer.bind("<Button-1>", on_tap)
timer.bind('<B1-Motion>', on_move)
timer.bind("<Double-Button-1>", lambda e: root.overrideredirect(1))
Thread(target=restore, daemon=True).start()


# 大小自动调整区
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
translate.rowconfigure(2, weight=1)
for col in range(4):
    translate.columnconfigure(col, weight=1)
translate_result.rowconfigure(0, weight=1)
translate_result.columnconfigure(0, weight=1)
note_tip.rowconfigure(3, weight=1)
note_tip.columnconfigure(0, weight=1)
replace.rowconfigure(1, weight=1)
replace.rowconfigure(3, weight=1)
replace.columnconfigure(0, weight=1)
label_t.rowconfigure(0, weight=1)
label_t.columnconfigure(0, weight=1)
calculator.rowconfigure(1, weight=1)
calculator.columnconfigure(0, weight=1)
calc.columnconfigure(0, weight=1)
com.rowconfigure(1, weight=1)
com.columnconfigure(0, weight=1)
picture.rowconfigure(0, weight=1)
for col in range(4):
    picture.columnconfigure(col, weight=1)
find.columnconfigure(0, weight=3)
find.columnconfigure(1, weight=3)
find.columnconfigure(2, weight=10)
find.rowconfigure(4, weight=1)
setting.rowconfigure(5, weight=1)
for col in range(4):
    setting.columnconfigure(col, weight=1)
explain.rowconfigure(0, weight=1)
explain.columnconfigure(0, weight=1)
tmd.columnconfigure(0, weight=1)
path.columnconfigure(0, weight=1)


# 主界面函数
root.title('万能工具箱')
root.minsize(width, height)
root.resizable(True, True)
root.attributes('-topmost', top.get())
root.geometry(f'{width}x{height}+{int((root.winfo_screenwidth()-width-16)/2)}+{int((root.winfo_screenheight()-height-32)/2)}')
root.mainloop()
