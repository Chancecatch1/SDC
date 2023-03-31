import os
import shutil

def gather_images(source, destination, extensions):
    for root, _, files in os.walk(source):
        for file in files:
            if file.lower().endswith(extensions):
                shutil.copy(os.path.join(root, file), destination)

source = 'D:/Dropbox'
destination = 'C:/Users/User/Desktop/Test/all_images'
extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff')

gather_images(source, destination, extensions)
