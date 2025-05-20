#Doormat Design
dmt=str(input('Enter doormat text: '))
val=1
var=' '
for outerlooploopvar in range(val):
    print('-----',end=(var))
    for innerloopvar in range(outerlooploopvar+1):
        var=' '
        print('-----',end=(var))
    print()
    print('  ---',end='---')
    print('\n|',dmt,' |')
    print('  ---',end='---')
    print('\n --------',end=' ')