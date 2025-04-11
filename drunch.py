# ===== Drunch Wordlist Generator =====

import itertools
import pyfiglet
import sys
import argparse

# === Version info ===
VERSION = "1.1"

# === ANSI color codes (Kali Linux friendly) ===
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
WHITE = "\033[97m"
RESET = "\033[0m"

# === Print ASCII art banner ===
def print_banner():
    ascii_banner = pyfiglet.figlet_format("Drunch")
    print(f"{CYAN}{ascii_banner}{RESET}")
    box = f"""{WHITE}
  ╔═══════════════════════════════════════╗
  ║     {CYAN}Drunch - Wordlist Generator{WHITE}       ║
  ║     {CYAN}Developed by: DORORO__404{WHITE}         ║
  ║     {CYAN}GitHub: DORORO-404{WHITE}                ║
  ║     {CYAN}Version: {VERSION}{WHITE}                      ║
  ╚═══════════════════════════════════════╝{RESET}
    """
    print(box)

# === Print welcome message ===
def print_title():
    print(f"{WHITE}[+] ===== {CYAN}Welcome to Drunch Wordlist Generator{WHITE} ===== [+]{RESET}")

# === Get minimum length from user ===
def get_min_length():
    while True:
        try:
            min_length = int(input(f"{YELLOW}Enter the minimum password length: {RESET}"))
            return min_length
        except ValueError:
            print(f"{RED}❌ Invalid input. Please enter a number.{RESET}")

# === Get maximum length from user ===
def get_max_length():
    while True:
        try:
            max_length = int(input(f"{YELLOW}Enter the maximum password length: {RESET}"))
            return max_length
        except ValueError:
            print(f"{RED}❌ Invalid input. Please enter a number.{RESET}")

# === Get character set choice from user ===
def get_chars():
    print(f"\n{CYAN}Choose a character set:{RESET}")
    print(f"{WHITE}[1]{RESET} Numbers only (0-9)")
    print(f"{WHITE}[2]{RESET} Letters only (a-z)")
    print(f"{WHITE}[3]{RESET} Custom characters")

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
                print(f"{RED}❌ Invalid choice. Please choose 1, 2, or 3.{RESET}")
        except ValueError:
            print(f"{RED}❌ Invalid input. Please enter a number.{RESET}")

# === Ask user for output file name ===
def get_file_name():
    return input(f"\n{YELLOW}Enter a file name to save the wordlist: {RESET}")

# === Generate wordlist and save it to file ===
def generate_wordlist():
    min_length = get_min_length()
    max_length = get_max_length()
    chars = get_chars()
    file_name = get_file_name()

    print(f"\n{GREEN}[+] Generating the wordlist. Please wait...{RESET}")

    with open(f"{file_name}.txt", "w") as file:
        for length in range(min_length, max_length + 1):
            for word in itertools.product(chars, repeat=length):
                file.write("".join(word) + "\n")

    print(f"{GREEN}[✓] Wordlist saved successfully as '{file_name}.txt'{RESET}")

# === Main function to control program flow ===
def main():
    # Check for --version flag
    if len(sys.argv) > 1 and sys.argv[1] == "--version":
        print(f"{CYAN}Drunch Wordlist Generator v{VERSION}{RESET}")
        sys.exit()

    print_banner()
    print_title()

    while True:
        generate_wordlist()

        while True:
            repeat = input(f"\n{YELLOW}Would you like to generate another wordlist? [Y/n]: {RESET}").strip().lower()
            if repeat in ["y", ""]:
                break
            elif repeat == "n":
                print(f"{GREEN}Thank you for using Drunch. Goodbye!{RESET}")
                return
            else:
                print(f"{RED}❌ Invalid input. Please enter 'y' or 'n'.{RESET}")

# === Run the program with version check ===
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="PassForge - Advanced Password Generator")
    parser.add_argument("--version", action="store_true", help="Show version and exit")
    args = parser.parse_args()

    if args.version:
        print(f"{CYAN}PassForge Version: {VERSION}{RESET}")
        exit()

    main()
