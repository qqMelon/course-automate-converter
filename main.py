# _STATE = '<no_state>'
# _STATE_T = '<no_state>'

def reader(file):
    file_readed = open(file, 'r')
    # line = file_readed.readline()
    lines = file_readed.readlines()

    # print(line)
    print(lines)

    # catch just the first line
    my_line = lines[0]

    print(my_line)

    # Split to catch the first anchor
    catch_anchor = my_line.split(' ')[0]

    print(catch_anchor)

    _STATE = '<no_state>'
    _STATE_T = '<no_state>'

    for index, line in enumerate(lines):

        line_splited = line.split(' ')[0]

        _STATE = 'in_loop'

        if line_splited:
            if '```' in line_splited and _STATE_T == '<no_state>':
                print('Start code block')
                _STATE_T = 'in_code_block'
            elif '```' in line_splited and _STATE_T == 'in_code_block':
                print('End code block')
                _STATE_T = '<no_state>'
            elif line_splited == '###' and _STATE_T == '<no_state>':
                _STATE = 'title_lvl_3'
            elif line_splited == '##' and _STATE_T == '<no_state>':
                _STATE = 'title_lvl_2'
            elif line_splited == '#' and _STATE_T == '<no_state>':
                _STATE = 'title_lvl_1'
            elif (line_splited == '*' or line_splited == '-') and _STATE_T == '<no_state>':
                _STATE = 'in_array'
            elif line_splited == '' and _STATE_T == '<no_state>':
                _STATE = 'empty_line'
        else:
            _STATE = 'on_para_text'

        print(_STATE)

    file_readed.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    reader('docs/test.md')
