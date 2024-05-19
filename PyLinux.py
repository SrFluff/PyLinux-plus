import os

if os.name == 'nt':

    uos = "Windows"

else:

    uos = "Unix-based OS"

def cls():

    os.system('cls' if os.name == 'nt' else 'clear')

pylinux = 0

pwd = "/"

root = ["user-files" , "about" , "extra-stuff"]

userfiles = ["PyLinuxPlus.txt"]

about = ["version.txt" , "credits.txt" , "license.txt"]

extrastuff = ["features.txt"]

ls = root

cls()

name = input("Please enter a name for yourself\n\n> ")

if name == "":

    name = "root"

cls()

host = input("Please enter a name for your PC\n\n> ")

if host == "":

    host = "PyLinux"

else:
    
    host = host

cls()

pylinux = 1

print("Type 'help' for a list of commands")

while pylinux:


    a = input(name + "@" + host + pwd +"$ ") 

    if a == "help":

        print("help - prints this help message")
        print("pwd - prints the working directory")
        print("ls - lists the contents the of the current directory")
        print("cd - changes the directory to a specified one")
        print("   ex - cd extra stuff")
        print("cat - reads a specified file")
        print("   ex - cat version.txt")
        print("whoami - prints all user information")
        print("chname - changes your user name")
        print("chhost - chnage the host name")
        print("clear - clears the screen")
        print("info - prints PyLinux information")
        print("credits - prints the credits")
        print("doc - print the PyLinux documentation")
        print("license - prints the license")
        print("map - show filesystem structure")
        print("echo - prints what you type after pressing enter, can show a file path if you type a filename")
        print("exit - close PyLinux")

        #The help message

    if a == "echo":

        cls()

        a = input("> ")

        cls()

        if a == "features.txt":

            print("/extra-stuff")

        if a == "PyLinuxPlus.txt":

            print("/user-files")

        if a == "pylinux.py":

            print("/user-files")

        if a == "version.txt":

            print("/about")

        if a == "credits.txt":

            print("/about")

        if a == "license.txt":

            print("/about")

        else:

            print(a)
    
    if a == "whoami":

        print("Name: " + name)
        print("Host: " + host)
        print("OS: " + uos)

    if a == "exit":

        cls()

        quit()
    
    if a == "clear":

        cls()

    if a == "chname":

        cls()

        print("Type your new name\n")

        name = input("> ")

        cls()

        print("Type 'help' for a list of commands")

    if a == "chhost":

        cls()

        print("Type your new host name\n")
        
        host = input("> ")

        cls()

        print("Type 'help' for a list of commands")
    
    if a == "pwd":

        print(pwd)

        #The pwd variable is set when you use cd and is also used at the promp screen

    if a == "ls":

        print(('   ').join(ls))

        #Same thing with ls, except ls is set to another variable that is a list, representing the contents of a directory
        #It also puts three spaces between each list item so you can tell the difference between them

    #The following lines are all the cd commands :3
    
    if a == "cd user files":

        ls = userfiles

        pwd = "/user-files"

    if a == "cd user-files":

        ls = userfiles

        pwd = "/user-files"

    if a == "cd /user-files":

        ls = userfiles

        pwd = "/user-files"

    if a == "cd /user files":

        ls = userfiles

        pwd = "/user-files"

    if a == "cd about":

        ls = about

        pwd = "/about"

    if a == "cd /about":

        ls = about

        pwd = "/about"

    if a == "cd /extra-stuff":

        ls = extrastuff

        pwd = "/extra-stuff"

    if a == "cd extra stuff":

        ls = extrastuff

        pwd = "/extra-stuff"

    if a == "cd /extra stuff":

        ls = extrastuff

        pwd = "/extra-stuff"

    #That's all folkes!

    if a == "cat PyLinuxPlus.txt":

        if ls == userfiles:

            print("This is PyLinux+")
            print("It's a more optomized version of PyLinux with some extra features, and some things trimmed down")
            print("Added stuff:\n")

            print("info")
            print("credits")
            print("license")
            print("doc")
            print("map")

    if a == "cat version.txt":

        if ls == about:

            print("You are running PyLinux+ v1.0.0")

    if a == "cat credits.txt":

        if ls == about:

            print("PyLinux+ v1.0.0 by Franco M. (SrFluff on GitHub) in Visual Studio Code by Microsoft with Python by Guido van Rossum, inspired by Linux by Linus Torvalds\n")

    if a == "cat license.txt":

        if ls == about:

            print("Licensed under the GNU public license\n")

    if a == "cat features.txt":

        if ls == extrastuff:

            print("PyLinux+ has its own documentation that can be accessed with the doc command")
            print("If you want to see the filesystem structure, type map")
            print("You can also access PyLinux info with the info command")
            print("If you want access the credits or license just type 'credits' or 'license'")

    if a == "info":

        print("PyLinux+ v1.0.0 'Mint chocolate chip'")
        print("Kernel: PyLinux kernel")
        print("Shell: No shell installed")
        print("Package manager: None installed")
        print("Packages: 0")
        print("Host: " + host)
        print("Commands: 14")

    if a == "credits":

        print("PyLinux+ v1.0.0 by Franco M. (SrFluff on GitHub) in Visual Studio Code by Microsoft with Python by Guido van Rossum, inspired by Linux by Linus Torvalds\n")

    if a == "license":

        print("Licensed under the GNU public license\n")

    #cd .. goes up one directory path
    
    if a == "cd ..":

        if ls == userfiles:

            ls = root

            pwd = "/"

        if ls == about:

            ls = root

            pwd = "/"

        if ls == extrastuff:

            ls = root

            pwd = "/"

    if a == "map":

        print("/")
        print("-> /user-files")
        print("-> /about")
        print("-> /extra-stuff\n")
        
        print("/user-files")
        print("     -> PyLinuxPlus.txt\n")

        print("/about")
        print("   -> version.txt")
        print("   -> credits.txt")
        print("   -> license.txt\n")

        print("/extra-stuff")
        print("      -> features.txt")

    if a == "doc":

        cls()
        
        print("PyLinux documentation\n")

        print("Navigating the file system\n")

        print("To print the current directory type 'pwd'")
        print("To list the contents of the current directory type 'ls'")
        print("To change directories, type 'cd' followed by the directory name, for example: 'cd example-directory'")
        print("To print the contents of a file type 'cat' followed by the file name, for example: 'cat file.txt'.")
        print("This only works if you're in the same directory as the specified file")
        print("To go up or back one directory path type 'cd ..'")
        print("To see the full file system structure type 'map'\n")

        print("User information\n")

        print("To see all user information type 'whoami'.")
        print("This will showw your name, password, and hostname.")
        print("To change your name type 'chname'")
        print("To change your host name type 'chhost'\n")

        print("Extra commands\n")

        print("To show the credits type 'credits'")
        print("To show the license type 'license'")
        print("To show the documentation type 'doc'")
        print("For help type 'help'")
        print("For OS information type 'info'")
        print("To clear the screen type 'clear'")
        print("To exit type 'exit'\n")

        print("Making your own distro\n")

        print("To add a file to your distro add it to the respective directory list, or make a new directory list and add the name of that directory to the list 'root', then add it to that list,")
        print("if you add a new file or directory add that to the map on line 229. If you add a directory add the cd commands for it on line 90, including the cd .. command. Once you add that file")
        print("to read it add its cat command on line 146, including the if ls == directory statement. To change the OS name change it on lines 164, 170, 189, 199, 13, 35, 43, 47, 66, 69, 71, 146,")
        print("150, 151, 164, 170, 182, 184, 189, 190, 199, and 235.")
        print("To add a new command add it to the help text on line 55, and add it to line 73.")
        print("If you create a new file you have to add it's file location to the echo command on line 91.\n")

        #Fixed a commit message