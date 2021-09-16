
import sys

string = ''
for line in sys.stdin.readlines():
    string += line
print(len(set(string.split())))