
import os

path = input("Enter the Directory:")
# Creating a list of all directories
file_attributes = [(root, dirs, files) for root, dirs, files in os.walk(path)]

print("List of all sub-directories and files:")
for root, dirs, files in file_attributes:
    print("Directory:", root)
    for file in files:
        print("File:", os.path.join(root, file))

