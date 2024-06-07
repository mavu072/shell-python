import sys


def main():
    sys.stdout.write("$ ")
    sys.stdout.flush()

    # Builtins
    builtins = ["exit", "echo", "type"]

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

        # Args
        if args in builtins:
            sys.stdout.write(f"{args} is a shell builtin\n")
        elif args == "cat":
            sys.stdout.write(f"{args} is /bin/cat\n")
        else:
            # Will be handled in not found
            command = args

    # Command not found
    if command not in builtins:
        sys.stdout.write(f"{command}: command not found\n")

    # REPL
    main()

if __name__ == "__main__":
    main()
