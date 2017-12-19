#! /bin/bash

mkdir build
pushd build
conan install .. --build=gtest
cmake .. && make
popd
