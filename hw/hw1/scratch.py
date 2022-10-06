'''
# generate_column_seating_sequence

def p2d(a):
    for i in a:
        print(i)
    print()


group1 = ['A01', 'A02', 'A03', 'A04',
          'A05', 'A06', 'A07', 'A08', 'A09', 'A10']
group2 = ['B01', 'B02', 'B03', 'B04', 'B05']

total_rows = 4
seats_p_row = 6


#seating_sequence = []
seating = [['-'] * seats_p_row for x in range(total_rows)]
# p2d(seating_sequence)
a, b = 0, 0
for i in range(0, seats_p_row, 2):
    for j in range(0, total_rows):
        if a < len(group1):
            seating[j][i] = group1[a]
            # seating_sequence.append(group1[a])
            # p2d(seating_sequence)
            a += 1
        else:
            pass
            # seating_sequence.append('-')

        # print(j, i, a, group1[a])
        if b < len(group2):
            seating[j][i + 1] = group2[b]
            # seating_sequence.append(group2[b])
            # p2d(seating_sequence)
            b += 1
        else:
            pass
            # seating_sequence.append('-')
        # print(j, i, a, group1[a])

p2d(seating)
# print(seating_sequence)

# for x in seating:
#     for y in x:
#         seating_sequence.append(y)

seating_sequence = [y for x in seating for y in x]

print(seating_sequence)
'''

seating_sequence = ['A01', 'B01', 'A05', 'B05', 'A09', ' - ', 'A02', 'B02', 'A06', ' - ', 'A10', ' - ',
                    'A03', 'B03', 'A07', ' - ', ' - ', ' - ', 'A04', 'B04', 'A08', ' - ', ' - ', ' - ']

# seating_sequence = ['A01', 'B01', 'A02', 'B02', 'A03', 'B03', 'A04', 'B04', 'A05', 'B05', 'A06',
#                     ' - ', 'A07', ' - ', 'A08', ' - ', 'A09', ' - ', 'A10', ' - ', ' - ', ' - ', ' - ', ' - ']

total_rows = 4
seats_per_row = 6

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
