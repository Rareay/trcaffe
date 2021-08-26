import os
import re

# 文件名的数字表示类别，如：300～400表示一类，400～500表示一类
def findfile_1(img_path, filename):
    file_write = open(filename, "w")
    line = ""
    for root,dirs,files in os.walk(img_path):
        for file in files:
            name = file.split('.',1)
            if name[1] == "jpg":
                if int(name[0]) >= 300 and int(name[0]) < 400:
                    line = line + os.path.join(root, file) + " 0\n"
                elif int(name[0]) >= 400 and int(name[0]) < 500:
                    line = line + os.path.join(root, file) + " 1\n"
                elif int(name[0]) >= 500 and int(name[0]) < 600:
                    line = line + os.path.join(root, file) + " 2\n"
                elif int(name[0]) >= 600 and int(name[0]) < 700:
                    line = line + os.path.join(root, file) + " 3\n"
                elif int(name[0]) >= 700 and int(name[0]) < 800:
                    line = line + os.path.join(root, file) + " 4\n"
    file_write.write(line)


def findfile(labels, img_path, filename):
    file_write = open(filename, "w")
    line = ""
    file_nums = 0
    for root, dirs, files in os.walk(img_path):
        for file in files:
            tag_index = 0
            for tag in labels:
                if re.search(tag, file) != None:
                    line = line + os.path.join(root, file) + " " + str(tag_index) + "\n";
                    file_nums += 1
                    break
                tag_index += 1
    file_write.write(line)
    print(img_path, " : have ", file_nums, " iamges.")

def changeFilename(path, key, new_key):
   for root,dirs,files in os.walk(path):
        for file in files:
            #name = file.split('.',1)
            file_new = file.replace(key, new_key)
            os.rename(os.path.join(path, file), os.path.join(path, file_new))
            #print(os.path.join(root, file))
            #print(os.path.join(root, file_new))
            #if name[1] == "jpg":

label1 = [
          "_none",
          "_green",
          "_red",
          ]
lables = label1

def getClass():
    return lables

if __name__ == '__main__':
    # 使用相对路径
    findfile(lables, r"data/tlc/test", "./imagelist/test.txt" )
    findfile(lables, r"data/tlc/train", "./imagelist/train.txt")
    #changeFilename(r"./data/tlc/test/0", ".jpg", "_none.jpg")

