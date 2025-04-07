# ===== Drunch Wordlist Generator =====

# Importing itertools for generating combinations
import itertools

# ANSI Escape Codes for color formatting
RED = "\033[1;31m"
GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
BLUE = "\033[1;34m"
RESET = "\033[0m"

# Function to print the title with red bold color
def print_title():
    """Display the welcome title."""
    print(f"{RED}[+] ====== {BLUE}Welcome to Drunch Wordlist Generator{RED} ====== [+]{RESET}")

# Function to get the minimum length of generated words
def get_min_length():
    """Prompt the user to enter the minimum word length."""
    while True:
        try:
            min_length = int(input(f"{YELLOW}Enter minimum length: {RESET}"))
            return min_length
        except ValueError:
            print(f"{RED}❌ Invalid input. Please enter a valid number.{RESET}")

# Function to get the maximum length of generated words
def get_max_length():
    """Prompt the user to enter the maximum word length."""
    while True:
        try:
            max_length = int(input(f"{YELLOW}Enter maximum length: {RESET}"))
            return max_length
        except ValueError:
            print(f"{RED}❌ Invalid input. Please enter a valid number.{RESET}")

# Function to let the user choose characters for wordlist generation
def get_chars():
    """Prompt user to choose character set for wordlist generation."""
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

# Function to get the file name for saving the wordlist
def get_file_name():
    """Prompt user to enter the file name to save wordlist."""
    return input(f"\n{YELLOW}Enter file name: {RESET}")

# Function to generate the wordlist
def generate_wordlist():
    """Generate and save the wordlist based on user input."""
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

# Main function
def main():
    """Main function to drive the program."""
    print_title()

    while True:
        generate_wordlist()

        while True:
            repeat = input(f"\n{YELLOW}Generate another wordlist? [Y/n]: {RESET}").strip().lower()
            if repeat == "y" or repeat == "":  # User wants to generate another wordlist
                break
            elif repeat == "n":  # User doesn't want to generate more wordlists
                print(f"{GREEN}Thank you for using Drunch Wordlist Generator. Goodbye!{RESET}")
                return
            else:  # Invalid input
                print(f"{RED}❌ Invalid input. Please enter 'y' or 'n'.{RESET}")

# Run the script
if __name__ == "__main__":  
    main()
