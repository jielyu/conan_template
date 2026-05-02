cmake_minimum_required(VERSION 3.15)
project(myapp CXX)

# 添加依赖包
find_package(glog REQUIRED)
find_package(gflags REQUIRED)
find_package(fmt REQUIRED)
find_package(yaml-cpp REQUIRED)
find_package(nlohmann_json REQUIRED)
find_package(OpenCV REQUIRED)
find_package(xtensor REQUIRED)
find_package(onnxruntime REQUIRED)

# 列举所有依赖库
set(REQUIRED_LIBS glog::glog 
        gflags::gflags 
        nlohmann_json::nlohmann_json 
        yaml-cpp::yaml-cpp 
        fmt::fmt 
        xtensor
        ${OpenCV_LIBS}  
        ${onnxruntime_LIBRARIES_RELEASE}
)

add_executable(${PROJECT_NAME} src/myapp.cpp src/main.cpp)
target_link_libraries(${PROJECT_NAME} ${REQUIRED_LIBS})


install(TARGETS myapp DESTINATION "."
        RUNTIME DESTINATION bin
        ARCHIVE DESTINATION lib
        LIBRARY DESTINATION lib
        )
