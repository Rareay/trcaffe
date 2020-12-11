#include <iostream>
#include <opencv2/opencv.hpp>
#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <boost/filesystem.hpp>
#include <boost/function.hpp>
#include <boost/random/random_device.hpp>
#include <boost/algorithm/string.hpp>

struct key_word
{
    std::string key;
    float word;
};


class Pretreamtment{
private:
    std::vector<key_word> m_params;
    std::vector<std::string> m_imagelist;
    std::string m_new_iamge_path;
    int m_suffix_num = 0;
    
public:
    Pretreamtment() {
        creatParams();
    }

    void creatParams() {
        key_word p;
        p.key = "cut_num";
        p.word = .0;
        m_params.push_back(p);
        p.key = "cut_min_percent";
        p.word = .8;
        m_params.push_back(p);
        p.key = "rotate_num";
        p.word = .0;
        m_params.push_back(p);
        p.key = "rotate_angle_range";
        p.word = 360.;
        m_params.push_back(p);
        p.key = "flip_num";
        p.word = 0.;
        m_params.push_back(p);
        p.key = "light_num";
        p.word = 0.;
        m_params.push_back(p);
        p.key = "light_contrast";
        p.word = 0.2;
        m_params.push_back(p);
        p.key = "light_light";
        p.word = 10.;
        m_params.push_back(p);

    }

    int readImageList(std::string iamge_path) {
        boost::filesystem::path path(iamge_path);
        if (!boost::filesystem::exists(path)) {
            std::cout << "路径: " << iamge_path << " 不存在" << std::endl;
            return -1;
        }
        // 遍历文件夹
        boost::filesystem::recursive_directory_iterator * end;
        boost::filesystem::recursive_directory_iterator * pos;
        end = new boost::filesystem::recursive_directory_iterator();
        pos = new boost::filesystem::recursive_directory_iterator(path);
        for (; *pos != *end; (*pos)++) {
            boost::filesystem::path p = **pos;
            if (p.extension().string() == ".jpg" || 
                p.extension().string() == ".png" ) { // 判断该文件是否是jpg格式的
                m_imagelist.push_back(p.string());
            }
        }
        if (m_imagelist.size() == 0) {
            std::cout << "文件夹中没有图片" << std::endl;
            return -1;
        }
        return 0;
    }

    void randomImageList(float percent, std::vector<std::string> &list) {
        list.clear();
        boost::random::random_device gen;
        for (int i = 0; i < m_imagelist.size() * percent; i++) {
            int index = gen() % m_imagelist.size();
            list.push_back(m_imagelist[index]);
        }
    }

    float getWord(std::string key) {
        for (int i = 0; i  < m_params.size(); i++) {
            if (m_params[i].key == key) 
            return m_params[i].word;
        }
        return 0.;
    }

    int readParamenter(std::string param_path) {
        cv::FileStorage fread(param_path.c_str(),
                            cv::FileStorage::READ);
        if (!fread.isOpened()) {
            fread.release();
            cv::FileStorage fwrite(param_path.c_str(),
                                cv::FileStorage::WRITE);
            for (int i = 0; i < m_params.size(); i++) {
                fwrite << m_params[i].key.c_str() << m_params[i].word;
            }
            fwrite.release();
        }

        for (int i = 0; i < m_params.size(); i++) {
            fread[m_params[i].key.c_str()] >> m_params[i].word;
        }

        fread.release();
    }

    //void checkRepeat(std::string &path, std::string key) {
    //    boost::filesystem::path p(path);
    //    if (!boost::filesystem::exists(p)) return;
    //    std::string parent = p.parent_path().string();
    //    std::string name = p.stem().string();
    //    std::string suffix = p.extension().string();

    //    std::string new_name;
    //    bool find_key = false;
    //    std::vector<std::string> line_split;
    //    boost::split(line_split, name, boost::is_any_of("_"), boost::token_compress_on);
    //    for (std::vector<std::string>::iterator it = line_split.begin();
    //        it != line_split.end(); it++) {
    //        std::string a = *it;
    //        if (a == key) {
    //            find_key = true;
    //            new_name += a;
    //        } else if (find_key) {
    //            find_key = false;
    //            int n = atoi(a.c_str());
    //            n++;
    //            new_name += std::to_string(n);
    //        } else {
    //            new_name += a;
    //        }
    //        if (a != "") new_name += "_";
    //    }
    //    path = parent + "/" + new_name + suffix;
    //}

    void getNewImagePath(std::string ori_path, std::string & new_path) {
        boost::filesystem::path p(ori_path);
        std::string name = p.stem().string();
        std::string suffix = p.extension().string();
        new_path = m_new_iamge_path
                    + name 
                    + "_"
                    + std::to_string(m_suffix_num)
                    + suffix;
        m_suffix_num ++;
        if (m_suffix_num % 500 == 0)
            std::cout << "Have been generated " 
                      << m_suffix_num << " images..." << std::endl;

    }

    void creatImages(std::string new_image_path) {
        m_new_iamge_path = new_image_path + "/";
        boost::filesystem::path p(new_image_path);
        if (!boost::filesystem::exists(p)) {
            boost::filesystem::create_directories(p);
        }
        doCut();
        doRotaet();
        doFlip();
        doLight();
    }

    // 裁剪
    void doCut() {
        float percent = getWord("cut_num");
        std::vector<std::string> filelist;
        randomImageList(percent, filelist);
        float min_percent = getWord("cut_min_percent");
            
        boost::random::random_device gen;
        for (int i = 0; i < filelist.size(); i++) {
            cv::Mat img = cv::imread(filelist[i], 1);
            std::string new_path;
            getNewImagePath(filelist[i], new_path);

            int X, Y, W, H;
            float p;
            if (min_percent >= 1. || min_percent <= 0.) continue;
            p = 1 - (gen() % (int)(1000 - 1000 * min_percent)) / 1000.;
            
            W = img.cols * p;
            H = img.rows * p;
            X = img.cols != W ? gen() % (img.cols - W) : 0;
            Y = img.rows != H ? gen() % (img.rows - H) : 0;
            img = img(cv::Rect(X, Y, W, H));
            cv::imwrite(new_path, img);
        }

    }

    // 镜像
    void doFlip() {
        float percent = getWord("flip_num");
        std::vector<std::string> filelist;
        randomImageList(percent, filelist);
        boost::random::random_device gen;
        for (int i = 0; i < filelist.size(); i++) {
            cv::Mat img = cv::imread(filelist[i], 1);
            std::string new_path;
            getNewImagePath(filelist[i], new_path);
            int type = gen() % 3 - 1;
            cv::flip(img, img, type);
            cv::imwrite(new_path, img);
        }

    }

    // 旋转
    void doRotaet() {
        float percent = getWord("rotate_num");
        std::vector<std::string> filelist;
        randomImageList(percent, filelist);
        boost::random::random_device gen;
        float rotate_angle_range = getWord("rotate_angle_range");
        if (rotate_angle_range <= 0.) return ;

        for (int i = 0; i < filelist.size(); i++) {
            cv::Mat img = cv::imread(filelist[i], 1);
            std::string new_path;
            getNewImagePath(filelist[i], new_path);

            cv::Mat new_img;
            float r = (gen() % (int)(100 * rotate_angle_range)) / 100.;
            cv::Point2f center(img.cols / 2, img.rows / 2);//中心
            cv::Mat M = getRotationMatrix2D(center, r, 1);//计算旋转的仿射变换矩阵 
            warpAffine(img, new_img, M, cv::Size(img.cols, img.rows));//仿射变换  
            cv::imwrite(new_path, new_img);
        }


    }

    // 亮度 对比度
    void doLight() {
        float percent = getWord("light_num");
        std::vector<std::string> filelist;
        randomImageList(percent, filelist);
        boost::random::random_device gen;
        float light_contrast = getWord("light_contrast");
        float light_light = getWord("light_light");
        if (light_contrast <= 0. && light_light <= 0.) return ;

        for (int i = 0; i < filelist.size(); i++) {
            cv::Mat img = cv::imread(filelist[i], 1);
            std::string new_path;
            getNewImagePath(filelist[i], new_path);

            cv::Mat new_img = img.clone();
            float contrast = 0.;
            float light = 0.;
            contrast = light_contrast > 0. ? 
                       (gen() % (int)(200 * light_contrast)) / 100. - light_contrast : 
                       0.;
            contrast = contrast < -0.5 ? -0.5 : contrast;
            light = light_light > 0. ? 
                    (gen() % (int)(200 * light_light)) / 100. - light_light : 
                    0.;
            for (int m = 0; m < img.cols; m++) {
                for (int n = 0; n < img.rows; n++) {
                    for (int c = 0; c < img.channels(); ++c) {
                        new_img.at<cv::Vec3b>(n, m)[c] = 
                            cv::saturate_cast<uchar>((contrast + 1) * img.at<cv::Vec3b>(n,m)[c] + light);
                    }
                }
            }
            cv::imwrite(new_path, new_img);
        }
    }

    // 色度

    // 饱和度

    // 模糊

    // 锐化

    // 噪声
};

int main(int argc, char * argv[])
{
    if (argc != 4) {
        std::cout << "Use command: \n\t./pretreamtment [image_path] [new_iamge_path] [parameter_path]" << std::endl;
        return -1;
    }
    std::string image_path = argv[1];
    std::string new_image_path = argv[2];
    std::string parameter_path = argv[3];
    //std::string image_path = "../../image/test";
    //std::string new_image_path = "../../image/test/new";
    //std::string parameter_path = "../../image/parameter.yaml";

    Pretreamtment creat_images;
    // 判断文件夹内是否有图片
    int b = creat_images.readImageList(image_path);
    if (b < 0) return -1;

    // 读取配置
    creat_images.readParamenter(parameter_path);

    // 根据配置生成扩充图
    creat_images.creatImages(new_image_path);

    std::cout << "Done!" << std::endl;

    //cv::FileStorage fwrite(p, cv::FileStorage::WRITE);
    return 0;
}