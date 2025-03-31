#ask user to input text and prefix to check
text = input("Enter a text: ")
prefix = input("Enter prefix to check: ")

#check if text starts with given prefix
if text[:len(prefix)] == prefix: #compare given text and prefix
    print("prefix matches")
else:
    print("prefix doesn't match")

