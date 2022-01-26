### Current Alg will only run 6 
from termcolor import colored 

colours = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

class Matrix:
    
    def build(self):
        size_input = str(input("How big of a board would you like to solve (max 6x6): " ))
        size_input = size_input.strip(" ")
        size_input = int(size_input)
        if size_input > 6:
            print("That board is currently unavailable")
            return False
        else:
            matrix_grid = [[None for i in range(size_input)] for j in range(size_input)]

            return matrix_grid, size_input


class Solution:
    grid_info = Matrix()
    grid_info = grid_info.build()
    matrix = grid_info[0]
    num_peices = grid_info[-1]

    peices = [] 
    for i in range(num_peices):
        peices.append(i)
    
    colored_peices = []
    
    for peice in peices:
        lst = [] 
        for colour in colours:
            dictionary = {peices.pop():colour}
            lst.append(dictionary)
        colored_peices.append(lst)

    
    lst_setup = []
    for i in range(num_peices):
        lst_setup.append(colored_peices[0])
    
    

test = Solution()
print(test)    
    


