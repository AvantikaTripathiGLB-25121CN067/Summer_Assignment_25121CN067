text=input("enter a sentence:")

words=text.split()
longest_word=""

for word in words:
    if len(word)>len(longest_word):
        longest_word=word

print("longest word:",longest_word)