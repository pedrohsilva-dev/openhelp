import os
from os import listdir, read

path_dir = os.path.join(
    os.path.abspath("."),
    os.path.relpath("files"),
)
print("pedro henrique")
for f in listdir(path_dir):
    print(read(os.path.join(
        os.path.abspath("."),
        os.path.relpath("files"),
    ), "5000000"))
