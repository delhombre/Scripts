#!/usr/bin/python3

import time
import os

#### Functions ####
def write_to_file(file_path):
    file = open_file(file_path, "a")
    if file:
        try:
            for index in range(1, 6):
                line = "This is line " + str(index)
                file.write(line + "\n")
        except:
            print(f"Error while writing ton file {file}", end="\n\n")
        finally:
            file.close()


def delete_file(file_path):
    print(f"*** Deleting file {file_path} ***", end="\n\n")
    if os.path.exists(file_path):
        os.remove(file_path)
        print()


def open_file(file_path, mode):
    try:
        file = open(file_path, mode)
    except FileNotFoundError:
        print(f"File {file_path} does not exist", end="\n\n")
        file = None
    except PermissionError:
        print(f"You do not have permission to access {file_path}", end="\n\n")
        file = None
    finally:
        return file


def read_file(file_path):
    print(f"Reading file {file_path} content")
    file = open_file(file_path, "r")
    if file:
        try:
            for line in file:
                if line == "\n":
                    continue
                print(line, end="")
                time.sleep(0.5)
        except:
            print(f"Error while reading the file {file}", end="\n\n")
        finally:
            file.close()


#### Main code ####
paths_list = ["/etc/hosts", "/etc/shells", "/etc/nofile", "/etc/shadow"]

for file_path in paths_list:
    read_file(file_path)
    print()

file_path = "tempo-file"
write_to_file(file_path)
read_file(file_path)
delete_file(file_path)
