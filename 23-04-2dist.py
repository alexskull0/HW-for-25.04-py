from os import system
import time
#matrix = [   #dimension 0
#    [1,2,3],    #0  |
#    [4,5,6],    #1  |
#    [7,8,9],    #2  |
                #....
#    0 1 2
#  dimension 1
#--------------->
#]               
#read ------------->

#строка, потом столбец

#print(matrix [1][2])

garden2d = [
    [".", ".", ".", ".", ".", ],
    [".", ".", ".", ".", ".", ],
    [".", "v", ".", "v", ".", ], #############
]

while True:
    system('cls')
    print()
    #len only for dimens 0
    for ri in range(len(garden2d)):
        print()
        for pi in range(len(garden2d[ri])):
            print(garden2d[ri][pi], end = ' ')

    print()
    print()

    ## stats ##
    count = 0
    for pi in range(len(garden2d[2])):
        if garden2d[2][pi] == 'v':
            count += 1 

    plants = count * 100 / len(garden2d[2])

    print(f'plants: {plants:3.0f} procent from the last row')

    print('\nACTIONS: \n1. plant\n2. gather\n3. exit')

    action = int(input('> '))

    if action == 1:
        idx = int(input('where (from 0 to 4)? '))
        if idx < 0 or idx > 4:
            print('range error')
            time.sleep(3)
            continue 
        if garden2d[2][idx] == 'v':
            print('already occupied')
            time.sleep(3)
            continue
        garden2d[2][idx] = 'v'
    
    if action == 2:
        idx = int(input('from where (from 0 to 4)? '))
        if idx < 0 or idx > 4:
            print('range error')
            time.sleep(3)
            continue
        elif garden2d[2][idx] == '.':
            print('nothing to gather')
            time.sleep(3)
            continue
        garden2d[2][idx] = '.'
    
    if action == 3:
        print('that is all')
        break