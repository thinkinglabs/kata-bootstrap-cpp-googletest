#Kata Bootstrap for CPP and Google Test

This is a bootstrap project for kata's in CPP  using Google Test.

The project makes use of [Conan.io](https://conan.io/) to download the Google Test library as a dependency.

# Basic Setup

To install Conan:

```
$ pip install conan
```

# Build

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

# Run unit tests

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

# Clean up

To clean up the project, just delete the `./build` folder:

```
$ rm -rf build
```

