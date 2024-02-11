import configparser
from PyQt5.QtWidgets import QFileDialog 
from PyQt5.QtCore import QDir
from file_navigation import get_first_image_in_folder


config = configparser.ConfigParser()
config.read('config.ini')

def get_last_opened_directory():
    try:
        return config.get('Settings', 'last_opened_directory')
    except configparser.NoOptionError:
        return QDir.homePath()

def set_last_opened_directory(directory):
    config.set('Settings', 'last_opened_directory', directory)
    with open('config.ini', 'w') as config_file:
        config.write(config_file)

def open_file_explorer(parent, image_loader):
    initial_directory = get_last_opened_directory()
    folder_path = QFileDialog.getExistingDirectory(parent, 'Select a Folder', initial_directory)
    if folder_path:
        set_last_opened_directory(folder_path)
        print(f"Selected folder path: {folder_path}")
        image_path = get_first_image_in_folder(folder_path)
        if image_path:
            image_loader.load_image(image_path)
