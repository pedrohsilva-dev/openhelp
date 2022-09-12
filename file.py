import os
from os import listdir, read

path_dir = os.path.join(
    os.path.abspath("."),
    os.path.relpath("files"),


)

for f in listdir(path_dir):
    print(read(os.path.join(
        os.path.abspath("."),
        os.path.relpath("files"),
        f
    ), "5000000"))
