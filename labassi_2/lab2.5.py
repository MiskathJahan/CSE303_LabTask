string = "Practice Problems to Drill List Comprehension in Your Head"
letters = string.split()
word = [i for i in letters if len(i) < 5]
print("The words in the string that are less than 5 letters: ", end="")
print(word)