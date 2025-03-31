#ask user to input text and preficx to check
text = input("Enter a text: ")
prefix = input("Enter prexif to check: ")

#check if text starts with given prefix
if text[:len(prefix)] == prefix: #compare given text and prefix
    print("prefix matches")
else:
    print("prefix dont match")

