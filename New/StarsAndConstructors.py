from time import sleep
#Q1:-
#*
#**
#***
#****
#We have to print this using while/for loop. We can decrease variables but not increase.
#Answer is below: - 


print('NOW PRINTNG PATTERN\n')
sleep(0.5)
stars = "****"
i = 4
while i > 0:
    length=len(stars)
    print(stars[:length - i + 1])
    i -= 1
    sleep(0.5)






#Q2: -
#Multiple constructors in a class with same name(the constructors)
#IF possible;
#create four constructors with numbers that will add different number of values like
#2,3,4,5

#Answer is Below:

#Class
class NoName():
    def __init__(self):#Constructor1
        print(1+1)
    def __init__(self):#Constructor2
        print(1+1+1)
    def __init__(self):#Constructor3
        print(1+1+1+1)
    def __init__(self):#Constructor4
        print(1+1+1+1+1)

#Checking if possible
print('\nQ2 ANSWER NOW SHOWING\n')
sleep(0.5)
NoNameHasAName=NoName()
NoNameHasAName.__init__()
conclusion='It is not possible to have four or more constructors(meaning __init__) with same name(__init__)\nResult was shown above you.'
print(f'WE HEREBY LEARN\n\n{conclusion}')