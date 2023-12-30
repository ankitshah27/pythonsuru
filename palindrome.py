string=(input("Enter your name:"))
rev=""
for x in string:
    rev=x+rev
    if(rev==string):
        print("palindrome")
    else:
        print("Not palindrome")
