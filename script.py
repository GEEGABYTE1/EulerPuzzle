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
    
    peices = [i for i in range(num_peices)]

    
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
                    self.ref_peices = current_set_of_peices[:]

                    for idx_matrix in range(len(current_row)):
                        current_peice = list(current_set_of_peices[idx_matrix].keys())[0]
                        current_colour = current_set_of_peices[idx_matrix][current_peice]

                        upper_peice = list(prev_row[idx_matrix].keys())[0]
                        upper_colour = list(prev_row[idx_matrix].values())[-1]

                        col_info = self.fetch_coloumn_peices(self.matrix)
                        col_colours = col_info[-1][idx_matrix]
                        col_peices = col_info[0][idx_matrix]

                        row_information = self.fetch_row_peices(current_row)
                        current_row_peices = row_information[0]
                        current_row_colours = row_information[-1]
                        

                        if upper_colour == current_colour and upper_peice == current_peice:
                            new_peice = current_set_of_peices[-1]
                            acc_peice = list(new_peice.keys())[0]
                            new_peice_colour = new_peice[acc_peice]


                            if not acc_peice in current_row_peices and not new_peice_colour in current_row_colours:
                                current_row[idx_matrix] = new_peice
                            if acc_peice in current_row_peices:
                                    counter = -1
                                    while acc_peice in current_row_peices:
                                         
                                        acc_peice = self.peices[counter]
                                        if acc_peice not in current_row_peices and acc_peice not in col_peices:
                                            break 
                                        else:
                                            counter +=1 
                                    
                                    list(current_set_of_peices[idx_matrix].keys())[0] = acc_peice
                                    current_row[idx_matrix] = {acc_peice:current_colour}
                                    continue
                                    
                            if new_peice_colour in current_row_colours:
                                counter = 0 
                                while new_peice_colour in current_row_colours:
                                    
                                    new_peice_colour = colours[counter]
                                    if new_peice_colour not in current_row_colours and new_peice_colour not in col_colours:
                                        break 
                                    else:
                                        counter += 1

                                current_set_of_peices[idx_matrix][current_peice] = new_peice_colour
                                current_row[idx_matrix] = {current_peice:new_peice_colour}
                                continue

                        elif current_colour in col_colours or current_colour in current_row_colours:
                            counter = 0 
                            while current_colour in col_colours or current_colour in current_row_colours:
                                new_colour = colours[counter]
                                if new_colour not in col_colours and new_colour not in current_row_colours:
                                    break 
                                else:
                                    counter += 1
                            
                            current_set_of_peices[idx_matrix][current_peice] = new_colour
                            current_row[idx_matrix] = {current_peice:new_colour}

                        elif current_peice in col_peices or current_peice in current_row_peices:
                            counter = 0 
                            while current_peice in current_row_peices or current_peice in col_peices:
                                new_peice = self.peices[counter]
                                if new_peice not in current_row_peices and new_peice not in col_peices:
                                    break 
                                else:
                                    counter += 1
                            
                            list(current_set_of_peices[idx_matrix].keys())[0] = new_peice
                            current_row[idx_matrix] = {new_peice:current_colour}
                        
                        else:
                            continue

                            
                        
                
    def fetch_row_peices(self, row):
        peices = []
        colours = []
        for dictionary in row:
            if type(dictionary) == dict:
                peices.append(list(dictionary.keys())[0])
                colours.append(list(dictionary.values())[-1])
            else:
                peices.append(None)
                colours.append(None)
    
        return peices, colours

    def fetch_coloumn_peices(self, matrix=matrix):
        columns = [[] for i in range(len(matrix))]
        colours = [[] for i in range(len(matrix))]
        peices = [[] for i in range(len(matrix))]

        counter = 0
        for j in range(len(self.matrix)):
            for i in range(len(self.matrix)):
                for col in self.matrix[i]:
                    if type(col) == dict:
                        colours[j].append(list(col.values())[0])
                        peices[j].append(list(col.keys())[0])
                    else:
                        colours[j].append(col)
                        peices[j].append(col)
                    break 
                continue
            counter += 1
        
        return peices, colours

        
                        

test = Solution()
print(test.algorithm())    
    


