./ncnn/build/tools/caffe/caffe2ncnn \
    model_resnet/ResNet_50_train_val.prototxt \
    model_resnet/solver_iter_16000.caffemodel \
    caffe-int8-convert-tools/test/resnet50-int8.param \
    caffe-int8-convert-tools/test/resnet50.bin \
    256 \
    caffe-int8-convert-tools/test/resnet50.table \
