# A 
# B B
# C C C
# D D D D
# E E E E E

import string
N = int(input("Rows: "))

for i in range(N):
    print(f"{string.ascii_uppercase[i]} "*(i+1))
