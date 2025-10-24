import os

def create_file(filename):
    try:
        with open(filename, "x") as f:
            print(f"File name {filename} is created succesfully")
    
    except FileExistsError:
        print(f"File name {filename} is already existed")
    
    except Exception as e:
        print("An error occured")


def view_all_files ():
    files = os.listdir()
    if not files:
        print("File is not found")
    else:
        print("File in directory")
        for file in files:
            print(file)



def delete_file (filename):
    try:
        os.remove(filename)
        print(f"File name {filename} is deleted successfully")
    except FileNotFoundError:
        print("file is not found")
    except Exception as e:
        print("An error occured")



def read_file(filename):
    try:
       with open("sample.txt", "r" ) as f:
          content =  f.read()
          print(f"Context of file name {filename} : \n{content}")
    except FileNotFoundError:
        print(f"File name {filename} is not found")
    except Exception as e:
        print("An error occured")           


def edit_file(filename):
    try:
        with open("sample.txt", "a") as f:
            content = input("Enter data to add")
            f.write(content + "\n")
            print(f"COntent added to {filename} successfully")
    except FileNotFoundError:
        print(f"File name {filename} is not found")
    except Exception as e:
        print("An error occured") 



def main():
    while True:
        print("File Manager System")
        print("1: to create  file")
        print("2: to view all files")
        print("3: to delete file")
        print("4: to read file")
        print("5: to Edit file")
        print("6: to Exit")

        choice = input("Enter you Choice(1 - 6) = ")

        if choice == "1":
            filename = input("Enter a file name to create = ")
            create_file(filename)

        elif choice == "2":
            view_all_files()

        elif choice == "3":
           filename = input("Enter your file name you want to delete = ")
           delete_file(filename)

        elif choice == "4":
          filename = input("Enter your file name you want to read = ")
          read_file(filename)

        elif choice == "5":
          filename = input("Enter your file name you want to edit = ")
          edit_file(filename)

        elif choice == "6":
          print("closing your system")
          break
        else:
            print("invalid Number Enter")

if __name__ == "__main__":
    main()

    