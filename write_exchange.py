import os


def write_exchange(content, filename, dir_):
    fle = os.path.join(dir_, filename)
    with open(fle, "w+") as fp:
        fp.write(content)
    print('written content to', fle)
