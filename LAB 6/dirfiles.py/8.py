import os

def delete_file(file_path):
    if os.path.exists(file_path):
        if os.access(file_path, os.W_OK):  # Check if writable before deleting
            os.remove(file_path)
            print(f"The file {file_path} has been deleted.")
        else:
            print(f"The file {file_path} is not writable, cannot delete.")
    else:
        print(f"The file {file_path} does not exist.")

# Specify the file path
file_path = "file_to_delete.txt"
delete_file(file_path)
