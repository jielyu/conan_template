from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout, CMakeDeps


class myappRecipe(ConanFile):
    name = "myapp"
    version = "0.1"
    package_type = "application"

    # Optional metadata
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of myapp package here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")

    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"

    # Sources are located in the same place as this recipe, copy them to the recipe
    exports_sources = "CMakeLists.txt", "src/*"

    def requirements(self):
        self.requires("glog/0.7.1")
        self.requires("fmt/12.1.0")
        self.requires("yaml-cpp/0.8.0")
        self.requires("xtensor/0.26.0")
        self.requires("opencv/4.13.0")
        self.requires("onnxruntime/1.24.4")
        self.requires("protobuf/6.33.5", override=True)
        self.requires("eigen/5.0.1", override=True)

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
