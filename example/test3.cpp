#include <iostream>

// Function to compute the longest prefix suffix (LPS) array
void computeLPSArray(const char *pattern, int M, int *lps)
{
    int length = 0; // length of the previous longest prefix suffix
    lps[0] = 0;     // lps[0] is always 0

    int i = 1;
    while (i < M)
    {
        if (pattern[i] == pattern[length])
        {
            length++;
            lps[i] = length;
            i++;
        }
        else
        {
            if (length != 0)
            {
                length = lps[length - 1];
            }
            else
            {
                lps[i] = 0;
                i++;
            }
        }
    }
}

// KMP search function
void KMPSearch(const char *pattern, const char *text)
{
    int M = 0; // length of pattern
    int N = 0; // length of text

    // Calculate the length of the pattern
    while (pattern[M] != '\0')
    {
        M++;
    }

    // Calculate the length of the text
    while (text[N] != '\0')
    {
        N++;
    }

    int *lps = new int[M];

    // Compute the LPS array
    computeLPSArray(pattern, M, lps);

    int i = 0; // index for text[]
    int j = 0; // index for pattern[]
    while (i < N)
    {
        if (pattern[j] == text[i])
        {
            j++;
            i++;
        }

        if (j == M)
        {
            std::cout << "Found pattern at index " << i - j << std::endl;
            j = lps[j - 1];
        }
        else if (i < N && pattern[j] != text[i])
        {
            if (j != 0)
            {
                j = lps[j - 1];
            }
            else
            {
                i++;
            }
        }
    }

    // Clean up the dynamically allocated memory
    delete[] lps;
}

int main()
{
    const char text[] = "ABABDABACDABABCABAB";
    const char pattern[] = "ABABCABAB";

    KMPSearch(pattern, text);

    return 0;
}
