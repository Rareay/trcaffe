TOOL=./cpp_pretreamtment/build/pretreamtment

## 原图像路径（使用相对路径）
ORI_IMAGE_PATH=./data/raw-img/train

## 扩充图的路径
NEW_IMAGE_PATH=${ORI_IMAGE_PATH}/new

## 配置文件，若没有，会自动创建，自行修改里面的内容
CONFIG_PATH=${ORI_IMAGE_PATH}/../parameter.yaml

rm ${NEW_IMAGE_PATH} -rf

if [ ! -e ${TOOL} ]; then
    cd cpp_pretreamtment
    rm build -rf
    mkdir build 
    cd build
    cmake ..
    make
    cd ../..
fi

${TOOL} \
   ${ORI_IMAGE_PATH} \
   ${NEW_IMAGE_PATH} \
   ${CONFIG_PATH}
