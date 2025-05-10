#Self Explanatory
userinput=input('Enter 1 value: ')
print(type(userinput))
if userinput>='a' and userinput<='z':
    print('Alphabet')
elif userinput>='1': # -> Showing Error
    print('Number')
# else:
#     print("Special Character")
