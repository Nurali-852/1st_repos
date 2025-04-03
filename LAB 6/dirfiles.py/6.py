import string

def generate_files():
    for letter in string.ascii_uppercase:  # 'A' to 'Z'
        file_name = f"{letter}.txt"
        with open(file_name, 'w') as file:
            file.write(f"This is the file {file_name}\n")

generate_files()
