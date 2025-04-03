def count_lines_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            print(f"Number of lines in the file: {len(lines)}")
    except FileNotFoundError:
        print("The file does not exist.")

# Specify the file path
file_path = "sample.txt"
count_lines_in_file(file_path)
