# CopyRAWtoSubDir
This script simply copies the RAW camera files from a directory to a new dir called "RAW". It's very short script but extremely useful for anyone using a DSLR.

If your camera takes pictures in another format, not ".cr3", change the extension on line 14. It's this line, just change "cr3" to whatever your file extension is:
```python
RAW_EXTENSION = "cr3"
```

# Requirements:
Python 3.11 or higher

# Usage
Either of 2 ways to use this script:
1. Copy it inside the directory where you want to separate the files, and run it.
2. Drag-and-drop the directory on top of the script. It will execute as the directory as parameter.

You don't need to manually create the RAW subdirectory, it will be created if it doesn't exist.
