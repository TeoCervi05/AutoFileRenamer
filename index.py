import os
import time

os.chdir(os.path.expanduser("~"))

def change(p1, path):

    if len(p1) > 0:
        if p1[0] != "-":
            path = p1
            p1 = ""

    if p1 in ["-u", "-U", "-up", "-UP"]:

        if path == "":
            os.chdir("..")
        
        else:
            print(" " + p1.lower() + " doesn't need a path information, do you mean -e?")

    elif p1 in ["-m", "-M", "-main", "-MAIN"]:

        if path == "":
            os.chdir(os.path.expanduser("~"))
        
        else:
            print(" " + p1.lower() + " doesn't need a path information, do you mean -e?")

    elif p1 in ["-e", "-E", "-enter", "-ENTER"]:
        
        if path == "":
            path = input(" Enter the new path: ")
        
        try:
            os.chdir(os.path.abspath(os.curdir) + path)

        except:
            print(" ERROR: This folder doesn't seems to exist")

    elif p1 == "":

        try:
            os.chdir(path)

        except:
            print(" ERROR: This folder doesn't seems to exist")

    else:
        print(" " + p1 + " is not a valid parameter")

    inputLine()

def clear(p1):

    if p1 in ["-t", "-title", "-T", "-TITLE"]:
        os.system("cls")
        title()

    elif p1 == "":
        os.system("cls")
        inputLine()

    else:
        print(" " + p1 + " is not a valid parameter")
        inputLine()

#def changeExtension(p1):
    #if p1 in ["-o", "-original", "-O", "-ORIGINAL"]:
        #print(" Extension now set on original")
        #return("original")

    #else:
        #newExt = input("  What will the extension be (do not use .)? ")
        #print(" Extension now set on ." + newExt)
        #return(newExt)

def help():
    print(" change (\"path\") = change to another path;\n clear = delete all previous text;\n exit = terminate this session;\n help = show general command list;\n extension = set the final extension of your files; \n list = list all the files and subdirectories of the current path;\n start = start renaming process.")
    inputLine()

def parameter(command):

    if command == "change":
        print("  CHANGE:\n -e or -enter = enter a path from the current folder;\n -h or -help = -h or -help = show a list of parameter for this command;\n -m or -main = go back to the user folder;\n -u or -up = go to parent folder.")

    elif command == "clear":
        print("  CLEAR:\n -h or -help = show a list of parameter for this command;\n -t or -title = show titlescreen after deleting previous test.")

    elif command == "exit":
        print("  EXIT:\n -h or -help = -h or -help = show a list of parameter for this command.")

    elif command == "extension":
        print("  EXTENSION:\n -h or -help = -h or -help = show a list of parameter for this command;\n -o or -original = use the original extension of the file.")

    elif command == "help":
        print("  HELP:\n seriously?")

    elif command == "list":
        print("  LIST:\n -d or -directories = show only subdirectories; \n -f or -files = show only files;\n -h or -help = -h or -help = show a list of parameter for this command.")
    
    elif command == "start":
        print("  START:\n -h or -help = -h or -help = show a list of parameter for this command.")

    else:
        print(" invalid command, try to check the spell")

    inputLine()

def listDir(p1):
    content = os.listdir(os.path.abspath(os.curdir))
    dirs = [d for d in content if os.path.isdir(os.path.abspath(os.curdir) + "/" + d)]
    files = [f for f in content if os.path.isfile(os.path.abspath(os.curdir) + "/" + f)]

    if p1 in ["-f", "-F", "-files", "-FILES", "-d", "-D", "-directories", "-DIRECTORIES", ""]:

        if not p1 in ["-f", "-F", "-files", "-FILES"]:
            for x in dirs:
                print(" - \\" + x)

        if not p1 in ["-d", "-D", "-directories", "-DIRECTORIES"]:
            for x in files:
                print(" - " + x)

    else:
        print(" " + p1 + " is not a valid parameter")

    inputLine()

def start():
    content = os.listdir(os.path.abspath(os.curdir))
    files = [f for f in content if os.path.isfile(os.path.abspath(os.curdir) + "/" + f)]
    
    print(" PATH: " + os.path.abspath(os.curdir))
    print(" RENAMING ORDER: " + order)
    print(" EXTENSION: " + extension)
    print(" FOLDER CONTENT (files):")
    
    for x in files:
        print(" - " + x)

    i = 1

    while i < 2:
        confirm = input(" Do you want to rename files in this folder? (y or n).> ")

        if confirm in ["n", "N"]:
            print(" operation aborted")
            break
    
        elif confirm in ["y", "Y"]:
            print(" LEGEND:\n  Use those instruction inside the new name\n  \\n = Standard numbers (1, 2, 3, ecc...)\n  \\n0 = Two digits numbers (01, 02, 03...)\n  \\n* = Standard numbers from zero (0, 1, 2, ecc...)\n  \\n*0 = Two digits numbers from zero (00, 01, 02, ecc...)")
            newNameRaw = input(" How do you want to rename those files?.> ")

            x = 0

            for file in files:
                newName = newNameRaw.split()
                
                if extension == "original":
                    oldName, ext = os.path.splitext(os.path.abspath(os.curdir) + file)

                else:
                    ext = "." + extension

                y = 0

                for word in newName:
                    
                    if word == "\\n":
                        newName [y] = str(x + 1)

                    elif word == "\\n0":

                        if x < 10:
                            newName [y] = "0" + str(x + 1)

                        else:
                            newName [y] = str(x + 1)

                    elif word == "\\n*":
                        newName [y] = str(x)

                    elif word == "\\n*0":

                        if x < 10:
                            newName [y] = "0" + str(x)

                        else:
                            newName [y] = str(x)
                        
                    y = y + 1
                
                separator = " "
                finalName = separator.join(newName)

                try:
                    os.rename(os.path.abspath(os.curdir) + "\\" + file, os.path.abspath(os.curdir) + "\\" + finalName + ext)
                    print(" - " + finalName + ext)
                
                except:
                   print(" ERROR: " + finalName + ext + " is not a valid name")
                
                x = x + 1

            break

        else:
            print(" Please answer: y or n")

    inputLine()

def title():
    print("     __                     ______              _____\n    /  \\                   |  ____|            |  _  \\ \n   / /\\ \\        ___  __   | |____  .      __  | |_| /   __                 __  _\n  / ____ \\  |  |  |  /  \\  |  ____| | |   |__  |     \\  |__ |\\ |  /\\  |\\/| |__ |_)\n /_/    \\_\\ \\__/  |  \\__/  |_|      | |__ |__  |__|\\__\\ |__ | \\| /--\\ |  | |__ | \\ ")
    print("                                                                         by TeoCervi05\n\nWrite \"help\" to see a list of commands,\nwrite \"(command) -h\" or \"(command) -help\" to see a list of parameter for that command.\nEnjoy!!! ;-)\n")
    inputLine()

def inputLine():
    inLine = input("\n" + os.path.abspath(os.curdir) + ".> ")
    command = inLine.split()

    if len(command) >= 2 and command[1] in ["-h", "-H", "-help", "-HELP"]:
        parameter(command [0])

    elif len(command) == 0:
        inputLine()
    
    elif command [0] in ["change", "CHANGE"]:

        if len(command) == 1:
            path = input(" Enter the new path: ")
            change("", path)

        elif len(command) == 2:
            change(command [1], "")

        elif len(command) == 3:
            change(command [1], command [2])

        elif len(command) > 3:
            pathAr = []

            for i in range(2, len(command)):
                pathAr.append(command [i])
            
            path = " ".join([str(i) for i in pathAr])
            change(command [1], path)

    elif command [0] in ["clear", "CLEAR"]:

        if len(command) == 1:
            clear("")

        elif len(command) == 2:
            clear(command [1])

        elif len(command) > 2:
            print(" \"clear\" accept max one parameter.")
            inputLine()

    elif command [0] in ["exit", "EXIT"]:

        if len(command) > 1:
            print(" " + command [1] + " is not a valid parameter.")
            inputLine()

        else:
            print("goodbye ;-)")
            time.sleep(1)
            exit()

    #elif command [0] in ["extension", "EXTENSION"]:

        #if len(command) == 1:
            #extension = changeExtension("")
            #inputLine()

        #elif len(command) == 2:
            #extension = changeExtension(command [1])
            #inputLine()

        #elif len(command) > 2:
            #print(" \"extension\" accept max one parameter.")
            #inputLine()

    elif command [0] in ["help", "HELP"]:

        if len(command) > 1:
            print(" " + command [1] + " is not a valid parameter.")
            inputLine()
        
        else:
            help()

    elif command [0] in ["list", "LIST"]:
        
        if len(command) == 1:
            listDir("")

        elif len(command) == 2:
            listDir(command [1])

        elif len(command) > 2:
            print(" \"clear\" accept max one parameter.")
            inputLine()

    elif command [0] in ["start", "START"]:
        if len(command) == 1:
            start()

        else:
            print(" \"start\" doesn't accept any parameter.")
            inputLine()

    else:
        print(" invalid command, try to check the spell.")
        inputLine()

order = "alphabetical"
extension = "original"
title()