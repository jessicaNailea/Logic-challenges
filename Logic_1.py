
inputT= [5, (1, 1), (4, 4), (3,1), (3,3), (10000000000,80000000000)]

#case1: row = column    (R/L)
#case2: row > column    (U/D)
#case3: row < column    (R/L)

def selectCase(couple):
    if(couple[0] == couple[1]):
        return 1
    elif (couple[0] > couple[1]):
        return 2
    elif (couple[0] < couple[1]):
        return 3


def calculateDir(case, row, col):
    if(case == 1):
        if(row % 2 == 0):
            return 'L'
        else:
            return 'R'
    elif(case == 2):
        if (col % 2 == 0):
            return 'U'
        else:
            return 'D'
    else:
        if (row % 2 == 0):
            return 'L'
        else:
            return 'R'


def init():
    for i in inputT[1::]:
        case = selectCase(i)
        direction = calculateDir(case, i[0], i[1])
        print(direction)
init()
