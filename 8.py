import random
import copy

def create_puzzle():
    square = [[1,2,3],
			  [4,5,6],
			  [7,8,0]]
    pozof0 = [2,2]
    n = 20
    while n > 0:
        
        ok = False     
        while ok == False:
            direction = random.choice([0,1]) # axa x sau y
            increment = random.choice([-1,1]) # directia pe axa aleasa
            if pozof0[direction]+increment<0 or pozof0[direction]+increment>2:
                ok = False
            else:
                ok = True
                new_pozof0 = pozof0[:]
                new_pozof0[direction]+=increment
                square[pozof0[0]][pozof0[1]], square[new_pozof0[0]][new_pozof0[1]] = square[new_pozof0[0]][new_pozof0[1]], square[pozof0[0]][pozof0[1]]
                pozof0 = new_pozof0[:]
        n-=1
    return square

def find_position_of_0(square):
    for i in range(len(square)):
        for j in range(len(square[i])):
            if square[i][j]==0:
                return (i,j)
            
def find_neighbors(poz):
    neighbors = []
    for increment in [-1,1]:
        if poz[0] + increment >= 0 and poz[0] + increment < 3:
            neighbors.append((poz[0] + increment, poz[1]))
        if poz[1] + increment >= 0 and poz[1] + increment < 3:
            neighbors.append((poz[0], poz[1] + increment))
    return neighbors

def print_square(square):
    print('---------')
    for row in square:
        print(row)

def solve_puzzle(square, len, max_len):  

    solution = [[1,2,3],[4,5,6],[7,8,0]]

    if square == solution:
        print_square(square)
        return True

    if len == max_len:
        return False
    
    poz_of_0 = find_position_of_0(square)
    neighbors = find_neighbors(poz_of_0)

    for coords in neighbors:
        square_aux = copy.deepcopy(square)
        square_aux[poz_of_0[0]][poz_of_0[1]], square_aux[coords[0]][coords[1]] = square_aux[coords[0]][coords[1]], square_aux[poz_of_0[0]][poz_of_0[1]]
        
        rez = solve_puzzle(square_aux, len+1, max_len)
        if rez == True:
            print_square(square)
            return True
    return False



square1 = create_puzzle()
print_square(square1)
print('/////////')

rez = False
maxi = 10
while rez == False:
    print(maxi)
    rez = solve_puzzle(square1, 0, maxi)
    if maxi<15:
        maxi+=1
    else:
        maxi+=5
