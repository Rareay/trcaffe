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

add_executable(pretreamtment pretreamtment.cpp)
target_link_libraries(pretreamtment
                        ${OpenCV_LIBS} 
                        ${Boost_LIBRARIES} 
)

