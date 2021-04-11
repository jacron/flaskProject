import os

from settings import cookie_path_name, sampledir


def get_exchange_files(request):
    names = []
    dir_ = request.cookies.get(cookie_path_name)
    if not dir_:
        dir_ = sampledir
    files = os.listdir(dir_)
    for file in files:
        if file.endswith('.bl8'):
            names.append(file)
    return names
