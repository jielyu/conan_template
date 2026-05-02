#include "myapp.h"
#include <vector>
#include <string>

int main() {
    myapp();

    std::vector<std::string> vec;
    vec.push_back("test_package");

    myapp_print_vector(vec);
}
