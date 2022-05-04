# Install script for directory: /home/krishnasathwik09/Dynamic_obstacle_WS/src/gopher_move_it/gopher_move_it_config

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/krishnasathwik09/Dynamic_obstacle_WS/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gopher_move_it_config/msg" TYPE FILE FILES "/home/krishnasathwik09/Dynamic_obstacle_WS/src/gopher_move_it/gopher_move_it_config/msg/Joints.msg")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gopher_move_it_config/srv" TYPE FILE FILES "/home/krishnasathwik09/Dynamic_obstacle_WS/src/gopher_move_it/gopher_move_it_config/srv/PlanTrajectory.srv")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gopher_move_it_config/cmake" TYPE FILE FILES "/home/krishnasathwik09/Dynamic_obstacle_WS/build/gopher_move_it/gopher_move_it_config/catkin_generated/installspace/gopher_move_it_config-msg-paths.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/home/krishnasathwik09/Dynamic_obstacle_WS/devel/include/gopher_move_it_config")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/roseus/ros" TYPE DIRECTORY FILES "/home/krishnasathwik09/Dynamic_obstacle_WS/devel/share/roseus/ros/gopher_move_it_config")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/common-lisp/ros" TYPE DIRECTORY FILES "/home/krishnasathwik09/Dynamic_obstacle_WS/devel/share/common-lisp/ros/gopher_move_it_config")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gennodejs/ros" TYPE DIRECTORY FILES "/home/krishnasathwik09/Dynamic_obstacle_WS/devel/share/gennodejs/ros/gopher_move_it_config")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  execute_process(COMMAND "/usr/bin/python2" -m compileall "/home/krishnasathwik09/Dynamic_obstacle_WS/devel/lib/python2.7/dist-packages/gopher_move_it_config")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages" TYPE DIRECTORY FILES "/home/krishnasathwik09/Dynamic_obstacle_WS/devel/lib/python2.7/dist-packages/gopher_move_it_config")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/krishnasathwik09/Dynamic_obstacle_WS/build/gopher_move_it/gopher_move_it_config/catkin_generated/installspace/gopher_move_it_config.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gopher_move_it_config/cmake" TYPE FILE FILES "/home/krishnasathwik09/Dynamic_obstacle_WS/build/gopher_move_it/gopher_move_it_config/catkin_generated/installspace/gopher_move_it_config-msg-extras.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gopher_move_it_config/cmake" TYPE FILE FILES
    "/home/krishnasathwik09/Dynamic_obstacle_WS/build/gopher_move_it/gopher_move_it_config/catkin_generated/installspace/gopher_move_it_configConfig.cmake"
    "/home/krishnasathwik09/Dynamic_obstacle_WS/build/gopher_move_it/gopher_move_it_config/catkin_generated/installspace/gopher_move_it_configConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gopher_move_it_config" TYPE FILE FILES "/home/krishnasathwik09/Dynamic_obstacle_WS/src/gopher_move_it/gopher_move_it_config/package.xml")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/gopher_move_it_config" TYPE PROGRAM FILES "/home/krishnasathwik09/Dynamic_obstacle_WS/build/gopher_move_it/gopher_move_it_config/catkin_generated/installspace/plan_trajectory.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gopher_move_it_config" TYPE DIRECTORY FILES "/home/krishnasathwik09/Dynamic_obstacle_WS/src/gopher_move_it/gopher_move_it_config/launch" REGEX "/setup\\_assistant\\.launch$" EXCLUDE)
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gopher_move_it_config" TYPE DIRECTORY FILES "/home/krishnasathwik09/Dynamic_obstacle_WS/src/gopher_move_it/gopher_move_it_config/config")
endif()

