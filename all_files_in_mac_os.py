import os


def recursive_files(prefix, paths):
    for path in paths:
        try:

            if prefix == '/':
                path = prefix + path
            else:
                path = prefix + '/' + path

            lst_paths = os.listdir(path)
            print("Path : ", path, '=', lst_paths)
            print()
            recursive_files(path, lst_paths)
        except:
            return


recursive_files('', [''])