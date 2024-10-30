#include <iostream>
#include <cstring> // for strlen

bool isPalindrome(const char input[])
{
    int length = strlen(input);
    for (int i = 0; i < length / 2; ++i)
    {
        if (input[i] != input[length - i - 1])
        {
            return false;
        }
    }
    return true;
}

int main()
{
    char input[100]; // assuming the maximum input length is 99
    std::cout << "Enter a string: ";
    std::cin.getline(input, 100); // read the entire line including spaces

    if (isPalindrome(input))
    {
        std::cout << "True" << std::endl;
    }
    else
    {
        std::cout << "False" << std::endl;
    }

    return 0;
}
