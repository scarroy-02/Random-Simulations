#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>
#include <fstream>
#include <string>
#include <iterator>

std::vector<std::string> motzkin_path(int length) {
    std::vector<std::string> w;
    int A = 0, B = 0;
    for (int i = 0; i <= length; i++) {
        std::string move;
        int r = rand() % 3;
        if (r == 0) {
            move = "a";
            A++;
        } else if (r == 1) {
            move = "b";
            B++;
        } else {
            move = "c";
        }
        w.push_back(move);
        if (A < B) {
            return motzkin_path(length);
        }
    }
    return w;
}

int main() {
    srand(time(NULL));
    std::vector<std::string> result = motzkin_path(1000);
    std::ofstream output_file("./motzkin_path.txt");
    std::ostream_iterator<std::string> output_iterator(output_file, "\n");
    std::copy(result.begin(), result.end(), output_iterator);
    for (std::string c : result) {
        std::cout << c << " ";

    }
    std::cout << std::endl;
    return 0;
}
