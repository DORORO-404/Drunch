# import modules
import itertools

# print title
print("\033[1;31m[+] ====== Welcome To Drunch ====== [+]\033[0m")

# The letters from which words will be generated
chars = "0123456789"

# Minimum and maximum word length
min_length = int(input("Entre min length: "))
max_length = int(input("Entre max length: "))

# file name
file_name = input("entre your file name: ")

# Open a file to write the results
with open(f"{file_name}.txt", "w") as file:
    for length in range(min_length, max_length + 1):
        for word in itertools.product(chars, repeat=length):
            file.write("".join(word) + "\n")