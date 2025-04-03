import os

def list_files_and_dirs(path):
    # List only directories
    dirs = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    print("Directories:", dirs)

    # List only files
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    print("Files:", files)

    # List both directories and files
    all_files_dirs = os.listdir(path)
    print("All files and directories:", all_files_dirs)

# Specify the path
path = "/path/to/directory"
list_files_and_dirs(path)
