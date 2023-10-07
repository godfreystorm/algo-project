# List of file paths (replace with your file paths)
file_paths = ['source1.txt', 'source2.txt', 'source3.txt','source4.txt','source5.txt']

# Loop through each file and read its contents
for file_path in file_paths:
    try:
        with open(file_path, 'r') as file:
            file_contents = file.read()
            # Process the file_contents as needed
            print(f"Contents of {file_path}:\n{file_contents}\n")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred while reading {file_path}: {str(e)}")
