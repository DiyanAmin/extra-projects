#Checking if user input is palindrome
uinp=input('Enter something: ')
rev=uinp[::-1]
if rev==uinp:
    print(uinp,'is a palindrome')
elif rev!=uinp:
    print(uinp,'Is not a palindrome')
else:
    print('Wrong Input')
