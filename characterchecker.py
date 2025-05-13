#Self Explanatory
userinput=input('Enter 1 value: ')
print(type(userinput))
if userinput>='a' and userinput<='z':
    userinput=str
    print(type(userinput))
    print('Alphabet')
elif userinput>=(1): # -> Showing Error
    userinput=int
    print(type(userinput))
    print('Number')
else:
    userinput=complex
    print(type(userinput))
    print("Special Character")
