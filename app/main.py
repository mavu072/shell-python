import sys


def main():
    sys.stdout.write("$ ")
    sys.stdout.flush()

    # Builtins
    builtins = ["exit 0", "echo"]

    # Wait for user input
    command = input()

    # Echo command
    if command.startswith("echo"):
        args = command.removeprefix("echo")
        command = "echo"
        sys.stdout.write(f"{args}\n")

    # Command not found
    if command not in builtins:
        sys.stdout.write(f"{command}: command not found\n")

    # REPL or Exit
    if command == "exit 0":
        sys.exit(0)
    else:
        main()

if __name__ == "__main__":
    main()
