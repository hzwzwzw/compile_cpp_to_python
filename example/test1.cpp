#include <iostream>
#include <cstring>

bool isPalindrome(const char *text)
{
    int length = strlen(text);
    for (int i = 0; i < length / 2; i += 1)
    {
        if (text[i] != text[length - i - 1])
        {
            return false;
        }
    }
    return true;
}

int main()
{
    char text[100];
    printf("Enter a string: ");
    scanf("%s", text);

    if (isPalindrome(text))
    {
        printf("True");
    }
    else
    {
        printf("False");
    }

    return 0;
}
