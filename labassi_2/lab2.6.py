string = "Practice Problems to Drill List Comprehension in Your Head."
letters = string.split()
Wordlength = [len(i) for i in letters]
print("The length of each word in a sentence: ")
print(Wordlength)