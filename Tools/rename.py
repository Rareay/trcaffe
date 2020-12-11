# -*- coding: utf-8 -*-

import os
import re

def addSuffix(dir, key):
    '''
    遍历目录下的某类型文件，并给文件名添加对应标识。
    dir: 目录
    key: 添加的关键字
    '''
    num = 0
    for root,dirs,files in os.walk(dir):
        for file in files:
            ori_path = os.path.join(root, file)
            file = file.split(".")
            name = file[0]
            suffix = file[-1]
            if suffix == "png" or suffix == "jpg" or suffix == "jpeg":
                match = re.search(key, name)
                if match != None:
                    continue
                num = num + 1
                new_file = name + key + '.' + suffix
                new_path = os.path.join(root, new_file)
                os.rename(ori_path, new_path)
    print("Rename ", num, " images!")




if __name__ == "__main__":
    addSuffix("/home/tamray/caffe/data/raw-img/cane", "_cane")    
    addSuffix("/home/tamray/caffe/data/raw-img/elefante", "_elefante")  
    addSuffix("/home/tamray/caffe/data/raw-img/gallina", "_gallina")  
    addSuffix("/home/tamray/caffe/data/raw-img/mucca", "_mucca")   
    addSuffix("/home/tamray/caffe/data/raw-img/ragno", "_ragno")
    addSuffix("/home/tamray/caffe/data/raw-img/cavallo", "_cavallo")  
    addSuffix("/home/tamray/caffe/data/raw-img/farfalla", "_farfalla")  
    addSuffix("/home/tamray/caffe/data/raw-img/gatto", "_gatto")    
    addSuffix("/home/tamray/caffe/data/raw-img/pecora", "_pecora")  
    addSuffix("/home/tamray/caffe/data/raw-img/scoiattolo", "_scoiattolo")
