#coding:utf-8

import re
import time
import numpy as np
import os
from pyecharts import options as opts
from pyecharts.charts import Bar, Line, Tab, Grid


def get_key_value(line_type, line):
    """
    从一行中提取键值
    :param line_type: 类型，如 "Test net output "
    :param line: 行数据
    """
    match = re.search(line_type, line)
    if match == None:
        return False, "", 0.
    line = line.split(line_type, 2)[1]
    line = line.split(" ")
    key = line[1]
    value = float(line[3])
    return True, key, value

def get_iteration(line):
    """
    获取 Iteration 值
    """
    key = "Iteration "
    match = re.search(key, line)
    if match != None:
        line = line.split(key, 2)[1]
        line = line.split(",")[0]
        if line.isdigit():
            return True, line
    return False, ""

def read_log(log_path, line_type):
    Keys = []
    Valus = []
    Datas = []
    Iter = ""
    state_front = False
    state_cur = False
    first_cycle = True
    file = open(log_path)
    for line in file:
        state, iteration = get_iteration(line)
        if state == True:
            Iter = iteration
        state, key, value = get_key_value(line_type, line)
        state_front = state_cur
        state_cur = state
        if state_cur == True:
            if first_cycle == True:
                Keys.append(key)
                Valus.append(value)
            else:
                index = 0
                for k in Keys:
                    if k == key:
                        Valus[index] = value
                    index = index + 1
        elif state_front == True:
            if first_cycle == True:
                first_cycle = False
                for i in range(len(Valus) + 1):
                    Datas.append([])
            Datas[0].append(Iter)
            for i in range(len(Valus)):
                Datas[i + 1].append(Valus[i])
    file.close()
    return Keys, Datas


def read_file(file_path):
    file = open(file_path)
    data = [[],[],[]]
    for line in file:
        d = line.split("\n", 1)[0]
        d = d.split(" ", 3)
        if len(d) >= 3:
            data[0].append(int(d[0]))
            data[1].append(float(d[1]))
            data[2].append(float(d[2]))
    file.close()
    return data


def line_accurate(data) -> Line:
    c = (
	Line(
            init_opts=opts.InitOpts(
            js_host="./",
            )
        )
        .add_xaxis(data[0])
        .add_yaxis("Accuracy", data[1])
        #.set_global_opts(title_opts=opts.TitleOpts(title="Accurate"))
	.set_global_opts(
	    xaxis_opts=opts.AxisOpts(is_scale=True),
	    yaxis_opts=opts.AxisOpts(
	        is_scale=True,
		splitarea_opts=opts.SplitAreaOpts(
		    is_show=True, areastyle_opts=opts.AreaStyleOpts(opacity=1)
		),
	    ),
	    #datazoom_opts=[opts.DataZoomOpts(pos_bottom="-2%")],
	    datazoom_opts=[opts.DataZoomOpts(type_="inside",
                                             range_start=0,
                                             range_end=100,
                                             )],
	    title_opts=opts.TitleOpts(title="Accuracy"),
	)
    )
    return c

def get_Line(name, x_data, y_data) -> Line:
    c = (
	Line(
            init_opts=opts.InitOpts(
            js_host="./",
            )
        )
        .add_xaxis(x_data)
        .add_yaxis(name, y_data)
        .set_global_opts(
	    xaxis_opts=opts.AxisOpts(is_scale=True),
	    yaxis_opts=opts.AxisOpts(
	        is_scale=True,
		splitarea_opts=opts.SplitAreaOpts(
		    is_show=True, areastyle_opts=opts.AreaStyleOpts(opacity=1)
		),
	    ),
	    #datazoom_opts=[opts.DataZoomOpts(pos_bottom="-2%")],
	    datazoom_opts=[opts.DataZoomOpts(type_="inside",
                                             range_start=0,
                                             range_end=100,
                                             )],
	    title_opts=opts.TitleOpts(title=name),
	)
    )
    return c


def tab_add_html(tab, keys, datas, type):
    index = 1
    for key in keys:
        tab.add(get_Line(key, datas[0], datas[index]), type + key)
        index = index + 1



if __name__ == "__main__":
    view = False
    while True:
        tab = Tab(js_host="./")

        keys, datas = read_log("_test_value.log", "Test net output ")
        tab_add_html(tab, keys, datas, "test-")

        keys, datas = read_log("_test_value.log", "Train net output ")
        tab_add_html(tab, keys, datas, "train-")

        tab.render("_test_value.html")

        print("update..")
        if view == False:
            view = True
            os.system("see _test_value.html &")
        time.sleep(10)

