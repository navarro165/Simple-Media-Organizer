## Simple Media Organizer
This project provides a solution for organizing media files in a directory by grouping them by their creation date and media type.

### Prerequisites
- Python 3
- `os`, `shutil`, `mimetypes`, `prompt_toolkit`, `tqdm` python modules
- `virtualenv` python module (only if you want to use the bash script)

### Running the script

#### Using Python script
1. Clone or download the repository
2. Open a terminal and navigate to the project directory
3. Run the command `pip install -r requirements.txt` to install the required python modules
4. Run the command `python main.py` and enter the path of the directory you want to organize when prompted. The script will use the `prompt_toolkit` library to provide tab-completion feature for directories and `tqdm` for displaying the progress
5. The script will organize the files in the specified directory

#### Using Bash script
1. Clone or download the repository
2. Open a terminal and navigate to the project directory
3. Make the script executable by running `chmod +x run.sh`
4. Run the command `./run.sh`
5. The script will install the required python modules in a virtual environment, activate the environment, run the main script and organize the files in the directory specified on the script, then it will deactivate the environment.

### Output
The script will create a new directory named `organized_media` in the same directory level as the source directory. Inside it, the files will be grouped by directories corresponding to the date the files were created and within each of those, organized by either video, image, or other media types.

### Note
- The script will copy the files and not move them from their original location.

### Troubleshooting
- Make sure that you are using Python 3 and have the required modules installed
- Make sure the script_path variable in the bash script is set correctly, to the location of your main.py file.
- Make sure you have the execution permissions on the script file.
- Double check that the path you have entered for the source directory is correct.
- Make sure you have the virtualenv module installed in your system

### Conclusion
This script can be a useful tool for keeping your media files organized and easily accessible. Feel free to modify the script to suit your specific needs.
