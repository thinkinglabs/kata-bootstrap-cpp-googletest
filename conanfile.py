from conans import ConanFile, CMake

class KataConan(ConanFile):
   settings = "os", "compiler", "build_type", "arch"
   requires = "gtest/1.8.0@bincrafters/stable"
   generators = "cmake", "txt"
   default_options = "gtest:shared=False", "gtest:build_gmock=True"

   def build(self):
      cmake = CMake(self)
      cmake.configure()
      cmake.build()
      cmake.test()
