def check_all():
    with open('output_tee.txt', 'r') as t1, open('output_peace.txt', 'r') as t2:
        fileone = t1.readlines()
        filetwo = t2.readlines()

    if range(len(fileone)) == range(len(filetwo)):
        for line1, line2 in zip(fileone, filetwo):
            if line1 != line2:
                print(line1, line2)
    else:
        print('Files are not the same length')


def check_one_line(line_number):
    line_number -= 1
    with open('output_tee.txt', 'r') as t1, open('output_peace.txt', 'r') as t2:
        fileone = t1.readlines()
        filetwo = t2.readlines()

    if range(len(fileone)) == range(len(filetwo)):
        print(fileone[line_number], filetwo[line_number])
        for x, y in zip(fileone[line_number].split(','), filetwo[line_number].split(',')):
            if x != y:
                print(x, y)
                break
    else:
        print('Files are not the same length')


# check_one_line(1878)
check_all()
