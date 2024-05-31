def firstpattern(n):
    for i in range(n):
        for j in range(n):
            print("*", end='')
        print()

def secondpattern(n):
    for i in range(n):
        for j in range(i):
            print("*", end='')
        print()

def thirdpattern(n):
    for i in range(n):
        for j in range(i):
            print(j+1, end='')
        print()

def fourthpattern(n):
    for i in range(n):
        for j in range(i):
            print(i, end='')
        print()

def fifthpattern(n):
    for i in range(n):
        for j in range(n-i):
            print('*', end='') 
        print()

def sixthprint(n):
    for i in range(n): 
        for j in range(n-i):
            print(j+1, end='')
        print()


def seventhpattern(n):
    for i in range(n):
        for j in range(n-i-1):
            print(' ', end='')
        for k in range(2*i+1):
            print('*', end='')
        print()

def eigthpattern(n):
    for i in range(n, 0, -1):
        for j in range(n-i):
            print(' ', end='')
        for j in range(2*i-1):
            print('*', end='')
        print()




firstpattern(5)
secondpattern(5)
thirdpattern(6)
fourthpattern(6)
fifthpattern(5)
sixthprint(5)
seventhpattern(5)
eigthpattern(5)