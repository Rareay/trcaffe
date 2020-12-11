#SET(CMAKE_CXX_FLAGS "-std=c++11 -O3")

cmake_minimum_required(VERSION 2.8)
project(use_model)

set(CMAKE_BUILD_TYPE Release)
set(CMAKE_CXX_FLAGS "-std=c++14 -O3")

list(APPEND CMAKE_MODULE_PATH ${PROJECT_SOURCE_DIR}/cmake)


# OpenCV
find_package(OpenCV REQUIRED)
include_directories(${OpenCV_INCLUDE_DIRS})

# Boost
add_definitions(-DBOOST_ERROR_CODE_HEADER_ONLY)
find_package(Boost REQUIRED COMPONENTS filesystem system thread date_time random)
include_directories(${Boost_INCLUDE_DIRS})

# Caffe
set(Caffe_INCLUDE_DIR ../caffe/include)
set(Caffe_LIBRARY_DIR ../caffe/build/lib) 
include_directories(${Caffe_INCLUDE_DIR})
#link_directories(${Caffe_LIBRARY_DIR})
find_library(Caffe_LIBS caffe ${Caffe_LIBRARY_DIR})


# Cuda
set(Cuda_INCLUDE_DIR /usr/local/cuda/include)
set(Cuda_LIBRARY_DIR /usr/local/cuda/lib64) 
include_directories(${Cuda_INCLUDE_DIR})

# Glog
set(GLOG_LIB glog)


add_executable(use_model classification.cpp)
target_link_libraries(use_model 
                        ${OpenCV_LIBS} 
                        ${Boost_LIBRARIES} 
                        ${Caffe_LIBS}
                        ${GLOG_LIB}
)

