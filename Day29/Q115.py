class StringProcessor:
    def length(self,s): return len(s)
    def reverse(self,s): return s[::-1]
    def count_vowels(self,s): return sum(1 for char in s.lower() if char in 'aeiou')
    def palindrome(self,s): return s==s[::-1] 

sp=StringProcessor()

while True:
    text=input("enter a string:")
    
    print("\n 1.Length 2.Reverse 3.Count vowel 4.Palindrome 5.Exit")

    ch=input("Choice:")

    if ch=='1': print("Length:",sp.length(text))
    elif ch=='2': print("Reversed:",sp.reverse(text))
    elif ch=='3': print("Count vowel",sp.count_vowels(text))
    elif ch=='4': print("Palindrome:",sp.is_palindrome(text))
    elif ch=='5': break



