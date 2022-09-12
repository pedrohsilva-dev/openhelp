from datetime import datetime
import os
from random import random


def ext_path(src: str):
    if (src == 'image/jpeg'):
        return '.jpg'
    elif (src == 'image/jpg'):
        return '.jpg'
    elif (src == 'image/png'):
        return '.png'
    else:
        return ''


def generate_namefile(file: str, ext: str):

    zero_day = ""
    zero_mon = ""
    mm = datetime.now().month
    yyyy = datetime.now().year
    dd = datetime.now().day
    tmstp = datetime.now().timestamp()
    if (dd < 10):
        zero_day = "0"
    if (mm < 10):
        zero_mon = "0"

    return f"{random.randint(0, 20)}-{yyyy}-{zero_mon}{mm}-{zero_day}{dd}-{tmstp}-{hash(file)}{ext_path(ext)}"


def dir_file(file, src: str = 'files'):
    return f"{os.path.realpath(src)}/{file}"
