#Fibonacci of user input
#In mathematics, the Fibonacci sequence is a sequence in which each element is the sum of the two elements that precede it. Numbers that are part of the Fibonacci sequence are known as Fibonacci numbers, commonly denoted Fn . Many writers begin the sequence with 0 and 1, although some authors start it from 1 and 1[1][2] and some (as did Fibonacci) from 1 and 2. Starting from 0 and 1, the sequence begins

#0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ... (sequence A000045 in the OEIS)
#userinput --> temp 
#temp-1
#previous num=temp-1
def fibonacci(n):
    val=0
    while val<1000:
     temp=n
     prevn=temp-1
     sum=prevn+temp
     temp-=1
     val+=1
    print('Number:\n',sum)
n=int(input('Enter a number to find its fibonacci!: '))
if n==0:
    print('Invalid num')
elif n==1:
    print('Invalid')
else:
   print('Error 404 name not defined')
