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

def findfile_2(img_path, filename):
    file_write = open(filename, "w")
    line = ""
    file_nums = 0
    for root,dirs,files in os.walk(img_path):
        for file in files:
            file_nums = file_nums + 1
            if re.search("_St_exc", file) != None:
                line = line + os.path.join(root, file) + " 0\n"
            elif re.search("_St_hac", file) != None:
                line = line + os.path.join(root, file) + " 1\n"
            elif re.search("_St_io", file) != None:
                line = line + os.path.join(root, file) + " 2\n"
            elif re.search("_St_ip", file) != None:
                line = line + os.path.join(root, file) + " 3\n"
            elif re.search("_St_not", file) != None:
                line = line + os.path.join(root, file) + " 4\n"
            else:
                file_nums = file_nums - 1
    file_write.write(line)
    print(img_path, " : have ", file_nums, " iamges.")

def findfile_3(img_path, filename):
    file_write = open(filename, "w")
    line = ""
    file_nums = 0
    for root,dirs,files in os.walk(img_path):
        for file in files:
            file_nums = file_nums + 1
            if re.search("_P_1", file) != None:
                line = line + os.path.join(root, file) + " 0\n"
            elif re.search("_P_2", file) != None:
                line = line + os.path.join(root, file) + " 1\n"
            elif re.search("_P_3", file) != None:
                line = line + os.path.join(root, file) + " 2\n"
            elif re.search("_P_4", file) != None:
                line = line + os.path.join(root, file) + " 3\n"
            elif re.search("_P_5", file) != None:
                line = line + os.path.join(root, file) + " 4\n"
            else:
                file_nums = file_nums - 1
    file_write.write(line)
    print(img_path, " : have ", file_nums, " iamges.")



def findfile_4(img_path, filename):
    file_write = open(filename, "w")
    line = ""
    file_nums = 0
    for root,dirs,files in os.walk(img_path):
        for file in files:
            file_nums = file_nums + 1
            if re.search("_cane", file) != None:
                line = line + os.path.join(root, file) + " 0\n"
            elif re.search("_elefante", file) != None:
                line = line + os.path.join(root, file) + " 1\n"
            elif re.search("_gallina", file) != None:
                line = line + os.path.join(root, file) + " 2\n"
            elif re.search("_mucca", file) != None:
                line = line + os.path.join(root, file) + " 3\n"
            elif re.search("_ragno", file) != None:
                line = line + os.path.join(root, file) + " 4\n"
            elif re.search("_cavallo", file) != None:
                line = line + os.path.join(root, file) + " 5\n"
            elif re.search("_farfalla", file) != None:
                line = line + os.path.join(root, file) + " 6\n"
            elif re.search("_gatto", file) != None:
                line = line + os.path.join(root, file) + " 7\n"
            elif re.search("_pecora", file) != None:
                line = line + os.path.join(root, file) + " 8\n"
            elif re.search("_scoiattolo", file) != None:
                line = line + os.path.join(root, file) + " 9\n"
            else:
                file_nums = file_nums - 1
    file_write.write(line)
    print(img_path, " : have ", file_nums, " iamges.")



if __name__ == '__main__':
    # 使用相对路径
    findfile_4(r"data/raw-img/test", "./imagelist/test.txt")
    findfile_4(r"data/raw-img/train", "./imagelist/train.txt")

