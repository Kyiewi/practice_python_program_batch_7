# ask user for string and substring to count
input_string = input("Enter a string: ")
search_substring = input("Enter substring to count: ")

# if substring empty, mimic count() behavior
if search_substring == "":
    print("Result:", len(input_string) + 1)
else:
    occurrence_count = 0

    # loop all possible start index
    for index in range(len(input_string) - len(search_substring) + 1):
        # if part of string same as substring, add to count
        if input_string[index:index + len(search_substring)] == search_substring:
            occurrence_count += 1

    # print total count
    print("Result:", occurrence_count)
