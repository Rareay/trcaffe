#!/usr/bin/env sh
TOOL=caffe/build/tools/caffe

## solver_xx.prototxt
SOLVER_PROTO=model_tlc/solver.prototxt

${TOOL} train \
    -solver  ${SOLVER_PROTO}\
    --gpu 7
    2>&1 |  tee ./_test_value.log

#${TOOL} train \
#    -solver  ${SOLVER_PROTO}\
#    -gpu 0 \
#    2>&1 |  tee ./_test_value.log
