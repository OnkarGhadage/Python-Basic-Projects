# E
# D E
# C D E
# B C D E
# A B C D E

import string
N = int(input("Size: "))

for i in range(N-1, -1, -1):
    print(" ".join(string.ascii_uppercase[i:N]))
