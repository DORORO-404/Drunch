# ========= Drunch - Wordlist Generator =========

# === Import necessary modules ===
import itertools
import pyfiglet
import sys
import os

# === Version info ===
VERSION = "1.3"

# === ANSI color codes ===
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"
RESET = "\033[0m"

# === Display the ASCII banner using pyfiglet ===
def print_banner():
    ascii_banner = pyfiglet.figlet_format("  Drunch")
    print(f"{MAGENTA}{ascii_banner}{RESET}")
    box = f"""{CYAN}
  ╔═══════════════════════════════════════╗
  ║     {MAGENTA}Drunch - Wordlist Generator {CYAN}      ║
  ║     {MAGENTA}Developed by: DORORO__404{CYAN}         ║
  ║     {MAGENTA}GitHub: DORORO-404{CYAN}                ║
  ║     {MAGENTA}Version: {VERSION}{CYAN}                      ║
  ╚═══════════════════════════════════════╝{RESET}
    """
    print(box)

# === Print welcome message ===
def print_title():
    print(f"\n{RED}[+] ===== {CYAN}Welcome to Drunch Wordlist Generator{RED} ===== [+]{RESET}")

# === Clear screen based on OS ===
def clear_screen():
    os.system("clear" if os.name == "posix" else "cls")

# === Exit safely with a message ===
def exit_program():
    print(f"{GREEN}Exiting Drunch...{RESET}")
    sys.exit()

# === Handle input and check for exit keywords ===
def safe_input(prompt):
    try:
        user_input = input(prompt).strip()
        if user_input.lower() in ["exit", "quit", "q", "x", "close"]:
            exit_program()
        return user_input
    except KeyboardInterrupt:
        print(f"\n{GREEN}Exiting Drunch...{RESET}")
        sys.exit()

# === Get user-defined minimum password length ===
def get_min_length():
    while True:
        user_input = safe_input(f"{YELLOW}Enter the minimum password length: {RESET}")
        try:
            return int(user_input)
        except ValueError:
            print(f"{RED}Invalid input. Please enter a valid number.{RESET}")

# === Get user-defined maximum password length ===
def get_max_length():
    while True:
        user_input = safe_input(f"{YELLOW}Enter the maximum password length: {RESET}")
        try:
            return int(user_input)
        except ValueError:
            print(f"{RED}Invalid input. Please enter a valid number.{RESET}")

# === Get character set based on user choice ===
def get_chars():
    print(f"\n{RED}Choose a character set:{RESET}")
    print(f"{CYAN}[1] Numbers only (0-9){RESET}")
    print(f"{CYAN}[2] Letters only (a-z){RESET}")
    print(f"{CYAN}[3] Custom characters{RESET}")

    while True:
        user_input = safe_input(f"{YELLOW}Enter your choice (1, 2, or 3): {RESET}")
        try:
            choice = int(user_input)
            if choice == 1:
                return "0123456789"
            elif choice == 2:
                return "abcdefghijklmnopqrstuvwxyz"
            elif choice == 3:
                custom = safe_input(f"{YELLOW}Enter your custom characters: {RESET}")
                return custom
            else:
                print(f"{RED}Invalid choice. Please select 1, 2, or 3.{RESET}")
        except ValueError:
            print(f"{RED}Please enter a valid number.{RESET}")

# === Get the file name to save the generated wordlist ===
def get_file_name():
    while True:
        file_name = safe_input(f"\n{YELLOW}Enter a file name to save the wordlist: {RESET}")
        if file_name.strip():
            return file_name.strip()
        else:
            print(f"{RED}File name cannot be empty. Please provide a valid name.{RESET}")

# === Create output folder if it doesn't exist ===
def create_output_folder():
    if not os.path.exists("wordlists"):
        os.mkdir("wordlists")

# === Generate the wordlist and save it ===
def generate_wordlist():
    min_length = get_min_length()
    max_length = get_max_length()
    chars = get_chars()
    file_name = get_file_name()

    create_output_folder()

    print(f"\n{GREEN}[+] Generating the wordlist. Please wait...{RESET}")

    with open(f"wordlists/{file_name}.txt", "w") as file:
        for length in range(min_length, max_length + 1):
            for word in itertools.product(chars, repeat=length):
                file.write("".join(word) + "\n")

    print(f"{GREEN}Wordlist saved successfully as 'wordlists/{file_name}.txt'{RESET}")

# === Ask the user if they want to generate another wordlist ===
def generate_more_wordlist():
    while True:
        repeat = safe_input(f"\n{YELLOW}Would you like to generate another wordlist? [Y/n]: {RESET}").strip().lower()
        if repeat == "exit":
            exit_program()
        elif repeat in ["y", ""]:
            break
        elif repeat == "n":
            print(f"{GREEN}Thank you for using Drunch. Goodbye!{RESET}")
            exit()
        else:
            print(f"{RED}Invalid input. Please enter 'y' or 'n'.{RESET}")

# === Main function ===
def main():
    # Handle version argument
    if "--version" in sys.argv or "-v" in sys.argv:
        print(f"{CYAN}Drunch Version: {VERSION}{RESET}")
        sys.exit()

    print_banner()

    while True:
        clear_screen()
        print_banner()
        print_title()
        generate_wordlist()
        generate_more_wordlist()

# === Entry point ===
if __name__ == "__main__":
    main()
