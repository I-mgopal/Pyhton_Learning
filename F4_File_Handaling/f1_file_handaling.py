import os

# Create a new file (write mode)
w = open(r"F4_File_handaling\file1.txt", 'w')
w.write("Hi, I am writing inside the file1")
w.close()  # Always close after writing

# Check if file exists
if os.path.exists(r"F4_File_handaling\file1.txt"):
    print("File1 exists")

# Read the content from the file
r = open(r"F4_File_handaling\file1.txt", 'r')
print(r.read())
r.close()  # Always close after reading

# -------------------------------------- OR ---------------------------------------------------

# Define file path
folder = "F4_File_handaling"
filename = "file2.txt"
filepath = os.path.join(folder, filename)

# Folder already exists from above, but safe to check again
if not os.path.exists(folder):
    os.makedirs(folder)

# Create a new file (write mode)
w = open(filepath, 'w')
w.write("Hi, I am writing inside the file2")
w.close()  # Always close after writing

# Check if file exists
if os.path.exists(filepath):
    print("File2 exists")

# Read the content from the file
r = open(filepath, 'r')
print(r.read())
r.close()  # Always close after reading

# Delete file
# os.remove(r"File_handaling\file1.txt")
