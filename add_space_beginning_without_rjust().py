# Ask user to input text and desired length
txt = input("Enter text: ")
length = int(input("Enter total length: "))

#Add desired spaces
txt = " " * max(0, length - len(txt)) + txt

# Print result
print("Result:", txt)
