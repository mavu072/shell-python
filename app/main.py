import sys
import os

def find_executable(filename):
    # PATH variables
    pathvars =  os.environ.get("PATH").split(":")
    # Locate PATH var
    for pathvar in pathvars:
        if os.path.isfile(f"{pathvar}/{filename}"):
            return f"{pathvar}/{filename}"
    return None

def main():
    sys.stdout.write("$ ")
    sys.stdout.flush()

    # Builtins
    builtins = ["exit", "echo", "type", "pwd", "cd"]

    # PATH
    PATH = os.environ.get("PATH")

    # PATH variables
    pathvars = PATH.split(":")

    # Wait for user input
    commandline = input()
    
    # Read command line input
    cmdarr = commandline.split(None)

    # Command
    command = cmdarr[0]

    # Arguments
    args = commandline.removeprefix(command).strip()

    # Executable file
    executablefile = find_executable(command)

    # Exit command
    if commandline == "exit 0":
        sys.exit(0)

    # Executable
    elif executablefile:
        # Execute file with command and arguments
        os.system(commandline)

    # Builtins
    elif command in builtins:
        # Handle builtin command
        match command:
            # CD command
            case "cd":
                cwd = os.getcwd()
                dir = args

                # HOME path
                if args == "~":
                    dir = os.environ.get("HOME")

                # Relative path
                if args.startswith("."):
                    # Navigate down the directory tree by one folder
                    dir = os.path.join(cwd, args)
                    dir = os.path.normpath(dir)

                # Is file or directory
                if os.path.exists(dir):
                    os.chdir(dir)
                # Not file or directory
                else:
                    sys.stdout.write(f"{dir}: No such file or directory\n")
            # PWD command
            case "pwd":
                cwd = os.getcwd()
                sys.stdout.write(f"{cwd}\n")
            # Echo command
            case "echo":
                sys.stdout.write(f"{args}\n")
            # Type command
            case "type":
                # Find executable in PATH 
                executable = find_executable(args)
                # Builtins
                if args in builtins:
                    sys.stdout.write(f"{args} is a shell builtin\n")
                # Executables - In PATH
                elif executable is not None:
                    sys.stdout.write(f"{args} is {executable}\n")
                # Not found
                else:
                    sys.stdout.write(f"{args} not found\n")

    # Command not found
    else:
        sys.stdout.write(f"{command}: command not found\n")

    # REPL
    main()

if __name__ == "__main__":
    main()
