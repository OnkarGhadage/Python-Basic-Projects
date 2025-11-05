# *        *
# **      **
# ***    ***
# ****  ****
# **********
# ****  ****
# ***    ***
# **      **
# *        *

N = int(input("Size: "))

for j in range(N*2-2, 0, -2):
    spaces = " "*j
    print(spaces.center(N*2,"*"))
for i in range(0,N*2,2):
    space = " "*i
    print(space.center(N*2,"*"))
