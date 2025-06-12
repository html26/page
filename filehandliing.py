b = input("file name: ")
def write():
    f = open(b+".txt","a")
    a = input("enter your contant:")
    print("----------------------------------------------------------------")
    f.write(a+"\n")
    f.close()
    return con()
def read():
    f = open(b+".txt")
    a = f.read()
    print(a)
    print("----------------------------------------------------------------")
    f.close()
    return con()
def erase():
    f = open(b+".txt","w")
    f.close()
    return con()
def menu2():
    a = input("""menu(2)
1.old file
2.new file
enter your option:""")
    print("----------------------------------------------------------------")
    return a
def file():
    a = menu2()
    b = input("enter your file name:")
    if a.lower() == "old" or a == "1":
        a = a
    elif a.lower() == "new" or a == "2":
        erase()
    else:
        a = a
    return con()
def menu():
    a = input("""menu
1.read
2.write
3.delete
4.exit
5.file settings
enter your option:""")
    print("----------------------------------------------------------------")
    return a
def con():
    a = menu()
    if a.lower() == "read" or a == "1":
        read()
    elif a.lower() == "write" or a == "2":
        write()
    elif a.lower() == "delete" or a == "3":
        erase()
    elif a.lower() == "exit" or a == "4":
        exit()
    elif a.lower() == "file" or a.lower() == "file setting" or a == "5":
        file()
    else:
        print("your option is wrong plz try again")
        return con()
con()