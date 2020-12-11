#!/usr/bin/env sh
TOOL=caffe/build/tools/caffe

## solver_xx.prototxt
#SOLVER_PROTO=model_resnet_imagenet/resnet_50/resnet_50_solver.prototxt
SOLVER_PROTO=model_test/solver_test.prototxt

${TOOL} train \
    -solver  ${SOLVER_PROTO}\
    2>&1 |  tee ./_test_value.log

#${TOOL} train \
#    -solver  ${SOLVER_PROTO}\
#    -gpu 0 \
#    2>&1 |  tee ./_test_value.log
