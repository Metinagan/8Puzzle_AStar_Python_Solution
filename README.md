#8-Puzzle_A-_Python_Solution


#initial matrix
startpos = [[0, 2, 3],
            [1, 4, 5],
            [7, 8, 6]]
![image](https://github.com/Metinagan/8Puzzle_AStar_Python_Solution/assets/130462728/1b1cbbbe-8d5d-469c-a3b2-33111a7065ee)

#end matrix
endpos = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 0]]

#Hamming value calculation
#If the elements in the same index of the matrices are different, we increase the hamming value by 1
def hamming(matris):
    hamming_Value = 0
    for x in range(3):
        for y in range(3):
            if matris[x][y] != endpos[x][y]:
                hamming_Value += 1
    return hamming_Value

#Mannathen value calculation.
#distance of the indexes of the current matrix to where they should be in the ending matrix.
#Subtraction must be done with absolute value.
#Because: If the element that should be at position [2][2] is at position [0][0], the distance gives a negative result.
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


#Heuristic value is the sum of mannathen and hamming values.
#heuristic value intuitively represents our distance from the outcome.
def heuristic(matris):
    return hamming(matris) + mannathen(matris)


#Returns the row and column containing element 0 in the matrix
def find_blanks(matris):
    for x in range(3):
        for y in range(3):
            if (matris[x][y] == 0):
                return x, y

#Adds to the list the places where the number 0 can move within the matrix
#clears the list before each step
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

#The function requires a matrix, row and column as values.
#If newly created matrices already exist, we do not add them to the list.
#This way we don't go through the same step again.
#and the function does not stay in an infinite loop
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

#We print the matrix.
#We give 2 seconds of sleep time. Because the matrixs flow so fast.
def printmatris(matris):
    for row in matris:
        for eleman in row:
            print(eleman, end=" ")
        print() 
    print("____________")
    time.sleep(2)
    
#Sıfır sayısının gidebileceği yere sıfır sayısını alıyoruz.
#Adds the new matrices we created to the list.
#This function creates matrices which will be one of our next steps.
def createneighbors(matris):
    neighbors_list.clear()
    node = [row[:] for row in matris]
    neighbors(node)
    for x in range(len(neighbors_list)):
        row,col=neighbors_list[x]
        change_blanks(node,row,col)



#A-Star Algorithm
def astar(matris):
    poslist.clear()         # clears the list on each iteration
    neighbors_list.clear()  # clears the list on each iteration
    list_hehur=[]            
    list_hehur.clear()
    if matris==endpos:      #if the current matrix is ​​equal to the ending matrix
        print("Bitti")
    else:
        node = [row[:] for row in matris]
        createneighbors(node)        #creates neighbors matrices of existing matrices
        for x in range(len(poslist)):      #for each neighbors matrix
            if poslist[x] in main_list:    
                pass
            else:
                heurvalue=heuristic(poslist[x])   # calculate heuristic value for every neighbors
                list_hehur.append(heurvalue)      # add calculated value to list
        minheur=min(list_hehur)                   # find minimum element in list
        minheurindex=list_hehur.index(minheur)    # find index with minimum element
        print("Adim: ",len(main_list))            # print step count
        main_list.append(poslist[minheurindex])   # add matrix with minimum heuristic value to main list
        print("heuristic=",minheur)               # print heuristic value
        printmatris(main_list[-1])                # print last element of main list
        astar(main_list[-1])                      # return function with last element of main list


#Clear main list and add starting matrix to the end of the list
#Finally send the last element of the main list to the function
main_list.clear()
main_list.append(startpos)
astar(main_list[-1])













