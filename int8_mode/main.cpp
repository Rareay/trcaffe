
#include <ncnn/net.h>
#include <algorithm>
#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <stdio.h>
#include <vector>
#include <iostream>


static int detect_squeezenet(const cv::Mat& bgr, std::vector<float>& cls_scores)
{
    ncnn::Net squeezenet;
    squeezenet.opt.use_vulkan_compute = true;

    squeezenet.load_param("mode/net-int8.param");
    squeezenet.load_model("mode/net-int8.bin");
    ///squeezenet.load_param("mode/squeezenet_v1.1.param");
    ///squeezenet.load_model("mode/squeezenet_v1.1.bin");

    ncnn::Mat in = ncnn::Mat::from_pixels_resize(bgr.data, ncnn::Mat::PIXEL_BGR, bgr.cols, bgr.rows, 224, 224);

    const float mean_vals[3] = {104.f, 117.f, 123.f};
    in.substract_mean_normalize(mean_vals, 0);

    ncnn::Extractor ex = squeezenet.create_extractor();

    ex.input("data", in);

    ncnn::Mat out;
    ex.extract("loss", out);

    cls_scores.resize(out.w);
    for (int j = 0; j < out.w; j++)
    {
        cls_scores[j] = out[j];
        std::cout << out[j]  << std::endl;
    }

    return 0;
}

int main()
{
    cv::Mat img = cv::imread("images/12.jpeg");
    //cv::imshow("1", img);
    //cv::waitKey(0);
    std::vector<float> cls_scores;
    detect_squeezenet(img, cls_scores);
    return 0;
}
