#!/usr/bin/env sh
TOOL=caffe/build/tools/caffe

## solver_xx.prototxt
SOLVER_PROTO=model_resnet/solver.prototxt

## 权重  .caffemodel
CAFFEMODEL=model_resnet/ResNet-50-model.caffemodel

${TOOL} train \
    -solver ${SOLVER_PROTO} \
    -weights ${CAFFEMODEL} \
    -gpu 0 \
    2>&1 |  tee ./_test_value.log

