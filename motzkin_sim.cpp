#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>

std::vector<char> motzkin_path(int length) {
    std::vector<char> w;
    int A = 0, B = 0;
    for (int i = 0; i <= length; i++) {
        char move;
        int r = rand() % 3;
        if (r == 0) {
            move = 'a';
            A++;
        } else if (r == 1) {
            move = 'b';
            B++;
        } else {
            move = 'c';
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
    std::vector<char> result = motzkin_path(1000);
    for (char c : result) {
        std::cout << c << " ";
    }
    std::cout << std::endl;
    return 0;
}
