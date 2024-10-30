#include <iostream>

// Function to swap two integer values
void swap(int &a, int &b)
{
    int temp = a;
    a = b;
    b = temp;
}

// Partition function that chooses a pivot and partitions the array
int partition(int arr[], int low, int high)
{
    int pivot = arr[high]; // Choosing the last element as the pivot
    int i = (low - 1);     // Index of the smaller element

    for (int j = low; j <= high - 1; ++j)
    {
        // If the current element is smaller than or equal to the pivot
        if (arr[j] <= pivot)
        {
            ++i;                  // Increment index of smaller element
            swap(arr[i], arr[j]); // Swap current element with the element at index i
        }
    }
    swap(arr[i + 1], arr[high]); // Swap the pivot element with the element at index i+1
    return (i + 1);
}

// QuickSort function that sorts the array
void quickSort(int arr[], int low, int high)
{
    if (low < high)
    {
        // Partition the array and get the pivot index
        int pi = partition(arr, low, high);

        // Recursively sort elements before and after partition
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}

// Function to print an array
void printArray(int arr[], int size)
{
    for (int i = 0; i < size; ++i)
    {
        std::cout << arr[i] << " ";
    }
    std::cout << std::endl;
}

int main()
{
    int arr[] = {10, 7, 8, 9, 1, 5};      // Sample array
    int n = sizeof(arr) / sizeof(arr[0]); // Calculate the number of elements in the array

    std::cout << "Original array: ";
    printArray(arr, n);

    quickSort(arr, 0, n - 1); // Sort the array using QuickSort

    std::cout << "Sorted array: ";
    printArray(arr, n);

    return 0;
}
