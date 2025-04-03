import os

def check_access(path):
    # Check if path exists
    if os.path.exists(path):
        print(f"The path '{path}' exists.")
        
        # Check for readability
        if os.access(path, os.R_OK):
            print(f"The path '{path}' is readable.")
        else:
            print(f"The path '{path}' is not readable.")
        
        # Check for writability
        if os.access(path, os.W_OK):
            print(f"The path '{path}' is writable.")
        else:
            print(f"The path '{path}' is not writable.")
        
        # Check for executability
        if os.access(path, os.X_OK):
            print(f"The path '{path}' is executable.")
        else:
            print(f"The path '{path}' is not executable.")
    else:
        print(f"The path '{path}' does not exist.")

# Specify the path
path = "/path/to/file_or_directory"
check_access(path)
