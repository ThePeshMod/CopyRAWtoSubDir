"""
Copyright (C) 2024 Daniel Dyankov

Script licensed under GNU GPL V3:
https://www.gnu.org/licenses/gpl-3.0.en.html

Short explanation of GNU GPL V3:
https://choosealicense.com/licenses/gpl-3.0/
"""

import os
import argparse


def main(working_dir: str):
    cwd = working_dir
    raw_path = cwd + "\\RAW"

    # CHeck if the RAW directory exists
    if not os.path.exists(raw_path):
        os.makedirs(raw_path)

    # Find all CR3 files and dirs in the working directory
    list_of_files = os.listdir(cwd)

    # Got through the file list and move the files (check if it's a file, not a dir) that end in .cr3 to the RAW folder
    for file in list_of_files:
        if os.path.isfile(cwd + "\\" + file) and str(file).lower().endswith(".cr3"):
            os.replace(str(cwd + "\\" + file), str(raw_path + "\\" + file))


parser = argparse.ArgumentParser()
parser.add_argument("working_dir", nargs="?", help="Path to the files", default=os.getcwd())
args = parser.parse_args()
main(args.working_dir)
