#!/usr/bin/env sh
TOOL=caffe/build/tools/caffe

## solver_xx.prototxt
SOLVER_PROTO=model_resnet_imagenet/resnet_50/resnet_50_solver.prototxt

## 权重  .caffemodel
CAFFEMODEL=model_resnet_imagenet/resnet_50/resnet_50_solver_iter_60000_home.caffemodel

${TOOL} train \
    -solver ${SOLVER_PROTO} \
    -weights ${CAFFEMODEL} \
    -gpu 0 \
    2>&1 |  tee ./_test_value.log

