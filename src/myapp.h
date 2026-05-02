#pragma once

#include <vector>
#include <string>


#ifdef _WIN32
  #define MYAPP_EXPORT __declspec(dllexport)
#else
  #define MYAPP_EXPORT
#endif

MYAPP_EXPORT void myapp();
MYAPP_EXPORT void myapp_print_vector(const std::vector<std::string> &strings);
