import sys


def main():
    sys.stdout.write("$ ")
    sys.stdout.flush()

    # Builtins
    builtins = ["exit 0"]

    # Wait for user input
    command = input()

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
