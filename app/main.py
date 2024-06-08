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
    builtins = ["exit", "echo", "type"]

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

    # Echo command
    elif command == "echo":
        sys.stdout.write(f"{args}\n")

    # Type command
    elif command == "type":
        # Find executable in PATH 
        executable = None
        for pathvar in pathvars:
            if os.path.isfile(f"{pathvar}/{args}"):
                executable = f"{pathvar}/{args}"
                break

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
    elif command not in builtins:
        sys.stdout.write(f"{command}: command not found\n")

    # REPL
    main()

if __name__ == "__main__":
    main()
