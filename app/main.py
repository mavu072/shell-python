import sys


def main():
    sys.stdout.write("$ ")
    sys.stdout.flush()

    # Wait for user input
    command = input()
    sys.stdout.write(f"{command}: command not found\n")

    # Exit or REPL
    if command == "exit":
        sys.stdout.write(f"exited\n")
    else:
        main()

if __name__ == "__main__":
    main()
