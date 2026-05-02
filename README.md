# conan 项目模版

用于固定依赖库的版本，避免不同项目依赖不同导致的频繁源码编译。

## 指令

### 创建应用

```
conan new cmake_exe -d name=myapp
```

### 安装依赖

```
conan install . --build=missing
```

### 编译

- 第一次编译

```
conan build .
```

- 再次编译

```
cmake --build --preset conan-release
```

或者

```
cmake --build  build/Release 
```

### 运行

```
./build/Release/myapp
```