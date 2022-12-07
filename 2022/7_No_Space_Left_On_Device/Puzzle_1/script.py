#!/usr/bin/env python3


file_system = {"/":{}}
pwd = "/"

with open("input", 'r') as file:
    for line in file:
        if line[0] == "$":
            if line[2:4] == "cd":
                if line[5] == "/":
                    continue
                elif line[5:7] == "..":
                    pwd = ".".join(pwd.split(".")[0:len(pwd) - 1])
                else:
                    pwd = pwd + "." + line.rstrip()[5:]
                    file_system_pointer = file_system
                    print("PWD:" + pwd)
                    for idx, directory in enumerate(pwd.split(".")):
                        print("Directory: " + directory)
                        if idx == len(pwd.split()) - 1:
                            file_system_pointer[line.rstrip()[5:]] = {}
                        file_system_pointer = file_system_pointer[directory]
                        print(file_system_pointer)

print(file_system)
