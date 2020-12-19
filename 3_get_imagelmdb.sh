#!/usr/bin/env sh
TOOL=caffe/build/tools/convert_imageset

echo "Create train lmdb.."

rm -rf ./img_train_lmdb
${TOOL} --shuffle \
    --resize_height=224 --resize_width=224 \
    --shuffle=true \
    ./ ./imagelist/train.txt  ./img_train_lmdb

echo "Create test lmdb.."

rm -rf ./img_test_lmdb
${TOOL} --shuffle \
    --resize_height=224 --resize_width=224 \
    --shuffle=true \
    ./ ./imagelist/test.txt  ./img_test_lmdb

echo "done."

