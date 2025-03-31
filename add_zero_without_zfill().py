# Ask user to input text and desired length
string = input("Enter a text: ")
length = int(input("Enter total length: "))

#Add desired 0
string = ("0" * max(length - len(string), 0) + string)

#print result
print("Result:", string)

