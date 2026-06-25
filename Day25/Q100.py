text=input("enter a sentence:")

words=text.split()

n=len(words)
for i in range(n):
    for j in range(0,n-i-1):
        if len(words[j])>len(words[j+1]):
            words[j],words[j+1]=words[j+1],words[j]

print("words sorted by length:",words)
