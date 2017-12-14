#Kata Bootstrap for CPP and Google Test

This is a bootstrap project for CPP kata's using Google Test.

# Basic Setup

Conan.io is used to handle project dependencies. To install Conan.io:

```
$ pip install conan
```

To install the Google Test dependency:

```
$ conan install . --build=gtest
```

# Generate Makefile

```
$ cmake .
```

# Run unit tests

```
$ make test
```

or if you want more verbosity:

```
$ ctest -V
```

