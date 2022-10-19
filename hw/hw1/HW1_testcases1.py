def is_inputs_valid(n_a, n_b, total_rows, seats_per_row, policy):
    # return True if all inputs are valid to continue
    #   otherwise return False
    # use the following error message to show that result
    error_student_number = 'ERROR: number of students must be 1 to 20.'
    error_total_rows = 'ERROR: total rows must be at least 4.'
    error_seats_per_row = 'ERROR: seats per row must be 4, 6 or 8.'
    error_not_enough_seat = 'ERROR: room is too small. Get a bigger exam room!'
    error_wrong_policy = 'ERROR: seating policy must be 0 or 1.'
    # Your code here
    if n_a < 1 or n_a > 20 or n_b < 1 or n_b > 20:
        print(error_student_number)
        return False

    if total_rows < 4:
        print(error_total_rows)
        return False

    if not seats_per_row in [4, 6, 8]:
        print(error_seats_per_row)
        return False

    if max([n_a, n_b]) > total_rows * seats_per_row:
        print(error_not_enough_seat)

    if not policy in [0, 1]:
        print(error_wrong_policy)
        return False

    return True
#------------------------------------------------------------#


def generate_seat_ids(subject_code, n):
    # returns a list of seat ID for this subject which is the combine
    # of subject_code and sequence from 01, 02, ..., 0n
    # For example,
    # generate_seat_ids('Z', 5) should return
    # ['Z01', 'Z02', 'Z03', 'Z04', 'Z05']
    # Hint: using for loop to generate the combination of
    #       subject_code and sequence

    # Your code here
    seat_ids = []

    for i in range(1, n + 1):
        seat_ids.append(subject_code + str('0' * (2 - len(str(i))) + str(i)))

    return seat_ids
#------------------------------------------------------------#


def generate_row_seating_sequence(group1, group2, total_rows, seats_p_row):
    # Hint:
    # - find the seating_sequence size and create it
    # - use list slicing to assign seat id of each group to seating_sequence
    # Your code here
    seating_sequence = [' - '] * (total_rows * seats_p_row)

    seating_sequence[0:len(group1)*2:2] = group1
    seating_sequence[1:len(group2)*2:2] = group2

    return seating_sequence
#------------------------------------------------------------#


def generate_column_seating_sequence(group1, group2, total_rows, seats_p_row):
    # Hint:
    # - find seating_sequence size and create it
    # - add empty seats to each group to have the size that fill half room
    # - using for loop to assign 2 columns per iteration:
    #     use list slicing to assign even column with group1
    #     use list slicing to assign odd column with group2

    # Your code here

    seating = [[' - '] * seats_p_row for x in range(total_rows)]

    a, b = 0, 0
    for i in range(0, seats_p_row, 2):
        for j in range(0, total_rows):
            if a < len(group1):
                seating[j][i] = group1[a]
                a += 1
            if b < len(group2):
                seating[j][i + 1] = group2[b]
                b += 1

    seating_sequence = [y for x in seating for y in x]

    return seating_sequence
#------------------------------------------------------------#


def display_seating_map(seating_sequence, total_rows, seats_per_row):
    # calculate line_len for display
    # display 'Exam Room' at center
    # use for loop to display each row in the room
    #   use str.join() to generate the output str from seating_sequence of each row

    # Your code here

    room_width = seats_per_row * 4 + 1

    print('-' * room_width)
    print('|', end='')
    print(' ' * ((room_width - 11) // 2), end='')
    print('Exam Room', end='')
    print(' ' * ((room_width - 11) // 2), end='')
    print('|')
    print('-' * room_width)

    for i in range(total_rows):
        print('|', end='')
        print('|'.join(seating_sequence[i*seats_per_row:(i+1) *
                                        seats_per_row]), end='')
        print('|')
        print('-' * room_width)

     # remove this line when you finish this function


def test(expected, actual):
    print('Expected:\t', expected)
    print('Your result:\t', actual)
    print(50*'-')


def test_is_input_valid_std():
    print('scoring is_inputs_valid')
    """valid data"""
    print('** valid data **')
    expected = True
    n_a = 3
    n_b = 4
    total_rows = 8
    seats_per_row = 4
    policy = 0  # valid
    r = is_inputs_valid(n_a, n_b, total_rows, seats_per_row, policy)
    test(expected, r)
    n_a = 20
    n_b = 20
    total_rows = 15
    seats_per_row = 6
    policy = 1  # valid
    r = is_inputs_valid(n_a, n_b, total_rows, seats_per_row, policy)
    test(expected, r)
    n_a = 1
    n_b = 1
    total_rows = 4
    seats_per_row = 8
    policy = 0  # valid
    r = is_inputs_valid(n_a, n_b, total_rows, seats_per_row, policy)
    test(expected, r)
    """--------------------------------------------------------------------------------"""
    """n_a invalid"""
    print('** n_a invalid **')
    expected = False
    n_a = -1
    n_b = 7
    total_rows = 8
    seats_per_row = 4
    policy = 0  # n_a invalid
    r = is_inputs_valid(n_a, n_b, total_rows, seats_per_row, policy)
    test(expected, r)
    n_a = 30
    n_b = 10
    total_rows = 10
    seats_per_row = 6
    policy = 1  # n_a invalid
    r = is_inputs_valid(n_a, n_b, total_rows, seats_per_row, policy)
    test(expected, r)
    """--------------------------------------------------------------------------------"""
    """n_b invalid"""
    print('** n_b invalid **')
    n_a = 10
    n_b = 0
    total_rows = 4
    seats_per_row = 8
    policy = 1  # n_b invalid
    r = is_inputs_valid(n_a, n_b, total_rows, seats_per_row, policy)
    test(expected, r)
    n_a = 5
    n_b = 21
    total_rows = 4
    seats_per_row = 8
    policy = 0  # n_b invalid
    r = is_inputs_valid(n_a, n_b, total_rows, seats_per_row, policy)
    test(expected, r)
    """--------------------------------------------------------------------------------"""
    """total_rows invalid"""
    print('** total_rows invalid **')
    n_a = 3
    n_b = 4
    total_rows = 3
    seats_per_row = 4
    policy = 0  # total row invalid
    r = is_inputs_valid(n_a, n_b, total_rows, seats_per_row, policy)
    test(expected, r)
    n_a = 3
    n_b = 4
    total_rows = -1
    seats_per_row = 4
    policy = 1  # total row invalid
    r = is_inputs_valid(n_a, n_b, total_rows, seats_per_row, policy)
    test(expected, r)
    """--------------------------------------------------------------------------------"""
    """seats_per_row invalid"""
    print('** seat_per_row invalid **')
    n_a = 3
    n_b = 4
    total_rows = 8
    seats_per_row = 1
    policy = 0  # seats per row invalid
    r = is_inputs_valid(n_a, n_b, total_rows, seats_per_row, policy)
    test(expected, r)
    n_a = 20
    n_b = 20
    total_rows = 15
    seats_per_row = 5
    policy = 1  # seats per row invalid
    r = is_inputs_valid(n_a, n_b, total_rows, seats_per_row, policy)
    test(expected, r)
    n_a = 20
    n_b = 20
    total_rows = 15
    seats_per_row = 7
    policy = 0  # seats per row invalid
    r = is_inputs_valid(n_a, n_b, total_rows, seats_per_row, policy)
    test(expected, r)
    n_a = 20
    n_b = 20
    total_rows = 15
    seats_per_row = 9
    policy = 1  # seats per row invalid
    r = is_inputs_valid(n_a, n_b, total_rows, seats_per_row, policy)
    test(expected, r)
    """--------------------------------------------------------------------------------"""
    """max seat invalid"""
    print('** max seat invalid **')
    n_a = 20
    n_b = 3
    total_rows = 8
    seats_per_row = 4
    policy = 0  # max seat invalid
    r = is_inputs_valid(n_a, n_b, total_rows, seats_per_row, policy)
    test(expected, r)
    n_a = 3
    n_b = 18
    total_rows = 4
    seats_per_row = 4
    policy = 0  # max seat invalid
    r = is_inputs_valid(n_a, n_b, total_rows, seats_per_row, policy)
    test(expected, r)
    n_a = 10
    n_b = 18
    total_rows = 4
    seats_per_row = 4
    policy = 0  # max seat invalid
    r = is_inputs_valid(n_a, n_b, total_rows, seats_per_row, policy)
    test(expected, r)
    """--------------------------------------------------------------------------------"""
    """invalid policy"""
    print('** invalid policy **')
    n_a = 3
    n_b = 4
    total_rows = 8
    seats_per_row = 4
    policy = -1  # policy invalid
    r = is_inputs_valid(n_a, n_b, total_rows, seats_per_row, policy)
    test(expected, r)
    n_a = 3
    n_b = 4
    total_rows = 4
    seats_per_row = 8
    policy = 69  # policy invalid
    r = is_inputs_valid(n_a, n_b, total_rows, seats_per_row, policy)
    test(expected, r)
    """--------------------------------------------------------------------------------"""


def test_generate_seat_ids():
    print('scoring generate_seat_ids')

    print('*** case #1 ***')
    subject = "N"
    n = 16
    expected = ['N01', 'N02', 'N03', 'N04', 'N05', 'N06', 'N07',
                'N08', 'N09', 'N10', 'N11', 'N12', 'N13', 'N14', 'N15', 'N16']
    test(expected, generate_seat_ids(subject, n))

    print('*** case #2 ***')
    subject = "A"
    n = 3
    expected = ['A01', 'A02', 'A03']
    test(expected, generate_seat_ids(subject, n))

    print('*** case #3 ***')
    subject = "B"
    n = 4
    expected = ['B01', 'B02', 'B03', 'B04']
    test(expected, generate_seat_ids(subject, n))

    print('*** case #4 ***')
    subject = "E"
    n = 1
    expected = ['E01']
    test(expected, generate_seat_ids(subject, n))

    print('*** case #5 ***')
    subject = "M"
    n = 7
    expected = ['M01', 'M02', 'M03', 'M04', 'M05', 'M06', 'M07']
    test(expected, generate_seat_ids(subject, n))


def test_generate_row_seating_sequence():
    print('scoring generate_row_seating_sequence')

    print('*** case #1 ***')
    group1 = ['A01', 'A02', 'A03', 'A04', 'A05']
    group2 = ['B01', 'B02', 'B03', 'B04', 'B05', 'B06', 'B07', 'B08', 'B09',
              'B10', 'B11', 'B12', 'B13', 'B14', 'B15', 'B16', 'B17', 'B18', 'B19', 'B20']
    total_rows = 10
    seats_p_row = 4
    expected = ['A01', 'B01', 'A02', 'B02', 'A03', 'B03', 'A04', 'B04', 'A05', 'B05', ' - ', 'B06', ' - ', 'B07', ' - ', 'B08', ' - ', 'B09', ' - ',
                'B10', ' - ', 'B11', ' - ', 'B12', ' - ', 'B13', ' - ', 'B14', ' - ', 'B15', ' - ', 'B16', ' - ', 'B17', ' - ', 'B18', ' - ', 'B19', ' - ', 'B20']
    test(expected, generate_row_seating_sequence(
        group1, group2, total_rows, seats_p_row))

    print('*** case #2 ***')
    group1 = ['A01', 'A02', 'A03', 'A04', 'A05', 'A06', 'A07', 'A08', 'A09',
              'A10', 'A11', 'A12', 'A13', 'A14', 'A15', 'A16', 'A17', 'A18', 'A19', 'A20']
    group2 = ['B01', 'B02', 'B03', 'B04', 'B05', 'B06', 'B07', 'B08', 'B09',
              'B10', 'B11', 'B12', 'B13', 'B14', 'B15', 'B16', 'B17', 'B18', 'B19', 'B20']
    total_rows = 5
    seats_p_row = 8
    expected = ['A01', 'B01', 'A02', 'B02', 'A03', 'B03', 'A04', 'B04', 'A05', 'B05', 'A06', 'B06', 'A07', 'B07', 'A08', 'B08', 'A09', 'B09', 'A10',
                'B10', 'A11', 'B11', 'A12', 'B12', 'A13', 'B13', 'A14', 'B14', 'A15', 'B15', 'A16', 'B16', 'A17', 'B17', 'A18', 'B18', 'A19', 'B19', 'A20', 'B20']
    test(expected, generate_row_seating_sequence(
        group1, group2, total_rows, seats_p_row))

    print('*** case #3 ***')
    group1 = ['A01', 'A02', 'A03', 'A04', 'A05', 'A06', 'A07', 'A08', 'A09',
              'A10', 'A11', 'A12', 'A13', 'A14', 'A15', 'A16', 'A17', 'A18', 'A19', 'A20']
    group2 = ['B01', 'B02', 'B03', 'B04', 'B05', 'B06', 'B07', 'B08', 'B09',
              'B10', 'B11', 'B12', 'B13', 'B14', 'B15', 'B16', 'B17', 'B18', 'B19', 'B20']
    total_rows = 10
    seats_p_row = 4
    expected = ['A01', 'B01', 'A02', 'B02', 'A03', 'B03', 'A04', 'B04', 'A05', 'B05', 'A06', 'B06', 'A07', 'B07', 'A08', 'B08', 'A09', 'B09', 'A10',
                'B10', 'A11', 'B11', 'A12', 'B12', 'A13', 'B13', 'A14', 'B14', 'A15', 'B15', 'A16', 'B16', 'A17', 'B17', 'A18', 'B18', 'A19', 'B19', 'A20', 'B20']
    test(expected, generate_row_seating_sequence(
        group1, group2, total_rows, seats_p_row))

    print('*** case #4 ***')
    group1 = ['C01', 'C02', 'C03', 'C04']
    group2 = ['P01', 'P02', 'P03', 'P04', 'P05']
    total_rows = 4
    seats_p_row = 4
    expected = ['C01', 'P01', 'C02', 'P02', 'C03', 'P03', 'C04',
                'P04', ' - ', 'P05', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ']
    test(expected, generate_row_seating_sequence(
        group1, group2, total_rows, seats_p_row))

    print('*** case #5 ***')
    group1 = ['A01', 'A02', 'A03']
    group2 = ['B01', 'B02', 'B03', 'B04']
    total_rows = 8
    seats_p_row = 4
    expected = ['A01', 'B01', 'A02', 'B02', 'A03', 'B03', ' - ', 'B04', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ',
                ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ']
    test(expected, generate_row_seating_sequence(
        group1, group2, total_rows, seats_p_row))


def test_generate_column_seating_sequence():
    print('scoring generate_column_seating_sequence')
    print('*** case #1 ***')
    group1 = ['A01', 'A02', 'A03', 'A04', 'A05']
    group2 = ['B01', 'B02', 'B03', 'B04', 'B05', 'B06', 'B07', 'B08', 'B09',
              'B10', 'B11', 'B12', 'B13', 'B14', 'B15', 'B16', 'B17', 'B18', 'B19', 'B20']
    total_rows = 10
    seats_p_row = 4
    expected = ['A01', 'B01', ' - ', 'B11', 'A02', 'B02', ' - ', 'B12', 'A03', 'B03', ' - ', 'B13', 'A04', 'B04', ' - ', 'B14', 'A05', 'B05', ' - ',
                'B15', ' - ', 'B06', ' - ', 'B16', ' - ', 'B07', ' - ', 'B17', ' - ', 'B08', ' - ', 'B18', ' - ', 'B09', ' - ', 'B19', ' - ', 'B10', ' - ', 'B20']
    test(expected, generate_column_seating_sequence(
        group1, group2, total_rows, seats_p_row))

    print('*** case #2 ***')
    group1 = ['A01', 'A02', 'A03', 'A04', 'A05', 'A06', 'A07', 'A08', 'A09',
              'A10', 'A11', 'A12', 'A13', 'A14', 'A15', 'A16', 'A17', 'A18', 'A19', 'A20']
    group2 = ['B01', 'B02', 'B03', 'B04', 'B05', 'B06', 'B07', 'B08', 'B09',
              'B10', 'B11', 'B12', 'B13', 'B14', 'B15', 'B16', 'B17', 'B18', 'B19', 'B20']
    total_rows = 5
    seats_p_row = 8
    expected = ['A01', 'B01', 'A06', 'B06', 'A11', 'B11', 'A16', 'B16', 'A02', 'B02', 'A07', 'B07', 'A12', 'B12', 'A17', 'B17', 'A03', 'B03', 'A08',
                'B08', 'A13', 'B13', 'A18', 'B18', 'A04', 'B04', 'A09', 'B09', 'A14', 'B14', 'A19', 'B19', 'A05', 'B05', 'A10', 'B10', 'A15', 'B15', 'A20', 'B20']
    test(expected, generate_column_seating_sequence(
        group1, group2, total_rows, seats_p_row))

    print('*** case #3 ***')
    group1 = ['C01', 'C02', 'C03', 'C04']
    group2 = ['P01', 'P02', 'P03', 'P04', 'P05']
    total_rows = 4
    seats_p_row = 4
    expected = ['C01', 'P01', ' - ', 'P05', 'C02', 'P02', ' - ',
                ' - ', 'C03', 'P03', ' - ', ' - ', 'C04', 'P04', ' - ', ' - ']
    test(expected, generate_column_seating_sequence(
        group1, group2, total_rows, seats_p_row))

    print('*** case #4 ***')
    group1 = ['C01']
    group2 = ['P01']
    total_rows = 7
    seats_p_row = 6
    expected = ['C01', 'P01', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ',
                ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ']
    test(expected, generate_column_seating_sequence(
        group1, group2, total_rows, seats_p_row))


def test_display_seating_map():
    print('scoring display_seating_map')
    #display_seating_map(seating_sequence, total_rows, seats_per_row)
    seating_sequence = ['A01', 'B01', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ',
                        ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ']
    total_rows = 7
    seats_p_row = 6
    expected = '''
-------------------------
|       Exam Room       |
-------------------------
|A01|B01| - | - | - | - |
-------------------------
| - | - | - | - | - | - |
-------------------------
| - | - | - | - | - | - |
-------------------------
| - | - | - | - | - | - |
-------------------------
| - | - | - | - | - | - |
-------------------------
| - | - | - | - | - | - |
-------------------------
| - | - | - | - | - | - |
-------------------------
'''
    print('*** case #1 ***')
    print('Expected')
    print(expected)
    print('Your result')
    display_seating_map(seating_sequence, total_rows, seats_p_row)

    seating_sequence = ['A01', 'B01', 'A11', 'B11', 'A02', 'B02', 'A12', 'B12', 'A03', 'B03', 'A13', 'B13', 'A04', 'B04', 'A14', 'B14', 'A05', 'B05', 'A15',
                        'B15', 'A06', 'B06', 'A16', 'B16', 'A07', 'B07', 'A17', 'B17', 'A08', 'B08', 'A18', 'B18', 'A09', 'B09', 'A19', 'B19', 'A10', 'B10', 'A20', 'B20']
    total_rows = 10
    seats_p_row = 4
    expected = '''
-----------------
|   Exam Room   |
-----------------
|A01|B01|A11|B11|
-----------------
|A02|B02|A12|B12|
-----------------
|A03|B03|A13|B13|
-----------------
|A04|B04|A14|B14|
-----------------
|A05|B05|A15|B15|
-----------------
|A06|B06|A16|B16|
-----------------
|A07|B07|A17|B17|
-----------------
|A08|B08|A18|B18|
-----------------
|A09|B09|A19|B19|
-----------------
|A10|B10|A20|B20|
-----------------
'''
    print('*** case #2 ***')
    print('Expected')
    print(expected)
    print('Your result')
    display_seating_map(seating_sequence, total_rows, seats_p_row)

    seating_sequence = ['A01', 'B01', 'A02', 'B02', 'A03', 'B03', ' - ', 'B04', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ',
                        ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ']
    total_rows = 8
    seats_p_row = 4
    expected = '''
-----------------
|   Exam Room   |
-----------------
|A01|B01|A02|B02|
-----------------
|A03|B03| - |B04|
-----------------
| - | - | - | - |
-----------------
| - | - | - | - |
-----------------
| - | - | - | - |
-----------------
| - | - | - | - |
-----------------
| - | - | - | - |
-----------------
| - | - | - | - |
-----------------
'''
    print('*** case #3 ***')
    print('Expected')
    print(expected)
    print('Your result')
    display_seating_map(seating_sequence, total_rows, seats_p_row)

    seating_sequence = ['A01', 'B01', 'A02', 'B02', 'A03', 'B03', 'A04',
                        'B04', 'A05', 'B05', 'A06', ' - ', 'A07', ' - ', 'A08', ' - ']
    total_rows = 4
    seats_p_row = 4
    expected = '''
-----------------
|   Exam Room   |
-----------------
|A01|B01|A02|B02|
-----------------
|A03|B03|A04|B04|
-----------------
|A05|B05|A06| - |
-----------------
|A07| - |A08| - |
-----------------
'''
    print('*** case #4 ***')
    print('Expected')
    print(expected)
    print('Your result')
    display_seating_map(seating_sequence, total_rows, seats_p_row)

    "=================================================================="
    seating_sequence = ['A01', 'B01', ' - ', 'B02', ' - ', 'B03', ' - ', 'B04', ' - ', 'B05', ' - ', 'B06', ' - ', 'B07', ' - ',
                        'B08', ' - ', 'B09', ' - ', 'B10', ' - ', 'B11', ' - ', 'B12', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ']
    total_rows = 4
    seats_p_row = 8
    expected = '''
---------------------------------
|           Exam Room           |
---------------------------------
|A01|B01| - |B02| - |B03| - |B04|
---------------------------------
| - |B05| - |B06| - |B07| - |B08|
---------------------------------
| - |B09| - |B10| - |B11| - |B12|
---------------------------------
| - | - | - | - | - | - | - | - |
---------------------------------
'''
    print('*** case #5 ***')
    print('Expected')
    print(expected)
    print('Your result')
    display_seating_map(seating_sequence, total_rows, seats_p_row)

    seating_sequence = ['A01', 'B01', 'A02', 'B02', 'A03', 'B03', 'A04', 'B04', 'A05', 'B05', 'A06', ' - ', 'A07', ' - ', 'A08', ' - ', 'A09', ' - ', 'A10', ' - ', 'A11', ' - ', 'A12', ' - ', 'A13', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ',
                        ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ']
    total_rows = 10
    seats_p_row = 8
    expected = '''
---------------------------------
|           Exam Room           |
---------------------------------
|A01|B01|A02|B02|A03|B03|A04|B04|
---------------------------------
|A05|B05|A06| - |A07| - |A08| - |
---------------------------------
|A09| - |A10| - |A11| - |A12| - |
---------------------------------
|A13| - | - | - | - | - | - | - |
---------------------------------
| - | - | - | - | - | - | - | - |
---------------------------------
| - | - | - | - | - | - | - | - |
---------------------------------
| - | - | - | - | - | - | - | - |
---------------------------------
| - | - | - | - | - | - | - | - |
---------------------------------
| - | - | - | - | - | - | - | - |
---------------------------------
| - | - | - | - | - | - | - | - |
---------------------------------
'''
    print('*** case #6 ***')
    print('Expected')
    print(expected)
    print('Your result')
    display_seating_map(seating_sequence, total_rows, seats_p_row)

    seating_sequence = ['A01', 'B01', 'A06', 'B06', 'A11', ' - ', 'A16', ' - ', 'A02', 'B02', 'A07', 'B07', 'A12', ' - ', 'A17', ' - ', 'A03', 'B03', 'A08',
                        ' - ', 'A13', ' - ', 'A18', ' - ', 'A04', 'B04', 'A09', ' - ', 'A14', ' - ', 'A19', ' - ', 'A05', 'B05', 'A10', ' - ', 'A15', ' - ', 'A20', ' - ']
    total_rows = 5
    seats_p_row = 8
    expected = '''
---------------------------------
|           Exam Room           |
---------------------------------
|A01|B01|A06|B06|A11| - |A16| - |
---------------------------------
|A02|B02|A07|B07|A12| - |A17| - |
---------------------------------
|A03|B03|A08| - |A13| - |A18| - |
---------------------------------
|A04|B04|A09| - |A14| - |A19| - |
---------------------------------
|A05|B05|A10| - |A15| - |A20| - |
---------------------------------
'''
    print('*** case #7 ***')
    print('Expected')
    print(expected)
    print('Your result')
    display_seating_map(seating_sequence, total_rows, seats_p_row)


def testsuite():
    print('-----------------------------')
    print('*** Testcases for scoring ***')
    print('-----------------------------')

    # uncomment each of the following test functions to test your code

    test_is_input_valid_std()
    test_generate_seat_ids()
    test_generate_row_seating_sequence()
    test_generate_column_seating_sequence()
    test_display_seating_map()


testsuite()
