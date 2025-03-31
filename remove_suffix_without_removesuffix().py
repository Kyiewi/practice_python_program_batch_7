#Ask user to input string and suffix to remove
string = input("Enter a word: ")
suffix = input("suffix to remove in the word: ")

# Check if the string ends with the given suffix
if string.endswith(suffix):
    # Remove the suffix by slicing the string
    string = string[:len(string) - len(suffix)]

# Print the resulting string
print("Result:", string)

