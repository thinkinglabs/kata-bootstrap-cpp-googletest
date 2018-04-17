# Kata Bootstrap for CPP and Google Test

This is a bootstrap project for kata's in CPP using Google Test.

The project makes use of [Conan.io](https://conan.io/) to download the Google Test library as a dependency. It's a simplified setup as tests are located in the main sources. As a result the binary produced by this project is the test runner.

A better option would be to locate tests in the sources sub-directory of the `test_package` directory and make use of Conan.io's [`test`](http://docs.conan.io/en/latest/reference/commands/creator/test.html) command. This way of working has been implemented for [Fizzbuzz kata in cpp using Catch and Conan.io](https://github.com/thinkinglabs/kata-bootstrap-cpp-catch).

## Basic Setup

To install Conan:

```
$ pip install conan
```

## Build

To build the project:

```
$ conan install . --build=gtest -if ./build && conan build . -bf ./build
```

All of this is also done by `./build.sh`.

After having build the project for the first time, you can rebuild it from the `./build` folder using `make`:

```
$ cd build
$ make
```

## Run unit tests

To run the unit tests:
```
$ cd build
$ make test
```

or

```
$ cd build
$ ctest
```

If you want more verbosity:

```
$ ctest -V
```

## Clean up

To clean up the project, just delete the `./build` folder:

```
$ rm -rf build
```

