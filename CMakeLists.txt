# 
# Experimental CMake configuration script for Elmer
# 
# Authors:
#  Sami Ilvonen, CSC - IT Center for Science, Ltd.
#  Phil Weir, NUMA Engineering Services, Ltd.
#
# First public beta release 11th of October, 2013
#
# Note that this version is highly experimental and includes
# only a very limited subset of features that are supported
# by the original autotools scripts.
#

CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

SET(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} "${PROJECT_SOURCE_DIR}/cmake/Modules")
# This is GNU/Linux only for the mo (although *BSD should work fine?)
INCLUDE(GNUInstallDirs)

SET(ETC_LOCATION ${CMAKE_INSTALL_SYSCONFDIR}/gosmart)
SET(ETC_FULL_LOCATION ${CMAKE_INSTALL_FULL_SYSCONFDIR}/gosmart)

ENABLE_TESTING()

EXEC_PROGRAM(
    "git"
    ${CMAKE_CURRENT_SOURCE_DIR}
    ARGS "describe" "--tags" "--always"
    OUTPUT_VARIABLE GIT_REVISION)

ADD_SUBDIRECTORY(gssa)
ADD_CUSTOM_COMMAND(
    OUTPUT ${CMAKE_CURRENT_BINARY_DIR}/web
    COMMAND ${CMAKE_COMMAND} -E copy_directory ${CMAKE_CURRENT_SOURCE_DIR}/web ${CMAKE_CURRENT_BINARY_DIR}/web
)
ADD_CUSTOM_TARGET(web ALL
    DEPENDS ${CMAKE_CURRENT_BINARY_DIR}/web
)
