import os


base_path = os.path.abspath(".")

nstep = 0

def listdir_as_tree(path,nstep):
    n = nstep
    b_path = path
    menu = os.listdir()
    for i in menu:
        print('-----'*n+i)
        i_path = b_path + '\\' + i
        if i == ".git":
            continue
        if os.path.isdir(i_path):
            print('|\n')
            n == 1
            os.chdir(i_path)
            path = os.path.abspath(".")
            listdir_as_tree(path,n+1)


if __name__ == "__main__":
    listdir_as_tree(base_path,nstep)