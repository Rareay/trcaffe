TOOL=./cpp_test_model/build/use_model

## deploy_xx.prototxt
DEPLOY_PROTO=model_resnet_imagenet/resnet_50/resnet_50_deploy.prototxt

## 权重  .caffemodel
CAFFEMODEL=model_resnet_imagenet/resnet_50/resnet_50_solver_iter_60000_home.caffemodel

## 均值  .binaryproto
MODEL_MEAN=mean.binaryproto

## 标签映射表 .txt
LABEL=labels/labels.txt

## 文件或目录
IMAGE=caffe/data/raw-img/test/elefante

if [ ! -f ${LABEL} ]; then
    touch ${LABEL}
fi

if [ ! -e ${TOOL} ]; then
    cd cpp_test_model
    rm build -rf
    mkdir build
    cd build
    cmake ..
    make
    cd ../..
fi

${TOOL} \
    ${DEPLOY_PROTO} \
    ${CAFFEMODEL} \
    ${MODEL_MEAN} \
    ${LABEL} \
    ${IMAGE}
