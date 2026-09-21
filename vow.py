
def count_vowel(word):
    count = 0
    for letter in word:
        if letter in "aeiou": 
          count=count+1
    return count
word=input("enter a word \n")
a= count_vowel(word)
print(a)