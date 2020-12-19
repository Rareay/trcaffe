
MODE_PATH=int8_mode/mode
if [ ! -e ${MODE_PATH} ]; then
    mkdir ${MODE_PATH}
fi

# .prototxt 的路径
#PROTOTXT_PATH=model_resnet/ResNet_50_train_val.prototxt
PROTOTXT_PATH=model_resnet/ResNet_18_deploy.prototxt

# .caffemodel 的路径
CAFFEMODE_PATH=model_resnet/solver_iter_3000.caffemodel

# 图像均值
MEAN1=127.5
MEAN2=127.5
MEAN3=127.5

# norm
NORM=0.00777

# 量化所需图像（如果有才量化）
IMAGE_PATH=int8_mode/images

# .table 文件存放位置
TABLE_PATH=${MODE_PATH}/net-int8.table


if [ ! -e ${IMAGE_PATH} ]; then
    echo "Donot have images for int8!"
    echo "Do: "
    echo ""
    echo "  mkdir ${IMAGE_PATH}"
    echo ""
    echo "And copy some images into it."
else
    python caffe-int8-convert-tools/caffe-int8-convert-tool-dev-weight.py \
        --proto=${PROTOTXT_PATH} \
        --model=${CAFFEMODE_PATH} \
        --mean ${MEAN1} ${MEAN2} ${MEAN3} \
        --norm=${NORM} \
        --images=${IMAGE_PATH} \
        --output=${TABLE_PATH} \
        --gpu=1

    echo ""
    echo "done!"
fi
