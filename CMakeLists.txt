cmake_minimum_required(VERSION 2.8)
project(DisplayImage)
set (CMAKE_CXX_STANDARD 11)
find_package(OpenCV REQUIRED)
include_directories(${OpenCV_INCLUDE_DIRS})

add_executable(VideoPlayer VideoPlayer.cpp)
target_link_libraries(VideoPlayer ${OpenCV_LIBS})

add_executable(DisplayImage DisplayImage.cpp)
target_link_libraries(DisplayImage ${OpenCV_LIBS})

install (TARGETS VideoPlayer DESTINATION bin)
install (TARGETS DisplayImage DESTINATION bin)

