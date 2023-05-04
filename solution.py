
#Task 1

# list_of_strings = input("Enter a list of strings: ")
# spliting = list_of_strings.split(",")


# def count_vowel(string):
#     vowel = "aeiouAEIOU"
#     count = 0
#     for char in string:
#         if char in vowel:
#             count += 1
#     return count
# result = sorted(spliting, key = count_vowel)
# print(result)


# Task

number = int(input("Enter the number of your items: "))
tuple_list = []
for num in range(number):
    item = input("(num1,num2)")
    tuple_list.append((item))
print(tuple_list)