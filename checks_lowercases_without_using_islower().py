#Ask user to input text
text = input("Enter a text: ")

#Assume text is in lowercase
is_lower = True

#Check each character
for letter in text:
    if 'A' <= letter <= 'Z': #if uppercase
        is_lower = False
    #stop loop
    break

#Peint result
if is_lower:
    print("Text is fully lowercase.")
else:
    print("Text is not fully lowercase.")