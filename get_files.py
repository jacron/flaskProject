import os


def get_exchange_files(path, ext):
    names = []
    try:
        files = os.listdir(path)
        for file in files:
            if file.endswith(ext):
                names.append(file)
    except FileNotFoundError as e:
        print(e)
    return sorted(names)
