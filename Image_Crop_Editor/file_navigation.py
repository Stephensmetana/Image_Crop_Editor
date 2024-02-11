from PyQt5.QtCore import QDir, QFileInfo

def get_first_image_in_folder(folder_path):
    # Find the first image file in the folder
    image_files = [file for file in QDir(folder_path).entryList(['*.png', '*.jpg', '*.jpeg'])]
    if image_files:
        return QDir(folder_path).filePath(image_files[0])
    return None

def new_get_first_image_in_folder(folder_path):
    # Find the first image file in the folder
    image_files = [file for file in QDir(folder_path).entryList(['*.png', '*.jpg', '*.jpeg'])]
    if image_files:
        return QDir(folder_path).filePath(image_files[0])
    return None


def get_file_index_in_folder(folder_path, current_image_path):
    # Get the list of image files in the folder
    image_files = [file for file in QDir(folder_path).entryList(['*.png', '*.jpg', '*.jpeg'])]
    # Sort the list so that the index is always determined the same way
    image_files.sort()

    # Get the current file name
    current_file_name = QFileInfo(current_image_path).fileName()
    try:
        # Try to find the index of the current file name in the list
        file_name_index = image_files.index(current_file_name)
    except ValueError:
        # Handle the case where the filename is not found
        file_name_index = 0  # or any default value or logic
        print("File not found in the list.")

    # Return the current index
    return file_name_index

def get_next_image_in_folder(folder_path, current_image_path):
    image_files = [file for file in QDir(folder_path).entryList(['*.png', '*.jpg', '*.jpeg'])]
    current_index = get_file_index_in_folder(folder_path, current_image_path)

    if current_index < len(image_files) - 1:
        return QDir(folder_path).filePath(image_files[current_index + 1])
    else:
        # Index is set to the last image and we want to loop to the beginning so the index should be set to the first image
        return QDir(folder_path).filePath(image_files[0])
    return None

def get_previous_image_in_folder(folder_path, current_image_path):
    image_files = [file for file in QDir(folder_path).entryList(['*.png', '*.jpg', '*.jpeg'])]
    current_index = get_file_index_in_folder(folder_path, current_image_path)

    if current_index > 0:
        return QDir(folder_path).filePath(image_files[current_index - 1])
    else:
        # Index is set to the first image and we want to loop to the end so the index should be set to the last image
        last_index = len(image_files) - 1
        return QDir(folder_path).filePath(image_files[last_index])
    return None
