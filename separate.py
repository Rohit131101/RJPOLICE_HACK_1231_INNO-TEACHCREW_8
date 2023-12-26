import os
import shutil

def separate_files(input_file, folder1, folder2):
    with open(input_file, 'r') as file:
        for line in file:
            filename, label = line.strip().split()
            source_path = os.path.join('data', filename)  # assuming data files are in the 'data' folder
            if label == 'label1':
                destination_path = os.path.join(folder1, filename)
            elif label == 'label2':
                destination_path = os.path.join(folder2, filename)
            else:
                print(f"Unknown label '{label}' for file '{filename}'. Skipping.")
                continue

            shutil.copy(source_path, destination_path)
            print(f"Moved '{filename}' to '{destination_path}'.")

# Example usage
input_file_path = 'C:\\Users\\hp\\mesonet(rajasthan police)\\release_in_the_wild'
folder_label1 = 'spoof'
folder_label2 = 'bona-fide'

# Create folders if they don't exist
os.makedirs(folder_label1, exist_ok=True)
os.makedirs(folder_label2, exist_ok=True)

# Call the function to separate files
separate_files(input_file_path, folder_label1, folder_label2)
