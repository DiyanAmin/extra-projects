#Skipping if  it is divisible by 2
n1=int(input('Enter upper range: '))
n2=int(input('Enter lower range: '))
for i in range(n1,n2):
    if i%2==0:
        continue
    print(i)
