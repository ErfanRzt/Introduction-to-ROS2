cmake_minimum_required(VERSION 3.8)
project(rpros2_interfaces)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
# uncomment the following section in order to fill in
# further dependencies manually.
# find_package(<dependency> REQUIRED)

find_package(rosidl_default_generators REQUIRED)

# >>>>>>>>>>> STUDENT IMPLEMENTATION >>>>>>>>>>>
#
# TODO: Add your custom message (.msg), service (.srv),
# and action (.action) files here. These files define
# the data structures and communication interfaces your
# ROS 2 nodes will use for the assignments and projects.
#
# Example:
#   set(STUDENT_INF
#       "msg/MyMessage.msg"
#       "srv/MyService.srv"
#       "action/MyAction.action"
#   )
#
# Make sure the files are placed in the correct folders
# (msg/, srv/, action/) inside the rpros2_interfaces package.
#
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

set(STUDENT_INF

)

set(SRV_FILES
  "srv/AddTwoInts.srv"
)

set(MSG_FILES
  "msg/String.msg"
)

rosidl_generate_interfaces(${PROJECT_NAME}
  ${SRV_FILES}
  ${MSG_FILES}
  ${STUDENT_INF}
)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # comment the line when a copyright and license is added to all source files
  set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # comment the line when this package is in a git repo and when
  # a copyright and license is added to all source files
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()
