
MODE_PATH=int8_mode/mode

# .prototxt 的路径
#PROTOTXT_PATH=model_resnet/ResNet_50_train_val.prototxt
PROTOTXT_PATH=model_resnet/ResNet_18_deploy.prototxt


# .caffemodel 的路径
CAFFEMODE_PATH=model_resnet/solver_iter_3000.caffemodel

# .param 存放路径
PARAM_PATH=${MODE_PATH}/net-int8.param


# .bin 存放路径
BIN_PATH=${MODE_PATH}/net-int8.bin


# .table 的路径
TABLE_PATH=${MODE_PATH}/net-int8.table

./ncnn/build/tools/caffe/caffe2ncnn \
    ${PROTOTXT_PATH} \
    ${CAFFEMODE_PATH} \
    ${PARAM_PATH} \
    ${BIN_PATH} \
    256 \
    ${TABLE_PATH}

