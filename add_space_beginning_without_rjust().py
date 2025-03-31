# Ask user to input text and desired length
string = input("Enter text: ")
length = int(input("Enter total length: "))

#Add desired spaces
string = " " * max(0, length - len(string)) + string

# Print result
print("Result:", string)
