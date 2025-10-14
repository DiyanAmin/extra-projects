#Calculating HCF using 'hcf' user defined function
def hcf(n1,n2):
    while n2>0:
        temp=n2
        n2=n1%n2
        n1=temp
    h=n1
    print('HCF is',h)
n1=int(input('Enter number 1: '))
n2=int(input('Enter number 2: '))
hcf(n1,n2)