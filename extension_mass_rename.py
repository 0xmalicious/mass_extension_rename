import os

def rename_files_in_directory(directory, new_extension):
    try:
        # Verify if the directory exists
        if not os.path.isdir(directory):
            print(f"The directory {directory} does not exist.")
            return

        # List all files in the directory
        files = os.listdir(directory)

        for file in files:
            file_path = os.path.join(directory, file)
            
            # Verify if the given path is a file or a directory
            if os.path.isfile(file_path):
                file_name, file_extension = os.path.splitext(file)

                # Rename the file if the extension is not the same as the one given
                if file_extension != new_extension:
                    new_file_name = f"{file_name}{new_extension}"
                    new_file_path = os.path.join(directory, new_file_name)

                    # If the file already exist, add a suffix
                    count = 1
                    while os.path.exists(new_file_path):
                        new_file_name = f"{file_name}_{count}{new_extension}"
                        new_file_path = os.path.join(directory, new_file_name)
                        count += 1

                    os.rename(file_path, new_file_path)
                    print(f"Renamed: {file} -> {new_file_name}")
                else:
                    print(f"The file {file} already have the extension {new_extension}.")
    except Exception as e:
        print(f"An error occured {e}")

if __name__ == "__main__":
    # Ask for the variable directory and the extension
    directory = input("Enter the directory path: ")
    new_extension = input("Enter a new extension (For exemple .txt): ")

    # Add a dot in front of the extension if there is not
    if not new_extension.startswith('.'):
        new_extension = f".{new_extension}"

    rename_files_in_directory(directory, new_extension)
