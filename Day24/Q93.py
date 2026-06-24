s1=input("enter a string:")
s2=input("enter a string:")

if len(s1)==len(s2) and s2 in (s1+s1):
    print(f" '{s2}'is a rotation of '{s1}'")
else:
    print(f" '{s2}' is not a  rotation of '{s1}'")
