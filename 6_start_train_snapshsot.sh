#!/usr/bin/env sh
TOOL=caffe/build/tools/caffe

## solver_xx.prototxt
SOLVER_PROTO=model_resnet_imagenet/resnet_50/resnet_50_solver.prototxt

## 快照  .solverstate
SOLVERSTATE=model_resnet_imagenet/resnet_50/resnet_50_solver_iter_110000_0.99.solverstate

${TOOL} train \
    -solver ${SOLVER_PROTO} \
    -snapshot ${SOLVERSTATE} \
    -gpu 0 \
    2>&1 |  tee ./_test_value.log
