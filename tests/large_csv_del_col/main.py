import os
import csv

def create_large_csv(rows:int)->None:
    with open("large.csv", "w") as file:
        file.write("Username; Identifier;First name;Last name\n")
        file.writelines(["booker12;9012;Rachel;Booker\n" for i in range(rows)])
    pass

def remove_csv_column(filename:str, column_index:str)->None:
    temp_filename = filename + '.tmp'
    with open(filename, 'r', newline='') as infile, open(temp_filename, 'w', newline='') as outfile:
        reader = csv.reader(infile, delimiter=';')
        writer = csv.writer(outfile, delimiter=';')
        for row in reader:
            del row[column_index]
            writer.writerow(row)
    os.replace(temp_filename, filename)
    pass

def main():
    os.chdir(os.path.dirname(__file__))
    print("--- begin ---")
    # create_large_csv(4000000)
    remove_csv_column('large.csv', 2)

if __name__ == "__main__":
    main()