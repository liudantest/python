import linecache

the_line=linecache.getline('test',222)
print(the_line)

def getline(the_file_path,line_number):
    if linecache<1:
        return ''
    for cur_line_number,line in enumerate(open(the_file_path,'rU')):
        if cur_line_number==line_number-1:
            return line
    return ''


if __name__ == '__main__':
    the_line=linecache.getline('test',222)
    print(the_line)