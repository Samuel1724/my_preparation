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


firstpattern(5)
secondpattern(5)
thirdpattern(6)