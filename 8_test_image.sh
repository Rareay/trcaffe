#TOOL=./cpp_test_model/build/use_model
TOOL=./caffe/build/examples/cpp_classification/classification.bin

## deploy_xx.prototxt
DEPLOY_PROTO=model_tlc/tlc.prototxt

## 权重  .caffemodel
CAFFEMODEL=model_tlc/tlc.caffemodel

## 均值  .binaryproto
MODEL_MEAN=mean.binaryproto

## 标签映射表 .txt
LABEL=labels/labels.txt

## 文件或目录
IMAGE=data/tlc/train/0

if [ ! -f ${LABEL} ]; then
    touch ${LABEL}
fi

#if [ ! -e ${TOOL} ]; then
#    cd cpp_test_model
#    rm build -rf
#    mkdir build
#    cd build
#    cmake ..
#    make
#    cd ../..
#fi

${TOOL} \
    ${DEPLOY_PROTO} \
    ${CAFFEMODEL} \
    ${MODEL_MEAN} \
    ${LABEL} \
    ${IMAGE}

