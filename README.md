# CopyRAWtoSubDir
This script simply copies the RAW camera files from a directory to a new dir called "RAW". It's very short script but extremely useful for anyone using a DSLR.

If your camera takes pictures in another format, not ".cr3", change the extension on line 28. It's the final parameter of this line:
if os.path.isfile(cwd + "\\" + file) and str(file).lower().endswith("<ins>.cr3</ins>"):
