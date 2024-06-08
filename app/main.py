import sys
import os

def main():
    sys.stdout.write("$ ")
    sys.stdout.flush()

    # Builtins
    builtins = ["exit", "echo", "type"]

    # PATH variable
    PATH = os.environ["PATH"]

    # Executables
    executables = PATH.split(":")

    # Wait for user input
    command = input()

    # Exit command
    if command == "exit 0":
        sys.exit(0)

    # Echo command
    elif command.startswith("echo"):
        args = command.removeprefix("echo").strip()
        command = "echo"
        sys.stdout.write(f"{args}\n")

    # Type command
    elif command.startswith("type"):
        args = command.removeprefix("type").strip()
        command = "type"

        # Find executable in PATH 
        executable = None
        for pathvar in executables:
            if pathvar.endswith(args):
                executable = pathvar
                break

        # Executables - In PATH
        if executable is not None:
            sys.stdout.write(f"{args} is {executable}\n")
        # Builtins
        elif args in builtins:
            sys.stdout.write(f"{args} is a shell builtin\n")
        # Cat
        elif args == "cat":
            sys.stdout.write(f"{args} is /bin/cat\n")
        # Not found
        else:
            sys.stdout.write(f"{args}: command not found\n")

    # Command not found
    elif command not in builtins:
        sys.stdout.write(f"{command}: command not found\n")

    # REPL
    main()

if __name__ == "__main__":
    main()
