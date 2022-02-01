



    
def solution():

    colours = ['red', 'blue', 'yellow', 'orange', 'pink', 'green', 'violet']
    size_input = int(input("How big of a board would you like to solve (max 6x6): " ))
    colours = colours[:size_input]
    peices = [i for i in range(size_input)]

    colour_sort(colours, size_input)
    print('\n')
    peices_sort(peices, size_input)

    merge = {key:value for key, value in zip(peices, colours)}
    merge_lst = []
    for key, value in merge.items():
        temp_dict = {key:value}
        merge_lst.append(temp_dict)
    
    print('\n')
    peices_sort(merge_lst, size_input)
    


def colour_sort(colours, size_input):
    
    
    for i in range(size_input - 1, -1, -1):
        lst = [colours[i], colours[i - 1], colours[i - 2], 
        colours[i - 3], colours[i - 4], colours[i - 5]]
        
        
        print(lst)
        

def peices_sort(peices, size_input):

    for i in range(size_input - 1, -1, -1):
        lst = [peices[i], peices[i - 1], peices[i - 2], 
        peices[i - 3], peices[i - 4], peices[i - 5]]
        
        
        print(lst)



    





print(solution())
        