cmake_minimum_required(VERSION 3.22)
project(Lab2_optimization_method)

set(CMAKE_CXX_STANDARD 23)
find_package(Eigen3 REQUIRED)
set(nlohmann_json_INCLUDE_DIR "/built1/json/include/nlohmann/json.hpp")
#find_package(nlohmann_json  REQUIRED)

include_directories(${EIGEN3_INCLUDE_DIR})
include_directories(${nlohmann_json_INCLUDE_DIR})


add_executable(Lab2_optimization_method main.cpp )
target_link_libraries(Lab2_optimization_method Eigen3::Eigen )
#target_link_libraries(Lab2_optimization_method )
