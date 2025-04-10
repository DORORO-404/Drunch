# ===== Drunch Wordlist Generator =====

import itertools
import pyfiglet

# ANSI Escape Codes for color formatting
RED = "\033[1;31m"
GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
BLUE = "\033[1;34m"
CYAN = "\033[1;36m"
MAGENTA = "\033[1;35m"
RESET = "\033[0m"

# Print the ASCII logo banner using pyfiglet
def print_banner():
    ascii_banner = pyfiglet.figlet_format("Drunch")
    print(f"{MAGENTA}{ascii_banner}{RESET}")
    box = f"""{CYAN}
  ╔═══════════════════════════════════════╗
  ║     {MAGENTA}Drunch - Wordlist Generator{CYAN}       ║
  ║     {MAGENTA}Developed by: DORORO{CYAN}              ║
  ║     {MAGENTA}Github: DORORO-404{CYAN}                ║
  ║     {MAGENTA}Version: 1.0{CYAN}                      ║
  ╚═══════════════════════════════════════╝{RESET}
    """
    print(box)

# Print the welcome title
def print_title():
    print(f"{RED}[+] ====== {BLUE}Welcome to Drunch Wordlist Generator{RED} ====== [+]{RESET}")

# Get minimum word length from user
def get_min_length():
    while True:
        try:
            min_length = int(input(f"{YELLOW}Enter minimum length: {RESET}"))
            return min_length
        except ValueError:
            print(f"{RED}❌ Invalid input. Please enter a valid number.{RESET}")

# Get maximum word length from user
def get_max_length():
    while True:
        try:
            max_length = int(input(f"{YELLOW}Enter maximum length: {RESET}"))
            return max_length
        except ValueError:
            print(f"{RED}❌ Invalid input. Please enter a valid number.{RESET}")

# Let the user choose character set
def get_chars():
    print(f"\n{YELLOW}Choose character set:{RESET}")
    print(f"{BLUE}[1]{RESET} Numbers only (0-9)")
    print(f"{BLUE}[2]{RESET} Letters only (a-z)")
    print(f"{BLUE}[3]{RESET} Custom (your own letters/numbers)")

    while True:
        try:
            choice = int(input(f"{YELLOW}Enter your choice (1, 2, or 3): {RESET}"))
            if choice == 1:
                return "0123456789"
            elif choice == 2:
                return "abcdefghijklmnopqrstuvwxyz"
            elif choice == 3:
                return input(f"{YELLOW}Enter your custom characters: {RESET}")
            else:
                print(f"{RED}❌ Invalid choice. Please enter 1, 2, or 3.{RESET}")
        except ValueError:
            print(f"{RED}❌ Invalid input. Please enter a valid number.{RESET}")

# Get file name from user
def get_file_name():
    return input(f"\n{YELLOW}Enter file name: {RESET}")

# Generate and save the wordlist
def generate_wordlist():
    min_length = get_min_length()
    max_length = get_max_length()
    chars = get_chars()
    file_name = get_file_name()

    print(f"\n{GREEN}[+] Generating wordlist... Please wait.{RESET}")

    with open(f"{file_name}.txt", "w") as file:
        for length in range(min_length, max_length + 1):
            for word in itertools.product(chars, repeat=length):
                file.write("".join(word) + "\n")

    print(f"{GREEN}[✓] Wordlist saved as '{file_name}.txt'.{RESET}")

# Main logic controller
def main():
    print_banner()
    print_title()

    while True:
        generate_wordlist()

        while True:
            repeat = input(f"\n{YELLOW}Generate another wordlist? [Y/n]: {RESET}").strip().lower()
            if repeat == "y" or repeat == "":
                break
            elif repeat == "n":
                print(f"{GREEN}Thank you for using Drunch Wordlist Generator. Goodbye!{RESET}")
                return
            else:
                print(f"{RED}❌ Invalid input. Please enter 'y' or 'n'.{RESET}")

# Run the script
if __name__ == "__main__":
    main()
