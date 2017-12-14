project(PackageTest CXX)
cmake_minimum_required(VERSION 2.8.12)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

# CTest is a testing tool that can be used to test your project.
enable_testing()

# Add test cpp file
add_executable( runUnitTests src/test.cpp )

# Link test executable against gtest & gtest_main
target_link_libraries(runUnitTests ${CONAN_LIBS})
add_test( runUnitTests bin/runUnitTests )
# add_test(NAME example
#          WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/bin
#          COMMAND example)
