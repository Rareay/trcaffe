#!/usr/bin/env sh
TOOL=caffe/build/tools/compute_image_mean

${TOOL} ./img_train_lmdb \
    ./mean.binaryproto

