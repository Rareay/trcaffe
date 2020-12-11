# -*- coding: utf-8 -*-

import numpy as np
from pyecharts import options as opts
from pyecharts.charts import Scatter
from pyecharts.charts import Line, Tab
import math


class LearningRate():
    min_learning_rate = 0.00000001
    lr_policy = "none"
    __base_lr = 0.1
    __gamma = 0.1
    __stepsize = 100
    __power = 0.1
    __max_iter = 10000
    __index = []
    __datas = []

    def __init__(self, learn_rate):
        self.__base_lr = learn_rate['base_lr']
        self.lr_policy = learn_rate['lr_policy']
        self.__gamma = learn_rate['gamma']
        self.__stepsize = learn_rate['stepsize']
        self.__power = learn_rate['power']
        self.__max_iter = learn_rate['max_iter']
        return
    
    def generate_data(self):
        iter = 0
        while True:
            if self.lr_policy == 'step':
                rate = self.math_step(iter)
            elif self.lr_policy == 'exp':
                rate = self.math_exp(iter)
            elif self.lr_policy == 'inv':
                rate = self.math_inv(iter)
            elif self.lr_policy == 'poly':
                rate = self.math_poly(iter)
            elif self.lr_policy == 'sigmoid':
                rate = self.math_sigmoid(iter)
            iter = iter + 1
            if iter > self.__max_iter or rate < self.min_learning_rate:
                break
            self.__index.append(str(iter))
            self.__datas.append(rate)
        return self.__index, self.__datas

    def math_step(self, iter):
        t = (math.floor(iter / self.__stepsize))
        return self.__base_lr * self.__gamma ** t
    
    def math_exp(self, iter):
        return self.__base_lr * self.__gamma ** iter

    def math_inv(self, iter):
        return self.__base_lr * (1 + self.__gamma * iter) ** (-self.__power)
        
    def math_poly(self, iter):
        return self.__base_lr * (1 - iter / self.__max_iter) ** self.__power
        
    def math_sigmoid(self, iter):
        return self.__base_lr * (1 / (1 + math.exp(-self.__gamma * (iter - self.__stepsize))))

def Line_html(index, data, title, save_path):
    (
	Line(
            init_opts=opts.InitOpts(
            js_host="./",
            )
        )
        .add_xaxis(index)
        .add_yaxis(
            series_name="learning rate",
            y_axis=data,
            symbol="emptyCircle",
            is_symbol_show=True,
            label_opts=opts.LabelOpts(is_show=False),
            )
        .set_global_opts(
	    xaxis_opts=opts.AxisOpts(is_scale=True),
	    yaxis_opts=opts.AxisOpts(
	        is_scale=True,
            splitarea_opts=opts.SplitAreaOpts(
                is_show=True, areastyle_opts=opts.AreaStyleOpts(opacity=1)
            ),
	    ),
	    datazoom_opts=[opts.DataZoomOpts(type_="inside",
                                             range_start=0,
                                             range_end=100,
                                             )],
	    title_opts=opts.TitleOpts(title=title),
        )
        .render(save_path)
    )

'''
step       <== base_lr | gamma | stepsize
exp        <== base_lr | gamma
inv        <== base_lr | gamma | power
poly       <== base_lr | max_iter | power
sigmoid    <== base_lr | gamma | stepsize
'''
LEARN_RATE = {
                "base_lr": 0.01,
                "lr_policy": "step",
                "gamma": 0.9,
                "stepsize": 5000,
                "power": 1.5,
                "max_iter": 100000
              }

if __name__ == "__main__":
    learn = LearningRate(LEARN_RATE)
    learn.min_learning_rate = 0.000001 # 学习率小于它则停止绘制
    index, data = learn.generate_data()
    Line_html(index, data, learn.lr_policy, "_learning_rate.html")
    print("see _learning_rate.html")







