import os

file_path = "text.txt"
if os.path.exists(file_path):
    print(f"The file location '{file_path}' exists.")

    if os.path.isfile(file_path):
        print("This is a file")
    elif os.path.isdir(file_path):
        print("This is a directory")

else:
    print("The file location doesn't exist.")
