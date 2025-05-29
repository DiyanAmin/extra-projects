#Binary val of num
num=float(input('Enter number to convert it to binary: '))
binary_val=''
while num>0:
 rem=num%2
 binary_val=str(rem)+binary_val
 num=num//2
print('Binary Number:\n',binary_val)