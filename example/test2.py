def swap(arr, a, b):
	temp = arr[a]
	arr[a] = arr[b]
	arr[b] = temp

def partition(arr, low, high):
	pivot = arr[high]
	i = (low-1)
	j = low
	while j<=high-1:
		if arr[j]<=pivot:
			i += 1
			swap(arr, i, j)
		j += 1
	swap(arr, i+1, high)
	return (i+1)

def quickSort(arr, low, high):
	if low<high:
		pi = partition(arr, low, high)
		quickSort(arr, low, pi-1)
		quickSort(arr, pi+1, high)

def printArray(arr, size):
	i = 0
	while i<size:
		print("{} ".format(arr[i]), end="")
		i += 1
	print("")

def main():
	arr = [10, 7, 8, 9, 1, 5]
	n = len(arr)
	print("Original array: ", end="")
	printArray(arr, n)
	quickSort(arr, 0, n-1)
	print("Sorted array: ", end="")
	printArray(arr, n)
	return 0

if __name__ == '__main__':
	main()