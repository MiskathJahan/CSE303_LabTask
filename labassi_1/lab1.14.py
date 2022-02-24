def palindrome_checker_2019_2_60_056(a):
    if a == a[::-1]:
        return True


a = input("Enter word: ")
if palindrome_checker_2019_2_60_056(a) == True:
    print(a, "is a palindrome")
else:
    print(a, "is not a palindrome")