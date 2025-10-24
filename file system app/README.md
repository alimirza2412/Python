# 🗂️ File Manager System

A simple command-line-based File Manager System built in Python.

It allows users to create, view, read, edit, and delete files directly from the terminal.

# 🚀 Features

Create File → Create a new file with a given name.

View All Files → Display all files available in the current directory.

Read File → Read and display the content of a selected file.

Edit File → Append new content to an existing file.

Delete File → Remove a specific file from the directory.

Exit System → Close the program safely.


# 🧩 Requirements

Python 3.x

Works on Windows, macOS, or Linux

# ⚙️ How to Run

Clone or Download the script into your local machine.

Open a terminal (or command prompt) in the script directory.

Run the following command:

python file_manager.py

Follow the on-screen menu to manage your files.

# 📘 Example Usage

File Manager System

1: to create  file

2: to view all files

3: to delete file

4: to read file

5: to Edit file

6: to Exit

Enter your Choice(1 - 6) = 1

Enter a file name to create = sample.txt

File name sample.txt is created successfully

# ⚠️ Notes & Fixes

In the functions read_file() and edit_file(), the filename is currently hardcoded as "sample.txt".

Update it to use the provided filename parameter instead:

with open(filename, "r") as f:

with open(filename, "a") as f:

Make sure you have the correct file permissions for creating/deleting files in the directory.

# 📄 License

This project is open source and available under the MIT License.
