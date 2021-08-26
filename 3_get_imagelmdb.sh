#!/usr/bin/env sh
TOOL=caffe/build/tools/convert_imageset
IMG_W=64
IMG_H=64

echo "Create train lmdb.."

rm -rf ./img_train_lmdb
${TOOL} --shuffle \
    --resize_height=${IMG_H} --resize_width=${IMG_W} \
    --shuffle=true \
    ./ ./imagelist/train.txt  ./img_train_lmdb

echo "Create test lmdb.."

rm -rf ./img_test_lmdb
${TOOL} --shuffle \
    --resize_height=${IMG_H} --resize_width=${IMG_W} \
    --shuffle=true \
    ./ ./imagelist/test.txt  ./img_test_lmdb

echo "done."

