from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout, CMakeDeps


class myappRecipe(ConanFile):
    name = "myapp"
    version = "0.1"
    package_type = "application"

    # Optional metadata
    license = ""
    author = ""
    url = ""
    description = ""
    topics = ("tag1", "tag2", "tag3")

    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"

    def requirements(self):
        self.requires("glog/0.7.1")
        self.requires("fmt/12.1.0")
        self.requires("yaml-cpp/0.8.0")
        self.requires("xtensor/0.26.0")
        self.requires("opencv/4.13.0")
        self.requires("onnxruntime/1.24.4")
        self.requires("protobuf/6.33.5", override=True)
        self.requires("eigen/5.0.1", override=True)
        self.requires("openssl/3.5.2")
        self.requires("jwt-cpp/0.7.1")

    def layout(self):
        cmake_layout(self)

    def generate(self):
        deps = CMakeDeps(self)
        deps.generate()
        tc = CMakeToolchain(self)
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()
