import json
import csv

txt_data="I like ASUS"
employees=["Hari","Sita","Gita","Ram"]
Employee={
    "Name":"Hari",
    "Age":25,
    "Salary":25000,
    "Job":"Developer"
}
A_employee=[["Name","Age","Salary","Job"],
            ["Tom",25,25000,"Developer"],
            ["Jerry",30,30000,"Manager"],
            ["Woody",35,35000,"CEO"],]
file_path = "output.txt"
# file_path = "output.json"
# file_path = "output.csv"
# with open(file_path,"w")as file:
#     file.write(txt_data)
#     print(f"Txt file {file_path} has been created.")
# try:
#     with open(file_path,"x")as file:
#         file.write(txt_data)
#         print(f"Txt file {file_path} has been created.")
# except FileExistsError:
#     print("That file already exists!")
# try:
#     with open(file_path,"a")as file:
#         file.write("\n"+txt_data)
#         print(f"Txt file {file_path} has been created.")
# except FileExistsError:
#     print("That file already exists!")
try:
    with open(file_path,"w")as file:
        for e in employees:
            file.write(e+"\n")
        print(f"Txt file {file_path} has been created.")
except FileExistsError:
    print("That file already exists!")
# try:
#     with open(file_path,"w")as file:
#         json.dump(Employee,file)
#         print(f"Json file {file_path} has been created.")
# except FileExistsError:
#     print("That file already exists!")
# try:
#     with open(file_path,"w",newline="")as file:
#         writer=csv.writer(file)
#         for row in A_employee:
#             writer.writerow(row)
#         print(f"Csv file {file_path} has been created.")
# except FileExistsError:
#     print("That file already exists!")