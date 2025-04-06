# ===== Drunch Wordlist Generator =====

# Importing itertools for generating combinations
import itertools

# Function to print the title with red bold color
def print_title():
    print("\033[1;31m[+] ====== Welcome to Drunch Wordlist Generator ====== [+]\033[0m")

# Function to get the minimum length of generated words
def get_min_length():
    while True:
        try:
            min_length = int(input("Enter minimum length: "))
            return min_length
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Function to get the maximum length of generated words
def get_max_length():
    while True:
        try:
            max_length = int(input("Enter maximum length: "))
            return max_length
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Function to let the user choose characters for wordlist generation
def get_chars():
    print("\nChoose character set:")
    print("[1] Numbers only (0-9)")
    print("[2] Letters only (a-z)")
    print("[3] Custom (your own letters/numbers)")

    while True:
        try:
            choice = int(input("Enter your choice (1, 2, or 3): "))
            if choice == 1:
                return "0123456789"
            elif choice == 2:
                return "abcdefghijklmnopqrstuvwxyz"
            elif choice == 3:
                return input("Enter your custom characters: ")
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Function to get the file name for saving the wordlist
def get_file_name():
    return input("\nEnter file name: ")

# Function to generate the wordlist
def generate_wordlist():
    min_length = get_min_length()
    max_length = get_max_length()
    chars = get_chars()
    file_name = get_file_name()

    print("\n[+] Generating wordlist... Please wait.")

    with open(f"{file_name}.txt", "w") as file:
        for length in range(min_length, max_length + 1):
            for word in itertools.product(chars, repeat=length):
                file.write("".join(word) + "\n")

    print(f"[✓] Wordlist saved as '{file_name}.txt'.")

# Main function
def main():
    print_title()

    while True:
        generate_wordlist()

        while True:
            repeat = input("\nGenerate another wordlist? [Y/n]: ").strip().lower()
            if repeat == "y" or repeat == "":
                break
            elif repeat == "n":
                print("Thank you for using Drunch Wordlist Generator. Goodbye!")
                return
            else:
                print("Invalid input. Please enter 'y' or 'n'.")

# Run the script
if __name__ == "__main__":
    main()
