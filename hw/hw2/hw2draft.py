def gradeNumber(x):  # write code for question 1
    if x == 'A':
        return 4
    elif x == 'B+':
        return 3.5
    elif x == 'B':
        return 3
    elif x == 'C+':
        return 2.5
    elif x == 'C':
        return 2
    elif x == 'D+':
        return 1.5
    elif x == 'D':
        return 1
    elif x == 'F':
        return 0


def operate(filename):
    def test(a):
        for x in a:
            print(x)
        print()

    f = open(filename, 'r')
    a = [x.replace('\n', '').strip() for x in f.readlines()]
    # print(a)
    f.close()

    b = []
    temp = 0
    for i in range(1, len(a)):
        if 'semester' in a[i]:
            b.append(a[temp:i])
            temp = i
        if i == len(a)-1:
            b.append(a[temp:len(a)])
    test(b)
    # grp subjects to list
    b = [[x[0], x[2:]] for x in b]
    test(b)
    # get only grade and credit
    b = [[x[0], [[y.split(',')[-1], y.split(',')[-2]]
                 for y in x[1]]] for x in b]
    test(b)
    # change letter grade to num and credit to float
    b = [[x[0], [[gradeNumber(y[0]), float(y[1])] for y in x[1]]] for x in b]
    test(b)
    # get grades times credits
    b = [[x[0], x[1], [y[0]*y[1] for y in x[1]]] for x in b]
    test(b)
    # get sum of credits
    b = [[x[0], x[1], x[2], sum([y[1] for y in x[1]])] for x in b]
    test(b)
    # get gpa of each semester
    b = [[x[0], x[1], x[2], x[3], sum(x[2])/x[3]] for x in b]
    test(b)
    # round gpa to 2 decimal places
    b = [[x[0], x[1], x[2], x[3], round(x[4], 2)] for x in b]
    test(b)

    # create new list with total credits and gpa
    c = [[x[0], x[3], x[4]] for x in b]
    test(c)

    # get running gpax
    tcreds = 0
    for i in range(0, len(c)):
        tcreds += c[i][1]
        print(tcreds)
        # get running gpax
        gpax = sum([x[2]*x[1] for x in c[0:i+1]])/tcreds
        # round gpax to 2 decimal places
        gpax = round(gpax, 2)
        print(gpax)
        c[i].append(gpax)

    # remove total credits
    c = [[x[0], x[2], x[3]] for x in c]

    print(c)

    return c


def generateReport(l, filename):
    print('######')
    print(l)
    a = ''
    for x in l:
        # a += f'{x[0]}\nGPA = {x[1]} GPAX = {x[2]}\n'
        a += str(x[0]) + '\n' + 'GPA = ' + str(x[1]) + \
            ' GPAX = ' + str(x[2]) + '\n'
    print(a)
    f = open(filename, 'w')
    f.write(a)
    f.close()
    return a


def main():
    # operate('grades2.txt')
    generateReport(operate('grades2.txt'), 'results1.txt')


if __name__ == '__main__':
    main()
