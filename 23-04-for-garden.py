from os import system
import time

garden = [   #index
    ".",     #0
    "v",     #1
    ".",
    ".",
    ".",
    ".",
    "v",
    ".",
    ".",     #8
    ".",     #9
]


### render the garden ###

while True:
    system('cls')
    print()

    for pi in range(len(garden)):
        print(garden[pi], end = '')

    print()
    print()


    ## stats ##
    count = 0
    for pi in range(len(garden)):
        if garden[pi] == 'v':
            count += 1 

    plants = count * 100 / len(garden)

    print(f'plants: {plants:3.0f} procent')

    print('\nACTIONS: \n1. plant\n2. gather\n3. exit')

    action = int(input('> '))

    if action == 1:
        idx = int(input('where (from 0 to 9)? '))
        if idx < 0 or idx > 9:
            print('range error')
            time.sleep(3)
            continue 
        if garden[idx] == 'v':
            print('already occupied')
            time.sleep(3)
            continue
        garden[idx] = 'v'
    
    if action == 2:
        idx = int(input('from where (from 0 to 9)? '))
        if idx < 0 or idx > 9:
            print('range error')
            time.sleep(3)
            continue
        elif garden[idx] == '.':
            print('nothing to gather')
            time.sleep(3)
            continue
        garden[idx] = '.'
    
    if action == 3:
        print('that is all')
        break