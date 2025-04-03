def copy_file(source_path, destination_path):
    try:
        with open(source_path, 'r') as source_file:
            content = source_file.read()
        
        with open(destination_path, 'w') as dest_file:
            dest_file.write(content)
        
        print(f"File copied from {source_path} to {destination_path}")
    except FileNotFoundError:
        print("Source file not found.")

# Specify the source and destination file paths
source_path = "source.txt"
destination_path = "destination.txt"
copy_file(source_path, destination_path)
