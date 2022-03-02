def Vowels(string):
    vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
    if string not in vowels:
        return True
    else:
        return False


string = "Practice Problems to Drill List Comprehension in Your Head."
Vowels = filter(Vowels, string)
print('After remove all of the vowels: ', end="")
for vowel in Vowels:
    print(vowel, end="")