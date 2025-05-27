#Perimeter
shape=str(input('Enter the shape name of which you want to find out the perimter(rectangle triangle or square): '))
#rectangle
if shape=='rectangle':
    l=int(input('Enter length: '))
    b=int(input('Enter breadth: '))
    perimeter=2*(l+b)
    print('Perimeter is:\n',perimeter)
#triangle
elif shape=='triangle':
    triangletype=str(input('Enter type of triangle: '))
    if triangletype=='equilateral':
        #equi
        tes=int(input('Enter length of 1 side: '))
        perimeter=tes*3
        print('Perimeter:\n',perimeter)
        #iso
    elif triangletype=='isosceles':
        tis1=int(input('Enter length of side 1(equal to another side): '))
        tis2=int(input('Enter length of side 2(not equal to above side): '))
        perimeter=2*(tis1+tis2)
        print('Perimeter is:\n',perimeter)
        #scalene
    elif triangletype=='scalene':
        tss1=int(input('Enter length of side 1: '))
        tss2=int(input('Enter length of side 2: '))
        tss3=int(input('Enter length of side 3: '))
        perimeter=tss1+tss2+tss3
        print('Perimeter is:\n',perimeter)
    else:
        print("Code not written for your triangle")
#square
elif shape=='square':
    ss=int(input("Enter length of 1 side: "))
    perimeter=4*ss
    print("Perimeter is:\n",perimeter)
