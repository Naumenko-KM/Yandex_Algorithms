# Test 7 failed

import string

with open('input.txt') as f:
    lines = f.readlines()
n, C, D = lines[0].split()
n = int(n)
program = " ".join(lines[1:])
chars = ''.join([i for i in string.printable if
                i not in string.ascii_uppercase
                + string.ascii_lowercase + string.digits + '_ \n'])


is_register_important = True if C == 'yes' else False
is_number_begin = True if D == 'yes' else False

if not is_register_important:
    program = program.lower()

program = program.translate({ord(i): " " for i in chars})


identifiers = program.split()
identifiers_dict = {}
max_cnt = 0
for identifier in identifiers:
    if not is_number_begin:
        if identifier[0] in '1234567890':
            pass
    if identifier.isdigit():
        pass
    if identifier in identifiers_dict.keys():
        identifiers_dict[identifier] += 1
    else:
        identifiers_dict[identifier] = 1
    if identifiers_dict[identifier] > max_cnt:
        max_cnt = identifiers_dict[identifier]
        identifier_max = identifier
print(identifier_max)
