### Current Alg will only run 6 
from termcolor import colored 


class Matrix:
    
    def build(self):
        size_input = str(input("How big of a board would you like to solve (max 6x6): " ))
        size_input = size_input.strip(" ")
        size_input = int(size_input)

        matrix_grid = [[None for i in range(size_input)] for j in range(size_input)]

        return matrix_grid


test_grid = Matrix()
print(test_grid.build())