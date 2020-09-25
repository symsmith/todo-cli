import sys
import io
import os.path
from os import path

def list_tasks():
    """
    Prints todo.txt
    """
    dir_path = path.dirname(os.path.realpath(__file__))
    f = io.open(dir_path + '/todo.txt', 'r')

    for l in f:
        print(l, end="")

    f.close()

def get_tasks():
    """
    Returns all tasks and checking status
    as list of list
    """
    dir_path = path.dirname(os.path.realpath(__file__))
    t = []
    o = io.open(dir_path + '/todo.txt', 'r')
    f = o.readlines()
    for i in range(len(f)):
        # Ignore the first 4 lines (title)
        if i < 4:
            continue

        # If number < 10
        check = True
        if f[i][1] == " ":
            if f[i][2] == "☐":
                check = False
            t.append([f[i][5:-1], check])

        # If number >= 10
        else:
            if f[i][3] == "☐":
                check = False
            t.append([f[i][6:-1], check])
    o.close()
    return t

def build_file(tasks):
    """
    Builds the file todo.txt with the
    tasks well formatted
    """
    dir_path = path.dirname(os.path.realpath(__file__))
    f = io.open(dir_path + '/todo.txt', 'w', encoding='utf8')
    f.write("                ╓──────╖\n")
    f.write("                ║ TODO ║\n")
    f.write("                ╙──────╜\n\n")
    for i in range(len(tasks)):
        check = "☒" if tasks[i][1] else "☐"
        f.write(str(i+1) + " " + check + "  " + tasks[i][0] + "\n")
    f.close()
    

def help():
    """
    Prints help
    """
    print("Help:")
    print("`todo help` - shows this help")
    print("`todo` - lists all tasks")
    print("`todo add 'task'` - adds a task at the end")
    print("`todo toggle i1 i2 ... iN` - checks or unchecks tasks i1, i2, ..., iN")
    print("`todo remove i1 i2 ... iN` - removes tasks i1, i2, ..., iN")
    print("`todo clear` - removes all tasks\n")

def main(): 
    # Create file if it doesn't exist
    dir_path = path.dirname(os.path.realpath(__file__))
    if not path.exists(dir_path + '/todo.txt'):
        build_file([])

    tasks = get_tasks()

    # Handling functions
    if len(sys.argv) == 1:
        ...
    
    elif sys.argv[1] == "add" or sys.argv[1] == "+":
        if len(sys.argv) == 2:
            print("You need to specify a task to add!")
        else:
            task = ""
            for w in sys.argv[2:]:
                task += w + " "
            tasks.append([task[:-1], False])
    
    elif sys.argv[1] == "toggle" or sys.argv[1] == "check":
        if len(sys.argv) == 2:
            print("You need to specify tasks to toggle!")
        else:
            try:
                i = sys.argv[2:] # Strings
                for k in i:    
                    tasks[int(k)-1][1] = not tasks[int(k)-1][1]
            except:
                print("Be careful to specify the index of the tasks you want to toggle!\nEx: todo toggle 1 3 4")
    
    elif sys.argv[1] == "remove" or sys.argv[1] == "rm":
        if len(sys.argv) == 2:
            print("You need to specify a task to remove!")
        else:
            try:
                i = sys.argv[2:]
                a = int(i[0])
                confirm = input("Do you really want to remove these " + str(len(i)) + " tasks? (yes/no)\n-> ")
                if confirm == "yes":
                    i = sorted([int(k)-1 for k in i])
                    for k in range(len(i)):    
                        del tasks[i[k]-k]
            except:
                print("Be careful to specify the index of the task you want to remove!")
    
    elif sys.argv[1] == "clear":
        confirm = input("Do you really want to remove all the tasks? (yes/no)\n-> ")
        if confirm == "yes":
            tasks = []
    
    else:
        help()

    # All is done
    all_done = True
    for t in tasks:
        all_done &= t[1]
    if all_done and len(tasks) > 0:
        print("All done! Add a new task or remove the completed ones with clear.")

    # Build file
    build_file(tasks)
    list_tasks()
    if len(tasks) == 0:
        print("No task yet! Create one with `todo add 'task'`")

if __name__ == '__main__':
    main()