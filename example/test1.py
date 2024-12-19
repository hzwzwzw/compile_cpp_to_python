def isPalindrome(text):
	length = len(text)
	i = 0
	while i<length/2:
		if text[i]!=text[length-i-1]:
			return False
		i+=1
	return True

def main():
	print("Enter a string: ", end='')
	text = input()
	if isPalindrome(text):
		print("True", end='')
	else:
		print("False", end='')
	return 0

if __name__ == '__main__':
	main()