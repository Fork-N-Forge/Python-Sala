import os
import shutil

def organize_files_by_type(source_dir, target_dir):
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    for filename in os.listdir(source_dir):
        source_path = os.path.join(source_dir, filename)

        if os.path.isfile(source_path):
            file_type = filename.split('.')[-1].lower()

            if file_type:
                target_subdir = os.path.join(target_dir, file_type)
                if not os.path.exists(target_subdir):
                    os.makedirs(target_subdir)

                target_path = os.path.join(target_subdir, filename)

                try:
                    shutil.move(source_path, target_path)
                    print(f"Moved '{filename}' to '{target_subdir}'")
                except Exception as e:
                    print(f"Failed to move '{filename}': {str(e)}")

if __name__ == "__main__":
    source_directory = input("Enter the source directory path: ")
    target_directory = input("Enter the target directory path: ")

    organize_files_by_type(source_directory, target_directory)
