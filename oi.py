import os
import shutil
import time

print("Welcome to File/Directory/Folder Ultimate Remover")
print("You're Welcomed to 'taste' this Great-Glorious Program")
print("Also Created by The Great-Glorious Programmer ever lived, Alvaro :3")
print(" ")
time.sleep(5)
ask=input("You Want to Delete File or Directory or Both (f/dir/bth), Perhaps your ex :v : ")

try:
    if ask == "dir"  :
        fs1 = input("are you sure to delete a file or empty folder? (y/n) ")
        time.sleep(5)
        if fs1 == "y":
            os.rmdir(input("Path to the directory: "))
            print("Completed Successfully")
            time.sleep(3)
        
        elif fs1 == "=" :
            print("Thx for using this program")
            time.sleep(10)
            pass

        else:
            print("You put the wrong command, or your input is unrecognized")
            print("Adios.")
        


    elif ask == "f":
        fs2 = input("are you sure to delete a file ? (y/n) ")
        time.sleep(5)
        if fs2 == "y":
            os.remove(input("path to the file: "))
            print("Completed Successfully")
            time.sleep(3)

        elif fs2 == "=" :
            print("Thx for using this program")
            time.sleep(10)
            pass

        else:
            print("You put the wrong command, or your input is unrecognized")
            print("Adios.")

    elif ask == "bth":
        fs3 = input("are you sure to delete files and or folders ? (y/n) ")
        time.sleep(5)
        if fs3 == "y":
            shutil.rmtree(input("path to the folder: "))
            print("Completed Successfully")
            time.sleep(3)

        elif fs3 == "=" :
            print("Thx for using this program")
            time.sleep(10)
            pass

        else:
            print("You put the wrong command, or your input is unrecognized")
            print("Adios.")



except PermissionError:
    print("Cannot Execute Commands")
    print("Permission Denied")
          
except FileNotFoundError:
    print("File Not Found")

except OSError:
    print("That Folder Contain File(s)")