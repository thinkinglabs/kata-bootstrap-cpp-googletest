cmake_minimum_required(VERSION 2.8)
set(PROJECT_NAME kata_bootstrap)
project(${PROJECT_NAME} CXX)

# Conan.io
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

# Project sources
file(GLOB SRC_FILES ${PROJECT_SOURCE_DIR}/src/*.cpp)
file(GLOB TEST_SRC_FILES ${PROJECT_SOURCE_DIR}/test/*.cpp)

# CTest is a testing tool that can be used to test your project.
enable_testing()

# Add test cpp file
#add_executable(runUnitTests ${TEST_SRC_FILES})
add_executable(runUnitTests ./test/test.cpp)

# Link test executable against gtest & gtest_main
target_link_libraries(runUnitTests ${CONAN_LIBS})

add_test(UnitTests ./bin/runUnitTests )
# add_test(NAME example
#          WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/bin
#          COMMAND example)
