#!/usr/bin/env bash

conan install . --build=gtest -if ./build && conan build . -bf ./build

