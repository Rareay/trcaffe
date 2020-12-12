python caffe-int8-convert-tools/caffe-int8-convert-tool-dev-weight.py \
    --proto=model_resnet/ResNet_50_train_val.prototxt \
    --model=model_resnet/solver_iter_16000.caffemodel \
    --mean 127.5 127.5 127.5 \
    --norm=0.00777 \
    --images=caffe-int8-convert-tools/test/images/ \
    --output=caffe-int8-convert-tools/test/resnet50.table \
    --gpu=1
