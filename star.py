import time

main_list = []
neighbors_list = []
poslist = []

startpos = [[0, 2, 3],
            [1, 4, 5],
            [7, 8, 6]]

endpos = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 0]]


def hamming(matris):
    hamming_Value = 0
    for x in range(3):
        for y in range(3):
            if matris[x][y] != endpos[x][y]:
                hamming_Value += 1
    return hamming_Value

def mannathen(matris):
    mannathen_value = 0
    for x in range(3):
        for y in range(3):
            if matris[x][y] != 0:
                for k in range(3):
                    for l in range(3):
                        if matris[x][y] == endpos[k][l]:
                            value = abs(l - y) + abs(k - x)
                            mannathen_value += value
    return mannathen_value

def heuristic(matris):
    return hamming(matris) + mannathen(matris)

def find_blanks(matris):
    for x in range(3):
        for y in range(3):
            if (matris[x][y] == 0):
                return x, y

def neighbors(matris):
    neighbors_list.clear()
    row, col = find_blanks(matris)
    if row > 0:
        neighbors_list.append([row - 1, col])
    if row < 2:
        neighbors_list.append([row + 1, col])
    if col > 0:
        neighbors_list.append([row, col - 1])
    if col < 2:
        neighbors_list.append([row, col + 1])

def change_blanks(matris, row, col):
    zerorow, zerocol = find_blanks(matris)
    node = [row[:] for row in matris]
    new = node[row][col]
    node[zerorow][zerocol] = new
    node[row][col] = 0
    if node in main_list:
        pass
    else:
        poslist.append(node)

def printmatris(matris):
    for row in matris:
        for eleman in row:
            print(eleman, end=" ")
        print() 
    print("____________")
    time.sleep(2)


def createneighbors(matris):
    neighbors_list.clear()
    node = [row[:] for row in matris]
    neighbors(node)
    for x in range(len(neighbors_list)):
        row,col=neighbors_list[x]
        change_blanks(node,row,col)


def astar(matris):
    poslist.clear()
    neighbors_list.clear()
    list_hehur=[]
    list_hehur.clear()
    if matris==endpos:
        print("bitti")
    else:
        
        node = [row[:] for row in matris]
        createneighbors(node)
        for x in range(len(poslist)):
            if poslist[x] in main_list:
                pass
            else:
                heurvalue=heuristic(poslist[x])     # calculate heuristic value for every neighbors
                list_hehur.append(heurvalue)        # add calculated value to list
        minheur=min(list_hehur)                     # find minimum element in list
        minheurindex=list_hehur.index(minheur)      # find index with minimum element
        print("Adim: ",len(main_list))              # print step count
        main_list.append(poslist[minheurindex])     # add matrix with minimum heuristic value to main list
        print("heuristic=",minheur)                 # print heuristic value
        printmatris(main_list[-1])                  # print last element of main list
        astar(main_list[-1])                        # return function with last element of main list
        

main_list.clear()
main_list.append(startpos)
astar(main_list[-1])







