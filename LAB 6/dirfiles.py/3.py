import os

def check_and_split_path(path):
    if os.path.exists(path):
        # Get the filename and directory portion of the path
        filename = os.path.basename(path)
        directory = os.path.dirname(path)
        print(f"Path exists. Filename: {filename}, Directory: {directory}")
    else:
        print("The path does not exist.")

# Specify the path
path = "/path/to/file_or_directory"
check_and_split_path(path)
