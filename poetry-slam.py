from random import choice

def get_file_lines(filename):
    in_file = open(filename, "r")
    lines = in_file.readlines()
    in_file.close()
    return lines

# print(get_file_lines('poem.txt'))

def lines_printed_backwards(lines_list):
    #this reverses a list
    lines_list.reverse()
    lines_length = len(lines_list)
    for i in range(lines_length):
        line = lines_list[i]
        line_num = lines_length - i
        print(f"{line_num} {line}")
# lines_printed_backwards(poem_lines)

def lines_printed_random(lines_list):
    for lines in lines_list:
        print(choice(lines_list))


def lines_printed_custom(lines_list):
    lines_length = len(lines_list)

    for i in range(lines_length):
    # Because line 5 is on index 4, we check modulus of 4
        if i % 4 == 0:
            print(lines_length)



poem_lines = get_file_lines('poem.txt')
lines_printed_custom(poem_lines)
#lines_printed_random(poem_lines)

