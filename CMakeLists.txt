cmake_minimum_required(VERSION 2.8.3)
project(thesis)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  tf)

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES thesis
#  CATKIN_DEPENDS roscpp rospy std_msgs
#  DEPENDS system_lib
)

include_directories(${catkin_INCLUDE_DIRS})


