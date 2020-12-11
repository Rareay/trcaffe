#!/usr/bin/env sh
TOOL=caffe/build/tools/caffe

## train_xx.prototxt
SOLVER_PROTO=model_resnet/ResNet_50_train_val.prototxt

## 权重 .caffemodel
CAFFEMODEL=model_resnet/solver_iter_2000.caffemodel


${TOOL} test \
    -model ${SOLVER_PROTO}\
    -weights ${CAFFEMODEL} \
    -gpu 0 \
    -iterations 1642
