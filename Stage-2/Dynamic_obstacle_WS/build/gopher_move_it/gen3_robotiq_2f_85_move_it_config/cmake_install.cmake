# Install script for directory: /home/krishnasathwik09/Dynamic_obstacle_WS/src/gopher_move_it/gen3_robotiq_2f_85_move_it_config

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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/krishnasathwik09/Dynamic_obstacle_WS/build/gopher_move_it/gen3_robotiq_2f_85_move_it_config/catkin_generated/installspace/gen3_robotiq_2f_85_move_it_config.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gen3_robotiq_2f_85_move_it_config/cmake" TYPE FILE FILES
    "/home/krishnasathwik09/Dynamic_obstacle_WS/build/gopher_move_it/gen3_robotiq_2f_85_move_it_config/catkin_generated/installspace/gen3_robotiq_2f_85_move_it_configConfig.cmake"
    "/home/krishnasathwik09/Dynamic_obstacle_WS/build/gopher_move_it/gen3_robotiq_2f_85_move_it_config/catkin_generated/installspace/gen3_robotiq_2f_85_move_it_configConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gen3_robotiq_2f_85_move_it_config" TYPE FILE FILES "/home/krishnasathwik09/Dynamic_obstacle_WS/src/gopher_move_it/gen3_robotiq_2f_85_move_it_config/package.xml")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gen3_robotiq_2f_85_move_it_config" TYPE DIRECTORY FILES "/home/krishnasathwik09/Dynamic_obstacle_WS/src/gopher_move_it/gen3_robotiq_2f_85_move_it_config/launch" REGEX "/setup\\_assistant\\.launch$" EXCLUDE)
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gen3_robotiq_2f_85_move_it_config" TYPE DIRECTORY FILES "/home/krishnasathwik09/Dynamic_obstacle_WS/src/gopher_move_it/gen3_robotiq_2f_85_move_it_config/config")
endif()

