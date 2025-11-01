#     A
#    ABA
#   ABCBA
#  ABCDCBA
# ABCDEDCBA

import string
char = string.ascii_uppercase
N = int(input("Size: "))

for i in range(1, N+1):
    row = char[:i]
    print(" "*(N-i),end="")
    print(f"{row[:-1]}{row[::-1]}")
