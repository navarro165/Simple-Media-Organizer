import stat
import ctypes

import os
import shutil
import mimetypes
from datetime import datetime
from tqdm import tqdm

FILE_ATTRIBUTE_HIDDEN = 0x2


def is_hidden(filepath):
    basename = os.path.basename(filepath)
    if basename.startswith('~$'):
        return True
    elif os.name == 'nt':
        try:
            attrs = os.stat(filepath).st_file_attributes
        except (OSError, AttributeError):
            attrs = os.stat(filepath).st_mode
        return attrs & FILE_ATTRIBUTE_HIDDEN != 0
    else:
        return basename.startswith('.')


def organize_media(src_dir):
    # Get the parent directory of the source directory
    parent_dir = os.path.abspath(os.path.join(src_dir, os.pardir))

    # Create the destination directory
    dest_dir = os.path.join(parent_dir, 'organized_media')
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # Get the size and file count of the organized media directory
    total_size = 0
    total_files = 0

    for dir_path, dir_names, file_names in tqdm(os.walk(src_dir), desc="Progress", position=0, leave=True)):
        for file in tqdm(file_names, desc="Progress", position=0, leave=True)):

            # Get the full path of the file
            file_path = os.path.join(dir_path, file)

            # Ignore hidden files
            if is_hidden(file_path):
                continue

            # Get the file's creation time
            file_ctime = os.path.getctime(file_path)
            file_ctime_str = datetime.fromtimestamp(file_ctime).strftime('%Y-%m-%d')

            # Create the directory for the file's creation date
            date_dir = os.path.join(dest_dir, file_ctime_str)
            if not os.path.exists(date_dir):
                os.makedirs(date_dir)

            # Get the file's media type using mimetypes
            file_mimetype, encoding = mimetypes.guess_type(file_path)

            if file_mimetype:
                if file_mimetype.startswith('image/'):
                    media_type = 'images'
                elif file_mimetype.startswith('video/'):
                    media_type = 'videos'
                elif file_mimetype.startswith('audio/'):
                    media_type = 'audio'
                elif file_mimetype.startswith('application/pdf'):
                    media_type = 'pdfs'
                elif file_mimetype.startswith('application/msword'):
                    media_type = 'msdocs'
                else:
                    media_type = 'others'

                # Create the directory for the file's media type
                media_dir = os.path.join(date_dir, media_type)
                if not os.path.exists(media_dir):
                    os.makedirs(media_dir)

                # Copy the file to the appropriate directory
                new_file_path = shutil.copy2(file_path, media_dir)

                # Collect file size and increment file counter
                total_size += os.path.getsize(new_file_path)
                total_files += 1

    # Print the number of files copied and the size of the new organized directory
    print(f"{total_files} files have been copied.")
    print(f"The size of the new organized directory is {total_size / 1024 ** 2:.2f} MB.")
