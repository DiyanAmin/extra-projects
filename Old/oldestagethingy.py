#Checking who is oldest among 3 user inputs
p1=str(input('Enter name of person 1: '))
p2=str(input('Enter name of person 2: '))
p3=str(input('Enter name of person 3: '))
a1=int(input('Age of Person 1: '))
a2=int(input('Age of Person 2: '))
a3=int(input('Age of Person 3: '))
sum=a1+a2+a3
averageage=sum/3
#Checking with greater than
if a1>=averageage:
    print(p1,'is the oldest')
elif a2>=averageage:
    print(p2,'is the oldest')
elif a3>=averageage:
    print(p3,'is the oldest')
elif a1>=averageage and a2>=averageage:
    print(p1,'and',p2,'are the oldest')
elif a1>=averageage and a3>=averageage:
    print(p1,'and',p2,'are the oldest')
elif a2>=averageage and a3>=averageage:
    print(p2,'and',p3,'are the oldest')
elif a1>=averageage and a2>=averageage and a3>=averageage:
    print('All are same age')
else:
    print('Enter valid input')
