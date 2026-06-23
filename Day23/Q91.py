str1=input("enter first string:")
str2=input("enter second string:")

if len(str1)!=len(str2):
    print("the strings are not anagrams.")
else:
    counts={}
    for char in str1:
        if char in counts:
            counts[char] +=1
        else:
            counts[char]=1

    is_anagram=True
    for char in str2:
        if char in counts and counts[char]>0:
            counts[char] -=1
        else:
            is_anagram=False
            break

    if is_anagram:
        print("the strings are anagrams.")
    else:
        print("the strings are not anagrams.")
