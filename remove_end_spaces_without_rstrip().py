# Ask user for input with spaces at the end
custom_rstrip = input("Enter Full Name with spaces at the end: ")

# Get the last index of the string
last_char = len(custom_rstrip) - 1

# Loop to check if the last characters are spaces
while last_char >= 0 and custom_rstrip[last_char] == " ":
    last_char -= 1 # Move left until a non-space character is found

# Print the string without trailing spaces
print(custom_rstrip[:last_char + 1])
