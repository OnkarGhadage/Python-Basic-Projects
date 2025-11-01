# A
# AB
# ABC
# ABCD
# ABCDE

import string
line = string.ascii_uppercase

N = int(input())

for i in range(N):
    print(line[:i+1])
