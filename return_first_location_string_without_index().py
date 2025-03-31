# ask user for string and substring to find
input_string = input("Enter a string: ")
search_substring = input("Enter substring to find: ")

# loop all possible start index
for index in range(len(input_string) - len(search_substring) + 1):
    # if slice equals substring then found, print index and break
    if input_string[index:index + len(search_substring)] == search_substring:
        print("Result:", index)
        break
else:
    print("ValueError: substring not found")
