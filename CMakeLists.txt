cmake_minimum_required(VERSION 2.8.3)
project(aa_metrics)

# Find build dependencies
find_package(catkin REQUIRED COMPONENTS
    rosbag
    rospy
)

# Set up python paths
catkin_python_setup()

# Find runtime dependencies
catkin_package(
    CATKIN_DEPENDS rosbag rospy
)

# Add other include files
include_directories(
    ${catkin_INCLUDE_DIRS}
)

# Install python scripts
catkin_install_python(PROGRAMS nodes/metrics
    DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
