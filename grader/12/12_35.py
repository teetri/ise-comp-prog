class Roman():
    def __init__(self, roman_string):
        self.roman_string = roman_string
        self.roman_dict = {'I': 1, 'V': 5, 'X': 10,
                           'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        self.roman_list = list(roman_string)
        self.roman_list.reverse()
        self.roman_list = [self.roman_dict[i] for i in self.roman_list]

    def __str__(self):
        return self.roman_string

    def __int__(self):
        result = 0
        for i in range(len(self.roman_list)):
            if i == 0:
                result += self.roman_list[i]
            elif self.roman_list[i] >= self.roman_list[i-1]:
                result += self.roman_list[i]
            else:
                result -= self.roman_list[i]
        return result

    def __add__(self, rhs):
        return Roman(self.int2roman(int(self) + int(rhs)))

    def __lt__(self, rhs):
        return int(self) < int(rhs)

    def int2roman(self, n):
        roman_dict = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL',
                      50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
        roman_list = sorted(roman_dict.keys())
        roman_list.reverse()
        result = ''
        for i in roman_list:
            while n >= i:
                result += roman_dict[i]
                n -= i
        return result


t, r1, r2 = input().split()
a = Roman(r1)
b = Roman(r2)
if t == '1':
    print(a < b)
elif t == '2':
    print(int(a), int(b))
elif t == '3':
    print(str(a), str(b))
elif t == '4':
    print(int(a + b))
else:
    print(str(a + b))
