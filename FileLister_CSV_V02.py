import os
import csv
from tkinter import filedialog
from tkinter import Tk

def list_files(directory, file_info):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if not os.path.isdir(file_path): # checks if it's not a directory
                file_size = os.path.getsize(file_path)
                file_info.append((file, os.path.relpath(root, directory), file_size)) # appends the file name, containing folder, and file size
    return file_info

def write_csv(directory, file_info):
    with open(os.path.join(directory, 'file_list.csv'), 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["File Name", "Containing Folder", "File Size (bytes)"])
        for info in file_info:
            writer.writerow(info)

def main():
    # create a Tk root widget
    root = Tk()
    # hide the main root window
    root.withdraw()
    # open a folder selection dialog and get the folder path
    folder_path = filedialog.askdirectory()
    if folder_path:
        # get the list of all files in the selected directory
        files = list_files(folder_path, [])
        # write the list of files to a CSV file in the selected directory
        write_csv(folder_path, files)

if __name__ == "__main__":
    main()