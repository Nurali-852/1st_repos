def write_list_to_file(list_data, file_path):
    with open(file_path, 'w') as file:
        for item in list_data:
            file.write(f"{item}\n")

# Specify the list and file path
data = ["apple", "banana", "cherry"]
file_path = "fruits.txt"
write_list_to_file(data, file_path)
