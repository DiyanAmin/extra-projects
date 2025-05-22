#Calculating the HCF of user input
num=int(input('Enter first number: '))
num2=int(input('Enter second number: '))
while num2>0:
    t1=num2
    num2=num%num2
    num=t1
hcf=num
print('HCF is:\n',hcf)