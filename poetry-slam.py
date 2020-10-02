from random import choice

#get file line strings
def get_file_lines(filename):
    in_file = open(filename, "r")
    lines = in_file.readlines()
    in_file.close()
    return lines

print(get_file_lines('poem.txt'))

# backward lines
def lines_printed_backwards(lines_list):
    #this reverses a list
    lines_list.reverse()
    lines_length = len(lines_list)
    for i in range(lines_length):
        line = lines_list[i]
        line_num = lines_length - i
        print(f"{line_num} {line}")

# random lines
def lines_printed_random(lines_list):
    for lines in lines_list:
        print(choice(lines_list))

# custom lines
def lines_printed_custom(lines_list):
    lines_length = len(lines_list)
    for i in range(len(lines_list)):
        if i % 5 == 0:
            print(lines_list[i])
  


lines_list = get_file_lines('poem.txt')
poem_lines = get_file_lines('poem.txt')

#lines_printed_backwards(lines_list)
#lines_printed_custom(lines_list)
#lines_printed_random(poem_lines)


# Collab with Lon, Liz, and Arjun

