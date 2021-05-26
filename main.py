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

    base_state = '<no_state>'
    base_state_end = '<no_state>'

    for _, line in enumerate(lines):

        line_splited = line.split(' ')[0]

        base_state = 'in_loop'

        if line_splited:
            if '```' in line_splited and base_state_end == '<no_state>':
                print('Start code block')
                base_state_end = 'in_code_block'
            elif '```' in line_splited and base_state_end == 'in_code_block':
                print('End code block')
                base_state_end = '<no_state>'
            elif line_splited == '###' and base_state_end == '<no_state>':
                base_state = 'title_lvl_3'
            elif line_splited == '##' and base_state_end == '<no_state>':
                base_state = 'title_lvl_2'
            elif line_splited == '#' and base_state_end == '<no_state>':
                base_state = 'title_lvl_1'
            elif line_splited in ('*', '-') and base_state_end == '<no_state>':
                base_state = 'in_array'
            elif line_splited == '' and base_state_end == '<no_state>':
                base_state = 'empty_line'
        else:
            base_state = 'on_para_text'

        print(base_state)

    file_readed.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    reader('docs/test.md')
