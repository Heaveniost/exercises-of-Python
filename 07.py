import os

def get_files(path):
    files = os.listdir(path)
    files_path = []
    for fi in files:
        fi_path = path + '/' + fi
        if os.path.isfile(fi_path):
            if fi.split('.')[-1]=='py':
                files_path.append(fi_path)
        elif os.path.isdir(fi_path):
            files_path += get_files(fi_path)
    return files_path

def count(files):
    line_of_code, blank, comments = 0, 0, 0
    for filename in files:
        f = open(filename, 'rb')
        for line in f:
            line = line.strip()
            line_of_code += 1
            if line == '':
                blank += 1
            # elif line[0] == '#':
            #     comments += 1
        f.close()
    return (line_of_code, blank, comments)

if __name__ == '__main__':
    files = get_files('./qq')
    print(files)
    
    lines = count(files)
    print('Line(s): %d, black line(s): %d, comments line(s): %d' % (lines[0], lines[1], lines[2]))