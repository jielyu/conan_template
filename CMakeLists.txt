cmake_minimum_required(VERSION 3.15)
project(myapp CXX)

# 设置 C++17（可选）
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# 设置 cuda torch torchvision tensorrt
set(USE_CUDA OFF)
set(USE_Torch OFF)
set(USE_TorchVision OFF)
set(USE_TensorRT OFF)


# 添加依赖包
find_package(glog REQUIRED)
find_package(gflags REQUIRED)
find_package(fmt REQUIRED)
find_package(yaml-cpp REQUIRED)
find_package(nlohmann_json REQUIRED)
find_package(OpenCV REQUIRED)
find_package(xtensor REQUIRED)
find_package(onnxruntime REQUIRED)
if(USE_CUDA)
    find_package(CUDA REQUIRED)
    include_directories(${CUDA_INCLUDE_DIRS})
endif()
if(USE_Torch)
    set(Torch_DIR $ENV{HOME}/Libraries/libtorch/share/cmake/Torch)
    list(APPEND CMAKE_PREFIX_PATH ${Torch_DIR})
    find_package(Torch REQUIRED)
endif()
if(USE_TorchVision)
    list(APPEND CMAKE_PREFIX_PATH ${TorchVision_DIR})
    set(TorchVision_DIR $ENV{HOME}/Libraries/libtorchvision/share/cmake/TorchVision)
    find_package(TorchVision REQUIRED)
endif()
if(USE_TensorRT)
    set(TENSORRT_ROOT "$ENV{HOME}/Libraries/TensorRT-10.14.1.48" CACHE PATH "TensorRT安装路径")
    # 查找TensorRT
    find_path(TENSORRT_INCLUDE_DIR NvInfer.h
        PATHS ${TENSORRT_ROOT}/include
        NO_DEFAULT_PATH)
    find_library(TENSORRT_LIBRARY NAMES nvinfer
        PATHS ${TENSORRT_ROOT}/lib
        NO_DEFAULT_PATH)
    find_library(TENSORRT_PARSER_LIBRARY NAMES nvonnxparser
        PATHS ${TENSORRT_ROOT}/lib
        NO_DEFAULT_PATH)
    include_directories(${TENSORRT_INCLUDE_DIR}
)
endif()
if(CMAKE_SYSTEM_NAME STREQUAL "Linux")
    message(STATUS "Running on Linux")
    # 添加 Linux 特定的配置
    find_package(OpenMP REQUIRED)
endif()

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
if(USE_CUDA)
    list(APPEND REQUIRED_LIBS ${CUDA_LIBRARIES})
endif()
if(USE_Torch)
    list(APPEND REQUIRED_LIBS ${TORCH_LIBRARIES})
endif()
if(USE_TorchVision)
    list(APPEND REQUIRED_LIBS TorchVision::TorchVision)
endif()
if(USE_TensorRT)
    list(APPEND REQUIRED_LIBS ${TENSORRT_LIBRARY} ${TENSORRT_PARSER_LIBRARY})
endif()

# 创建目标
add_executable(${PROJECT_NAME} src/myapp.cpp src/main.cpp)

# 设置OpenMP和依赖库
if(APPLE)
    # 避免重复链接 C++ 标准库
    set(CMAKE_CXX_STANDARD_LIBRARIES "")
    # 或者明确指定
    # set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -stdlib=libc++")
    target_compile_options(${PROJECT_NAME} PRIVATE -Xpreprocessor -fopenmp)
    if(CMAKE_SYSTEM_PROCESSOR MATCHES "arm64|aarch64")
        message(STATUS "Running on Apple Silicon (ARM)")
        include_directories(/opt/homebrew/Cellar/libomp/18.1.8/include)
        target_link_libraries(${PROJECT_NAME} PUBLIC "/opt/homebrew/Cellar/libomp/18.1.8/lib/libomp.dylib" ${REQUIRED_LIBS})
    elseif(CMAKE_SYSTEM_PROCESSOR STREQUAL "x86_64")
        message(STATUS "Running on Intel x86_64")
        include_directories(/usr/local/Cellar/libomp/18.1.7/include)
        target_link_libraries(${PROJECT_NAME} PUBLIC "/usr/local/Cellar/libomp/18.1.7/lib/libomp.dylib" ${REQUIRED_LIBS})
    else()
        message(FATAL_ERROR "Unknown CPU architecture: ${CMAKE_SYSTEM_PROCESSOR}")
    endif()
    
else()
    target_link_libraries(${PROJECT_NAME} OpenMP::OpenMP_CXX ${REQUIRED_LIBS})
endif()


install(TARGETS myapp DESTINATION "."
        RUNTIME DESTINATION bin
        ARCHIVE DESTINATION lib
        LIBRARY DESTINATION lib
        )
