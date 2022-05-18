import os
import csv
from pprint import pprint

filename = '/home/arsh/scripts/webdashnew.csv'
fileds = []
rows = []

moved = []
not_moved = []

with open(filename,'r') as csvfile:
    csvreader = csv.reader(csvfile)
     
    # extracting field names through first row
    fields = next(csvreader)
 
    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)

    #pprint(fields)
    #pprint(rows)

    for row in rows:
        folder_to_check_in = '/home/arsh/scripts/renewal-16May'
        files = os.listdir(folder_to_check_in)
        folder_to_move_in = '/home/arsh/scripts/move_folder'

        for cell in row:
            cell+='.conf'
            if cell in files:
                print(f'File copied - {cell}')
                moved.append(cell)
                os.system(f'cp {folder_to_check_in}/{cell} {folder_to_move_in}/')
            else:
                print(f'Not Copied - {cell}')
                not_moved.append(cell)
                
    print('Files Moved:-')
    for i in moved:
        print(i)
    print(f'Total Files Moved - {len(moved)}')
    
    print('\n\n')

    print('Files not moved:-')
    for i in not_moved:
        print(i)
    print(f'Total Files not moved - {len(not_moved)}')