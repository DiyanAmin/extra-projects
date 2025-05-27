#Employee Details
name=str(input('Enter your name: '))
age=int(input('Enter your age: '))
if name=='Diyan' and age==11:
    print('Admin panel Initated')
    exec=input('Execute: ')
    if exec=='show code':
        print('''#Employee Details
name=str(input('Enter your name: '))
age=int(input('Enter your age: '))
if name=='Diyan':
    print('Admin panel Initated')
    exec=input('Execute: ')
    if exec=='show code':''')
        print('The print statement above is not shown due to infinity loops')
else:
    print('Your name is',name,'andd your age is',age)
    print("You work at McDonald's")
    print('I do not know what else to write for employee details')
