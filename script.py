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
    
    initial_perm = lst_setup[0]
    for row in matrix:
        for element in range(len(row)):
            row[element] = initial_perm[element]
        break

    
    def algorithm(self):
        for term in range(len(self.matrix)):
            if term == 0:
                continue 
            else:
                for peice_color in range(len(self.lst_setup)):
                    current_row = self.matrix[term]
                    prev_row = self.matrix[term - 1] 
                    current_set_of_peices = self.lst_setup[peice_color]

                    for idx_matrix in range(len(current_row)):
                        current_peice = list(current_set_of_peices[idx_matrix].keys())[0]
                        current_colour = current_set_of_peices[idx_matrix][current_peice]

                        upper_peice = list(prev_row[idx_matrix].keys())[0]
                        upper_colour = list(prev_row[idx_matrix].values())[-1]

                        if upper_colour == current_colour and upper_peice == current_peice:
                            new_peice = current_set_of_peices.pop()
                            acc_peice = [new_peice.keys()][0]
                            new_peice_colour = new_peice[acc_peice]

                            row_information = self.fetch_row_peices(current_row)
                            current_row_peices = row_information[0]
                            current_row_colours = row_information[-1]
                            

                            

                            current_row[idx_matrix] = new_peice

    
    def fetch_row_peices(self, row):
        peices = []
        colours = []
        for dictionary in row:
            peices.append(list(dictionary.keys())[0])
            peices.append(list(dictionary.keys())[-1])
    
        return peices, colours
        
                        

test = Solution()
print(test.algorithm())    
    


