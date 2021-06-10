import os
number = 0

def Scan_dir(prefix, path):
    my_prefix = prefix + '\t'
    arr = os.listdir(path)

    for f in arr:
        this_file = path + "\\" + f
        if os.access(this_file, os.R_OK):
            if os.path.isdir(this_file):
               Scan_dir(my_prefix, this_file)
            else:
                global number
                number += 1
                print(number , my_prefix, f, '(', os.stat(this_file).st_size, ')')


if __name__ == '__main__':
    Scan_dir('', 'C:\\Projects')

