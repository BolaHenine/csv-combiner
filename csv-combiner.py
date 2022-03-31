import sys
import csv
import os

def combine_files(file_list):
    #The combined rows that will be added to the output file in the end
    final_rows = []

    #Looping through the files to combine them
    for file in file_list:
        #Opening each of the files to combine them
        with open(file) as file_to_combines:
            reader = csv.reader(file_to_combines)             
            header = next(reader)
            file_name = os.path.basename(file)
            header.append('filename')
            for row in reader:
                row.append(file_name)
                final_rows.append(row)
    csv_output(final_rows)

#Writing the final combined csv files to the output file
def csv_output(final_rows):
    writer = csv.writer(sys.stdout)
    for i in final_rows:
        writer.writerow(i)

if __name__ == '__main__':
    combine_files(sys.argv[1:])