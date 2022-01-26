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
    ref_peices = None

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
                    self.ref_peices = current_set_of_peices[:-1]

                    for idx_matrix in range(len(current_row)):
                        current_set_of_peices = self.ref_peices
                        current_peice = list(current_set_of_peices[idx_matrix].keys())[0]
                        current_colour = current_set_of_peices[idx_matrix][current_peice]

                        upper_peice = list(prev_row[idx_matrix].keys())[0]
                        upper_colour = list(prev_row[idx_matrix].values())[-1]

                        col_peices = self.fetch_coloumn_peices(self.matrix)

                        if upper_colour == current_colour and upper_peice == current_peice:
                            new_peice = current_set_of_peices.pop()
                            acc_peice = list(new_peice.keys())[0]
                            new_peice_colour = new_peice[acc_peice]

                            row_information = self.fetch_row_peices(current_row)
                            current_row_peices = row_information[0]
                            current_row_colours = row_information[-1]


                            if not acc_peice in current_row_peices and not new_peice_colour in current_row_colours:
                                current_row[idx_matrix] = new_peice
                            elif acc_peice in current_row_peices:
                                    while acc_peice in current_row_peices:
                                        counter = 0 
                                        acc_peice = self.peices[counter]
                                        if acc_peice not in current_row_peices and acc_peice != upper_peice:
                                            break 
                                        else:
                                            counter +=1 
                            elif new_peice_colour in current_row_colours:
                                while new_peice_colour in current_row_colours:
                                    counter = 0 
                                    new_peice_colour = colours[counter]
                                    if new_peice_colour not in current_row_colours and new_peice_colour != upper_colour:
                                        break 
                                    else:
                                        counter += 1
                        
                    


    
    def fetch_row_peices(self, row):
        peices = []
        colours = []
        for dictionary in row:
            if type(dictionary) == dict:
                peices.append(list(dictionary.keys())[0])
                colours.append(list(dictionary.keys())[-1])
            else:
                peices.append(None)
                colours.append(None)
    
        return peices, colours

    def fetch_coloumn_peices(self, matrix=matrix):
        columns = [[] for i in range(len(matrix))]

        counter = 0
        for i in range(len(self.matrix)):
            for col in self.matrix[i]:
                columns[i].append(col)

        
                        

test = Solution()
print(test.algorithm())    
    


