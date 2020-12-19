#SET(CMAKE_CXX_FLAGS "-std=c++11 -O3")

cmake_minimum_required(VERSION 2.8)
project(use_model)

set(CMAKE_BUILD_TYPE Release)

list(APPEND CMAKE_MODULE_PATH ${PROJECT_SOURCE_DIR}/cmake)

# OpenMP
FIND_PACKAGE( OpenMP REQUIRED)
if(OPENMP_FOUND)
    set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} ${OpenMP_C_FLAGS}")
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${OpenMP_CXX_FLAGS}")
endif()

# OpenCV
find_package(OpenCV REQUIRED)
include_directories(${OpenCV_INCLUDE_DIRS})

# Boost
add_definitions(-DBOOST_ERROR_CODE_HEADER_ONLY)
find_package(Boost REQUIRED COMPONENTS filesystem system) 
include_directories(${Boost_INCLUDE_DIRS})

# Ncnn
set(Ncnn_INCLUDE_DIR /home/tamray/trcaffe/ncnn/build/install/include)
set(Ncnn_LIBRARY_DIR /home/tamray/trcaffe/ncnn/build/install/lib) 
include_directories(${Ncnn_INCLUDE_DIR})
LINK_DIRECTORIES(${Ncnn_LIBRARY_DIR})

add_executable(app main.cpp)
target_link_libraries(app
                        ${OpenCV_LIBS} 
                        ${Boost_LIBS} 
                        libncnn.a
)
