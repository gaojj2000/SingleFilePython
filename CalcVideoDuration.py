# _*_ coding:utf-8 _*_
# FileName: CalcVideoDuration.py
# IDE: PyCharm

import os
from moviepy.editor import VideoFileClip

files = []
suffixs = ['mp4', 'mkv']


def get_file(path: str, deep: (str, int)):
    """
    获取文件目录树
    :param path: 文件目录
    :param deep: 文件目录深度【*或1~】
    """
    if deep and os.path.isdir(path):
        if isinstance(deep, int):
            d = os.listdir(path)
            if d:
                for f in d:
                    if os.path.isfile(f'{path}\\{f}'):
                        if f.split('.')[-1] in suffixs:
                            files.append(f'{path}\\{f}')
                    else:
                        get_file(f'{path}\\{f}', deep - 1)
        elif deep == '*':
            for d in os.walk(path):
                if d[2]:
                    for f in d[2]:
                        if f.split('.')[-1] in suffixs:
                            files.append(f'{d[0]}\\{f}')


def get_time(path: str, deep: (int, str)):
    """
    获取文件目录树
    :param path: 文件目录
    :param deep: 文件目录深度【*或1~】
    :returns 视频时长【s和h-m-s】
    """
    if os.path.isdir(path):
        print('\n正在获取文件列表')
        get_file(path, deep)
        all_time = 0  # 秒
        if files:
            for f in files:
                print(f'正在获取视频{f}的视频时长...')
                all_time += int(VideoFileClip(f).duration + 0.5)
        s = int(all_time % 60)
        m = int(all_time / 60 % 60)
        h = int(all_time / 3600)
        return all_time, f'{h}时{m}分{s}秒'


mm = get_time('F:\\桌面\\视频1', 1)
lz = get_time('F:\\桌面\\视频2', 1)
jsj = get_time('F:\\桌面\\视频3', '*')
print('\n视频时间总长差异：')
print(f'视频1总时长：{mm[0]}秒，视频2总时长：{lz[0]}秒')
print(f'视频1总时长：{mm[1]}，视频2总时长：{lz[1]}')
print(f'\n视频3时间总长：{jsj[0]}秒，{jsj[1]}')

