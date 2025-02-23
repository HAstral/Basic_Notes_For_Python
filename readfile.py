import json
import csv
# file_path="output.txt"
# file_path="output.json"
file_path="output.csv"
try:
    with open(file_path,"r")as file:
        # content=file.read()
        # content=json.load(file)
        # print(content)
        content=csv.reader(file)
        for line in content:
            print(line[2])
except FileNotFoundError:
    print("File has not been found.")
except PermissionError:
    print("You do not have permission to open this file.")