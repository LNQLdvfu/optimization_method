cmake_minimum_required(VERSION 3.22)

project(Lab1_optimization)

# Set the path to the Eigen library


# Find Eigen package
find_package(Eigen3 REQUIRED)

# Include Eigen headers
include_directories(${EIGEN3_INCLUDE_DIR})

#find_package(jsoncpp REQUIRED)
#include_directories(${JSONCPP_INCLUDE_DIRS})

# Add the executable
add_executable(Lab1_optimization main.cpp)

# Link Eigen to the executable
target_link_libraries(Lab1_optimization Eigen3::Eigen)
#target_link_libraries(Lab1_optimization jsoncpp_lib)

