#!/usr/bin/python
# -*- coding:utf8 -*-
# test env: python2.7
import numpy as np
import pandas as pd
import matplotlib

# set backend to avoid runtime error
# https://stackoverflow.com/questions/34977388/matplotlib-runtimeerror-python-is-not-installed-as-a-framework
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
import argparse


def main(file_position='data.csv', result_index=0):
    csv_file = pd.read_csv(file_position)

    # 数据组数，不计入时间
    data_group_counts = len(csv_file.columns) - 1

    # 没有数据
    if data_group_counts <= 0:
        raise RuntimeError('Not enough data or csv file is not right')

    # 获取时间数据
    # time_data = csv_file.iloc[:, 0].values

    group_data = []  # 数据组
    group_result_abs = []  # 分解向量模
    group_result_deg = []  # 分解向量度数

    # 读取数据
    for i in range(0, data_group_counts):
        column_index = i + 1
        data = csv_file.iloc[:, column_index].values
        group_data.append(data)

    # FFT 分解
    for data in group_data:
        # 分解向量
        fft_result = np.fft.fft(data)
        # 分解向量模
        # https://blog.csdn.net/lee008108/article/details/78906086
        fft_result_abs = [2 * abs(item) / int(len(data)) for item in fft_result]
        fft_result_abs[0] = fft_result_abs[0] / 2
        fft_result_abs[len(fft_result_abs) - 1] = fft_result_abs[len(fft_result_abs) - 1] / 2
        # 分解向量角度
        fft_result_deg = [np.angle(item, deg=True) for item in fft_result]

        group_result_abs.append(fft_result_abs)
        group_result_deg.append(fft_result_deg)

    abs_result_list = []
    deg_result_list = []
    for result in zip(group_result_abs, group_result_deg):
        _abs, _deg = result
        abs_result_list.append(_abs[result_index - 1])
        deg_result_list.append(_deg[result_index - 1])

    print('abs: ' + str(abs_result_list))
    print('deg: ' + str(deg_result_list))

    # 绘图
    x = range(0, len(abs_result_list))
    plt.title('abs')
    plt.scatter(x, abs_result_list)
    plt.draw()  # 显示绘图
    plt.savefig("abs.png", format='png')  # 保存图象
    plt.close()  # 关闭图表

    plt.title('deg')
    plt.scatter(x, deg_result_list)
    plt.draw()  # 显示绘图
    plt.savefig("deg.png", format='png')  # 保存图象
    plt.close()  # 关闭图表


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process FFT calculation from csv file.')
    parser.add_argument('-i', metavar='INDEX', type=int, help='FFT result index')
    parser.add_argument('-f', metavar='FILE', help='csv file position')

    args = parser.parse_args()
    if args.i and args.f:
        main(args.f, args.i)
    else:
        raise RuntimeError('Not enough params!')
