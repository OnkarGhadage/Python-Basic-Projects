# A B C D E F
# A B C D E
# A B C D
# A B C
# A B
# A

import string
line = string.ascii_uppercase

N = int(input())

for i in range(N,-1,-1):
    print(" ".join(line[:i+1]))
